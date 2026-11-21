# Measurable planning goals: baseline, target, method, result

Status: **definitions only. No goal result has been measured.** The Result column is blank on purpose and stays blank until a run produces it. Targets marked *proposed* are the team's to set or change; they are not outcomes and not agency commitments.

How to read the columns:

* **Baseline** is what the repository shows today. It describes this repository, not the world.
* **Target (source)** says where a target came from. A target taken from the DHS challenge is source-reported. A target the team proposes is labeled *proposed* and is not from the brief.
* **Method** is the repeatable way to produce the result.
* **Result** is blank until measured. An interim indicator is never the result.

The three goals follow the DHS challenge as summarized in `docs/PROJECT_SCOPE.md` (Goal 1) and in the team handover (Goals 2 and 3). The DHS PDF itself was not re-read when this file was written, so its exact wording should be checked before the goals are quoted in the submission.

## Goal 1: hazard-specific AFN maps for every county and tract

| Item | Record |
|---|---|
| Statement | Hazard-specific AFN vulnerability maps for hurricane, wildfire, tsunami and flood, for every county, reaching all census tracts |
| Baseline (repository, 2026-11-21) | No AFN-by-hazard tract map is produced by this repository. The CMIST aggregate estimate method is a draft and "nothing in this method has been run" (`docs/CMIST_ESTIMATION_METHOD.md`). |
| Interim indicator (not the result) | Hazard-side modeled-risk values exist for 435 of the 461 tracts for each hazard (`data/hazard-tract-ledger/`). This is an input to the goal. It is not an AFN measure and not the goal's result. |
| Target (source-reported) | 100% of census tracts, every county, per `docs/PROJECT_SCOPE.md` (challenge PDF pp. 5-7) |
| Method (proposed) | For each hazard, count tracts that have both (a) a valid hazard value or overlay result and (b) an AFN estimate from the documented CMIST method that a reviewer has examined, and divide by the 461 official tracts. Report positive, zero, missing, invalid and not-evaluated counts separately for every hazard, and list the tracts not evaluated. Keep modeled risk, hazard overlays and the fictional scenario assumptions in separate columns. |
| Result | *Not measured.* |
| Known limits | 26 tracts are not in the risk source and their GEOIDs are not yet enumerated. Overlay measures (tsunami zones, DFIRM) are not yet in the ledger. ZIP-level emPOWER counts must not be allocated to tracts arbitrarily (`data/README.md`). |

## Goal 2: CMIST needs estimates reviewed for reasonableness by authorized partners

| Item | Record |
|---|---|
| Statement | CMIST need estimates are reviewed for reasonableness by authorized county, DHS and partner reviewers |
| Baseline (repository, 2026-11-21) | No CMIST estimate has been run, so none has been reviewed. |
| Target (*proposed*, not from the brief) | Every CMIST estimate shown to a user carries a recorded reviewer disposition (accept, revise, reject, or unable to assess), a rationale and a date, from at least one authorized county or DHS reviewer. No estimate is described as validated without one. |
| Method (proposed) | A reviewer worksheet with one line per estimate: dimension, proxy, source vintage, base, low, high, uncertainty, reviewer role, disposition, rationale, date. Report the count of estimates by disposition, and the count with no disposition. |
| Result | *Not measured.* |
| Known limits | Reviewers must be authorized by their agencies, and no reviewer has been engaged in this repository. Aggregate estimates describe planning needs and never classify a person. |

## Goal 3: shorter time to a coordinated needs-and-resources planning option

| Item | Record |
|---|---|
| Statement | Less elapsed time to produce a coordinated needs-and-resources planning option |
| Baseline | *Not measured.* Protocol: one reviewer produces a planning option for the same synthetic Kapolei scenario packet with no tool support, timed. |
| Start and stop (*proposed*) | Start when the scenario packet is handed to the reviewer. Stop when the reviewer approves a planning option that contains every required element below. |
| Required elements (*proposed*) | (1) a needs summary by CMIST dimension; (2) resource questions, each with status unknown unless an authoritative owner has confirmed it; (3) a list of evidence gaps; (4) the human decision points; (5) the assumptions, labeled. |
| Target (*proposed*) | The tool-supported run reaches the same stop condition in less time than the manual baseline, with every required element present and a human approval. A numeric threshold is not set until a baseline exists. |
| Method (proposed) | Repeat the manual and the tool-supported runs on the same case, with and without each inject. Report every run, not the best one, with start time, stop time, elapsed seconds, elements present and reviewer disposition. See `docs/TABLETOP_EVALUATION_PROTOCOL.md`. |
| Result | *Not measured.* |
| Known limits | Tabletop runs on synthetic inputs are observations of a method. They are not real-world performance and do not show an operational time benefit. |

## What would change a status here

| Status | Evidence needed |
|---|---|
| Goal 1 result | A reviewed AFN estimate joined to a valid hazard value for each counted tract, per hazard, with the 26 unevaluated tracts accounted for |
| Goal 2 result | Reviewer worksheets with dispositions from authorized reviewers |
| Goal 3 baseline and result | Timed manual and tool-supported runs recorded in `data/tabletop-runs/` |
