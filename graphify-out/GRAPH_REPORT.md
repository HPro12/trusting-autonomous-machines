# Graph Report - .  (2026-06-30)

## Corpus Check
- Corpus is ~2,498 words - fits in a single context window. You may not need a graph.

## Summary
- 29 nodes · 29 edges · 6 communities (5 shown, 1 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.87)
- Token cost: 0 input · 50,139 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Edge-Case Failure & Takeover|Edge-Case Failure & Takeover]]
- [[_COMMUNITY_L2 Assistance & Responsibility|L2 Assistance & Responsibility]]
- [[_COMMUNITY_Human Driving & Scene Engine|Human Driving & Scene Engine]]
- [[_COMMUNITY_Project & Trust Framing|Project & Trust Framing]]
- [[_COMMUNITY_SAE Levels & Car Comparison|SAE Levels & Car Comparison]]
- [[_COMMUNITY_Summary & Host Hook|Summary & Host Hook]]

## God Nodes (most connected - your core abstractions)
1. `edgeChoice() Handler` - 5 edges
2. `Can You Trust Your Car? Interactive Experience` - 3 edges
3. `goTo() Scene Navigation Function` - 3 edges
4. `Scene 3: Edge Case (Construction Zone)` - 3 edges
5. `l2Choice() Handler` - 3 edges
6. `Takeover / Handover Problem` - 3 edges
7. `Trusting Autonomous Machines (Project)` - 2 edges
8. `Chapter 1 — Can You Trust Your Car?` - 2 edges
9. `Central Question: When and How Much to Trust Machines` - 2 edges
10. `Scene 1: Human Driving` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Trust Calibration` --conceptually_related_to--> `Central Question: When and How Much to Trust Machines`  [INFERRED]
  can_you_trust_your_car_chapter1.html → README.md
- `Chapter 1 — Can You Trust Your Car?` --references--> `Can You Trust Your Car? Interactive Experience`  [EXTRACTED]
  README.md → can_you_trust_your_car_chapter1.html
- `Can You Trust Your Car? Interactive Experience` --implements--> `Single Static HTML, No Build Step`  [EXTRACTED]
  can_you_trust_your_car_chapter1.html → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Chapter 1 Five-Scene Branching Narrative Flow** — can_you_trust_your_car_chapter1_scene_human_driving, can_you_trust_your_car_chapter1_scene_l2_assistance, can_you_trust_your_car_chapter1_scene_edge_case, can_you_trust_your_car_chapter1_scene_compare_cars, can_you_trust_your_car_chapter1_scene_summary [EXTRACTED 1.00]
- **Core Autonomous-Driving Safety Themes** — can_you_trust_your_car_chapter1_automation_induced_complacency, can_you_trust_your_car_chapter1_long_tail_corner_cases, can_you_trust_your_car_chapter1_l2_not_autonomous, can_you_trust_your_car_chapter1_trust_calibration [INFERRED 0.85]

## Communities (6 total, 1 thin omitted)

### Community 0 - "Edge-Case Failure & Takeover"
Cohesion: 0.47
Nodes (6): Automation-Induced Complacency, edgeChoice() Handler, Minimal Risk Maneuver, Scene 3: Edge Case (Construction Zone), Takeover / Handover Problem, 2016 Tesla Autopilot Fatality

### Community 1 - "L2 Assistance & Responsibility"
Cohesion: 0.33
Nodes (6): China L2 Legal Liability (2026), initL2() Scene Animator, L2 ≠ Autonomous (Driver Remains Responsible), l2Choice() Handler, Long-Tail / Corner Case Scenarios, Scene 2: L2 Assistance

### Community 2 - "Human Driving & Scene Engine"
Cohesion: 0.33
Nodes (6): driveChoice() Handler, goTo() Scene Navigation Function, initDrive1() Scene Animator, initEdge() Scene Animator, Reaction Time & Braking Distance Model, Scene 1: Human Driving

### Community 3 - "Project & Trust Framing"
Cohesion: 0.40
Nodes (6): Can You Trust Your Car? Interactive Experience, Trust Calibration, Central Question: When and How Much to Trust Machines, Chapter 1 — Can You Trust Your Car?, Single Static HTML, No Build Step, Trusting Autonomous Machines (Project)

### Community 4 - "SAE Levels & Car Comparison"
Cohesion: 0.67
Nodes (3): pickCar() Handler, SAE Automation Levels (L0/L2/L4/L5), Scene 4: Compare Cars (L0/L2/L4)

## Knowledge Gaps
- **7 isolated node(s):** `Scene 4: Compare Cars (L0/L2/L4)`, `Scene 5: Summary / Final`, `sendPrompt() Host-Provided Function`, `SAE Automation Levels (L0/L2/L4/L5)`, `China L2 Legal Liability (2026)` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `goTo() Scene Navigation Function` connect `Human Driving & Scene Engine` to `L2 Assistance & Responsibility`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._
- **Why does `edgeChoice() Handler` connect `Edge-Case Failure & Takeover` to `L2 Assistance & Responsibility`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Why does `Scene 3: Edge Case (Construction Zone)` connect `Edge-Case Failure & Takeover` to `Human Driving & Scene Engine`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **What connects `Single Static HTML, No Build Step`, `Scene 4: Compare Cars (L0/L2/L4)`, `Scene 5: Summary / Final` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._