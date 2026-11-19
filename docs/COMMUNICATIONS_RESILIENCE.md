# Communications & Infrastructure Resilience Notes

**Prepared for:** Cyber Coalition, HAIC 2026 (ESF-6 AFN challenge)
**Source:** Voice working session, 2026-11-16.
**Status:** Working notes for architecture mapping. Not yet validated against state or official sources unless marked. Follows the project's standard classification: **Fact**, **Source Reported Claim**, **Analysis**, or **Opinion**, each with a stated confidence.

## Purpose

Capture the layered communications dependency chain for Oʻahu so the team can map what fails, in what order, and what fallback exists at each layer during a disaster — with focus on people with Access and Functional Needs (AFN), who often depend most on their devices for medical, mobility, and communication needs. This directly supports the Communication CMIST dimension and responds to the DHS challenge's own pain-point language: *"Communities with limited Wi-Fi... can be harder to plan for and reach and require more advanced planning and communication."*

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
| Two main Oʻahu data centers carry most of the load — DRFortress (near the airport, Honolulu) and AlohaNAP (Kapolei). Smaller operators include Servpac and Hawaiian Telcom. Directory sources list ~6 data centers in the Honolulu market. | Source Reported Claim (directory listings, not operator-confirmed) | Moderate |
| DRFortress reports on-site diesel lasting up to 80 hours at full load. | Source Reported Claim (Data Center Map listing) | Moderate |
| Large cloud providers spread each region across separate sites with independent power and replicate critical data to other regions. | Analysis | Moderate |
| Nearly all Hawaiʻi mainland traffic rides a small number of undersea cables; cable landing sites and internet exchange points are concentrated single points of failure. | Analysis | Moderate |
| Oʻahu fuel arrives largely through the harbor and the Kapolei refinery; port damage could cut generator resupply statewide. | Analysis — needs validation with state energy sources | Moderate |

## The critical question: after 80 hours

If a hurricane blocks fuel trucks, who decides which generators get diesel first — hospitals, shelters, cell towers, or data centers? This spans multiple Emergency Support Functions (energy, communications, ESF-6 mass care). **Classification: Analysis** — the official ESF numbering and lead agencies in the Hawaiʻi State Emergency Operations Plan still need verification before citing.

**Risk:** without a defined fuel priority that accounts for communications, AFN individuals in shelters may lose the device connectivity they rely on for medical, mobility, and communication needs.

## Fallback layers when the internet is down

In order of what remains as each layer fails:

1. Satellite internet (Starlink and other low-orbit networks) — far less capacity than cables; priority likely goes to government and emergency users.
2. Inter-island cables and local networks keep working inside Hawaiʻi, but mainland-hosted cloud services become hard to reach.
3. Long-range HF radio (ham and government) — works with no cables or satellites; very slow.
4. Email over radio: Winlink, already used by emergency groups.
5. Regional amateur radio data networks: AREDN carries internet-style traffic between linked radios.
6. Phone mesh: Meshtastic — a low-cost long-range radio that pairs with a phone by Bluetooth to text with no cell, internet, or satellite. Relevant for AFN users who already rely on phones.
7. Planned offline operation: local data copies, cash, and manual procedures that work with no network at all.

**Classification:** Analysis, based on general knowledge. **Confidence:** Moderate.

## Concentration risk on the backup layer

If cables or power fail, satellites become the last link out of state. Starlink is largely controlled by one company, so concentration risk sits on the fallback layer itself. For an island state, this is a governance gap worth naming. **Classification:** Analysis and Opinion. **Confidence:** Moderate.

## Historical note

ALOHAnet, built at the University of Hawaiʻi in 1971, was one of the first radio data networks and influenced Ethernet and Wi-Fi. Radio fallback returns to where networking began. **Classification:** Fact. **Confidence:** High.

## Open items for architecture mapping

1. Verify Hawaiʻi State Emergency Operations Plan ESF assignments and fuel priority policy.
2. Identify which Oʻahu cell towers have generator backup and their fuel endurance.
3. Confirm undersea cable landing sites and their power backup.
4. Confirm AlohaNAP generator endurance.
5. Map AFN device dependencies (medical devices, mobility aids, communication apps) against each failure layer.
6. Evaluate Meshtastic and Winlink as shelter communication options.
7. Confirm Kapolei refinery and harbor resupply dependencies with state energy sources.

None of this has been independently verified by the project beyond what's marked Fact above; treat every Analysis/Source Reported Claim row as a planning hypothesis requiring authoritative confirmation, consistent with the rest of this project's evidence discipline.
