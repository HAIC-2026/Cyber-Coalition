# POA&M Alignment

This document maps the current working POA&M to repository artifacts. POA&M items remain open unless the stated evidence is completed and reviewed. “Gap” in this project means a planning item not yet evidenced or an agency question, not a confirmed operational deficiency.

| POA&M item | Repository implementation | Evidence still needed |
|---|---|---|
| PM-01: written challenge requirements | `PROJECT_SCOPE.md` flags the kickoff-versus-matrix hazard discrepancy. | Page-level requirements-to-evidence matrix from the challenge PDF, including exact hazards, geography, and metrics. |
| PM-02: statewide framework and local pilot | `README.md`, `PROJECT_SCOPE.md`, and prototype scope tags distinguish them. | Team review that claims remain bounded to what is implemented. |
| PM-03: coverage ledger | Evidence register describes candidate sources and missingness. | Actual county/island × geography × hazard × CMIST × vintage coverage counts. |
| PM-04: aggregate CMIST method | Prototype shows CMIST dimensions without person-level data. | Reproducible estimation method, validation, uncertainty, assumptions, and sample output. |
| PM-05: Category 5 pilot | Prototype labels a fictional Kapolei wind-stress tabletop and separates other hazards. | Scenario packet, synthetic input set, repeatable walkthrough, and scenario review. |
| PM-06: resource status | Prototype uses proposed, confirmation requested, confirmed, stale/unavailable, and unknown states. | Current source/owner/time/validity evidence for any item labeled confirmed. |
| PM-07: county-to-state path | Prototype labels the State-support step simulated. | Verify roles and request pathway against current official state and county plans. |
| PM-08: historical lessons | `EVIDENCE_REGISTER.md` records dated ʻIniki findings and transfer limits. | Page-check every claim and find current exercise/AAR evidence before calling any issue recurring. |
| PM-09: Datatrove/source reproduction | `EVIDENCE_REGISTER.md` treats its outputs as discovery leads. | Reproduce queries, schemas, counts, aggregations, dates, amendment logic, and checksums. |
| PM-10: performance measurement | Prototype presents proposed start/stop boundaries and says results are unmeasured. | Baseline protocol, target rationale, repeatable tabletop observations, and independent review. |
| PM-11: privacy, security, accessibility, authority | `SECURITY_PRIVACY.md` and interface disclose boundaries and fail-safe unknowns. | Project-specific review, accessible/multilingual review, and security/privacy statement within submission limits. |
| PM-12: package assembly | Root README and docs establish the initial package. | Final source index, evidence matrix, method, scenario outputs, and judge instructions. |
| PM-13: video and form | Not implemented in repository. | Verify submission limits and produce accessible video/form artifacts. |
| PM-14: team review | Not implemented in repository. | Team member/owner confirmation and recorded review. |
| PM-15: tools and access | README links to team ArcGIS resources; no keys or account secrets stored. | Track Datatrove Pro account/renewal and separately confirm ArcGIS voucher entitlement; protect credentials. |

## Acceptance checks for this draft

- A reviewer can distinguish statewide design intent from the Kapolei pilot.
- Fictional wind category remains separate from other hazard assumptions.
- Every operational status shown as confirmed has a current, attributable source; otherwise it remains unknown or simulated.
- Historical ʻIniki material is described as historical evidence and does not prove a present-day recurring gap.
- Source geography, date, masking, and uncertainty remain visible.
- The demo has no personal records, secrets, live integrations, or operational decision authority.
- No measured performance or statewide completeness is claimed without results.
