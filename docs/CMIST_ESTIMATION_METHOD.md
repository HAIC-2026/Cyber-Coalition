# Aggregate CMIST Screening-Estimate Method (draft v0.1)

**Status:** Draft methodology, not yet implemented or run. Responds to POA&M item PM-04 and the DHS challenge's explicit Section 6/7 requirement to "model the types and scale of support required for each disaster scenario" and "generate needs estimates for each hazard across the CMIST categories." No figures in this document have been computed — it specifies the formula, data sources, and acceptance checks a future run would use.

## What this is and is not

This produces a **screening estimate**: a defensible, reproducible, tract-level order-of-magnitude figure built entirely from public aggregate data. It is explicitly **not** a validated need count, a service-demand forecast, or an individual-level assessment. Per the DHS challenge's own success criteria, County/DHS/partner organizations must validate any output "as reasonable" before it informs planning — this method produces the thing to be validated, not a finished answer. Every output must carry the label: *"Screening estimate from public aggregate data; not confirmed by an authoritative source; requires County/DHS/partner review before use."*

## Data sources by CMIST dimension

| CMIST dimension | Primary proxy variable | Source | Native geography | Status |
|---|---|---|---|---|
| **Communication** | % households with Limited English Proficiency (LEP) | Census ACS 5-year estimates, table S1602 (Limited English Speaking Households) | Census tract | Not yet pulled into this project |
| **Maintaining Health** | Count of electricity-dependent Medicare beneficiaries (de-identified) | HHS emPOWER Map | ZIP code (cannot be split to tract — existing project rule) | Already in evidence register, not yet joined to any estimate |
| **Independence** | % population with an ambulatory or self-care disability | Census ACS 5-year estimates, table S1810 (Disability Characteristics) | Census tract | Not yet pulled into this project |
| **Support & Safety** | % population under 5 or over 65 living alone or in group quarters requiring assistance, cross-referenced with CDC/ATSDR SVI "Household Composition & Disability" theme (not just the composite Count already in this project) | Census ACS + CDC/ATSDR SVI theme-level fields | Census tract | SVI composite Count already pulled; theme-level breakdown not yet pulled |
| **Transportation** | % households with no vehicle available | Census ACS 5-year estimates, table B08201 (Household Size by Vehicles Available) | Census tract | Not yet pulled into this project |

All five proxies are **aggregate, tract- or ZIP-level counts** — consistent with the project's existing privacy rule (`SECURITY_PRIVACY.md`: public, aggregate, de-identified, or synthetic data only).

## Formula structure (per hazard × CMIST dimension × tract)

```
Base estimate  = tract population (or households) × dimension proxy rate
Low estimate   = Base × (1 − suppression_margin)
High estimate  = Base × (1 + undercount_margin)
```

- `suppression_margin` and `undercount_margin` must be stated explicitly and sourced from the ACS variable's own margin of error (MOE) field, not invented. ACS 5-year tables publish MOE for every estimate — use it directly rather than an arbitrary percentage.
- Hazard exposure (FEMA NRI, DFIRM overlay, tsunami evacuation zones) is a **separate multiplier applied afterward**, not folded into the base estimate. This preserves the project's existing rule: hazard exposure and AFN need are distinct until a documented, defensible join method combines them. A tract's screening estimate for "Independence" need does not change by hazard — only how many of those tract residents are inside a given hazard's modeled or mapped extent does.
- Output for each hazard × tract × CMIST row: `{dimension, proxy variable, source vintage, base, low, high, hazard-exposure flag, confidence}`.

## Example (Kapolei pilot only — numbers are placeholders, not computed)

| Tract GEOID | Hazard | CMIST dimension | Proxy | Base | Low | High | Hazard exposure | Confidence |
|---|---|---|---|---|---|---|---|---|
| 15003xxxxx | Hurricane | Transportation | % no-vehicle households (ACS B08201) | [pending ACS pull] | — | — | Within Cat-5 wind-stress scenario extent | Not yet computed |

This table is a template, not a result. Filling it in is the actual next step.

## Acceptance checks before any figure is presented as more than a screening estimate

1. Source table, variable code, vintage, and retrieval date recorded for every ACS pull (same evidence-register discipline as every other source in this project).
2. MOE-based low/high range is shown, not a single point estimate.
3. Hazard exposure and CMIST need are never summed or averaged together — reported as two separate, explicitly labeled figures.
4. Every output is traceable to this document's formula — no manually adjusted numbers.
5. A county, DHS, or partner reviewer's name and date are recorded before any figure is called "reasonable" or used in a planning narrative, per DHS's own measurable-goal language.

## Honest current status

**Nothing in this method has been run.** The tables above are schema, not data. Implementing this requires: pulling the four ACS tables listed (S1602, S1810, SVI theme fields, B08201) into ArcGIS as hosted tables or feature layers, joining them to the existing 435-tract layer by GEOID, and computing the base/low/high formula per tract. That is real, scoped work for the team to decide whether to attempt before Saturday — this document exists so that decision can be made with a concrete plan in hand, not from scratch in the room.
