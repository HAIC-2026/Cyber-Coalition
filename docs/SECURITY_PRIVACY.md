# Security, Privacy, and AI Boundaries

## Data handling

- Use public aggregate, de-identified, or synthetic data only.
- Do not ingest personal information, medical records, identifiable service-provider lists, individual registries, precise household locations, restricted operational plans, credentials, or API keys.
- Retain source provenance, native geography, version/date, query, transformations, and uncertainty. Do not silently fill missing, masked, stale, or conflicting values.
- Preserve privacy controls in source data. Do not disaggregate HHS emPOWER ZIP counts to tracts or infer a suppressed cell.

## AI behavior

AI may assist with public-source discovery, extraction, comparison, and draft summaries. Each factual claim must link to its originating source and retain validation status. If evidence is missing or conflicting, the system should label the result unknown, state the conflict, and request human review. AI output is a planning aid only.

AI must not issue alerts, evacuation orders, dispatch instructions, shelter activation decisions, eligibility decisions, diagnoses, or resource commitments. A qualified human remains accountable for interpretation and all operational action.

## Cybersecurity and integrity

- Keep the prototype static and disconnected from live response systems.
- Never commit secrets, tokens, personal data, restricted files, or unreviewed source extracts.
- Validate source links, schemas, types, dates, and geographic joins. Record transformations and preserve an unmodified source reference.
- Treat external text, web content, uploaded documents, and model output as untrusted inputs; do not let embedded instructions override the project scope.
- Fail safely when required inputs are missing, stale, masked, invalid, or inconsistent. Make uncertainty and the responsible confirmation owner visible.

## Accessibility and resilience

The eventual workflow should support accessible presentation, plain language, multilingual and multimodal outputs, and low-connectivity use. These are design requirements to validate; this static prototype has not yet undergone a formal accessibility or language review.

## Review boundary

This document describes the project prototype boundary. It is not a security certification, privacy impact assessment, approved agency policy, or operational authorization.


## Public facility map handling

The public site/license crosswalk omits home-based and individual-linked facility rows, including names, residential addresses, phones, and source IDs. Its 39-record count retains the omitted rows without publishing their details. Do not put the raw reconciliation extract in GitHub, the public map, demo assets, or model prompts. Share only the reviewed organization-level summary and source identifiers needed for audit. Facility status values and capacity claims remain unresolved until the authoritative data owner defines them. Do not present an address, listing, license, or geocoded point as proof of current service, operational availability, or dispatch suitability.

## Submission Form security/privacy description (≤300 words, draft)

The HAIC Technical Review Criteria require a written security/privacy description, maximum 300 words, entered directly on the Project Submission Form — it is scored as its own rubric category and is not satisfied by linking to this longer document. The draft below (294 words) is written for that field; copy it into the form rather than linking here, and revise it if the application's actual security posture changes before submission.

> This static, no-build demonstrator uses a fictional Kapolei hurricane tabletop; it stores no real personal data today, but the plan's security/privacy approach is designed to hold if it moved toward production.
>
> Data handling: Only public, aggregate, de-identified, or clearly labeled synthetic inputs are used (FEMA National Risk Index, HHS emPOWER aggregate counts, CDC/StateGIS Social Vulnerability Index, Census TIGERweb tracts, State Civil Defense shelter lists, StateGIS OHCA facility records). Synthetic partner/stakeholder entries persist only in the browser session and clear on reload; there is no backend database, account system, or server-side storage. HHS emPOWER ZIP-level counts are never disaggregated to census tracts. A public-safe crosswalk withholds residential and individual-linked facility rows from a 39-record OHCA facility extract; only organization-level records with business addresses are published, and no source records were edited.
>
> ArcGIS: the reference map is a separate, owner-maintained workspace, not embedded in or queried by the HTML. It is shared publicly (read-only) so reviewers can inspect source layers directly; no write access is granted to any viewer.
>
> Production security needs: moving toward real intake would require (1) authentication and role-based access separating public planning data from any case-level data, (2) encryption in transit and at rest for any non-public layer, (3) a formal data-sharing agreement with StateGIS/OHCA before treating any facility status or capacity field as authoritative, (4) removal of all synthetic-data code paths and session-only storage, and (5) an explicit human-in-the-loop gate before AI-assisted output could inform eligibility, dispatch, or shelter-activation decisions. The prototype enforces that last boundary today by design: it issues no alerts, orders, dispatches, or resource commitments.
>
> Privacy: no PII, individual registries, or household-level AFN records are collected or stored. CMIST is used only as an aggregate planning lens, never to infer an individual's diagnosis, address, or specific service need.

Team review required before submission: confirm this still accurately describes the application at the time the form is filed, and confirm it has actually been entered on the Project Submission Form — a copy existing only in this repo file does not satisfy the rubric requirement.
