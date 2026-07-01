# Trusting Autonomous Machines

An interactive, public-interest educational project about autonomous driving safety and the question at its core: **when should humans trust machines — and how much?**

## Chapter 1 — Can You Trust Your Car?

*The Last Human Decision*

A self-contained, interactive web experience that puts you behind the wheel on a late-night highway drive. Through a short branching story, you feel — rather than read about — what human driving actually costs and where assistance systems promise help but fall short.

The chapter walks through five scenes:

1. **Human driving** — A fatigued, distracted midnight drive. Your choice about a phone notification is scored against real reaction-time and braking-distance data.
2. **L2 assistance** — The car takes over lane keeping and adaptive cruise. You confront the question of who is actually responsible.
3. **The edge case** — Lane markings vanish in a construction zone and the system demands an instant takeover, illustrating "automation-induced complacency" and the long-tail problem.
4. **Choose your car** — Compare L0, L2, and L4 vehicles. Your pick is meant to carry into future chapters.
5. **Summary** — A recap of the chapter's themes: human limitations, "L2 ≠ autonomous," edge cases, and trust calibration.

The content is based on interviews with autonomous-driving industry professionals in China and reflects the legal and technical landscape as of 2026.

## Chapter 2 — Inside the Machine

*How does a machine perceive the world — and what does it miss?*

You keep driving, but now you can see what the car sees. Augmented-reality overlays paint the road with the machine's own perception:

1. **Sensor operation** — camera bounding boxes and confidence scores, a LiDAR point cloud, and radar brackets, all locked to the moving world.
2. **Sensor fusion** — a pedestrian at night. You drag Camera/LiDAR/Radar weight sliders and watch a live certainty score respond, then hit **AUTO** to see how the car itself weighs each sensor by how reliable it is right now.
3. **Sensor failure** — oncoming glare blinds the camera; you watch its confidence collapse and the system re-weight onto LiDAR and radar to stay safe.
4. **Fusion decision** — with the camera blind and an ambiguous object in the lane, you decide which sensor to trust — with real consequences.

Central themes: sensor fusion, redundancy, adaptive weighting, and graceful degradation.

## Chapter 3 — The Long Tail

*How do you prove a machine is safe enough?*

You step out of the car and into the role of a safety evaluator at an AV company, working a control-room review station (the road engine is reused as reviewed dashcam footage):

1. **Log review** — scan through 10,000 km of mostly-uneventful fleet logs on a timeline; one near-miss flags.
2. **Classification** — decide what the near-miss is: a software bug, a rare edge case, or an acceptable statistical risk — each defensible, none clearly right.
3. **Statistical impossibility** — an interactive look at the math: you'd need ~275 million miles (RAND) just to show, with confidence, that the car is as safe as a human — and billions for real proof, which no fleet has driven incident-free. The long tail of rare events can never be fully tested.
4. **Recommendation** — under that irreducible uncertainty, you still have to advise: deploy, keep testing, or a limited supervised rollout.

Central themes: the long tail, the limits of statistical proof, simulation, and deciding under uncertainty.

## Running it

The chapter is a single static HTML file with all CSS and JavaScript inlined — no build step, dependencies, or server required.

Open it directly in any modern browser:

```sh
open can_you_trust_your_car_chapter1.html
```

Or double-click the file in your file manager.

> **Note:** The "Continue to Chapter 2" button calls a `sendPrompt(...)` function intended to be provided by a host environment. In a standalone browser this button is inert; the rest of the experience works fully offline.

## Project structure

```
.
├── can_you_trust_your_car_chapter1.html   # Chapter 1 — The Last Human Decision
├── can_you_trust_your_car_chapter2.html   # Chapter 2 — Inside the Machine
├── can_you_trust_your_car_chapter3.html   # Chapter 3 — The Long Tail
└── README.md
```

## Status

Prototype. Chapters 1–3 are complete; further chapters are planned.
