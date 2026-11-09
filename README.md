# HAIC 2026 Cyber Coalition

**Working project:** DHS Enhanced ESF-6 planning through AI-supported insights  
**Team:** Cyber Coalition  
**Status:** Initial implementation draft for team review. This repository and prototype are not approved by DHS, HI-EMA, Honolulu DEM, or another emergency-management authority.

## Mission

Develop a privacy-preserving, evidence-traceable planning workflow that helps emergency planners consider where people may need mass care or related assistance, estimate aggregate needs, identify information and resource gaps, and prepare human-reviewed coordination options. AI may assist with data discovery and analysis. Authorized people retain every operational decision.

## Scope

- **Planning framework:** statewide, designed to account for all Hawaiʻi counties and islands, the five hazards described in the challenge kickoff, all five CMIST dimensions, and rural, urban, and visitor communities. The written challenge PDF and exact required metrics still need page-level reconciliation before these are called final requirements.
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
| [`data/README.md`](data/README.md) | Rules for source records and future public/synthetic data extracts. |

## Open the prototype

Open `web/index.html` in a current browser. It has no server requirement, external JavaScript libraries, API calls, credentials, or live operational integrations. The present interface is a planning concept and may contain static source summaries; verify source claims before using them in a submission.

ArcGIS resources for the team:

- [ArcGIS Online](https://www.arcgis.com/home/index.html)
- [Hawaiʻi State GIS Hub Map Viewer](https://hawaiihub.maps.arcgis.com/apps/mapviewer/index.html)

The currently open map contains business/economy layers and is outside this project prototype. Do not treat it as the ESF-6 project map or modify it as part of this draft. A project map should be created separately after layer provenance, ownership, licensing, and field limits are recorded.

## Evidence and validation status

The 1993 Hurricane ʻIniki assessments provide historical Oʻahu/Kauaʻi hurricane evidence. They support questions and test cases around shelter suitability, communications, staffing, accessibility, and public information. They do not establish that the same conditions exist today. The current shelter CSV is a candidate-location source with unresolved date, count, flag meanings, capacity, accessibility, staffing, and current status. HHS emPOWER counts are limited to their published geography and suppression rules; ZIP counts must not be split into tracts. FEMA NRI risk outputs remain separate from fictional scenario severity.

Datatrove is a discovery and analysis workbench, not the authority for a claim. Retain the originating dataset/report, query, retrieval time, schema, transformation, and review outcome. See the evidence register and POA&M for open validation tasks.

## Development status

This is a first working structure, not a complete submission. Required next work includes reconciling the written challenge PDF, reproducing source counts, adding source-linked scenario inputs, defining an aggregate CMIST estimation method, confirming current county/state workflow from public plans, and measuring a repeatable tabletop. Planned statewide coverage must not be described as completed coverage. Performance and operational benefits have not been measured.
