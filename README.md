# Trusting Autonomous Machines

An interactive, public-interest educational project about autonomous driving safety and the question at its core: **when should humans trust machines — and how much?**

## Chapter 1 — Can You Trust Your Car?

*The Night Drive*

A self-contained, real-3D (WebGL / [Three.js](https://threejs.org)) driving experience that puts you in a first-person cockpit on a late-night expressway. You sit in a minimalist EV-style interior (no brand marks) and drive a two-carriageway highway with a median wall, lane markings, NPC traffic in both directions, and a starlit skyline. The car holds a constant speed; you change lanes with **A/D** or the **arrow keys** — a discrete, banked, pre-animated lane switch, so you can't drift off the road. Audio is a synthesized EV powertrain (inverter whine rising with speed + a wind bed) plus an adaptive night score. A branching story, typewritten dialogue, and two live meters (Trust and Attention) play as overlays, and your run is saved to `localStorage` (`cytc.v1`) to carry into later chapters.

The drive moves through five beats:

1. **Human driving** — A fatigued midnight drive. An **iMessage arrives on the car's central touchscreen**; your choice about it is scored against real reaction-time and braking-distance data.
2. **L2 assistance** — Rain, and the car takes over steering and speed. You confront who is actually responsible.
3. **The takeover** — A stalled car blocks your lane and the system hands control back. You must **change lanes in time** — a 3D dodge that measures your real reaction time. Illustrates "automation-induced complacency."
4. **Choose your car** — Compare L0, L2, and L4 vehicles. Your pick, and the rest of your run, is saved to `cytc.v1`.
5. **Debrief** — A personalized recap: a timeline of every choice and its consequence, your final Trust and Attention meters, your takeover reaction time, and a closing verdict written from the path you took — then on to Chapter 2.

The content is based on interviews with autonomous-driving industry professionals in China and reflects the legal and technical landscape as of 2026.

> **Portability note:** Chapter 1 **inlines** Three.js so it stays a single, offline, double-clickable page. A `WEBSITE-TODO` comment marks where to swap the inlined library for a CDN importmap once the chapters are served as part of a website.

## Chapter 2 — Inside the Machine

*How does a machine perceive the world — and what does it miss?*

You keep driving, but now you can see what the car sees. Augmented-reality overlays paint the road with the machine's own perception:

1. **Sensor operation** — camera bounding boxes and confidence scores, a LiDAR point cloud, and radar brackets, all locked to the moving world.
2. **Sensor fusion** — a pedestrian at night. You drag Camera/LiDAR/Radar weight sliders and watch a live certainty score respond, then hit **AUTO** to see how the car itself weighs each sensor by how reliable it is right now.
3. **Sensor failure** — oncoming glare blinds the camera; you watch its confidence collapse and the system re-weight onto LiDAR and radar to stay safe.
4. **Fusion decision** — with the camera blind and an ambiguous object in the lane, you decide which sensor to trust — with real consequences.

Central themes: sensor fusion, redundancy, adaptive weighting, and graceful degradation.

Chapter 2 runs on the same real-3D (Three.js) engine as Chapter 1 — the perception overlays are projected onto the live 3D world — and reads your car pick from Chapter 1's `cytc.v1` save.

## Chapter 3 — The Long Tail

*How do you prove a machine is safe enough?*

You step out of the car and into the role of a safety evaluator at an AV company, working a control-room review station (the road engine is reused as reviewed dashcam footage):

1. **Log review** — scan through 10,000 km of mostly-uneventful fleet logs on a timeline; one near-miss flags.
2. **Classification** — decide what the near-miss is: a software bug, a rare edge case, or an acceptable statistical risk — each defensible, none clearly right.
3. **Statistical impossibility** — an interactive look at the math: you'd need ~275 million miles (RAND) just to show, with confidence, that the car is as safe as a human — and billions for real proof, which no fleet has driven incident-free. The long tail of rare events can never be fully tested.
4. **Recommendation** — under that irreducible uncertainty, you still have to advise: deploy, keep testing, or a limited supervised rollout.

Central themes: the long tail, the limits of statistical proof, simulation, and deciding under uncertainty.

Chapter 3 reuses the Three.js engine as the reviewed dashcam footage (the cockpit is hidden for a forward-camera look, and the flagged pedestrian gets a live detection box).

## Chapter 4 — Who's Responsible?

*When a machine causes harm, who answers for it?*

You leave the driver's seat again — this time as the **regulator** investigating a crash. A car was driving under L2 assistance when it struck a pedestrian, and you have to decide who is accountable:

1. **The reconstruction** — the engine replays the incident as dashcam footage (rain, an L2 takeover request, a detected pedestrian, impact). The car *saw* her — the detection box is right there — and still handed control back to a distracted driver.
2. **Three testimonies** — the engineer who certified the system, the manufacturer's counsel, and the injured party's family each give an account of the same four seconds. None agree.
3. **The black box** — an interactive evidence inspector. Three logs (perception, actuators, driver-monitoring) are *complete*; the fourth — the decision-layer reasoning, the only one that says **why** — is unreadable. A deep-learning model can't reconstruct its own choice, so fault can't be cleanly assigned.
4. **The policy call** — under a live countdown, you draft a rule for the next thousand crashes: mandate transparency, keep the state as data steward, or require interpretability to certify. Let the clock run out and the status quo wins by default.

Central themes: the interpretability / black-box problem, L2 handover liability, and the transparency-vs-managed-trust fork. Grounded in the interviews (the crash, testimonies, and survey framing are dramatized; every stat and insight quote is from the primary research).

## Chapter 5 — The Trust Gap

*When does the public's trust in a technology need to be earned versus built?*

You're a **city official** deciding whether to approve robotaxi deployment in your district. The engine runs as a live daytime feed of a robotaxi gliding through the district:

1. **The trust gap, in numbers** — a data dossier: the real exposure gap (under 1,000 robotaxis against 100,000+ human cabs) and a clearly-labelled *illustrative* district pilot survey keyed on prior experience. The honest finding is an absence — almost no one has ridden one, so no real public opinion has had the chance to form.
2. **The pitch** — the operator's slide deck. You fact-check four bold claims against what the research actually supports (safety floor vs. undefined ceiling, ridership ≠ demand, "ready" tech missing law and acceptance).
3. **The community meeting** — five resident voices: an enthusiast, a skeptic who expects perfection from a machine, a cab driver whose livelihood is at stake, someone who came around slowly, and a crossing guard who's watched pedestrians learn to walk straight out in front of the cars.
4. **The decision** — what you allow (approve district-wide, a phased geofenced rollout, or deny pending national standards) **and** how you announce it (full transparency, managed stewardship, or a quiet start).

Central themes: real-world exposure as the engine of trust, claims-vs-reality, phased/whitelist rollout, and transparency. Chapter 5 is the **finale**: its debrief reads your whole five-chapter path back to you.

### Continuity

All five chapters share one `localStorage` save (`cytc.v1`, merge-on-write): Chapter 1 records your car pick and drive, Chapter 2 your sensor-trust, Chapter 3 your safety verdict, Chapter 4 your fault findings and policy, Chapter 5 your deployment and framing calls — none clobbers the others, and Chapter 5's finale debrief reads the whole path back. Each chapter's **Continue** button first tries a host `sendPrompt(...)`, then falls back to navigating to the next file (`chapter1 → chapter2 → chapter3 → chapter4 → chapter5`), so the arc plays as one connected flow in a plain browser.

## Running it

The chapter is a single static HTML file with all CSS and JavaScript inlined — no build step, dependencies, or server required.

Open it directly in any modern browser:

```sh
open can_you_trust_your_car_chapter1.html
```

Or double-click the file in your file manager.

> **Note:** Each chapter inlines Three.js and runs from `file://` with no build or server. Audio is synthesized with the Web Audio API and stays silent until your first interaction; a mute toggle (top-right, or the **M** key) persists across reloads. See **Continuity** above for how the chapters chain together and share the `cytc.v1` save.

## Project structure

```
.
├── can_you_trust_your_car_chapter1.html   # Chapter 1 — The Night Drive (3D, Three.js inlined)
├── can_you_trust_your_car_chapter2.html   # Chapter 2 — Inside the Machine
├── can_you_trust_your_car_chapter3.html   # Chapter 3 — The Long Tail
├── can_you_trust_your_car_chapter4.html   # Chapter 4 — Who's Responsible?
├── can_you_trust_your_car_chapter5.html   # Chapter 5 — The Trust Gap (finale)
├── Interviews/                            # primary-research transcripts (9 professionals)
└── README.md
```

## Status

Prototype. All five chapters are complete and play as one connected arc. Chapters 4–5 are built on the same single-file Three.js engine as 1–3 (cockpit hidden for the regulator/official roles, per the Chapter 3 precedent) and are grounded in the interview transcripts in `Interviews/`.
