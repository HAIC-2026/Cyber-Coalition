# Evidence Register

This register records candidate evidence and what it can support. The originating agency source is the authority for dataset facts. Datatrove and AI-generated summaries help discover and organize sources; they do not independently validate the underlying data. Confirm exact versions, fields, retrieval dates, and page references before submission.

## Historical hurricane evidence

| Source | Source-reported finding | Appropriate use | Limit |
|---|---|---|---|
| [Hurricane ʻIniki Assessment (1993), USACE/FEMA/State of Hawaiʻi](https://coast.noaa.gov/data/hes/docs/postStorm/H_INIKI_ASSESSMENT_REVIEW_HES_UTILIZATION_INFO_DISSEMINATION.pdf) | The report describes past evacuation, public sheltering, and information-distribution observations, including shelter manager staffing, EOC communications, parking, pet messaging, restroom access for people with disabilities, public notice of open sites, and clarity about unavailable medical support. It reports about 30,000 shelter users compared with an earlier estimate around 80,000 and notes the difference is difficult to explain without a post-storm behavior study. | Build test cases and validation questions for demand assumptions, accessibility, staffing, communications, and shelter-status confirmation. | Findings concern the 1992 event and 1993 report. They do not establish current conditions or a recurring gap. Check page references in the source before quoting. |
| [NWS Natural Disaster Survey Report: Hurricane ʻIniki (1993)](https://www.weather.gov/media/publications/assessments/iniki1.pdf) | The report includes findings and recommendations concerning hurricane shelter criteria. | Test whether candidate facilities are appropriate for the modeled hurricane conditions and distinguish hurricane suitability from other shelter designations. | Historical recommendation; do not imply present-day noncompliance or current unsuitability without current evidence. |

The historical reports are primary evidence of what those reports recorded, not proof that a problem persists. Any claim that a condition is recurring requires more recent, relevant corroboration, such as a current plan, exercise evaluation, after-action report, or agency-confirmed status.

## Candidate public data

| Source | Potential planning use | Known limitation / validation requirement |
|---|---|---|
| [FEMA National Risk Index](https://www.fema.gov/about/openfema/data-sets/national-risk-index-data) | Modeled hazard and risk context by supported geography. | Preserve dataset vintage and exact hazard fields. Expected annual loss and risk ratings are modeled context, not event forecasts or shelter capacity. Keep these separate from fictional scenario severity. |
| [HHS emPOWER Map](https://empowerprogram.hhs.gov/about-empowermap.html) and [de-identified data job aid](https://empowerprogram.hhs.gov/De-Identified-Dataset-Job-Aid.pdf) | Aggregate context for certain electricity-dependent Medicare beneficiaries and selected services. | Medicare population only; geography and monthly vintage matter; small cells are suppressed. Do not split ZIP values to census tracts or infer individuals. |
| [CDC Social Vulnerability Index](https://www.atsdr.cdc.gov/place-health/php/svi/index.html) | Aggregate neighborhood context for planning equity and access considerations. | Verify release, source variables, and geography. SVI is not an individual assessment or direct service-need count. |
| [State Civil Defense Hurricane Shelters CSV](https://opendata.hawaii.gov/dataset/702fa548-5ef8-419a-9038-11628078e2b0/resource/80923691-94fc-4867-a8cc-c5f2ab2d0b1d/download/state-civil-defense-hurricane-shelters-csv.csv) | Candidate designated shelter locations and source flags for a preliminary map. | Current source date, row count, flag meaning, capacity, accessibility, staffing, wind suitability, opening status, and availability are unresolved. Location listing does not prove operational readiness. |
| [FEMA Mission Assignments v2](https://www.fema.gov/openfema-data-page/mission-assignments-v2) | Historical federal mission-assignment records for context on federal support. | Verify schema and code semantics. Obligations are not actual costs; this is not a complete state/county ESF activation record or measure of response effectiveness. |
| [FEMA Disaster Declarations](https://www.fema.gov/openfema-data-page/fema-web-disaster-declarations-v1) and [Public Assistance Projects](https://www.fema.gov/openfema-data-page/public-assistance-funded-projects-details-v2) | Historical incidents and funded assistance context. | Reproduce counts, periods, amendments, and geography. Declaration/project records alone do not establish unmet mass-care needs or causal lessons. |
| [Hawaiʻi Statewide GIS Hub](https://hawaiihub.maps.arcgis.com/apps/mapviewer/index.html) | ArcGIS map and geospatial layer discovery. | Read each layer's item details, owner, source, update date, licensing, geometry, and fields. The current user map shown in the project context contains business/economy content and is not the ESF-6 project map. |

## Open questions, not confirmed deficiencies

The current catalog review did not locate an authoritative, complete record for shelter capacity and current accessibility, up-to-date hurricane suitability and opening status, current county-to-state workflow, exercise corrective actions, mutual aid resource typing, or EOC activation records. Catalog absence is not proof that records do not exist. The project should use public/shareable records or synthetic demonstration data and label unavailable fields as unknown.

## Evidence record for each future claim

Record source title and owner, exact URL/item ID, source date and retrieval timestamp with timezone, native geography, fields used, query/filter, transformation, checksum or version when available, source-reported content, independent validation state, confidence, limitations, and the requirement or test informed. Separate source finding, inference, scenario assumption, proposed requirement, and agency question.
