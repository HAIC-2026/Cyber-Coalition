# Tabletop evaluation protocol (synthetic, human-reviewed)

Status: **protocol only. No human-reviewed run has been recorded.** `data/tabletop-runs/widget_output_by_inject_set.csv` records what the tool displays; it is not a human-reviewed run.

Purpose: produce repeatable observations for Goals 2 and 3 in `docs/PLANNING_GOALS.md`, and show what changes when scenario assumptions change. Every value is a **synthetic tabletop observation**, not real-world performance.

## Fixed starting case

Use one fixed scenario packet for every run: the fictional Kapolei / Leeward Oʻahu Category 5 wind-stress tabletop already in the page. Record its version (date or commit) in `scenario_packet_version`. The Category label describes wind only. Surge, rainfall flooding, tornadoes, outages, road access, timing, footprint and participation stay separate assumptions (`docs/PROJECT_SCOPE.md`).

## Run matrix

| Condition | Injects | Purpose |
|---|---|---|
| manual baseline | none, then all | Elapsed time and elements with no tool support (Goal 3 baseline) |
| tool-supported | none (baseline case) | The starting case with no injects |
| tool-supported | each inject alone (six) | What each inject adds |
| tool-supported | all six, and each set with one removed | Interactions and what removing one changes |

The page's widget offers six injects: power interruption, communications disruption, road access disruption, language access and trusted messengers, limited connectivity in rural and visitor areas, and extended high-rise power loss with shelter in place. The last three are review prompts that are off by default. The themes of those three come from the team handover's summary of the DHS challenge. The brief itself was not re-read when they were added.

Run each cell at least twice, with at least two different reviewers where possible, so that variation between runs and between people is visible.

## Roles

| Role | Does |
|---|---|
| Facilitator | Hands over the packet, applies injects, keeps time, records the row. Does not decide. |
| Reviewer | Examines the planning option and records a disposition. Record the **role** (for example "county emergency management reviewer"), not a name. A reviewer is a reviewer only if their agency authorizes them to review; otherwise record "team member, not an authorized agency reviewer". |

## What is timed (proposed)

* **Start:** the packet is handed to the reviewer (and the injects for that run are applied).
* **Stop:** the reviewer approves a planning option containing all five required elements below. If they do not approve, record the stop as the point the run was abandoned and say so in `notes`. Do not leave the stop time blank or invent one.
* Use a stopwatch or a recorded clock; record start and stop in HST and compute `elapsed_seconds`.

## Required elements of a planning option (proposed)

| Element | Present when |
|---|---|
| Needs summary | Needs are summarized by CMIST dimension, in aggregate, with no individual classified |
| Resource questions | Each resource has a stated status, which is *unknown* unless an authoritative owner has confirmed it, with owner, date and validity |
| Evidence gaps | The gaps are listed, including capacity, accessibility, current operating status and route safety where unconfirmed |
| Human decision points | The decisions a person must make are named, with who has authority |
| Assumptions | Assumptions are listed and labeled, separate from observations and from modeled risk |

Record each element as `yes` or `no` in its own column.

## What is recorded per run

`run_id`, `run_date_hst`, `scenario_packet_version`, `condition` (manual baseline or tool-supported), `injects_active`, `reviewer_role`, `start_time_hst`, `stop_time_hst`, `elapsed_seconds`, `planning_questions_raised` (count), `evidence_gaps_exposed` (text), the five element columns, `reviewer_disposition` (accept, revise, reject, or unable to assess), `disposition_rationale`, `notes`.

## Rules that protect the evidence

1. **Report every run.** No run is dropped because it was slow, abandoned or contradicts another.
2. **Label everything synthetic.** Do not describe a tabletop result as operational performance or as proof of a time benefit in the field.
3. **No real personal data.** Use fictional details only. Do not enter real names, phone numbers, addresses or medical information, in the page or in the log.
4. **Resource status stays unknown** unless an authoritative owner confirms it in the run, and then the owner, date and validity are recorded.
5. **The tool does not decide.** A person decides shelter openings, alerts, eligibility, resource commitments and requests for assistance.
6. **Keep scopes apart.** Statewide design intent, the local Kapolei demonstration, synthetic inputs and unknown resource status are never merged into one claim.
7. **Do not set a numeric time target** until a manual baseline exists.

## How results are reported

Per run: the row. Per cell of the matrix: every run, the range of elapsed times, and the dispositions. Then state plainly what the runs do and do not show. For example, "in these runs on synthetic input, the tool-supported option reached approval in X to Y seconds against a manual baseline of A to B seconds" is a statement about those runs, with the number of runs and reviewers named. It is not a statement about real incidents.

## What this protocol does not establish

* Real-world performance, readiness or time benefit.
* That any listed resource exists, is available or is suitable.
* That an AFN estimate is correct. That needs Goal 2 reviewers.
