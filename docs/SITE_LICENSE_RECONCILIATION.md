# Kapolei OHCA Site and License Reconciliation

**Snapshot:** 2026-11-14 (HST)  
**Status:** Working source reconciliation for review. No OHCA or StateGIS owner confirmation is represented as received. Source feature records were not edited.

## Scope and method

The State of Hawaiʻi StateGIS OHCA Facilities layer (MapServer/3) was queried by `address_addressCity = Kapolei` with feature geometry returned in WGS84. Points were tested against the official 2020 Census TIGERweb Kapolei CDP boundary, GEOID `1530300`. The point-in-polygon result is 39 OHCA feature records. Grouping by the source address string and six-decimal coordinate yields 37 address-coordinate keys. These are keys for reconciliation, **not 37 verified unique facilities**. Co-located suite records remain separate unless the source owner confirms identity.

The source row `objectid` and UUID `id` are retained as separate identifiers. Displayed longitude/latitude are rounded to six decimals; the source geometries retain greater precision. Source `license_licenseOrCertNumber` values are transcribed as observed, not validated as current. The map layer was geocoded from OHCA Licensing Section API data on 2026-09-15 per its metadata.

## Privacy handling

The 39-record count includes 7 Community Care Foster Family Home rows, 2 Licensed Dietitian rows, 2 individual-named medical-office rows, and 1 Domiciliary Home row. Their names, home/residential addresses, phones, and source IDs are not copied into this public-facing crosswalk. The remaining 27 organizational facility records are listed below. This exclusion is a presentation safeguard and does not remove those records from the source count or decide their licensing status.

## Public organizational record detail

