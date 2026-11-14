# HAIC 2026 Cyber Coalition

**Working project:** DHS Enhanced ESF-6 planning through AI-supported insights  
**Team:** Cyber Coalition  
**Status:** Working implementation and planning package for team review. This repository and prototype are not approved by DHS, HI-EMA, Honolulu DEM, or another emergency-management authority.

## Mission

Develop a privacy-preserving, evidence-traceable planning workflow that helps emergency planners consider where people may need mass care or related assistance, estimate aggregate needs, identify information and resource gaps, and prepare human-reviewed coordination options. AI may assist with data discovery and analysis. Authorized people retain every operational decision.

## Scope

- **Planning framework:** statewide, designed for all Hawaiʻi counties and islands, all five CMIST dimensions, and rural, urban, off-grid, and visitor communities. The DHS challenge PDF’s scope and measurable-goal sections (pp. 5–7) specify four core hazards—hurricane, wildfire, tsunami, and flood—with hazard-specific AFN mapping for every county and a 100% census-tract coverage target. Section 4 also mentions earthquake; this conflicting reference remains an explicit scope question. The working baseline follows the four-hazard scope and metric language; the pilot does not demonstrate statewide coverage.
- **First demonstrator:** a fictional Category 5 hurricane wind-stress scenario in Kapolei / Leeward Oʻahu, within the City and County of Honolulu. This demonstrates the method in one bounded area; it does not validate statewide data coverage or operational readiness.
- **ESF-6 alignment:** mass care, emergency assistance, housing, and human services planning, coordinated through the county-led response model described in the kickoff. Exact roles and procedures must be checked against current official plans.
- **Data boundary:** public, aggregate, de-identified, or synthetic data only. No personal information, identifiable client records, individual registries, restricted operational data, or live government-system integrations.

Category 5 describes the Saffir-Simpson maximum sustained wind category (157 mph or greater). It does not define storm surge, rainfall flooding, tornadoes, outages, local impacts, or forecast certainty. Those are separate scenario inputs. This is a fictional tabletop, not a forecast, warning, order, or recommendation for real-world action.

## Demonstration workflow

The implementation follows the six-step planning method captured in the project POA&M:

1. Define the objective and call to action.
2. Set the scenario, location, and backstory.
3. Identify stakeholders, roles, and usable data.
4. Analyze themes and potential root causes from cited evidence.
5. Develop feasible scenarios and decision points.
6. Specify the proposed plan and workflow, including owners, open questions, and measures.

The pilot should make source dates, native geography, assumptions, uncertainty, and unknown values visible. A candidate shelter is not treated as open, suitable, accessible, staffed, or available unless a current authoritative source confirms that exact attribute.

## Repository contents

| Path | Purpose |
|---|---|
| [`web/index.html`](web/index.html) | Standalone, no-build planning prototype. |
| [`docs/PROJECT_SCOPE.md`](docs/PROJECT_SCOPE.md) | Mission, geographic scope, hazard and authority boundaries. |
| [`docs/POAM_ALIGNMENT.md`](docs/POAM_ALIGNMENT.md) | Mapping from POA&M items to implementation and acceptance evidence. |
| [`docs/EVIDENCE_REGISTER.md`](docs/EVIDENCE_REGISTER.md) | Source-backed historical findings, candidate data, and validation state. |
| [`docs/SECURITY_PRIVACY.md`](docs/SECURITY_PRIVACY.md) | Data handling, AI limits, source integrity, and fail-safe behavior. |
| [`docs/SITE_LICENSE_RECONCILIATION.md`](docs/SITE_LICENSE_RECONCILIATION.md) | Public-safe Kapolei OHCA record-to-site and separate-license crosswalk. |
| [`data/README.md`](data/README.md) | Rules for source records and future public/synthetic data extracts. |

## Open the prototype

Open `web/index.html` in a current browser. It has no server requirement, external JavaScript libraries, API calls, credentials, or live operational integrations. The present interface is a planning concept and may contain static source summaries; verify source claims before using them in a submission.

ArcGIS and HAIC resources:

