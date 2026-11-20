# Communications & Infrastructure Resilience Notes

**Prepared for:** Cyber Coalition, HAIC 2026 (ESF-6 AFN challenge)
**Source:** Voice working session, 2026-11-16.
**Status:** Working notes for architecture mapping. HI-EMA assignment and communications-fuel findings below are reconciled to opened primary sources; remaining statements retain their individual labels. Classifications include Fact, Source Reported Claim, Analysis, Recommendation, Opinion, and Unknown, each with confidence.

## Purpose

Capture the layered communications dependency chain for Oʻahu so the team can map what fails, in what order, and what fallback exists at each layer during a disaster — with focus on people with Access and Functional Needs (AFN). This supports the Communication CMIST dimension and responds to the DHS challenge pain-point language about communities with limited Wi-Fi requiring more advanced planning and communication.

## The dependency chain

Power → Fuel → Data centers → Connectivity out of state → Local communications → People.

| Layer | What it covers |
|---|---|
| Power | Grid supply to facilities, towers, and homes |
| Fuel | Diesel resupply for backup generators |
| Data centers | Local hosting and interconnection on-island |
| Connectivity out of state | Undersea cables, then satellites |
| Local communications | Cell towers, inter-island cables, local networks |
| People | Shelters, hospitals, AFN populations, responders |

## Key findings

| Finding | Classification | Confidence |
|---|---|---|
| Two main Oʻahu data centers carry most of the load — DRFortress (near the airport, Honolulu) and AlohaNAP (Kapolei). Smaller operators include Servpac and Hawaiian Telcom. Directory sources list about six data centers in the Honolulu market. | Source Reported Claim (directory listings, not operator-confirmed) | Moderate |
| DRFortress reports on-site diesel lasting up to 80 hours at full load. | Source Reported Claim (Data Center Map listing) | Moderate |
| Large cloud providers spread each region across separate sites with independent power and replicate critical data to other regions. | Analysis | Moderate |
| Hawaiʻi mainland traffic relies on a small number of undersea cables; landing sites and internet exchange points may be concentrated failure points. | Analysis | Moderate |
| Oʻahu fuel arrives largely through the harbor and Kapolei refinery; port damage could cut generator resupply statewide. | Analysis — needs validation with state energy sources | Moderate |

## State-plan assignments and fuel coordination: reconciled evidence

The February 2026 HI-EOP assigns SESF #2 Communications to DAGS/ETS (printed p. 5-20) and SESF #12 Energy to DBEDT/Hawaiʻi State Energy Office (printed p. 5-21). **Fact, HIGH** as recorded from the reviewed [HI-EOP Base Plan](https://dod.hawaii.gov/hiema/files/2026/03/HI-EOP-Base-Plan-Final-Signed.pdf).