| Map OID | Source record UUID | Facility / type | Source address | Longitude, latitude (WGS84) | Source phone | Embedded credential ID | Source expiry date |
|---:|---|---|---|---|---|---|---|
| 55 | ef709ca9-fd57-ee11-be6e-001dd8065b8f | AHCS-Pali Women's Health / Lab - Waiver | 711 Kamokila Blvd, Ste 103 | -158.083367, 21.331992 | +1 808 263 5148 | CP1-766 | 2027-09-19 |
| 105 | 9753187d-b268-d0bc-7e18-3a22e63255c1 | Alikai Health LLC / Durable Medical Equipment Supplier | 599 Farrington Highway, Building 2 | -158.075920, 21.339127 | +1 484 983 7355 | DME-0116 | 2029-09-30 |
| 122 | 57a0f525-09b8-ef11-b8e9-001dd80296e7 | Aloha Care Connections LLC / Case Management Agency | 91-1037 Palala Street | -158.071939, 21.338208 | +1 808 200 5421 | 69 | 2027-01-31 |
| 266 | aa83784e-9e67-ee11-8def-001dd8065b8f | Arovini Case Management Agency / Case Management Agency | 91-1041 Makahani Street | -158.067763, 21.337070 | +1 808 554 5439 | 68 | 2026-10-31 |
| 456 | bbfb9060-88f3-ed11-a7c6-001dd8070ecc | Castle Physician Network dba Adventist Health Castle Urgent Care Kapolei / Lab - Waiver | 91-710 Farrington Hwy, Ste A100 | -158.072314, 21.343187 | +1 808 263 5148 | CP1-747 | 2028-02-22 |
| 574 | 70ef7a25-743c-e911-a966-001dd800d5b0 | Complete Dermatology LLC Kapolei / Lab - PPMP | 1001 Kamokila Blvd, Suite 181 | -158.080333, 21.334798 | +1 808 621 1000 | CP1-389 | 2029-07-11 |
| 617 | 38611194-96c4-ef11-b8e9-001dd801d1a8 | Daniel K Akaka State Veterans Home / Lab - Waiver | 91-1204 Kealanani Ave | -158.071946, 21.339960 | +1 808 861 0926 | CP2-812 | 2026-12-26 |
| 720 | 91e17a25-743c-e911-a966-001dd800d5b0 | Dsi Kapolei Dialysis / End Stage Renal Disease Facility | 555 Farrington Highway | -158.078536, 21.337789 | +1 808 696 8980 | Not present in extract | Not present in extract |
| 1312 | 10e07a25-743c-e911-a966-001dd800d5b0 | Ilima at Leihano / Assisted Living Facility | 739 Leihano Street | -158.074096, 21.330656 | +1 808 674 8022 | 20-ALF | 2028-08-31 |
| 1577 | dee97a25-743c-e911-a966-001dd800d5b0 | Ka Puna Wai Ola / Lab - Waiver | 575 Farrington Hwy | -158.076782, 21.337837 | +1 808 674 9262 | CP2-61 | 2028-02-06 |
| 1582 | f6e07a25-743c-e911-a966-001dd800d5b0 | Ka Punawai Ola / Skilled Nursing Facility/Nursing Facility Dual Cert | 91-575 Farrington Highway | -158.076786, 21.337827 | +1 808 674 9262 | 59-N/125051 | 2026-11-30 |
| 1654 | aaab3f97-2246-eb11-a812-001dd8018831 | Kaiser Permanente West Oahu Med Ofc Lab / Lab - Compliance | 401 Kamokila Blvd | -158.085665, 21.329027 | +1 808 432 3668 | CL-544 | 2026-12-07 |
| 1658 | 5f059c81-2646-eb11-a812-001dd8018831 | Kaiser Permanente West Oahu Med Ofc PPMP / Lab - PPMP | 401 Kamokila Blvd 2nd Floor | -158.085665, 21.329027 | +1 808 432 3663 | CP1-545 | 2026-12-07 |
| 1681 | 64eb7a25-743c-e911-a966-001dd800d5b0 | Kapolei Health Care Center / Federally Qualified Health Center | 525 Farrington Highway | -158.078760, 21.336917 | +1 808 674 9352 | Not present in extract | Not present in extract |
| 1740 | bbef7a25-743c-e911-a966-001dd800d5b0 | Keiki Korner Pediatrics / Lab - Waiver | 1001 Kamokila Blvd | -158.080333, 21.334798 | +1 808 6749 | Not present in extract | Not present in extract |
| 1782 | 278cd310-0511-ec11-b6e6-001dd8029d2c | Koa Laboratory LLC dba Koa Labs / Lab - Accreditation | 599 Farrington Highway, Building 2 | -158.075920, 21.339127 | +1 808 282 9186 | CL-613 | 2027-04-10 |
| 1818 | f08eaa71-0010-eb11-a813-001dd8018921 | KSL Ilima at Leihano, LLC / Lab - Waiver | 739 Leihano Street | -158.074096, 21.330656 | +1 760 804 5900 | CP2-509 | 2029-09-23 |
| 2456 | ceee7a25-743c-e911-a966-001dd800d5b0 | MinuteClinic Diagnostic of Hawaii LLC #9317 / Lab - Waiver | 590 Farrington Hwy Unit 300 | -158.081734, 21.336921 | +1 866 389 2747 | CP1-334 | 2027-07-23 |
| 2601 | 57cd26d2-c3b3-ed11-83fe-001dd80726a4 | Ohana  Endoscopy Center / Lab - Waiver | 590 Farrington Hwy, #170 | -158.081734, 21.336921 | +1 808 468 4600 | CP1-733 | 2027-01-04 |
| 2793 | cde57a25-743c-e911-a966-001dd800d5b0 | Queen's Health Care Centers-Kapolei / Lab - Waiver | 599 Farrington Hwy #201 | -158.076477, 21.339553 | +1 808 691 7338 | CP1-122 | 2029-04-21 |
| 3058 | a2a65834-573d-ef11-8409-001dd80a7422 | Senior Helpers of West Oahu / Home Care Agency | 1001 Kamokila Boulevard, Suite #133 | -158.080333, 21.334798 | +1 808 913 4322 | 207-HCA | 2028-06-30 |
| 3167 | 7fee7a25-743c-e911-a966-001dd800d5b0 | Straub Medical Center Kapolei / Lab - PPMP | 91-5431 Kapolei Parkway, Suite 1706 | -158.052366, 21.333326 | +1 808 522 4000 | CP1-323 | 2027-06-30 |
| 3345 | 47e47a25-743c-e911-a966-001dd800d5b0 | USRC Kapolei, LLC dba US Renal Care Kapolei Dialysis / Lab - Waiver | 555 Farrington Hwy | -158.078536, 21.337789 | +1 808 693 8980 | CP1-31 | 2027-08-13 |
| 3352 | 37f07a25-743c-e911-a966-001dd800d5b0 | USRC West Oahu LLC dba US Renal Care West Oahu Dialysis / Lab - Waiver | 889 Kamokila Blvd, Suite 200 | -158.082043, 21.332506 | +1 808 674 9604 | CP1-397 | 2027-09-10 |
| 3479 | 77e77a25-743c-e911-a966-001dd800d5b0 | WCCHC-West Oahu Community Health Center / Lab - PPMP | 599 Farrington Hwy Ste 100 | -158.076477, 21.339553 | +1 808 674 3800 | CP1-98 | 2026-10-30 |
| 3526 | c493358a-8a78-f011-b4cc-001dd8062d4a | WorkStar / Lab - Waiver | 599 Farrington Hwy | -158.075920, 21.339127 | +1 808 676 5331 | CP1-830 | 2026-09-10 |
| 3531 | 4aec7a25-743c-e911-a966-001dd800d5b0 | Workstar / Lab - Waiver | 599 Farrington Hwy Building 2 | -158.075920, 21.339127 | +1 808 676 5331 | CP1-707 | 2029-09-10 |

