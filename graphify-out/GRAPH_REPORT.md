# Graph Report - .  (2026-07-21)

## Corpus Check
- 17 files · ~134,025 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 79 nodes · 111 edges · 8 communities
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 40 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Perception, Sensors & Autonomy Levels|Perception, Sensors & Autonomy Levels]]
- [[_COMMUNITY_Safety Decisions & the Long Tail|Safety Decisions & the Long Tail]]
- [[_COMMUNITY_Public Trust & Deployment|Public Trust & Deployment]]
- [[_COMMUNITY_Responsibility & Game Design|Responsibility & Game Design]]
- [[_COMMUNITY_Robotaxi Operations & L5|Robotaxi Operations & L5]]
- [[_COMMUNITY_Proving Safety & Disclosure|Proving Safety & Disclosure]]
- [[_COMMUNITY_Ethics & the Wuhan Flashpoint|Ethics & the Wuhan Flashpoint]]
- [[_COMMUNITY_Regulation & Operating Domains|Regulation & Operating Domains]]

## God Nodes (most connected - your core abstractions)
1. `Trusting Autonomous Machines (interactive education project)` - 10 edges
2. `Public trust and acceptance (心智 / mindshare)` - 9 edges
3. `Chapter 5 - The Trust Gap (finale)` - 9 edges
4. `Deploy-first, regulate-later (pilot-first, then converge)` - 6 edges
5. `Chapter 1 - The Night Drive (Can You Trust Your Car?)` - 6 edges
6. `Corner cases (low-frequency, high-risk edge scenarios)` - 5 edges
7. `L4-to-L5 barrier: not a linear upgrade` - 5 edges
8. `LiDAR+HD-map (Waymo) vs vision/end-to-end (Tesla) routes` - 5 edges
9. `Safety as the hard constraint (top priority)` - 5 edges
10. `Chapter 2 - Inside the Machine (machine perception)` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Statistical impossibility of proving safety (~275M miles, RAND)` --semantically_similar_to--> `Data-driven models improve but never reach 100 / no defined ceiling`  [INFERRED] [semantically similar]
  README.md → Interviews/周勋.txt
- `Chapter 5 - The Trust Gap (finale)` --conceptually_related_to--> `Asymmetric tolerance: human error accepted, machine error is not`  [INFERRED]
  README.md → Interviews/唐一斐.txt
- `Chapter 5 - The Trust Gap (finale)` --conceptually_related_to--> `Public loss-of-control fear and driver unemployment anxiety`  [INFERRED]
  README.md → Interviews/唐一斐.txt
- `Chapter 1 - The Night Drive (Can You Trust Your Car?)` --conceptually_related_to--> `L2 assistance vs L4 autonomy (decision base, redundancy, sensors)`  [INFERRED]
  README.md → Interviews/孙雷.txt
- `Chapter 4 - Who's Responsible? (liability)` --conceptually_related_to--> `L2 assistance vs L4 autonomy (decision base, redundancy, sensors)`  [INFERRED]
  README.md → Interviews/孙雷.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Deploy-first, regulate-later regulatory posture (pilot, whitelist, rings, EV precedent)** — concept_deploy_first_regulate_later, concept_whitelist_regulation, concept_ring_based_rollout, concept_ev_transition_precedent, concept_gov_interdept_game [INFERRED 0.85]
- **The liability / black-box problem (opaque decision layer, fault assignment, undefined ceiling)** — concept_model_interpretability_black_box, concept_liability_assignment, concept_data_driven_never_100, readme_chapter4_whos_responsible [INFERRED 0.85]
- **Building public trust: exposure, experience, error-tolerance asymmetry** — concept_public_trust_acceptance, concept_exposure_gap, concept_experience_builds_trust, concept_human_vs_machine_error_acceptance, readme_chapter5_trust_gap [INFERRED 0.85]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Perception, Sensors & Autonomy Levels"
Cohesion: 0.18
Nodes (14): China vs US road environment and regulatory philosophy, Government inter-department game: safety vs tech progress, L2 as comfort feature for selling cars (70-80 points), L2 assistance vs L4 autonomy (decision base, redundancy, sensors), LiDAR+HD-map (Waymo) vs vision/end-to-end (Tesla) routes, L4 redundancy and minimal-risk-condition fallback (Plan B), Safety floor (下限) vs ceiling (上限), Multi-sensor fusion (LiDAR, radar, camera) (+6 more)

### Community 1 - "Safety Decisions & the Long Tail"
Cohesion: 0.21
Nodes (12): Carmaker owns the full data set / golden training data, Corner cases (low-frequency, high-risk edge scenarios), Data augmentation, synthesis and simulation for rare data, Layered decision module (perception, prediction, planning, control), Ghost-probe: sudden pedestrian dart-out (鬼探头), Multi-objective constrained decision optimization, Near-miss vs collision data capture (golden data), Safety as the hard constraint (top priority) (+4 more)