The live [HI-EMA Emergency Operations Plan and Annexes index](https://dod.hawaii.gov/hiema/emergency-operations-plan-and-annexes/) has been independently re-fetched three times across this project's work (2× 2026-11-19, 1× 2026-11-20); in all three checks its SESF #2 link resolves only to the [November 2026 Communications Annex](https://dod.hawaii.gov/hiema/files/2026/11/State-Emergency-Support-Function-SESF-2-Communications-Annex-Updated-Nov9-2026-1.pdf) (an earlier claim here that it resolved to the Feb 2022 annex did not reproduce and is corrected). Both the November 2026 PDF and the [February 2022 PDF](https://dod.hawaii.gov/hiema/files/2022/04/22-0412-State-Emergency-Support-Function-SESF-2-Communications-Annex.pdf) (still directly reachable, just not linked from this index) were opened directly on 2026-11-20. Both contain the same §4.3.3 fuel-coordination language at printed p. 4-4, lightly rephrased between versions: SESF #12 coordinates power-restoration timelines, identifies communications-outage impacts, and prioritizes fuel requirements for assets supporting critical communications. **Fact, HIGH** for both the index destination and both texts, directly compared.

**Correction, 2026-11-20:** the paragraph above and the one that originally followed it (claiming the index linked Feb 2022 and that the Nov 2026 PDF could not be retrieved) do not hold up. The [November 2026 SESF #2 Annex](https://dod.hawaii.gov/hiema/files/2026/11/State-Emergency-Support-Function-SESF-2-Communications-Annex-Updated-Nov9-2026-1.pdf) was retrieved directly via `curl` (HTTP 200) with no difficulty and opened in full: printed p. i names ETS Coordinating/Primary Agency, and §4.3.3 printed p. 4-4 contains the fuel-coordination language quoted above. **Fact, HIGH — freshly verified**, not a prior-review record. The live index was independently re-fetched three times total (across this project's work) and in every check links only this November 2026 file, never the February 2022 one.

The live index links the November 2021 [SESF #12 Energy Annex](https://dod.hawaii.gov/hiema/files/2022/01/HI-EOP-SESF-12-Annex.pdf) and shows no newer SESF #12 annex on that page. The annex describes fuel-supplier coordination, priority setting for scarce fuel/energy, emergency fuel for critical facilities, transportation, communications, and emergency operations, plus a Fuels Set-Aside tied to a Governor energy-emergency declaration; printed pp. 4-3 to 4-4. **Fact, HIGH** as to the observed index listing and opened 2021 text. A newer annex or separate procedure elsewhere remains **Unknown, HIGH**.

**Analysis, HIGH:** The reviewed HI-EOP and 2021 annex establish agency assignments and describe coordination mechanisms, but the reviewed primary pages do not establish a comparative fuel-priority order among hospitals, shelters, towers, data centers, or other asset classes. Actual fuel availability, generator endurance, and present operational capacity also remain **Unknown, HIGH**. See [HIEMA_PLAN_CROSSWALK.md](HIEMA_PLAN_CROSSWALK.md).

## Fallback layers when the internet is down

In order of what remains as each layer fails:

1. Satellite internet (Starlink and other low-orbit networks) — lower capacity than cables; priority likely goes to government and emergency users.
2. Inter-island cables and local networks may keep working inside Hawaiʻi while mainland-hosted cloud services become hard to reach.
3. Long-range HF radio (amateur and government) — works without cables or satellites; very slow.
4. Email over radio: Winlink, used by emergency groups.
5. Regional amateur radio data networks: AREDN carries internet-style traffic between linked radios.
6. Phone mesh: Meshtastic — a low-cost long-range radio that pairs with a phone by Bluetooth to text without cell, internet, or satellite. Relevance for AFN users requires evaluation.
7. Planned offline operation: local data copies and manual procedures that work with no network.

**Classification:** Analysis, based on general knowledge. **Confidence:** Moderate.

## Concentration risk on the backup layer

If cables or power fail, satellites may become a last link out of state. Starlink is largely controlled by one company, so concentration risk sits on the fallback layer itself. For an island state, this is a governance question. **Classification:** Analysis and Opinion. **Confidence:** Moderate.

## Historical note

ALOHAnet, built at the University of Hawaiʻi in 1971, was one of the first radio data networks and influenced Ethernet and Wi-Fi. **Classification:** Fact. **Confidence:** High.

## Open items for architecture mapping

1. **Resolved for ESF assignments and the 2022-vs-2026 fuel-coordination comparison; comparative priority ranking remains open.** The February 2026 HI-EOP assigns SESF #2 to DAGS/ETS (printed p. 5-20) and SESF #12 to DBEDT/Hawaiʻi State Energy Office (printed p. 5-21) — freshly confirmed by directly opening the November 2026 SESF #2 annex's printed p. i. The live HI-EMA index links only the November 2026 SESF #2 annex (confirmed in three independent checks); the February 2022 annex is real but not linked from it. Both annexes' §4.3.3, printed p. 4-4, were directly opened and compared on 2026-11-20: both record the same three elements — power-restoration timelines, communications-outage impacts, and critical-communications fuel coordination — lightly rephrased between versions. Fact, HIGH. The index links the November 2021 SESF #12 Energy annex; printed pp. 4-3 to 4-4 describe scarce-fuel priority setting and a Fuels Set-Aside. Comparative ranking among hospitals, shelters, communications assets, and data centers, and any SESF #12 procedure newer than November 2021, remain Unknown. See [HIEMA_PLAN_CROSSWALK.md](HIEMA_PLAN_CROSSWALK.md).
2. Identify which Oʻahu cell towers have generator backup and their fuel endurance.
3. Confirm undersea cable landing sites and their power backup.
4. Confirm AlohaNAP generator endurance.
5. Map AFN device dependencies (medical devices, mobility aids, communication apps) against each failure layer.
6. Evaluate Meshtastic and Winlink as shelter communication options.
7. Confirm Kapolei refinery and harbor resupply dependencies with state energy sources.

Unverified architecture statements above remain hypotheses as labeled. Official assignment and annex findings are limited to the cited dated documents; they do not establish present operational status. Fact/Analysis/Unknown, HIGH. See [EVIDENCE_REGISTER.md](EVIDENCE_REGISTER.md) and [HIEMA_PLAN_CROSSWALK.md](HIEMA_PLAN_CROSSWALK.md) for sources and printed-page citations.
