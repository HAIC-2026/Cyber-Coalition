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
