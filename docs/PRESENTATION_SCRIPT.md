# Presentation Day Script — Draft

**Format constraint (2026 Judging Criteria):** 6 minutes total — 2 min presentation, 2 min live demo, 2 min Q&A. Presentation + demo are cut off at the 4-minute mark; Q&A ends at 2 minutes. Judges score 0 for any of the four Presentation Judging categories the talk does not explicitly cover: **Requirements, Originality & Design, Utility & Impact, Presentation & Delivery.** This draft is written so each category is addressed in a specific, identifiable passage — the bracketed tags are for team rehearsal only and should not be read aloud.

Team: confirm presenter and backup, rehearse against a visible timer, and cut content rather than run over — a strong unfinished answer during Q&A beats losing a category to the clock.

---

## Minute 0:00–0:30 — Opening + problem framing **[Requirements]**

"We're Cyber Coalition, presenting [state your HAIC-registered team name if it differs from the project name]. The DHS ESF-6 challenge asks for hazard-specific AFN vulnerability maps across hurricane, wildfire, tsunami, and flood, for 100% of census tracts statewide. We built a bounded, evidence-led method to get there — starting with one real, defensible pilot instead of a shortcut to statewide claims we can't back up."

## Minute 0:30–1:15 — What we built and why it's different **[Originality & Design]**

"Our planning workflow runs Map → Model → Match → Human Review. Every number in it is tagged — source finding, inference, assumption, or open question — so a reviewer always knows what's verified and what isn't. That's the innovation: most AI planning tools hide their uncertainty. Ours surfaces it on purpose. For example, our ArcGIS tract reconciliation shows 435 of 461 Census tracts matched — and we show the 26 that didn't, with the reason why, instead of rounding up to 100%."

## Minute 1:15–2:00 — Who it helps and what changes **[Utility & Impact]**

"This gives county and state planners something they don't have today: a single evidence trail connecting CMIST needs — communication, health, independence, support, transportation — to actual candidate resources, for a specific scenario, with every gap labeled instead of assumed away. For our Kapolei hurricane pilot, that means a planner can see which facilities have license data, which status fields are undefined, and what still needs confirmation — before anyone relies on it operationally."

## Minute 2:00–4:00 — Live demo **[Requirements + Originality & Design + Utility & Impact, reinforced visually]**

Suggested walkthrough (adjust to whatever's actually working live — test this exact path beforehand):
1. Open the live planning demonstrator — show the Coverage & audit tab with the 435/461 tract checkpoint and the four-hazard evidence boundaries.
2. Switch to the ArcGIS reference map (now public — confirm the link opens cleanly, logged out, before you're on stage) and show one reconciled layer (e.g., the OHCA facility crosswalk or the SFHA/flood overlay).
3. Point out one deliberately-labeled "unknown" (e.g., the undefined operational-status field) — this is a feature of the method, not a gap to hide. Say so explicitly.

## Minute 4:00–6:00 — Q&A **[Presentation & Delivery, demonstrated throughout]**

Anticipated questions and how to answer without overclaiming:
- *"Is this statewide yet?"* → "No — this is a bounded Kapolei pilot that proves the method. Statewide is design intent, not a current claim, and we say so in the repo."
- *"What happens to the 26 unmatched tracts?"* → "They're zero-population/zero-housing in the 2020 Census count, which doesn't mean zero need — we flag that distinction explicitly rather than resolving it for them."
- *"Who verifies the AI's output?"* → "A human, always. The system never issues alerts, assigns resources, or makes eligibility calls — it prepares evidence for a person to decide."

---

**Presentation & Delivery checklist (self-score before rehearsal):**
- [ ] Stays inside 4:00 for talk + demo, tested with a timer
- [ ] States the team's HAIC-registered name if "Cyber Coalition" differs from it
- [ ] Explicitly names all four hazards and the CMIST dimensions at least once
- [ ] Demo path tested logged-out, same-day, on the actual presentation device/network
- [ ] Backup screenshots/video ready in case live ArcGIS or GitHub Pages is unreachable in the room
