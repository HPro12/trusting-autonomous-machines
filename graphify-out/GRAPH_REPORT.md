# Graph Report - .  (2026-07-05)

## Corpus Check
- 2 files · ~35,656 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 57 nodes · 64 edges · 12 communities (7 shown, 5 thin omitted)
- Extraction: 59% EXTRACTED · 41% INFERRED · 0% AMBIGUOUS · INFERRED: 26 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Chapter 1 — Human Limits & Trust|Chapter 1 — Human Limits & Trust]]
- [[_COMMUNITY_3D Drive Sim — Cockpit & Engine|3D Drive Sim — Cockpit & Engine]]
- [[_COMMUNITY_Chapter 2 — Perception & Fusion|Chapter 2 — Perception & Fusion]]
- [[_COMMUNITY_Chapter 3 — Long Tail & Proof|Chapter 3 — Long Tail & Proof]]
- [[_COMMUNITY_Drive Sim — Story & Save|Drive Sim — Story & Save]]
- [[_COMMUNITY_Drive Sim — Driving Mechanics|Drive Sim — Driving Mechanics]]
- [[_COMMUNITY_Cross-Chapter Themes|Cross-Chapter Themes]]
- [[_COMMUNITY_Accessibility & Inclusion|Accessibility & Inclusion]]
- [[_COMMUNITY_Brand & Tone|Brand & Tone]]
- [[_COMMUNITY_Diegetic UI|Diegetic UI]]
- [[_COMMUNITY_Portable Architecture|Portable Architecture]]
- [[_COMMUNITY_Show, Don't Lecture|Show, Don't Lecture]]

## God Nodes (most connected - your core abstractions)
1. `Chapter 1 — The Last Human Decision` - 7 edges
2. `Chapter 1 — The Last Human Decision` - 6 edges
3. `Chapter 2 — Inside the Machine` - 5 edges
4. `Chapter 3 — The Long Tail` - 5 edges
5. `Takeover / edge case` - 4 edges
6. `Sensor fusion` - 4 edges
7. `Graceful degradation` - 4 edges
8. `First-person cockpit driving sim` - 4 edges
9. `Takeover / edge case` - 4 edges
10. `Chapter 1 3D WebGL drive rebuild` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Minimal-risk maneuver` --semantically_similar_to--> `Graceful degradation`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter1.html → can_you_trust_your_car_chapter2.html
- `The long-tail problem` --semantically_similar_to--> `The long tail`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter1.html → can_you_trust_your_car_chapter3.html
- `3D takeover lane-dodge measuring reaction time` --semantically_similar_to--> `Takeover / edge case`  [INFERRED] [semantically similar]
  can_you_trust_your_car_drive.html → README.md
- `Chapter 2 — Inside the Machine` --references--> `Chapter 3 — The Long Tail`  [INFERRED]
  can_you_trust_your_car_chapter2.html → can_you_trust_your_car_chapter3.html
- `Choices leave marks` --rationale_for--> `Trust calibration (Trust & Attention meters)`  [INFERRED]
  PRODUCT.md → can_you_trust_your_car_chapter1.html

## Import Cycles
- None detected.

## Communities (12 total, 5 thin omitted)

### Community 0 - "Chapter 1 — Human Limits & Trust"
Cohesion: 0.22
Nodes (11): Automation-induced complacency, Automation levels (L0/L2/L4), Braking distance (68 meters), L2 assistance, Reaction time, Takeover / edge case, Chapter 1 — The Last Human Decision, Trust calibration (Trust & Attention meters) (+3 more)

### Community 1 - "3D Drive Sim — Cockpit & Engine"
Cohesion: 0.27
Nodes (10): First-person cockpit driving sim, iMessage on the central touchscreen, Inlined three.js (single-file, offline, file://), Tesla-style minimalist cockpit (copyright-safe), Three.js / WebGL engine, WEBSITE-TODO: swap inlined library for CDN, Chapter 1 — The Last Human Decision, Chapter 1 3D WebGL drive rebuild (+2 more)

### Community 2 - "Chapter 2 — Perception & Fusion"
Cohesion: 0.36
Nodes (8): Minimal-risk maneuver, Adaptive weighting, Graceful degradation, Chapter 2 — Inside the Machine, Sensor redundancy, Sensor failure / glare, Sensor fusion, Sensor operation (camera/LiDAR/radar)

### Community 3 - "Chapter 3 — Long Tail & Proof"
Cohesion: 0.38
Nodes (7): The long-tail problem, Near-miss classification, Deciding under uncertainty, Log review, The long tail, Statistical impossibility (~275M miles, RAND), Chapter 3 — The Long Tail

### Community 4 - "Drive Sim — Story & Save"
Cohesion: 0.29
Nodes (7): 3D takeover lane-dodge measuring reaction time, Ported branching story, decisions, and debrief, cytc.v1 localStorage save, Automation-induced complacency, cytc.v1 localStorage save, L2 assistance, Takeover / edge case

### Community 5 - "Drive Sim — Driving Mechanics"
Cohesion: 0.40
Nodes (5): Constant forward speed, Discrete pre-animated banked lane change, Synthesized EV powertrain audio and adaptive score, NPC traffic (same-direction and oncoming), Two-carriageway highway with median wall

### Community 6 - "Cross-Chapter Themes"
Cohesion: 0.50
Nodes (4): Chapter 2 — Inside the Machine, Chapter 3 — The Long Tail, Long tail and limits of statistical proof, Sensor fusion and adaptive weighting

## Knowledge Gaps
- **11 isolated node(s):** `L2 ≠ autonomous`, `Accessibility & inclusion`, `Cinematic, grounded, sober brand`, `The long-tail problem`, `Automation levels (L0/L2/L4)` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Chapter 1 — The Last Human Decision` connect `3D Drive Sim — Cockpit & Engine` to `Drive Sim — Story & Save`, `Cross-Chapter Themes`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `Chapter 2 — Inside the Machine` connect `Chapter 2 — Perception & Fusion` to `Chapter 1 — Human Limits & Trust`, `Chapter 3 — Long Tail & Proof`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Why does `Chapter 1 — The Last Human Decision` connect `Chapter 1 — Human Limits & Trust` to `Chapter 2 — Perception & Fusion`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Takeover / edge case` (e.g. with `Automation-induced complacency` and `Minimal-risk maneuver`) actually correct?**
  _`Takeover / edge case` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Show, don't lecture`, `Diegetic UI`, `Choices leave marks` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._