### Community 2 - "Public Trust & Deployment"
Cohesion: 0.26
Nodes (12): First-hand experience builds objective public trust, Public exposure gap (few robotaxis vs many human cabs), Asymmetric tolerance: human error accepted, machine error is not, Pedestrians exploit AV yielding behavior, POI pickup/dropoff points (bus-stop-like) and user-education gap, Public trust and acceptance (心智 / mindshare), Ring-based phased rollout (outer/middle/inner rings), Whitelist regulation mechanism (default-deny, prove-then-open) (+4 more)

### Community 3 - "Responsibility & Game Design"
Cohesion: 0.29
Nodes (10): Accident liability and responsibility assignment, Model interpretability / deep-learning black-box problem, Design principle: Choices leave marks, Design principle: Diegetic UI, Design principle: Portable by construction, Design principle: Show, don't lecture, Trusting Autonomous Machines (interactive education project), Chapter 1 - The Night Drive (Can You Trust Your Car?) (+2 more)

### Community 4 - "Robotaxi Operations & L5"
Cohesion: 0.22
Nodes (9): L5 as an AGI / embodied-AI end-state, Intercity routes vs high-speed rail and jurisdiction, L4-to-L5 barrier: not a linear upgrade, Remote operators (RO) and P0/P1/P2 incident grading, Robotaxi economics: commercial closed-loop and scale effect, Robotaxi onboard safety processes (seatbelt, door interlock), Robotaxi comfort/experience advantage over human taxi, Core user need: safe, low-cost A-to-B movement (+1 more)

### Community 5 - "Proving Safety & Disclosure"
Cohesion: 0.25
Nodes (8): Public disclosure of safety data (China vs US), Data-driven models improve but never reach 100 / no defined ceiling, Deploy-first, regulate-later (pilot-first, then converge), EV-transition precedent (undisclosed fires, smooth adoption), Four dimensions: law, technology, industrialization cost, public cognition, China: government wiser than public + high public trust in government, Design principle: Data is the drama, Statistical impossibility of proving safety (~275M miles, RAND)

### Community 6 - "Ethics & the Wuhan Flashpoint"
Cohesion: 0.33
Nodes (7): All lives weighted equally (no passenger vs pedestrian preference), Downgrade/degradation strategy over binary A/B choice, Shadow-mode learning / imitating the median human driver, Trolley problem as ethics, not engineering, Wuhan Robotaxi (Luobo Kuaipao) incident, Policy uncertainty tightening after Wuhan; ops tooling gaps, Brake-first: collision avoidance is a vehicle technical problem

### Community 7 - "Regulation & Operating Domains"
Cohesion: 0.29
Nodes (7): AV law layered on top of general traffic law (additive, not conflicting), Need for national universal AV legislation, Operational Design Domain (可运营域, operational area), Driving skill not degraded by using automation, Firms define edge-case rules differently; risk without a common standard, Highway L2 relieves fatigue; city driving stays harder, Automation-induced complacency

## Knowledge Gaps
- **11 isolated node(s):** `L2 as comfort feature for selling cars (70-80 points)`, `Carmaker owns the full data set / golden training data`, `New-tech precedent: automobile vs the horse-carriage era`, `Robotaxi comfort/experience advantage over human taxi`, `AV law layered on top of general traffic law (additive, not conflicting)` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Trusting Autonomous Machines (interactive education project)` connect `Responsibility & Game Design` to `Perception, Sensors & Autonomy Levels`, `Safety Decisions & the Long Tail`, `Public Trust & Deployment`, `Proving Safety & Disclosure`?**
  _High betweenness centrality (0.390) - this node is a cross-community bridge._
- **Why does `Chapter 5 - The Trust Gap (finale)` connect `Public Trust & Deployment` to `Responsibility & Game Design`?**
  _High betweenness centrality (0.270) - this node is a cross-community bridge._
- **Why does `L4-to-L5 barrier: not a linear upgrade` connect `Robotaxi Operations & L5` to `Public Trust & Deployment`, `Proving Safety & Disclosure`, `Regulation & Operating Domains`?**
  _High betweenness centrality (0.241) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Public trust and acceptance (心智 / mindshare)` (e.g. with `Public exposure gap (few robotaxis vs many human cabs)` and `Asymmetric tolerance: human error accepted, machine error is not`) actually correct?**
  _`Public trust and acceptance (心智 / mindshare)` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Chapter 5 - The Trust Gap (finale)` (e.g. with `Asymmetric tolerance: human error accepted, machine error is not` and `Pedestrians exploit AV yielding behavior`) actually correct?**
  _`Chapter 5 - The Trust Gap (finale)` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `Deploy-first, regulate-later (pilot-first, then converge)` (e.g. with `EV-transition precedent (undisclosed fires, smooth adoption)` and `Government inter-department game: safety vs tech progress`) actually correct?**
  _`Deploy-first, regulate-later (pilot-first, then converge)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Chapter 1 - The Night Drive (Can You Trust Your Car?)` (e.g. with `Design principle: Show, don't lecture` and `L2 assistance vs L4 autonomy (decision base, redundancy, sensors)`) actually correct?**
  _`Chapter 1 - The Night Drive (Can You Trust Your Car?)` has 3 INFERRED edges - model-reasoned connections that need verification._