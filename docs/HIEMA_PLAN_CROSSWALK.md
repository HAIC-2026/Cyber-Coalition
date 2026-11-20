# HI-EMA Plan Crosswalk

**Project:** HAIC 2026 Cyber Coalition, ESF-6 planning challenge  
**Review date:** 2026-11-19  
**Baseline:** Original handoff named c2b194b; repository reviewed after later changes merged.  
**Status:** Documents only. No HI-EMA endorsement or operational readiness is implied.

Page references use printed PDF page numbers. Classifications use Fact, Source Reported Claim, Analysis, Unknown, or Recommendation, with confidence.

## Sources and revision findings

> **Correction (2026-11-20):** the note below (dated 2026-11-19) that the live index "resolves to the February 2022 PDF" does not reproduce. The live HI-EMA index was re-fetched directly three times across this project's work on this question — twice on 2026-11-19 and again on 2026-11-20 — and in all three checks it contains exactly one "SESF #2 / Communications" link, pointing only to the November 2026 PDF; no February 2022 URL appears anywhere on the page. The February 2022 PDF is a real file and still resolves directly (HTTP 200), it simply isn't linked from this index page. The 2026-11-19 claim below is retained struck through for the record rather than deleted, consistent with this project's practice of preserving a dated history rather than silently overwriting a prior claim; treat the November 2026 PDF as the index's actual, current, and repeatedly-confirmed destination.
>
> **Also resolved (2026-11-20):** the November 2026 SESF #2 PDF was retrieved directly via `curl` (HTTP 200) and read in full. Its §4.3.3 "Coordination with Other SESFs," printed p. 4-4, item (c), reads: "SESF #12 ENERGY: Determining power restoration timelines, identifying outage impacts on communications systems, and prioritizing fuel requirements for assets supporting critical communications." This is the same three elements, same section number, and same printed page as the February 2022 version's §4.3.3, lightly rephrased — a direct, fresh comparison, not a prior-review record. Fact, HIGH.
>
> ~~**Source reconciliation note (2026-11-19):** The live HI-EMA index was reopened and its SESF #2 link followed. It currently resolves to the February 2022 PDF, contrary to the earlier index description in this crosswalk and the merged Evidence Register. The February 2022 PDF was opened; §4.3.3, printed p. 4-4, contains the cited coordination elements. The direct November 2026 PDF could not be retrieved in the current pass, so the prior claim that its p. 4-4 retains the same language is a prior review record and is not freshly reconfirmed here. The reason for the index discrepancy is Unknown.~~
>
> **Also resolved (2026-11-20):** the 2015 Catastrophic Hurricane Plan PDF was retrieved directly via `curl` (HTTP 200, 2.9MB) and its cover letter and Executive Summary (ES-1 through ES-4) opened. It is a genuine, signed plan (Gov. David Y. Ige; FEMA Region IX Acting Regional Administrator Karen E. Armes; HI-EMA Director MG Arthur J. Logan), matching the prior review's citation of "Figure ES-1: Joint Task Organization." The deeper page-specific findings previously cited (shelter-demand estimates on pp. 3-14–3-17, the 916-person personal-assistance-services estimate) were not re-opened in this pass and remain prior-review Source Reported Claims, MEDIUM. The document's existence, authenticity, and ES-1–ES-4 content are now Fact, HIGH.
>
> ~~The Catastrophic Hurricane Plan is listed by the live HI-EMA index. Its direct PDF timed out in the current source reader and browser. Page-specific findings below and in PM-08 are retained as prior review records from the merged crosswalk/PR #18; they are not freshly reverified in this pass. Current plan status remains Unknown.~~


