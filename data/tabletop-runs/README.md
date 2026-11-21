# Tabletop run evidence

Everything in this folder is a **synthetic tabletop observation**. None of it is real-world performance, an operational time benefit, or a statement about any agency, shelter, route or resource.

## Files

| File | What it is | Who or what produced it |
|---|---|---|
| `widget_output_by_inject_set.csv` | What the page's tabletop widget displays for 15 inject combinations (baseline, the default three, each single inject, each set with one inject removed, all six) | `scripts/capture_tabletop_widget_output.js` reads the rendered page. It is **tool output only**: no person reviewed it, and it records no decision and no elapsed time. |
| `run_log_template.csv` | The column layout for a human-reviewed run. **It contains no runs.** | Filled in by the facilitator and reviewer during a real tabletop. |

## What the widget capture shows (measured, deterministic)

* With no injects the page shows a placeholder prompt and **0** review questions.
* Each inject adds exactly one fixed review question, so N active injects display N questions, for every combination captured. The three original injects each add a question, and so do the three review prompts added later (language access and trusted messengers; limited connectivity in rural and visitor areas; extended high-rise power loss and shelter in place).
* The page does not calculate demand, choose actions, or assume any resource status. It flags questions for a human.

What it does **not** show: whether a question is the right one, whether a reviewer found it useful, how long a person took, or what a person decided. Those need the run log.

## How to record a human-reviewed run

Follow `docs/TABLETOP_EVALUATION_PROTOCOL.md`. Add one row to a copy of `run_log_template.csv` per run, with roles and not names for reviewers. Report every run, including slow, abandoned or contradictory ones. Do not delete a run because it looks bad.
