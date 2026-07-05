# Graph Report - .  (2026-07-06)

## Corpus Check
- 2 files · ~30,902 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 51 nodes · 56 edges · 12 communities (7 shown, 5 thin omitted)
- Extraction: 68% EXTRACTED · 32% INFERRED · 0% AMBIGUOUS · INFERRED: 18 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Chapter 1 — Story & Save|Chapter 1 — Story & Save]]
- [[_COMMUNITY_Chapter 1 — Human Limits & Driving|Chapter 1 — Human Limits & Driving]]
- [[_COMMUNITY_Chapter 1 — Night Drive & World|Chapter 1 — Night Drive & World]]
- [[_COMMUNITY_Chapter 2 — Perception & Fusion|Chapter 2 — Perception & Fusion]]
- [[_COMMUNITY_Chapter 3 — Long Tail & Proof|Chapter 3 — Long Tail & Proof]]
- [[_COMMUNITY_Chapter 1 — Cockpit & Motion|Chapter 1 — Cockpit & Motion]]
- [[_COMMUNITY_Three.js  Inlined Engine|Three.js / Inlined Engine]]
- [[_COMMUNITY_Accessibility & Inclusion|Accessibility & Inclusion]]
- [[_COMMUNITY_Brand & Tone|Brand & Tone]]
- [[_COMMUNITY_Diegetic UI|Diegetic UI]]
- [[_COMMUNITY_Portable Architecture|Portable Architecture]]
- [[_COMMUNITY_Show, Don't Lecture|Show, Don't Lecture]]

## God Nodes (most connected - your core abstractions)
1. `Chapter 3 — The Long Tail` - 5 edges
2. `first-person cockpit driving sim` - 5 edges
3. `Chapter 2 — Inside the Machine` - 4 edges
4. `Sensor fusion` - 4 edges
5. `Chapter 1 — Can You Trust Your Car? (The Night Drive)` - 4 edges
6. `Chapter 1 — Can You Trust Your Car? (The Night Drive)` - 4 edges
7. `Chapter 2 — Inside the Machine` - 4 edges
8. `Graceful degradation` - 3 edges
9. `Statistical impossibility (~275M miles, RAND)` - 3 edges
10. `Deciding under uncertainty` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Chapter 2 — Inside the Machine` --references--> `Chapter 3 — The Long Tail`  [INFERRED]
  can_you_trust_your_car_chapter2.html → can_you_trust_your_car_chapter3.html
- `Choices leave marks` --rationale_for--> `trust calibration (Trust & Attention meters)`  [INFERRED]
  PRODUCT.md → can_you_trust_your_car_chapter1.html
- `Data is the drama` --rationale_for--> `braking distance (68 metres)`  [INFERRED]
  PRODUCT.md → can_you_trust_your_car_chapter1.html
- `L2 ≠ autonomous` --conceptually_related_to--> `L2 assistance`  [INFERRED]
  PRODUCT.md → can_you_trust_your_car_chapter1.html
- `Chapter 1 — Can You Trust Your Car? (The Night Drive)` --semantically_similar_to--> `Chapter 1 — Can You Trust Your Car? (The Night Drive)`  [EXTRACTED] [semantically similar]
  README.md → can_you_trust_your_car_chapter1.html

## Import Cycles
- None detected.

## Communities (12 total, 5 thin omitted)

### Community 0 - "Chapter 1 — Story & Save"
Cohesion: 0.22
Nodes (9): automation levels (L0/L2/L4), branching decisions, outcomes, and a personalized debrief, cytc.v1 localStorage save, a decision pauses/freezes the sim, L2 assistance, L2 ≠ autonomous, trust calibration (Trust & Attention meters), Choices leave marks (+1 more)

### Community 1 - "Chapter 1 — Human Limits & Driving"
Cohesion: 0.25
Nodes (8): automation-induced complacency, braking distance (68 metres), discrete pre-animated banked lane change (A/D or arrows, low sensitivity, cannot leave road), NPC traffic (same-direction and oncoming), reaction time, takeover / edge case as 3D lane-dodge measuring reaction time, two-carriageway highway with median wall and ≥2 lanes per side, Data is the drama

### Community 2 - "Chapter 1 — Night Drive & World"
Cohesion: 0.43
Nodes (7): Continue to Chapter 2 link, Chapter 1 — Can You Trust Your Car? (The Night Drive), night sky with stars/moon and distant city skyline, Chapter 1 — Can You Trust Your Car? (The Night Drive), Chapter 2 — Inside the Machine, Chapter 3 — The Long Tail, Trusting Autonomous Machines (project)

### Community 3 - "Chapter 2 — Perception & Fusion"
Cohesion: 0.43
Nodes (7): Adaptive weighting, Graceful degradation, Chapter 2 — Inside the Machine, Sensor redundancy, Sensor failure / glare, Sensor fusion, Sensor operation (camera/LiDAR/radar)

### Community 4 - "Chapter 3 — Long Tail & Proof"
Cohesion: 0.47
Nodes (6): Near-miss classification, Deciding under uncertainty, Log review, The long tail, Statistical impossibility (~275M miles, RAND), Chapter 3 — The Long Tail

### Community 5 - "Chapter 1 — Cockpit & Motion"
Cohesion: 0.40
Nodes (5): constant forward speed, synthesized EV powertrain audio (whine rising with speed + wind bed) and adaptive score, first-person cockpit driving sim, iMessage on the central touchscreen, Tesla-style minimalist cockpit (no brand logos, copyright-safe)

### Community 6 - "Three.js / Inlined Engine"
Cohesion: 0.67
Nodes (4): inlined three.js (single-file, offline, file://) with WEBSITE-TODO to swap to CDN, Three.js / WebGL engine, 3D night-drive (WebGL/Three.js first-person expressway), inlined Three.js with WEBSITE-TODO to swap for CDN importmap

## Knowledge Gaps
- **8 isolated node(s):** `L2 ≠ autonomous`, `Accessibility & inclusion`, `Cinematic, grounded, sober brand`, `Log review`, `The long tail` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `first-person cockpit driving sim` connect `Chapter 1 — Cockpit & Motion` to `Chapter 1 — Human Limits & Driving`, `Chapter 1 — Night Drive & World`, `Three.js / Inlined Engine`?**
  _High betweenness centrality (0.241) - this node is a cross-community bridge._
- **Why does `discrete pre-animated banked lane change (A/D or arrows, low sensitivity, cannot leave road)` connect `Chapter 1 — Human Limits & Driving` to `Chapter 1 — Cockpit & Motion`?**
  _High betweenness centrality (0.178) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Sensor fusion` (e.g. with `Adaptive weighting` and `Sensor redundancy`) actually correct?**
  _`Sensor fusion` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Show, don't lecture`, `Diegetic UI`, `Choices leave marks` to the rest of the system?**
  _13 weakly-connected nodes found - possible documentation gaps or missing edges._