| Source | Version evidence and finding | Classification |
|---|---|---|
| [HI-EOP Base Plan](https://dod.hawaii.gov/hiema/files/2026/03/HI-EOP-Base-Plan-Final-Signed.pdf) | February 2026 signed revision. Reviewed for county requests, WebEOC, SESF assignments, and annex list. | Fact, HIGH |
| [SESF #6 Annex](https://dod.hawaii.gov/hiema/files/2025/10/SESF6-Annex_30SEP25.pdf) | September 2025. Reviewed for mass care, shelter coordination, AFN, and human-service roles. | Fact, HIGH |
| [SESF #2 Communications, November 2026 file](https://dod.hawaii.gov/hiema/files/2026/11/State-Emergency-Support-Function-SESF-2-Communications-Annex-Updated-Nov9-2026-1.pdf) | **Freshly verified 2026-11-20** (retrieved via direct `curl`, HTTP 200, 19 pages): printed p. i names ETS as State ESF Coordinating and Primary Agency; printed p. ii Record of Changes confirms the 11/2026 revision, the OHS (DOD→LAW) and HIWIN (ETS→HIEMA) moves, and signatures dated 11/16–11/17/2026; §4.3.3 printed p. 4-4 contains the fuel-coordination language quoted above. This is the index's actual, repeatedly-confirmed current link (see correction note above). | Fact, HIGH — direct fresh read, not a prior-review record |
| [SESF #2 Communications, February 2022 version](https://dod.hawaii.gov/hiema/files/2022/04/22-0412-State-Emergency-Support-Function-SESF-2-Communications-Annex.pdf) | A real, directly reachable PDF (HTTP 200). Not linked from the live HI-EMA EOP/annexes index in any of three independent checks (2× on 2026-11-19, 1× on 2026-11-20). Section 4.3.3, printed p. 4-4, contains the same three coordination elements as the Nov 2026 version, lightly rephrased. | Fact, HIGH for the file's existence, text, and non-linkage from this index page |
| [SESF #12 Energy](https://dod.hawaii.gov/hiema/files/2022/01/HI-EOP-SESF-12-Annex.pdf) | November 2021. The live HI-EMA index was reopened 2026-11-19 and links this annex; no newer SESF #12 annex appears on that page. This does not rule out a newer file or separate procedure elsewhere. | Fact, HIGH for observed index listing; Unknown, HIGH beyond it |
| [SESF #7 Logistics](https://dod.hawaii.gov/hiema/files/2022/04/22-0317-SESF-7-Logistics-Management-Resource-Support-Annex.pdf) | March 2022 annex located. Whether a newer version exists was not established. | Fact, HIGH for date; Unknown, HIGH for currentness |
| [Catastrophic Hurricane Plan](https://dod.hawaii.gov/hiema/files/2016/03/2015Hawaii_Cat_Plan.pdf) | The live HI-EMA index lists it under Incident Annexes. Freshly retrieved via direct `curl` (HTTP 200, 2.9MB) on 2026-11-20; cover letter and ES-1–ES-4 opened and confirmed genuine, matching prior review's "Figure ES-1" citation. Deeper page-specific findings (p. 4, pp. 2-7, 3-14–3-17) summarized in PM-08 were not reopened in this pass. | Index listing, authenticity, ES-1–ES-4: Fact, HIGH; deeper page-specific findings: Source Reported Claim, MEDIUM; current operative status: Unknown, HIGH |

## A. PM-07: County-to-State pathway

| Stage | Plan-supported process | Evidence |
|---|---|---|
| Local response | An on-scene Incident Commander leads most incidents. If size or complexity exceeds on-scene capacity, the county may activate its EOC. | HI-EOP Base Plan, printed p. 4-2. Fact, HIGH. |
| County request | Incident Commander requests through County EOC. If it cannot fulfill, county submits an RFA to SEOC through WebEOC; counties may also submit RFIs there. | HI-EOP Base Plan, printed pp. 5-15 to 5-16. Fact, HIGH. |
| State screening | State Operations verifies the request and assigns a SESF. SESF Primary Agency checks whether it or Support Agencies can meet it. | HI-EOP Base Plan, printed p. 5-16. Fact, HIGH. |
| Approval and fulfillment | If feasible, the mission goes to the Operations Section Chief for approval, then SESF coordinates with requester. If not, it may be reassigned or referred to Logistics and Resource Support. | HI-EOP Base Plan, printed p. 5-16. Fact, HIGH. |
| SESF #6 interface | HIEMA and DHS are primary agencies. DHS is the primary interface with the SEOC Operations Section Chief. RFAs/RFIs are managed through the OSC with HIEMA WebEOC. | SESF #6 Annex, printed pp. 1-2. Fact, HIGH. |
| Beyond state capability | Base Plan identifies EMAC as a possible path when the Governor has declared a state of emergency and describes federal assistance pathways. | HI-EOP Base Plan, printed p. 5-16 and section 4.4. Fact, HIGH. |

The Base Plan calls WebEOC the State's primary internal incident communications and situational-awareness tool. County EOCs and State Department Operations Centers submit RFAs/RFIs there; HIEMA manages accounts and permitted access. HI-EOP Base Plan, printed p. 6-2. Fact, HIGH.

| Prototype comparison | Assessment |
|---|---|
| Original handoff baseline | At c2b194b, PM-07 and the prototype described County-to-State as simulated. The plans supply the documented request and review stages. Analysis, HIGH. |
| Current repository | PR #6 later merged plan-based descriptions of county EOC, WebEOC, SEOC Operations, SESF assignment, and mission approval. The project remains a static planning demonstrator. It does not submit to WebEOC, authenticate requests, approve missions, or verify service/resource availability. Repository change is Fact, HIGH; boundary is Analysis, HIGH. |
| Treatment | Present plan stages alongside the demonstrator boundary. Do not describe it as an operational state request channel. Recommendation, HIGH. |

## B. Communications resilience: agency and fuel

| Function | Assignment evidence | Classification |
|---|---|---|
| SESF #2 Communications | The February 2026 Base Plan Table 8 lists DAGS/ETS as primary, printed p. 5-20. The November 2026 annex, freshly reopened 2026-11-20, printed p. i names ETS as Coordinating and Primary Agency. | Fact, HIGH for both — freshly verified |
| SESF #12 Energy | 2026 Base Plan Table 8 lists DBEDT/Hawaiʻi State Energy Office as primary, printed p. 5-21. 2021 annex names HSEO coordinating/primary and Energy Sector Partners support. | Fact, HIGH |

The 2021 SESF #12 annex describes fuel supplier coordination, priority setting for scarce fuel/energy, emergency fuel for critical facilities, transportation, communications, and emergency operations, and a Fuels Set-Aside tied to a Governor's energy emergency declaration. Printed pp. 4-3 to 4-4. Fact, HIGH as to that annex.

The February 2022 SESF #2 annex says SESF #12 coordinates power-restoration timelines, communications outage impacts, and fuel requirements for assets supporting critical communications (§4.3.3, printed p. 4-4; not currently linked from the live HI-EMA index — see correction note above). The November 2026 annex, freshly reopened 2026-11-20, contains the same three elements at the same section/page, lightly rephrased: "Determining power restoration timelines, identifying outage impacts on communications systems, and prioritizing fuel requirements for assets supporting critical communications." Fact, HIGH for both texts — this is now a direct comparison, not a pending one. No comparative priority order among hospitals, shelters, cellular towers, data centers, or other asset classes is established in either version. Unknown, HIGH.

## C. SESF #6: AFN and sheltering

The September 2025 annex names HIEMA and DHS as primary agencies, Salvation Army for feeding, American Red Cross for temporary shelter operations, and HVOAD for community mass-care delivery. Printed pp. 1-2. Fact, HIGH.

The State is not a shelter provider; it coordinates shelter resources with counties and partners when requested by local jurisdictions. The annex covers general, evacuation, non-congregate, pet-friendly, and temporary housing support. Medical shelters fall under SESF #8. Attachment 1, printed p. 3; Attachment 3, pp. 12-13. Fact, HIGH.

The annex addresses accessible sheltering and functional-needs resources, including durable medical equipment, assistive technology, personal assistance, dedicated power and water, special-needs shelter requirements, and SESF #8 coordination for medical or mental-health needs. It also addresses service animals, pets, reunification, language access, children, older adults, disability, limited English proficiency, homelessness, and transportation disadvantage. Attachment 1, pp. 2-3; Attachment 2, pp. 8-10; Attachment 3, pp. 12-14. Fact, HIGH.

These are planning and coordination roles, not proof a particular shelter is open, staffed, accessible, supplied, or hazard-suitable. Analysis, HIGH. Preserve the distinction that the State coordinates shelter resources and is not itself a shelter provider. Recommendation, HIGH.

## D. PM-08: Catastrophic Hurricane Plan, historical

The live HI-EMA index lists the Catastrophic Hurricane Plan under Incident Annexes. The PDF was freshly retrieved and opened 2026-11-20 (direct `curl`, HTTP 200, 2.9MB): it is genuine, titled "2015 Hawaii Catastrophic Hurricane Plan / FEMA RIX Hawaii Catastrophic Annex," signed by Governor David Y. Ige, FEMA Region IX Acting Regional Administrator Karen E. Armes, and HI-EMA Director MG Arthur J. Logan. Its Executive Summary (ES-1 through ES-4) was read and matches the prior citation of "Figure ES-1: Joint Task Organization." It explicitly supersedes a 2009 plan and does not itself state it has been superseded by anything newer. The specific page-level findings previously cited (p. 4, p. 2-7, pp. 3-14 to 3-17, including historical shelter-demand estimates of 425,867 before and 141,957 after a hurricane and an estimate of 916 people requiring personal assistance services using a 2013 FEMA Region X metric) were not reopened in this pass and remain prior-review Source Reported Claims, MEDIUM. These historical estimates do not establish present demand, capacity, or current operations; whether the plan has been superseded since 2015 and whether its estimates remain valid are Unknown, HIGH.

| Treatment | Classification |
|---|---|
| Label the linked plan as a 2015 historical reference. | Analysis, HIGH. |
| Do not treat its listing as evidence of current shelter inventory, routes, assignments, communications, fuel allocation, or availability. | Recommendation, HIGH. |
| Whether the 2015 plan remains operative/current, and whether its historical estimates remain valid, are unverified. | Unknown, HIGH. |

## Open verification items

1. **Resolved 2026-11-20:** the live HI-EMA index links only the November 2026 SESF #2 PDF (confirmed in three independent checks); the February 2022 PDF is real but not linked from this index. Both PDFs' §4.3.3 (printed p. 4-4) were directly opened and compared: the fuel-coordination language is the same three elements, lightly rephrased. Fact, HIGH.
2. **Partially answered:** the live HI-EMA index links the November 2021 SESF #12 Energy annex and shows no newer SESF #12 annex on that page. Newer annex/procedure elsewhere remains Unknown. Fact, HIGH for observed index listing; Unknown, HIGH beyond it.
3. **Resolved 2026-11-20 for authenticity and ES-1–ES-4; page-specific findings still prior-review:** the 2015 Catastrophic Hurricane Plan was freshly retrieved and its Executive Summary read, confirming it is genuine and matches the prior citation. The deeper page-specific shelter-demand findings were not reopened in this pass and remain Source Reported Claim, MEDIUM; whether the plan has been superseded since 2015 and whether its estimates remain valid are Unknown, HIGH.
4. Keep WebEOC, mission approval, service availability, county/State authority, and operational status outside prototype claims unless independently verified.

## Official sources

- [HIEMA Emergency Operations Plan and Annexes index](https://dod.hawaii.gov/hiema/emergency-operations-plan-and-annexes/)
- [HI-EOP Base Plan, February 2026](https://dod.hawaii.gov/hiema/files/2026/03/HI-EOP-Base-Plan-Final-Signed.pdf)
- [SESF #6 Annex, September 2025](https://dod.hawaii.gov/hiema/files/2025/10/SESF6-Annex_30SEP25.pdf)
- [SESF #2 Annex, November 2026 version](https://dod.hawaii.gov/hiema/files/2026/11/State-Emergency-Support-Function-SESF-2-Communications-Annex-Updated-Nov9-2026-1.pdf)
- [SESF #2 Annex, February 2022 version](https://dod.hawaii.gov/hiema/files/2022/04/22-0412-State-Emergency-Support-Function-SESF-2-Communications-Annex.pdf)
- [SESF #12 Energy Annex, November 2021](https://dod.hawaii.gov/hiema/files/2022/01/HI-EOP-SESF-12-Annex.pdf)
- [SESF #7 Logistics Annex, March 2022](https://dod.hawaii.gov/hiema/files/2022/04/22-0317-SESF-7-Logistics-Management-Resource-Support-Annex.pdf)
- [Catastrophic Hurricane Plan linked by HI-EMA](https://dod.hawaii.gov/hiema/files/2016/03/2015Hawaii_Cat_Plan.pdf)