- [HAIC DHS challenge PDF](https://haic.hawaii.gov/wp-content/uploads/2026/10/HAIC_AI-Challenge_Submission_DHS_Disaster_2026.pdf)
- [HAIC judging criteria and submission rules](https://haic.hawaii.gov/haic-judging-criteria/)
- [Esri HAIC Resource Hub](https://esri-haic-histategis.hub.arcgis.com/)
- [Hawaiʻi StateGIS Hub Community organization](https://hawaiihub.maps.arcgis.com/home/index.html)
- [Map Viewer in the Hawaiʻi StateGIS organization](https://hawaiihub.maps.arcgis.com/apps/mapviewer/index.html)
- [My Content in the Hawaiʻi StateGIS organization](https://hawaiihub.maps.arcgis.com/home/content.html)

The project has a separate ArcGIS reference map: [Cyber Coalition ESF-6 Hawaiʻi Hazard Reference Map](https://hawaiihub.maps.arcgis.com/home/item.html?id=d7b64dfd6e5a4e7589be7bcfbe355ad0). It is a reference artifact and is not integrated into this static prototype. The current ArcGIS item Details panel shows Sharing: Owner; external judge access remains untested. Review layer provenance, ownership, terms, geography, and privacy limits before relying on map content.

**Current build snapshot (2026-11-14):** The separate [ArcGIS reference map](https://hawaiihub.maps.arcgis.com/home/item.html?id=d7b64dfd6e5a4e7589be7bcfbe355ad0) displays 26 layer-list entries (10 Kapolei QA/boundary items and 16 statewide/reference layers) plus one `Hospital - Review` table. Its Kapolei OHCA QA table shows 39 source records and 37 address-coordinate reconciliation keys, not 37 certified sites. Site/license associations, source IDs, and unresolved exceptions are documented in [`docs/SITE_LICENSE_RECONCILIATION.md`](https://github.com/HAIC-2026/Cyber-Coalition/blob/main/docs/SITE_LICENSE_RECONCILIATION.md). All 39 source operational-status values are `0` without a published domain; meaning is unresolved. The facility-capacity field has no defined units and is not treated as validated capacity. The current ArcGIS item Details panel shows Sharing: Owner; external judge access remains untested. No source features were edited. Tract inventory: 461 2020 Census GEOIDs; 435 exact matches in each candidate StateGIS Census and Coastal SVI set; 26 Census-only zero-population/zero-housing GEOIDs, with tract 9812 one of the 26. This is not hazard-coverage validation. The public repo is updated; the team functional-evaluation video and final form submission remain pending.



## Evidence and validation status

The 1993 Hurricane ʻIniki assessments provide historical Oʻahu/Kauaʻi hurricane evidence. They support questions and test cases around shelter suitability, communications, staffing, accessibility, and public information. They do not establish that the same conditions exist today. The current shelter CSV is a candidate-location source with unresolved date, count, flag meanings, capacity, accessibility, staffing, and current status. HHS emPOWER counts are limited to their published geography and suppression rules; ZIP counts must not be split into tracts. FEMA NRI risk outputs remain separate from fictional scenario severity.

Datatrove is a discovery and analysis workbench, not the authority for a claim. Retain the originating dataset/report, query, retrieval time, schema, transformation, and review outcome. See the evidence register and POA&M for open validation tasks.

## Development status

The written DHS challenge PDF has been reviewed. The working baseline is four hazards, with the PDF’s separate earthquake mention recorded as an unresolved scope question. Remaining work includes validating source counts and schemas with owners, adding source-linked scenario inputs, defining and validating an aggregate CMIST estimation method, confirming current county/State procedures from official plans, completing the statewide hazard-specific coverage ledger, measuring a repeatable tabletop, and confirming map/reviewer access. Planned statewide coverage must not be described as completed coverage. Performance and operational benefits have not been measured. HAIC’s technical-review requirements also include a completed plan with access to supporting resources, a functional evaluation video (maximum 10 minutes or 50 MB), and a solution-specific security/privacy description limited to 300 words; see the official judging criteria.