## Site-level associations and exceptions

| Site key | Associated source records and separate OHCA directory credential | Reconciliation disposition |
|---|---|---|
| 555 Farrington Highway, Kapolei | StateGIS OHCA OID 720, source UUID `91e17a25-743c-e911-a966-001dd800d5b0` (ESRD type, no embedded license ID, phone 808-696-8980); OID 3345, source UUID `47e47a25-743c-e911-a966-001dd800d5b0` (USRC Kapolei Lab-Waiver, embedded `CP1-31`, phone 808-693-8980); separate OHCA ESRD directory listing U.S. Renal Care Kapolei, CCN `122508`, phone 808-693-8980. | Associate the OHCA ESRD listing and two geocoded records with the same address/point for review; preserve separate ESRD and lab-waiver records. DSI/USRC naming and phone discrepancy remains unresolved. Do not count two treatment sites or assert current slots/operations. |
| 889 Kamokila Boulevard, Suite 200, Kapolei | StateGIS OID 3352, source UUID `37f07a25-743c-e911-a966-001dd800d5b0`, USRC West Oahu Lab-Waiver, embedded `CP1-397`, phone 808-674-9604; separate OHCA ESRD directory listing U.S. Renal Care West Oahu Dialysis at 889 Kamokila. | Associate as a candidate same-site directory match. The map layer classifies its row as Lab-Waiver while the directory lists an ESRD facility. No separate ESRD identifier was captured in this comparison; keep classification/credential mapping open. |
| 91-1204 Kealanani Avenue, Kapolei | StateGIS OID 617, source UUID `38611194-96c4-ef11-b8e9-001dd801d1a8`, Lab-Waiver `CP2-812`; separate OHCA SNF directory license `6-N` for Daniel K. Akaka State Veterans Home, directory-reported 120 licensed beds, expiry 2027-01-31. | Associate the lab credential and SNF license to the site but retain separate license records and facility types. The reviewed map extract returns the lab row but no SNF row; this is a layer coverage/classification exception, not proof of facility absence. Do not substitute directory bed claims for the undefined map capacity field. |
| 739 Leihano Street, Kapolei | StateGIS OID 1312, source UUID `10e07a25-743c-e911-a966-001dd800d5b0`, Assisted Living Facility, embedded `20-ALF`; OID 1818, source UUID `f08eaa71-0010-eb11-a813-001dd8018921`, KSL Ilima lab-waiver `CP2-509`, same address and point. Separate OHCA April 2026 ALF list shows expiry 2026-08-31; the map record shows 2028-08-31. | Associate the ALF and lab records at one address/point but preserve two credential types. Expiry discrepancy and current status require OHCA confirmation. The map capacity field unit is undefined and is not validated by this association. |
| 91-575 Farrington Highway / 575 Farrington Highway, Kapolei | StateGIS OID 1582, source UUID `f6e07a25-743c-e911-a966-001dd800d5b0`, SNF/NF dual certificate, embedded `59-N/125051`; OID 1577, source UUID `dee97a25-743c-e911-a966-001dd800d5b0`, co-located lab-waiver `CP2-61`. Separate OHCA SNF directory lists `59-N`, CCN `125051`, 120 licensed beds, expiry 2026-11-30. | Same phone and near-identical coordinates support a site association; addresses differ slightly. Keep the SNF and lab-waiver credentials distinct. Directory licensed-bed data is source-specific; do not infer the unit or meaning of the GIS `additionalInfo_capacity` field. |
| 599 Farrington Highway, Building 2, Kapolei | StateGIS OID 105 Alikai Health LLC DME supplier, embedded `DME-0116`, phone 484-983-7355; OID 1782 Koa Laboratory LLC dba Koa Labs, embedded `CL-613`, phone 808-282-9186; same geocoded point. | Co-located organizational records with different names, types, phones, and credentials. Preserve as separate facilities/program records; shared geocoding alone does not establish common operations. |
| 401 Kamokila Boulevard, Kapolei | StateGIS OID 1654 Kaiser Permanente West Oahu Med Ofc Lab, `CL-544`, phone 808-432-3668; OID 1658 PPMP lab, `CP1-545`, phone 808-432-3663, same point with 2nd-floor address. | Preserve the two lab credentials and phone values as separate records. Confirm suite/floor and contact details with source owner if used for routing. |
| 1001 Kamokila Boulevard, Kapolei | StateGIS OID 574 Complete Dermatology, Suite 181, `CP1-389`; OID 1740 Keiki Korner Pediatrics, no embedded ID shown and phone is source-rendered `+1 808 6749`; OID 3058 Senior Helpers of West Oahu, Suite 133, `207-HCA`; all share one geocoded point. | Distinct organizations/suites at one point. Keep records separate. Keiki Korner phone and missing credential value need source validation. |
| 590 Farrington Highway, Kapolei | StateGIS OID 2456 MinuteClinic, Unit 300, `CP1-334`; OID 2601 Ohana Endoscopy Center, #170, `CP1-733`; same point. | Distinct suite-level records and credentials, not duplicates. Verify point precision and unit-specific service details before using for dispatch or availability. |
| 599 Farrington Highway, Kapolei | StateGIS OID 2793 Queen’s Health Care Centers-Kapolei, #201, `CP1-122`; OID 3479 WCCHC-West Oahu Community Health Center, Ste 100, `CP1-98`; same point but different provider, suite, and phone. | Preserve as distinct organizations/suites; the common point likely reflects building-level geocoding. |
| 599 Farrington Highway / Building 2, Kapolei | StateGIS OID 3526 WorkStar, address without unit, `CP1-830`, source expiry 2026-09-10; OID 3531 Workstar, Building 2, `CP1-707`, source expiry 2029-09-10; same point and phone 808-676-5331. | Likely related brand/site records, but the unit-level identity and conflicting credential IDs/expiry dates are unresolved. Preserve both source records pending owner confirmation; do not deduplicate licenses. |

