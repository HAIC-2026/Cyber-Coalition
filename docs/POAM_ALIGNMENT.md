# POA&M Alignment

This document maps the current working POA&M to repository artifacts. POA&M items remain open unless the stated evidence is completed and reviewed. “Gap” in this project means a planning item not yet evidenced or an agency question, not a confirmed operational deficiency.

| POA&M item | Repository implementation | Evidence still needed |
|---|---|---|
| PM-01: written challenge requirements | `PROJECT_SCOPE.md` records the reviewed four-hazard baseline, statewide county/tract target, and the PDF’s separate earthquake reference. | Team acceptance of this interpretation and any written HAIC clarification; keep earthquake outside the committed baseline unless scope is explicitly expanded. |
| PM-02: statewide framework and local pilot | `README.md`, `PROJECT_SCOPE.md`, and prototype scope tags distinguish them. | Team review that claims remain bounded to what is implemented. |
| PM-03: coverage ledger | Evidence register describes candidate sources and missingness. First hazard-side measurement (modeled risk, 435 of 461 tracts, four hazards) is in `data/hazard-tract-ledger/`; it has no CMIST dimension and no overlay measure yet. | Actual county/island × geography × hazard × CMIST × vintage coverage counts. |
| PM-04: aggregate CMIST method | Prototype shows CMIST dimensions without person-level data. | Reproducible estimation method, validation, uncertainty, assumptions, and sample output. |
| PM-05: Category 5 pilot | Prototype labels a fictional Kapolei wind-stress tabletop and separates other hazards. | Scenario packet, synthetic input set, repeatable walkthrough, and scenario review. |
| PM-06: resource status | Prototype uses proposed, confirmation requested, confirmed, stale/unavailable, and unknown states. | Current source/owner/time/validity evidence for any item labeled confirmed. |
| PM-07: county-to-state path | Prototype models the State-support step on the actual documented HI-EOP §5.3 / SESF #6 RFA-via-WebEOC pathway (county → SEOC → tasked SESF primary agency), with citations in `EVIDENCE_REGISTER.md` ("HI-EOP and SESF #6 Mass Care Annex reviewed," 2026-11-19). | HIEMA has not reviewed or confirmed this depiction matches current operational practice; no live WebEOC connection exists. The March 2022 SESF #7 Logistics annex, the November 2026 SESF #2 Communications annex currently linked from the HI-EMA index, and (for comparison) the February 2022 SESF #2 annex were all opened and reviewed directly, with findings in `HIEMA_PLAN_CROSSWALK.md`. The 2026 and 2022 SESF #2 fuel-coordination text (§4.3.3) was directly compared and found substantively unchanged. Whether a newer SESF #7 or SESF #12 annex exists beyond what the index lists remains Unknown. |
| PM-08: historical lessons | `EVIDENCE_REGISTER.md` records dated ʻIniki findings and transfer limits. | Page-check every claim and find current exercise/AAR evidence before calling any issue recurring. |
| PM-09: Datatrove/source reproduction | `EVIDENCE_REGISTER.md` treats its outputs as discovery leads. | Reproduce queries, schemas, counts, aggregations, dates, amendment logic, and checksums. |
| PM-10: performance measurement | Prototype presents proposed start/stop boundaries and says results are unmeasured. Goal definitions are in `PLANNING_GOALS.md` and the run protocol is in `TABLETOP_EVALUATION_PROTOCOL.md`; no goal result and no human-reviewed run has been recorded. | Baseline protocol, target rationale, repeatable tabletop observations, and independent review. |
| PM-11: privacy, security, accessibility, authority | `SECURITY_PRIVACY.md` and interface disclose boundaries and fail-safe unknowns. | Project-specific review, accessible/multilingual review, and security/privacy statement within submission limits. |
| PM-12: package assembly | Root README and docs establish the initial package. | Final source index, evidence matrix, method, scenario outputs, and judge instructions. |
| PM-13: video and form | Not implemented in repository. | Complete the HAIC Project Submission Form; provide a functional evaluation video explaining the AI plan (maximum 10 minutes or 50 MB); provide the solution-specific security/privacy description (maximum 300 words); confirm the completed plan and supporting resources are accessible to reviewers. |
| PM-14: team review | Not implemented in repository. | Team member/owner confirmation and recorded review. |
| PM-15: tools and access | README links to the Esri HAIC Resource Hub and the Hawaiʻi StateGIS organization/Map Viewer; no keys or account secrets are stored. Team lead reports Datatrove Pro subscription and Esri $25 voucher registration. | Verify Datatrove MCP access is enabled for the registered email, check available plan limits/renewal, and confirm ArcGIS voucher activation/credit status. The separate ArcGIS reference map's sharing was changed and reconfirmed **public** on 2026-11-19 via an anonymous Esri Portal REST API check (see `docs/EVIDENCE_REGISTER.md`), superseding the Owner-only / unverified-judge-access status recorded here on 2026-11-14. Dependent StateGIS source-layer access was not separately rechecked. Keep credentials out of GitHub and the submission form. |

## Acceptance checks for this draft

- A reviewer can distinguish statewide design intent from the Kapolei pilot.
- The core hazard baseline follows the challenge PDF’s explicit four-hazard scope and metric sections; the earthquake reference in Section 4 remains visible as an unresolved interpretation question.
- Fictional wind category remains separate from other hazard assumptions.
- Every operational status shown as confirmed has a current, attributable source; otherwise it remains unknown or simulated.
- Historical ʻIniki material is described as historical evidence and does not prove a present-day recurring gap.
- Source geography, date, masking, and uncertainty remain visible.
- The demo has no personal records, secrets, live integrations, or operational decision authority.
- No measured performance or statewide completeness is claimed without results.


| PM-16: ArcGIS reference map and OHCA site/license reconciliation | The separate map displays 26 layer-list entries and a `Hospital - Review` table; [`SITE_LICENSE_RECONCILIATION.md`](SITE_LICENSE_RECONCILIATION.md) records 39 source records, 37 address-coordinate keys, separate license associations, privacy exclusions, and unresolved source conflicts. Item sharing reconfirmed public 2026-11-19 (see evidence register); reviewer access resolved for the three checked ArcGIS Online items. | Confirm site identity, separate license records, source-defined status and capacity units, current license state, provider terms, all layer wiring, and dependent StateGIS source-service access with authoritative owners. Do not claim capacity, operations, or current availability from this extract. |

## Current evidence note (2026-11-14)

The ArcGIS Map Viewer currently shows 26 layer-list entries (10 Kapolei QA/boundary plus 16 statewide/reference layers) and one `Hospital - Review` table. The statewide tract comparison is 461 Census GEOIDs, 435 exact candidate StateGIS/SVI matches, and 26 Census-only zero-population/zero-housing GEOIDs; tract 9812 is one of the 26. Base geography matching does not close hazard-specific coverage. The functional evaluation video remains pending team production; final form submission and team review are open.
