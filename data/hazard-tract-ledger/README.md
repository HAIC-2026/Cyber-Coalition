# Hazard-by-hazard tract ledger (data provenance)

Status: **first measurement.** Five rows are modeled risk and one row is a project-produced flood overlay, kept apart. None of it is AFN or CMIST coverage, and none of it is operational readiness.

Everything here is produced by `scripts/build_hazard_tract_ledger.py`. Re-running it re-queries the sources and rewrites these files. Values are expected to be identical unless a source layer has changed; the retrieval timestamps and checksums in `ledger_run.json` show whether it did.

## Provenance (the checklist from `data/README.md`)

| Item | Record |
|---|---|
| Modeled-risk source | FEMA National Risk Index, Census Tracts feature service, item `9da4eeb936544335a6db0cd7a8448a51` (owner `FEMA_NationalRiskIndex`, public). Layer: `https://services.arcgis.com/XG15cJAlne2vxtgt/arcgis/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0`. `NRI_VER` = "December 2025" for all 435 Hawaii records. |
| Tract universe | Census TIGERweb, Census 2020 Tracts_Blocks MapServer layer 0 (`STATE='15'`): 461 records. Retrieved in this run. |
| Identifier cross-check | Hawaii Statewide GIS Program, 2020 Census Tracts, `https://geodata.hawaii.gov/arcgis/rest/services/Census/MapServer/31` (435 records, identifiers only) |
| Overlay source | The project's own ArcGIS Online results, read-only: `HAIC ESF6 DFIRM SFHA_TF by 435 Tracts QA 2026 11 17` (web map `a090abe420f041ffb03d3356035ddd64`; layer 0 and the GroupBySummary table, `435` tracts and `736` summary rows). It is a Summarize Within output produced by a team member. It was **not recomputed** here. |
| Retrieved | 2026-11-21 01:44:34 UTC (2026-11-20 15:44:34 HST) |
| Native geography | 2020 Census tract (11-digit GEOID); Hawaii state FIPS `15` |
| Fields used | NRI: `TRACTFIPS`, `STCOFIPS`, `NRI_VER`, and `<hazard>_RISKV` / `<hazard>_RISKR` for `HRCN`, `WFIR`, `TSUN`, `CFLD`, `IFLD`. Census: `GEOID`, `COUNTY`, `POP100`, `HU100`. DFIRM result: `geoid20`, `Join_ID`, `sfha_tf`, `sum_Area_SquareMiles`, `Polygon_Count`. |
| Query | Attribute-only queries, no geometry requested. Exact URLs and response SHA-256 values are in `ledger_run.json`. |
| Transformations | None to identifiers. Each risk value is classed positive, zero, missing or invalid. The overlay is classed from the group-by table joined to tracts by `Join_ID`. No smoothing, allocation, imputation or population join. |
| Terms | The NRI item carries FEMA's terms and conditions in its `licenseInfo`. They say the data is "meant for planning purposes only" and "for broad nationwide comparisons", that it "is not a substitute for localized risk assessment analysis", and they include a no-reverse-engineering clause and a rescind clause. Read from the item record on 2026-11-21; the FEMA web page version was not retrievable (HTTP 403 to a scripted request). Census and StateGIS terms were not separately reviewed. |
| What is committed | Counts, per-county counts, rating labels as reported, a per-tract class (positive / zero / missing / invalid), and the 26 Census-only tracts with their 2020 counts. **Raw NRI risk values are not committed**; the script regenerates them. Whether to commit raw values is a team decision. |
| Privacy | Public aggregate geography only. No individual, household, address or medical data. |
| Validation state | Counts reproduced from live queries in one session by one reviewer (the script). Not independently reviewed by an agency or a second person. |

## Class definitions

| Class | Rule |
|---|---|
| positive (risk) | `<hazard>_RISKV` is numeric and greater than 0 |
| zero (risk) | `<hazard>_RISKV` is numeric and equal to 0 |
| missing (risk) | the tract is in the source layer and the value is null |
| invalid (risk) | non-numeric, negative or not finite |
| positive (overlay) | the tract has a DFIRM polygon with `sfha_tf='T'` and a summed area greater than 0 |
| zero (overlay) | the tract has DFIRM polygons but none with `sfha_tf='T'` (only `'F'`) |
| missing (overlay) | the tract has no row in the group-by table |
| invalid (overlay) | a flag other than T or F, or a negative or null area or count |
| not in source | the Census universe minus the tracts present in the source layer. Listed in `census_only_tracts_not_evaluated.csv` |

For every row, positive + zero + missing + invalid equals the matched count, and the script asserts it.

## Results (435 matched of 461)

Modeled risk (FEMA NRI):

