# Graph Report - .  (2026-07-06)

## Corpus Check
- 3 files · ~75,834 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 63 nodes · 74 edges · 11 communities (6 shown, 5 thin omitted)
- Extraction: 73% EXTRACTED · 27% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Chapter 3 — Long Tail Review|Chapter 3 — Long Tail Review]]
- [[_COMMUNITY_Chapter 1 — Human Limits & Trust|Chapter 1 — Human Limits & Trust]]
- [[_COMMUNITY_Chapter 2 — Perception & Fusion|Chapter 2 — Perception & Fusion]]
- [[_COMMUNITY_Cross-Chapter Continuity|Cross-Chapter Continuity]]
- [[_COMMUNITY_3D Engine — Audio & Nav|3D Engine — Audio & Nav]]
- [[_COMMUNITY_3D Driving Mechanics|3D Driving Mechanics]]
- [[_COMMUNITY_Accessibility & Inclusion|Accessibility & Inclusion]]
- [[_COMMUNITY_Brand & Tone|Brand & Tone]]
- [[_COMMUNITY_Diegetic UI|Diegetic UI]]
- [[_COMMUNITY_Portable Architecture|Portable Architecture]]
- [[_COMMUNITY_Show, Don't Lecture|Show, Don't Lecture]]

## God Nodes (most connected - your core abstractions)
1. `Inside the Machine — 3D perception chapter` - 7 edges
2. `Chapter 2 — Inside the Machine` - 6 edges
3. `Chapter 3 — The Long Tail` - 6 edges
4. `The Long Tail — 3D dashcam safety review` - 6 edges
5. `first-person cockpit driving sim` - 5 edges
6. `Shared real-3D Three.js/WebGL engine` - 5 edges
7. `cytc.v1 shared localStorage continuity (merge-on-write)` - 5 edges
8. `Sensor-fusion weight sliders (Camera/LiDAR/Radar)` - 4 edges
9. `Camera glare collapse forces re-weighting (graceful degradation)` - 4 edges
10. `Chapter 1 — Can You Trust Your Car? (The Night Drive)` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Shares Ch1 3D engine, cockpit, and audio` --semantically_similar_to--> `Shared real-3D Three.js/WebGL engine`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter2.html → README.md
- `Reuses Three.js engine as reviewed dashcam footage (cockpit hidden)` --semantically_similar_to--> `Shared real-3D Three.js/WebGL engine`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter3.html → README.md
- `Sensor-fusion weight sliders (Camera/LiDAR/Radar)` --semantically_similar_to--> `Sensor fusion, redundancy, adaptive weighting (Ch2 themes)`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter2.html → README.md
- `Inside the Machine — 3D perception chapter` --semantically_similar_to--> `Chapter 2 — Inside the Machine`  [EXTRACTED] [semantically similar]
  can_you_trust_your_car_chapter2.html → README.md
- `Camera glare collapse forces re-weighting (graceful degradation)` --semantically_similar_to--> `Graceful degradation under sensor failure`  [INFERRED] [semantically similar]
  can_you_trust_your_car_chapter2.html → README.md

## Import Cycles
- None detected.

## Communities (11 total, 5 thin omitted)

### Community 0 - "Chapter 3 — Long Tail Review"
Cohesion: 0.19
Nodes (13): Scan 10,000 km of fleet logs to near-miss at km 6,213, Graceful finale (no Chapter 4 link), Classify near-miss (bug / edge case / acceptable risk), Flagged pedestrian gets live detection box, Recommendation (deploy / keep testing / limited rollout), Control-room review station (scrubber, near-miss flag, stats panel), Reuses Three.js engine as reviewed dashcam footage (cockpit hidden), Statistical-impossibility panel (275M miles RAND, 11B for proof) (+5 more)

### Community 1 - "Chapter 1 — Human Limits & Trust"
Cohesion: 0.18
Nodes (12): automation-induced complacency, automation levels (L0/L2/L4), branching decisions, outcomes, and a personalized debrief, cytc.v1 localStorage save, a decision pauses/freezes the sim, iMessage on the central touchscreen, L2 assistance, L2 ≠ autonomous (+4 more)

### Community 2 - "Chapter 2 — Perception & Fusion"
Cohesion: 0.28
Nodes (9): AR perception overlay (camera boxes, LiDAR points, radar brackets), AUTO reliability-based weighting, Camera glare collapse forces re-weighting (graceful degradation), Live certainty score, Inside the Machine — 3D perception chapter, Sensor-fusion weight sliders (Camera/LiDAR/Radar), Trust calibration (Ch2 theme), Trust-the-sensor A/B/C decision (possible crash) (+1 more)

### Community 3 - "Cross-Chapter Continuity"
Cohesion: 0.31
Nodes (9): Reads Ch1 car pick, writes chapter2 to cytc.v1, Shares Ch1 3D engine, cockpit, and audio, Writes chapter3 to cytc.v1, Chapter 1 — Can You Trust Your Car? (3D Night Drive), Chapter 2 — Inside the Machine, cytc.v1 shared localStorage continuity (merge-on-write), Trusting Autonomous Machines (project), Sensor fusion, redundancy, adaptive weighting (Ch2 themes) (+1 more)

### Community 4 - "3D Engine — Audio & Nav"
Cohesion: 0.25
Nodes (8): constant forward speed, Continue to Chapter 2 link, synthesized EV powertrain audio (whine rising with speed + wind bed) and adaptive score, first-person cockpit driving sim, inlined three.js (single-file, offline, file://) with WEBSITE-TODO to swap to CDN, Chapter 1 — Can You Trust Your Car? (The Night Drive), night sky with stars/moon and distant city skyline, Three.js / WebGL engine

### Community 5 - "3D Driving Mechanics"
Cohesion: 0.29
Nodes (7): braking distance (68 metres), discrete pre-animated banked lane change (A/D or arrows, low sensitivity, cannot leave road), NPC traffic (same-direction and oncoming), reaction time, takeover / edge case as 3D lane-dodge measuring reaction time, two-carriageway highway with median wall and ≥2 lanes per side, Data is the drama

## Knowledge Gaps
- **11 isolated node(s):** `L2 ≠ autonomous`, `Accessibility & inclusion`, `Cinematic, grounded, sober brand`, `NPC traffic (same-direction and oncoming)`, `night sky with stars/moon and distant city skyline` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `first-person cockpit driving sim` connect `3D Engine — Audio & Nav` to `Chapter 1 — Human Limits & Trust`, `3D Driving Mechanics`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Why does `Inside the Machine — 3D perception chapter` connect `Chapter 2 — Perception & Fusion` to `Cross-Chapter Continuity`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `takeover / edge case as 3D lane-dodge measuring reaction time` connect `3D Driving Mechanics` to `Chapter 1 — Human Limits & Trust`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **What connects `Show, don't lecture`, `Diegetic UI`, `Choices leave marks` to the rest of the system?**
  _19 weakly-connected nodes found - possible documentation gaps or missing edges._