# ArcGIS StoryMap — draft content

Status: draft narrative text for a proposed StoryMap, not yet built in ArcGIS StoryMaps. Paste section-by-section into the builder; nothing here claims the StoryMap exists yet. Treat every number below as already-reconciled (see `EVIDENCE_REGISTER.md`) — do not add new figures here without the same sourcing discipline.

## Cover
**Title:** Evidence Into a Coordinated Plan
**Subtitle:** Cyber Coalition · HAIC 2026 · ESF-6 AI-Assisted Planning
**Cover image:** the Oʻahu shaded-relief tract context image (`docs/images/oahu-shaded-relief-tract-context.png`) already in the repo.

## Section 1 — The problem
Text: "DHS's ESF-6 challenge asks for hazard-specific AFN vulnerability maps across four hazards — hurricane, wildfire, tsunami, flood — for 100% of Hawaiʻi's census tracts. Most AI planning tools answer that kind of question with confident-sounding numbers. We built a method that shows its work instead: every figure in this project is tagged as a source finding, an inference, an assumption, or an open question, and stays that way until someone with authority confirms it."

## Section 2 — The pilot, bounded on purpose
Text: "Rather than claim statewide coverage, we built one real, defensible pilot: a fictional Category 5 hurricane wind-stress tabletop in Kapolei, Leeward Oʻahu. [Embed: Coverage & audit tab screenshot or live link to https://haic-2026.github.io/Cyber-Coalition/]"
Map embed: the public reference map (`d7b64dfd6e5a4e7589be7bcfbe355ad0`), zoomed to Kapolei.

## Section 3 — Geography is the join foundation
Text: "Before any hazard or need analysis means anything, the base geography has to reconcile. Of 461 official 2020 Census tract GEOIDs statewide, 435 (94.4%) appear in both candidate StateGIS layers. The other 26 are Census-only tracts with zero recorded population and housing — not proof of zero need, just tracts our candidate layers don't yet cover."
Map embed: the public tract reconciliation layer (`06c11dc78afa44e7992a1348527fed7b`).
Sidecar stat block: 461 / 435 / 26, matching the repo's own coverage dashboard.

## Section 4 — CMIST: five lenses, not five boxes checked
Text: short intro to Communication, Maintaining Health, Independence, Support & Safety, Transportation — pull directly from `web/index.html`'s CMIST planning matrix (priorities/objectives/resources per row). Note explicitly: "These are planning considerations, not individual assessments. We never infer a person's diagnosis, address, or specific need from aggregate data."

## Section 5 — What the data can and can't tell us
Express as a swipe or side-by-side: **FEMA NRI** (modeled long-term risk, not a forecast) vs. **DFIRM flood overlay** (mapped area, not people-count) vs. **StateGIS OHCA facilities** (license records, not confirmed current operations). Use the exact hedge language already in `web/index.html`'s source cards — don't rephrase it looser.

## Section 6 — [INSERT once analyses complete] Where need and distance don't line up
Placeholder for the drive-time / Service Area analysis result: "Trauma centers have a defined service area. Overlaying that against Coastal SVI tracts shows [N] high-vulnerability tracts outside a 15-minute drive — not proof of unmet need, but a concrete question for county planners to check." Map embed: the drive-time result layer, once it exists and is public.

## Section 7 — [INSERT once analyses complete] Compounded vulnerability
Placeholder for the LIDAC × Medically Underserved × SVI cross-tabulation: "[N] tracts are flagged by more than one independent equity measure." Same evidentiary hedge as everything else — correlation across indicators, not a confirmed service gap.

## Section 8 — Human authority, every step
Text: pull directly from the repo's own line: "AI can help find, organize, and explain evidence; it does not assign people, declare a resource suitable, or issue an operational recommendation." List the five things the prototype explicitly cannot do (open shelters, issue alerts, dispatch, determine eligibility, commit resources).

## Section 9 — What's still open
Short, honest list pulled from the README's "Open validation priorities" — don't hide the gaps, the whole narrative's credibility depends on this section existing.

## Closing
Links: GitHub repo, live demonstrator, evidence register. One line: "Built by Cyber Coalition for HAIC 2026."