| Hazard (field) | Matched | Positive | Zero | Missing | Invalid | Not in source |
|---|---:|---:|---:|---:|---:|---:|
| Hurricane (`HRCN_RISKV`) | 435 | 434 | 1 | 0 | 0 | 26 |
| Wildfire (`WFIR_RISKV`) | 435 | 304 | 131 | 0 | 0 | 26 |
| Tsunami (`TSUN_RISKV`) | 435 | 229 | 8 | 198 | 0 | 26 |
| Flood, coastal (`CFLD_RISKV`) | 435 | 203 | 232 | 0 | 0 | 26 |
| Flood, inland (`IFLD_RISKV`) | 435 | 433 | 2 | 0 | 0 | 26 |

Overlay (project DFIRM result):

| Measure | Matched | Positive | Zero | Missing | Invalid | Not in source |
|---|---:|---:|---:|---:|---:|---:|
| Flood, SFHA overlay (`sfha_tf='T' area (project DFIRM result)`) | 435 | 306 | 129 | 0 | 0 | 26 |

Reading the tables:

* All 198 missing tsunami values carry the source rating "Not Applicable". The source gives no reason in the fields retrieved.
* Every risk "zero" carries the source rating "No Rating". What "No Rating" means in the NRI method has **not** been checked, so a zero is reported as a zero, not interpreted as "no hazard".
* Flood appears three times: NRI models coastal and inland flooding separately, and the project's DFIRM overlay is a different kind of measure. They are not combined and the modeled-risk rows are not substitutes for the overlay row.
* The overlay's "zero" means the summarized DFIRM polygons have no `sfha_tf='T'` area in that tract. It does not mean no flooding can occur there.
* In the overlay result, the T and F areas together cover 96.3% to 100% of every tract's analysis area, so the DFIRM polygons span the whole tract and there are no coverage gaps.
* The meaning of `sfha_tf` is taken from the layer's name. It has not been checked against FEMA NFHL metadata here, and the DFIRM input item and vintage are not recorded on the project's item (open in the project's own QA note).

## Tract reconciliation reproduced in this run

* NRI: 435 records, 435 distinct valid 11-digit GEOIDs, all prefix `15`, no duplicates.
* StateGIS layer 31: 435 records, 435 distinct. Intersection with NRI 435; only in NRI 0; only in StateGIS 0.
* Census 2020 universe: **461** distinct valid GEOIDs, all prefix `15`. Intersection with NRI 435. Only in NRI: 0. **Census-only: 26**, and all 26 have `POP100=0,HU100=0` in the 2020 enumeration.
* 29 tracts overall have zero population and zero housing; 3 of them are in NRI (`15003980000`, `15003980700`, `15009980000`). This matches what `docs/EVIDENCE_REGISTER.md` recorded on 2026-11-18, now reproduced independently.
* The project's DFIRM layer holds exactly the same 435 GEOIDs as NRI (True). Its summary table joins to tracts with 0 orphan rows and 0 duplicate (tract, flag) pairs.
* The declared width of StateGIS `geoid20` is 12 characters but the stored values are 11, so there is no key mismatch.
* Zero Census population and housing describes the 2020 enumeration only. It does not establish zero need, and these 26 tracts remain unevaluated, not zero.

## What this does not establish

* **Not hazard coverage of the whole universe.** 26 of 461 tracts are not in the risk source or in the project's overlay and were not evaluated.
* **Modeled risk is not a hazard overlay.** NRI scores combine hazard, exposure and loss estimates at a national scale. They are not the tsunami evacuation zones, the DFIRM zones or any other mapped footprint.
* **Not an AFN or CMIST measure.** No AFN estimate has been joined or run (`docs/CMIST_ESTIMATION_METHOD.md`).
* **Only flood has an overlay row.** Tsunami, hurricane and wildfire have modeled risk only.
* **Nothing about resources.** Shelter capacity, accessibility, operating status and route safety remain unknown.

## What a fuller measurement still needs

| Needed | Status |
|---|---|
| Tsunami overlay (evacuation zones) | Not done. Needs a decision on the authoritative layer (the Honolulu emergency-management item or the statewide StateGIS layers) and on the overlay rule (any intersection, or an area threshold), plus tract geometry. |
| Hurricane and wildfire overlays | No overlay source has been chosen. The StateGIS `Fire Risk Areas` layer is noted in `docs/EVIDENCE_REGISTER.md` as unchecked. |
| DFIRM input item and vintage | Not recorded on the project's item; the project's own QA note lists it as open. |
| NRI "No Rating" and "Not Applicable" definitions | To be checked against the NRI technical documentation. |
| Second-person review of this ledger | Not done. |

## Files

| File | Contents |
|---|---|
| `ledger_summary.csv` | One row per measure, with its type and the counts above |
| `ledger_by_county.csv` | The same counts by county |
| `ledger_ratings_as_reported.csv` | The NRI rating labels exactly as reported, with counts |
| `tract_hazard_classes.csv` | One row per matched tract with its class for each hazard and for the flood overlay (no raw scores) |
| `census_only_tracts_not_evaluated.csv` | The 26 Census-only tracts with their 2020 population and housing counts |
| `ledger_run.json` | Retrieval time, query URLs, response checksums, reconciliation, class definitions, limits |
