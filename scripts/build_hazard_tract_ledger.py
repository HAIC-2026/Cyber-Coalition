#!/usr/bin/env python3
"""Build the hazard-by-hazard tract ledger for Hawaii (read-only, standard library only).

What this measures
    For each hazard, how the 435 Hawaii tracts present in the FEMA National Risk Index (NRI)
    tract layer are distributed across: positive, zero, missing value, invalid. It also
    reproduces the tract-ID reconciliation between NRI and the Hawaii Statewide GIS Program
    2020 Census Tracts layer.

What this does NOT measure
    * It is MODELED RISK from a national dataset, not a hazard footprint or overlay.
    * It is not an AFN or CMIST measure and is not hazard-specific AFN coverage.
    * The 461-tract universe is retrieved from the Census TIGERweb Tracts service when that host is
      reachable, and the Census-only tracts are then listed. If it is not reachable the script falls
      back to the count recorded in docs/EVIDENCE_REGISTER.md and says so in ledger_run.json; it
      then cannot list the Census-only tracts.
    * It says nothing about shelter capacity, accessibility, operating status or route safety.

Usage
    python3 scripts/build_hazard_tract_ledger.py            # writes data/hazard-tract-ledger/
    python3 scripts/build_hazard_tract_ledger.py --out DIR

Outputs are deterministic for a given source state; only the retrieval timestamps differ
between runs. A change in a source layer shows up as a change in the checksums and counts.
"""
import argparse
import collections
import csv
import datetime
import hashlib
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request

SCRIPT_VERSION = "1.1"
MT_RISK = "Modeled risk (FEMA NRI, December 2025)"
MT_OVERLAY = "Overlay (project DFIRM result, read-only)"

NRI_LAYER = "https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0"
STATEGIS_LAYER = "https://geodata.hawaii.gov/arcgis/rest/services/Census/MapServer/31"
# Project-produced flood overlay (Summarize Within by the team, DFIRM polygons against 435 tracts), read-only.
DFIRM_SERVICE = "https://services7.arcgis.com/4oZC3kLP6Hu4wqUM/arcgis/rest/services/HAIC%20ESF6%20DFIRM%20SFHA_TF%20by%20435%20Tracts%20QA%202026%2011%2017/FeatureServer"
CENSUS_LAYER = "https://tigerweb.geo.census.gov/arcgis/rest/services/Census2020/Tracts_Blocks/MapServer/0"

# Fallback only: the count recorded in docs/EVIDENCE_REGISTER.md (Census TIGERweb check, 2026-11-18).
# Used when the Census service cannot be reached; the run record then says the universe was not re-retrieved.
UNIVERSE_COUNT = 461

HAZARDS = [
    # key, label, NRI field prefix
    ("hurricane", "Hurricane", "HRCN"),
    ("wildfire", "Wildfire", "WFIR"),
    ("tsunami", "Tsunami", "TSUN"),
    ("flood_coastal", "Flood, coastal", "CFLD"),
    ("flood_inland", "Flood, inland", "IFLD"),
]

COUNTIES = {
    "15001": "Hawaii County",
    "15003": "Honolulu County",
    "15005": "Kalawao County",
    "15007": "Kauai County",
    "15009": "Maui County",
}

CLASSES = ("positive", "zero", "missing", "invalid")


def fetch(url, params, tries=3):
    full = url + "/query?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(full, timeout=90) as resp:
                return resp.read(), full
        except Exception as exc:  # noqa: BLE001 - report and retry
            last = exc
            time.sleep(2 * (attempt + 1))
    raise SystemExit("Could not retrieve %s: %s" % (full, last))


def classify(value):
    """Classify a numeric risk value. None is a missing value; anything non-numeric or negative is invalid."""
    if value is None:
        return "missing"
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return "invalid"
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return "invalid"
    if value < 0:
        return "invalid"
    return "zero" if value == 0 else "positive"


