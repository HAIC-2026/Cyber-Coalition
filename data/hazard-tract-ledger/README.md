# Hazard-by-hazard tract ledger (data provenance)

Status: **first measurement, modeled-risk only.** Not hazard-overlay coverage, not AFN or CMIST coverage, not operational readiness.

Everything here is produced by `scripts/build_hazard_tract_ledger.py`. Re-running it re-queries the sources and rewrites these files. Values are expected to be identical unless a source layer has changed; the retrieval timestamps and checksums in `ledger_run.json` show whether it did.

## Provenance (the checklist from `data/README.md`)

| Item | Record |
|---|---|
| Primary source | FEMA National Risk Index, Census Tracts feature service, item `9da4eeb936544335a6db0cd7a8448a51` (owner `FEMA_NationalRiskIndex`, public). Layer: `https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0` |
| Source version | `NRI_VER` = "December 2025" for all 435 Hawaii records |
| Cross-check source | Hawaii Statewide GIS Program, 2020 Census Tracts, `https://geodata.hawaii.gov/arcgis/rest/services/Census/MapServer/31` (used for tract identifiers only) |
| Retrieved | 2026-11-21 01:33:19 UTC (2026-11-20 15:33:19 HST) |
| Native geography | 2020 Census tract (11-digit GEOID); Hawaii state FIPS `15` |
| Fields used | `TRACTFIPS`, `STCOFIPS`, `NRI_VER`, and `<hazard>_RISKV`, `<hazard>_RISKR` for `HRCN`, `WFIR`, `TSUN`, `CFLD`, `IFLD` |
| Query | `where STATEFIPS='15'`, geometry not requested; exact URLs and response SHA-256 values are in `ledger_run.json` |
| Transformations | None to the identifiers. Each hazard's `_RISKV` value is classed positive, zero, missing or invalid (definitions below). No smoothing, allocation, imputation or joining to population. |
| Terms | The NRI item carries FEMA's terms and conditions in its `licenseInfo`. They say the data is "meant for planning purposes only" and "for broad nationwide comparisons", that it "is not a substitute for localized risk assessment analysis", and they include a no-reverse-engineering clause and a rescind clause. Those terms were read from the item record on 2026-11-21. The FEMA web page version of the terms was not retrievable (HTTP 403 to a scripted request). |
| What is committed | Counts, per-county counts, the rating labels as reported, and a per-tract class (positive / zero / missing / invalid). **The raw NRI risk values are not committed.** `scripts/build_hazard_tract_ledger.py` regenerates them from the source. Whether to commit raw values is a team decision. |
| Privacy | Public aggregate geography only. No individual, household, address or medical data. |
| Validation state | Counts reproduced from live queries in one session by one reviewer (the script). Not independently reviewed by an agency or by a second person. |

## Class definitions

| Class | Rule (applied to `<hazard>_RISKV`) |
|---|---|
| positive | numeric and greater than 0 |
| zero | numeric and equal to 0 |
| missing | the tract is in the source layer and the value is null |
| invalid | non-numeric, negative or not finite |
| not in source | 461 universe minus the tracts present in the source layer. These GEOIDs are **not enumerated** here |

The four classes plus "not in source" account for the whole 461 universe for every hazard. The script asserts that the first four sum to the matched count.

## Results (435 matched of 461)

| Hazard (NRI field) | Matched | Positive | Zero | Missing | Invalid | Not in source |
|---|---:|---:|---:|---:|---:|---:|
| Hurricane (`HRCN_RISKV`) | 435 | 434 | 1 | 0 | 0 | 26 |
| Wildfire (`WFIR_RISKV`) | 435 | 304 | 131 | 0 | 0 | 26 |
| Tsunami (`TSUN_RISKV`) | 435 | 229 | 8 | 198 | 0 | 26 |
| Flood, coastal (`CFLD_RISKV`) | 435 | 203 | 232 | 0 | 0 | 26 |
| Flood, inland (`IFLD_RISKV`) | 435 | 433 | 2 | 0 | 0 | 26 |

Reading the table:

* All 198 missing tsunami values carry the source rating "Not Applicable". The source does not give a reason in the fields retrieved.
* Every "zero" carries the source rating "No Rating". What "No Rating" means in the NRI methodology has **not** been checked in this run, so a zero is reported as a zero, not interpreted as "no hazard".
* Flood appears twice because NRI models coastal and inland flooding as separate hazards. They are reported separately and are not combined.

## Tract-ID reconciliation reproduced in this run

* NRI: 435 records, 435 distinct valid 11-digit GEOIDs, all with prefix `15`, no duplicates.
* StateGIS layer 31: 435 records, 435 distinct GEOIDs.
* Intersection: 435. Only in NRI: 0. Only in StateGIS: 0.
* The declared width of `geoid20` is 12 characters but the stored values are 11 characters, so there is no key mismatch.
* This reproduces the 435-ID agreement recorded in `docs/EVIDENCE_REGISTER.md`. It remains an **identifier** reconciliation only.

## What this does not establish

* **Not hazard coverage of the 461 universe.** 26 tracts are not in the source and were not evaluated.
* **Modeled risk, not a hazard overlay.** NRI scores combine hazard, exposure and loss estimates at a national scale. They are not the tsunami evacuation zones, the DFIRM flood zones or any other mapped hazard footprint.
* **Not an AFN or CMIST measure.** No AFN estimate has been joined or run (see `docs/CMIST_ESTIMATION_METHOD.md`).
* **Not statewide completeness.** It says nothing about other sources, vintages or resource data.
* **Nothing about resources.** Shelter capacity, accessibility, operating status and route safety remain unknown.

## What blocked a fuller measurement

| Needed | Why not done here |
|---|---|
| The 26 Census-only GEOIDs and an independent re-check of the 461 | Census hosts (`tigerweb.geo.census.gov`, `www2.census.gov`, `api.census.gov`, `geocoding.geo.census.gov`) are blocked by the sandbox network policy. An Esri-hosted tract layer was reachable but did not answer within the time limit. The 461 and the 26 come from `docs/EVIDENCE_REGISTER.md`. |
| Reading the project's flood overlay result (`HAIC ESF6 DFIRM Overlap 435 Tracts QA`) | Its host, `services7.arcgis.com`, is blocked by the sandbox network policy. An exported table of that layer would allow its positive, zero and missing counts to be added as a separate overlay row. |
| Tsunami evacuation-zone overlay | Not attempted. It needs a defined overlay rule (any intersection, or an area threshold) and a decision on which layer is authoritative. |
| Hurricane and wildfire overlays | No overlay source has been chosen. The `Fire Risk Areas` layer is noted in `docs/EVIDENCE_REGISTER.md` as unchecked. |

## Files

| File | Contents |
|---|---|
| `ledger_summary.csv` | One row per hazard with the counts in the table above |
| `ledger_by_county.csv` | The same counts by county (five counties) |
| `ledger_ratings_as_reported.csv` | The NRI rating labels exactly as reported, with counts |
| `tract_hazard_classes.csv` | One row per matched tract with its class for each hazard (no raw scores) |
| `ledger_run.json` | Retrieval time, query URLs, response checksums, ID reconciliation, class definitions, limits |
