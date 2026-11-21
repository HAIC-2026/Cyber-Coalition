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
    * It cannot enumerate the 26 Census-only tracts (the Census hosts are not reachable
      from the sandbox this was built in). The 461 universe is taken from
      docs/EVIDENCE_REGISTER.md and is NOT re-retrieved here.
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

SCRIPT_VERSION = "1.0"

NRI_LAYER = "https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0"
STATEGIS_LAYER = "https://geodata.hawaii.gov/arcgis/rest/services/Census/MapServer/31"

# Taken from docs/EVIDENCE_REGISTER.md (Census TIGERweb check recorded 2026-11-18). Not re-retrieved here.
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

    # ---- identifier checks -------------------------------------------------------------
    nri_ids = [str(r["TRACTFIPS"]) for r in rows]
    id_counts = collections.Counter(nri_ids)
    duplicates = sorted(k for k, v in id_counts.items() if v > 1)
    malformed = sorted(g for g in set(nri_ids) if not valid_geoid(g))
    unknown_county = sorted({str(r["STCOFIPS"]) for r in rows} - set(COUNTIES))
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
        "universe_count_per_evidence_register": UNIVERSE_COUNT,
        "universe_reretrieved_here": False,
        "census_only_tracts_not_evaluated": UNIVERSE_COUNT - len(set(nri_ids)),
        "census_only_geoids_enumerated_here": False,
    }

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
            "hazard": label, "nri_field": prefix + "_RISKV", "universe_461": UNIVERSE_COUNT,
            "matched_in_source": matched, "not_in_source": UNIVERSE_COUNT - matched,
            **{c: tallies[c] for c in CLASSES},
        })
        for fips in sorted(county_tallies):
            by_county.append({"hazard": label, "county_fips": fips, "county": COUNTIES.get(fips, "UNRECOGNISED"),
                              "tracts": sum(county_tallies[fips].values()), **{c: county_tallies[fips][c] for c in CLASSES}})
        for rating, n in sorted(rating_tallies.items(), key=lambda kv: (-kv[1], kv[0])):
            ratings.append({"hazard": label, "nri_rating_as_reported": rating, "tracts": n})
    for r in sorted(rows, key=lambda x: str(x["TRACTFIPS"])):
        rec = {"tract_geoid": str(r["TRACTFIPS"]), "county_fips": str(r["STCOFIPS"])}
        for key, label, prefix in HAZARDS:
            rec[key + "_class"] = classify(r.get(prefix + "_RISKV"))
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

    run = {
        "script": "scripts/build_hazard_tract_ledger.py", "script_version": SCRIPT_VERSION,
        "retrieved_utc": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"), "retrieved_hst": hst.strftime("%Y-%m-%dT%H:%M:%S-10:00"),
        "sources": {
            "fema_nri_census_tracts": {"query_url": nri_url, "sha256_of_response": hashlib.sha256(nri_raw).hexdigest(),
                                         "records": len(rows), "nri_version_values": sorted({str(r["NRI_VER"]) for r in rows})},
            "stategis_2020_census_tracts_layer31": {"query_url": sg_url, "sha256_of_response": hashlib.sha256(sg_raw).hexdigest(),
                                                       "records": len(sg_ids)},
        },
        "tract_id_reconciliation": recon,
        "class_definitions": {
            "positive": "NRI <hazard>_RISKV is numeric and greater than 0",
            "zero": "NRI <hazard>_RISKV is numeric and equal to 0",
            "missing": "NRI <hazard>_RISKV is null (the tract is in the source layer but has no value)",
            "invalid": "NRI <hazard>_RISKV is non-numeric, negative or not finite",
            "not_in_source": "the 461 universe minus tracts present in the source layer; these GEOIDs are not enumerated here",
        },
        "limits": [
            "Modeled risk from a national dataset; not a hazard footprint, overlay or AFN measure.",
            "FEMA terms for the NRI state it is for planning purposes only and not a substitute for localized risk assessment.",
            "'zero' and the NRI rating labels are reported as the source gives them; their meaning has not been checked against the NRI technical documentation in this run.",
            "The 461 universe and the 26 Census-only tracts come from docs/EVIDENCE_REGISTER.md and were not re-retrieved.",
        ],
    }
    with open(os.path.join(args.out, "ledger_run.json"), "w", encoding="utf-8") as fh:
        json.dump(run, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print("Retrieved %s UTC; NRI records %d; StateGIS layer 31 records %d; ID intersection %d" % (
        run["retrieved_utc"], len(rows), len(sg_ids), recon["intersection"]))
    for s in summary:
        print("%-16s matched %d | positive %d | zero %d | missing %d | invalid %d | not in source %d" % (
            s["hazard"], s["matched_in_source"], s["positive"], s["zero"], s["missing"], s["invalid"], s["not_in_source"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