def valid_geoid(geoid):
    return isinstance(geoid, str) and len(geoid) == 11 and geoid.isdigit() and geoid.startswith("15")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join("data", "hazard-tract-ledger"))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    hst = now_utc.astimezone(datetime.timezone(datetime.timedelta(hours=-10)))

    layer_meta = json.loads(urllib.request.urlopen(NRI_LAYER + "?f=json", timeout=90).read())
    layer_fields = {f["name"] for f in layer_meta["fields"]}
    fields = ["TRACTFIPS", "STCOFIPS", "NRI_VER"]
    for _, _, p in HAZARDS:
        fields += [p + "_RISKV", p + "_RISKR"]
    missing_fields = [f for f in fields if f not in layer_fields]
    if missing_fields:
        raise SystemExit("Fields not present in the NRI layer (refusing to treat absent fields as null values): %s" % missing_fields)
    nri_raw, nri_url = fetch(NRI_LAYER, {
        "where": "STATEFIPS='15'", "outFields": ",".join(fields), "returnGeometry": "false",
        "orderByFields": "TRACTFIPS", "resultRecordCount": 2000, "f": "json"})
    nri = json.loads(nri_raw)
    if nri.get("exceededTransferLimit"):
        raise SystemExit("NRI response exceeded the transfer limit; paging is required before counts can be trusted.")
    rows = [f["attributes"] for f in nri["features"]]

    sg_raw, sg_url = fetch(STATEGIS_LAYER, {
        "where": "1=1", "outFields": "geoid20", "returnGeometry": "false", "resultRecordCount": 1000, "f": "json"})
    sg = json.loads(sg_raw)
    if sg.get("exceededTransferLimit"):
        raise SystemExit("StateGIS response exceeded the transfer limit; paging is required.")
    sg_ids = [str(f["attributes"]["geoid20"]) for f in sg["features"]]

    census_rows, census_raw, census_url, census_error = None, None, None, None
    try:
        census_raw, census_url = fetch(CENSUS_LAYER, {
            "where": "STATE='15'", "outFields": "GEOID,COUNTY,POP100,HU100", "returnGeometry": "false",
            "orderByFields": "GEOID", "resultRecordCount": 2000, "f": "json"}, tries=2)
        census = json.loads(census_raw)
        if census.get("exceededTransferLimit") or "features" not in census:
            raise ValueError("Census response unusable: %s" % (census.get("error") or "transfer limit exceeded"))
        census_rows = [f["attributes"] for f in census["features"]]
    except (SystemExit, Exception) as exc:  # noqa: BLE001 - fall back and record why
        census_error = str(exc)
        census_rows = None

    # ---- identifier checks -------------------------------------------------------------
    nri_ids = [str(r["TRACTFIPS"]) for r in rows]
    id_counts = collections.Counter(nri_ids)
    duplicates = sorted(k for k, v in id_counts.items() if v > 1)
    malformed = sorted(g for g in set(nri_ids) if not valid_geoid(g))
    unknown_county = sorted({str(r["STCOFIPS"]) for r in rows} - set(COUNTIES))
    census_ids = [str(r["GEOID"]) for r in census_rows] if census_rows is not None else None
    universe = len(set(census_ids)) if census_ids is not None else UNIVERSE_COUNT
    census_only = sorted(set(census_ids) - set(nri_ids)) if census_ids is not None else None
    recon = {
        "nri_records": len(rows),
        "nri_distinct_geoids": len(set(nri_ids)),
        "nri_duplicate_geoids": duplicates,
        "nri_malformed_geoids": malformed,
        "nri_unrecognised_county_fips": unknown_county,
        "stategis_layer31_records": len(sg_ids),
        "stategis_layer31_distinct_geoids": len(set(sg_ids)),
        "intersection": len(set(nri_ids) & set(sg_ids)),
        "only_in_nri": sorted(set(nri_ids) - set(sg_ids)),
        "only_in_stategis": sorted(set(sg_ids) - set(nri_ids)),
        "universe_count_used": universe,
        "universe_count_per_evidence_register": UNIVERSE_COUNT,
        "universe_reretrieved_here": census_ids is not None,
        "census_records": len(census_ids) if census_ids is not None else None,
        "census_distinct_geoids": len(set(census_ids)) if census_ids is not None else None,
        "census_malformed_geoids": sorted(g for g in set(census_ids) if not valid_geoid(g)) if census_ids is not None else None,
        "census_error_if_not_retrieved": census_error,
        "intersection_census_nri": len(set(census_ids) & set(nri_ids)) if census_ids is not None else None,
        "only_in_nri_vs_census": sorted(set(nri_ids) - set(census_ids)) if census_ids is not None else None,
        "census_only_tracts_not_evaluated": universe - len(set(nri_ids)),
        "census_only_geoids_enumerated_here": census_only is not None,
    }
    if census_rows is not None:
        by_id = {str(r["GEOID"]): r for r in census_rows}
        recon["census_only_pop100_hu100_values"] = sorted({"POP100=%s,HU100=%s" % (by_id[g]["POP100"], by_id[g]["HU100"]) for g in census_only})
        zero_zero = sorted(g for g, r in by_id.items() if str(r["POP100"]) == "0" and str(r["HU100"]) == "0")
        recon["zero_population_and_zero_housing_tracts_in_census"] = len(zero_zero)
        recon["zero_zero_tracts_that_are_in_nri"] = sorted(set(zero_zero) & set(nri_ids))

    # ---- project DFIRM SFHA overlay (read-only), tolerant of failure -------------------------
    overlay = {"retrieved": False}
    overlay_class = {}
    try:
        lay_raw, lay_url = fetch(DFIRM_SERVICE + "/0", {
            "where": "1=1", "outFields": "geoid20,Join_ID", "returnGeometry": "false",
            "orderByFields": "geoid20", "resultRecordCount": 2000, "f": "json"}, tries=2)
        tab_raw, tab_url = fetch(DFIRM_SERVICE + "/1", {
            "where": "1=1", "outFields": "Join_ID,sfha_tf,sum_Area_SquareMiles,Polygon_Count",
            "resultRecordCount": 2000, "f": "json"}, tries=2)
        lay = json.loads(lay_raw)
        tab = json.loads(tab_raw)
        if lay.get("exceededTransferLimit") or tab.get("exceededTransferLimit") or "features" not in lay or "features" not in tab:
            raise ValueError("DFIRM response unusable")
        lay_rows = [f["attributes"] for f in lay["features"]]
        tab_rows = [f["attributes"] for f in tab["features"]]
        join_to_geoid = {r["Join_ID"]: str(r["geoid20"]) for r in lay_rows}
        per = collections.defaultdict(dict)
        dup_pairs = 0
        orphan_rows = 0
        for r in tab_rows:
            g = join_to_geoid.get(r["Join_ID"])
            if g is None:
                orphan_rows += 1
                continue
            if r["sfha_tf"] in per[g]:
                dup_pairs += 1
            per[g][r["sfha_tf"]] = r
        for g in nri_ids:
            rws = per.get(g)
            if not rws:
                overlay_class[g] = "missing"
                continue
            bad = False
            for flag, r in rws.items():
                a, n = r.get("sum_Area_SquareMiles"), r.get("Polygon_Count")
                if flag not in ("T", "F") or not isinstance(a, (int, float)) or a < 0 or not isinstance(n, (int, float)) or n < 0:
                    bad = True
            if bad:
                overlay_class[g] = "invalid"
            else:
                t = rws.get("T")
                overlay_class[g] = "positive" if (t and t["sum_Area_SquareMiles"] > 0) else "zero"
        overlay = {
            "retrieved": True, "layer_query_url": lay_url, "table_query_url": tab_url,
            "layer_sha256": hashlib.sha256(lay_raw).hexdigest(), "table_sha256": hashlib.sha256(tab_raw).hexdigest(),
            "layer_records": len(lay_rows), "table_records": len(tab_rows),
            "layer_geoids_equal_nri_geoids": {str(r["geoid20"]) for r in lay_rows} == set(nri_ids),
            "table_rows_without_a_tract": orphan_rows, "duplicate_tract_flag_pairs": dup_pairs,
            "sfha_tf_values": dict(collections.Counter(r["sfha_tf"] for r in tab_rows)),
        }
    except (SystemExit, Exception) as exc:  # noqa: BLE001 - the overlay row is simply left out
        overlay = {"retrieved": False, "error": str(exc)}
        overlay_class = {}

    # ---- classification ----------------------------------------------------------------
    per_tract = []
    summary = []
    by_county = []
    ratings = []
    for key, label, prefix in HAZARDS:
        tallies = collections.Counter()
        county_tallies = collections.defaultdict(collections.Counter)
        rating_tallies = collections.Counter()
        for r in rows:
            c = classify(r.get(prefix + "_RISKV"))
            tallies[c] += 1
            county_tallies[str(r["STCOFIPS"])][c] += 1
            rating_tallies[r.get(prefix + "_RISKR") if r.get(prefix + "_RISKR") is not None else "(null)"] += 1
        matched = len(rows)
        assert sum(tallies[c] for c in CLASSES) == matched, "classification must account for every matched tract"
        summary.append({
            "hazard": label, "measure_type": MT_RISK, "source_field": prefix + "_RISKV", "universe_461": universe,
            "matched_in_source": matched, "not_in_source": universe - matched,
            **{c: tallies[c] for c in CLASSES},
        })
        for fips in sorted(county_tallies):
            by_county.append({"hazard": label, "county_fips": fips, "county": COUNTIES.get(fips, "UNRECOGNISED"),
                              "tracts": sum(county_tallies[fips].values()), **{c: county_tallies[fips][c] for c in CLASSES}})
        for rating, n in sorted(rating_tallies.items(), key=lambda kv: (-kv[1], kv[0])):
            ratings.append({"hazard": label, "nri_rating_as_reported": rating, "tracts": n})
    if overlay_class:
        o_t = collections.Counter(overlay_class.values())
        o_county = collections.defaultdict(collections.Counter)
        for r in rows:
            o_county[str(r["STCOFIPS"])][overlay_class[str(r["TRACTFIPS"])]] += 1
        assert sum(o_t[c] for c in CLASSES) == len(rows), "overlay classification must account for every matched tract"
        summary.append({
            "hazard": "Flood, SFHA overlay", "measure_type": MT_OVERLAY, "source_field": "sfha_tf='T' area (project DFIRM result)",
            "universe_461": universe, "matched_in_source": len(rows), "not_in_source": universe - len(rows),
            **{c: o_t[c] for c in CLASSES},
        })
        for fips in sorted(o_county):
            by_county.append({"hazard": "Flood, SFHA overlay", "county_fips": fips, "county": COUNTIES.get(fips, "UNRECOGNISED"),
                              "tracts": sum(o_county[fips].values()), **{c: o_county[fips][c] for c in CLASSES}})
    for r in sorted(rows, key=lambda x: str(x["TRACTFIPS"])):
        rec = {"tract_geoid": str(r["TRACTFIPS"]), "county_fips": str(r["STCOFIPS"])}
        for key, label, prefix in HAZARDS:
            rec[key + "_class"] = classify(r.get(prefix + "_RISKV"))
        if overlay_class:
            rec["flood_sfha_overlay_class"] = overlay_class[str(r["TRACTFIPS"])]
        per_tract.append(rec)

    def write_csv(name, records):
        path = os.path.join(args.out, name)
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(records[0].keys()), lineterminator="\n")
            w.writeheader()
            w.writerows(records)
        return path

    write_csv("ledger_summary.csv", summary)
    write_csv("ledger_by_county.csv", by_county)
    write_csv("ledger_ratings_as_reported.csv", ratings)
    write_csv("tract_hazard_classes.csv", per_tract)
    if census_only is not None:
        by_id = {str(r["GEOID"]): r for r in census_rows}
        write_csv("census_only_tracts_not_evaluated.csv", [
            {"tract_geoid": g, "county_fips": g[:5], "pop100_2020": by_id[g]["POP100"], "hu100_2020": by_id[g]["HU100"]}
            for g in census_only] or [{"tract_geoid": "", "county_fips": "", "pop100_2020": "", "hu100_2020": ""}])

    run = {
        "script": "scripts/build_hazard_tract_ledger.py", "script_version": SCRIPT_VERSION,
        "retrieved_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"), "retrieved_hst": hst.strftime("%Y-%m-%dT%H:%M:%S-10:00"),
        "sources": {
            "fema_nri_census_tracts": {"query_url": nri_url, "sha256_of_response": hashlib.sha256(nri_raw).hexdigest(),
                                         "records": len(rows), "nri_version_values": sorted({str(r["NRI_VER"]) for r in rows})},
            "stategis_2020_census_tracts_layer31": {"query_url": sg_url, "sha256_of_response": hashlib.sha256(sg_raw).hexdigest(),
                                                       "records": len(sg_ids)},
            "census_tigerweb_2020_tracts": ({"query_url": census_url, "sha256_of_response": hashlib.sha256(census_raw).hexdigest(),
                                              "records": len(census_ids)} if census_ids is not None else {"retrieved": False, "error": census_error}),
        },
        "tract_id_reconciliation": recon,
        "flood_sfha_overlay_project_dfirm_result": overlay,
        "class_definitions": {
            "positive": "NRI <hazard>_RISKV is numeric and greater than 0",
            "zero": "NRI <hazard>_RISKV is numeric and equal to 0",
            "missing": "NRI <hazard>_RISKV is null (the tract is in the source layer but has no value)",
            "invalid": "NRI <hazard>_RISKV is non-numeric, negative or not finite",
            "overlay_positive": "the tract has a DFIRM polygon with sfha_tf='T' and a summed area greater than 0 in the project's Summarize Within result",
            "overlay_zero": "the tract has DFIRM polygons but none with sfha_tf='T' (only 'F')",
            "overlay_missing": "the tract has no row in the project's group-by summary table",
            "not_in_source": "the universe (Census 2020 tracts for Hawaii) minus tracts present in the NRI layer; listed in census_only_tracts_not_evaluated.csv when the Census service was reachable",
        },
        "limits": [
            "The overlay row reads the project's own Summarize Within output; it was not recomputed here. The DFIRM input item and vintage are not recorded on the item (open in the project's QA note). The meaning of sfha_tf is taken from the layer's name and has not been checked against FEMA NFHL metadata in this run.",
            "Modeled risk from a national dataset; not a hazard footprint, overlay or AFN measure.",
            "FEMA terms for the NRI state it is for planning purposes only and not a substitute for localized risk assessment.",
            "'zero' and the NRI rating labels are reported as the source gives them; their meaning has not been checked against the NRI technical documentation in this run.",
            "Zero Census population and housing in 2020 describes the 2020 enumeration only; it does not establish zero need.",
        ] + ([] if census_ids is not None else [
            "The Census service was not reachable, so the 461 universe is the count recorded in docs/EVIDENCE_REGISTER.md and the Census-only tracts are not listed."]),
    }
    with open(os.path.join(args.out, "ledger_run.json"), "w", encoding="utf-8") as fh:
        json.dump(run, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print("Retrieved %s UTC; NRI records %d; StateGIS layer 31 records %d; ID intersection %d; universe %d (%s)" % (
        run["retrieved_utc"], len(rows), len(sg_ids), recon["intersection"], universe,
        "Census service" if census_ids is not None else "FALLBACK count, Census service not reached"))
    for s in summary:
        print("%-20s matched %d | positive %d | zero %d | missing %d | invalid %d | not in source %d" % (
            s["hazard"], s["matched_in_source"], s["positive"], s["zero"], s["missing"], s["invalid"], s["not_in_source"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