For all other organizational rows above, the embedded credential identifier is a field in the 2026-09-15 StateGIS OHCA layer. A separate current OHCA directory/license lookup was not completed for each row. Missing IDs in the layer are “not present in this extract,” not proof that no license exists.

## Status and capacity fields

All 39 queried rows carry `additionalInfo_operationalStatus = 0`; the layer publishes no coded-value domain for that field. No operational meaning is assigned to zero. The layer labels `additionalInfo_capacity` only as “Facility Capacity” and does not publish units or equivalence to licensed beds; this crosswalk does not reproduce its values as validated capacity. Credential expiry dates are dated source fields, not independent proof of current licensure. License/type-code domains and owner-maintained currency remain unverified.

## Evidence and limits

- Boundary: U.S. Census TIGERweb, Places layer 5, query for `GEOID=1530300` (Kapolei CDP), retrieved 2026-11-14.
- Facility layer: State of Hawaiʻi Geodata, HumanHealthSafety MapServer/3, OHCA Facilities, queried 2026-11-14. Layer metadata attributes geocoding to State GIS from OHCA Licensing Section API data dated 2026-09-15.
- Official directory comparisons cited in the main [AI/GIS Resource Crosswalk](https://drive.google.com/file/d/1QlTlb76Km-bsWshFpHYILNJaHZ1O_kQf/view).
- Spatial co-location is a candidate identity link. Exact shared coordinates may represent building-level geocoding; suite-level distinctions, addresses, phone, and credentials are retained.
- This is a planning-data reconciliation, not a live registry, licensure certification, operations check, capacity assessment, or provider commitment. Owner confirmation remains required for the unresolved matches and definitions.
