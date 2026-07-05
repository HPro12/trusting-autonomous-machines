# Trusting Autonomous Machines

An interactive, public-interest educational project about autonomous driving safety and the question at its core: **when should humans trust machines — and how much?**

## Chapter 1 — Can You Trust Your Car?

*The Last Human Decision*

A self-contained, interactive web experience that puts you behind the wheel on a late-night highway drive. Through a short branching story with a typewritten narrative layer and synthesized night-drive audio, you feel — rather than read about — what human driving actually costs and where assistance systems promise help but fall short. Your choices adjust two live meters, Trust and Attention, and change which scenes and outcomes you see later.

The chapter walks through five scenes:

1. **Human driving** — A fatigued, distracted midnight drive. Your choice about a phone notification is scored against real reaction-time and braking-distance data.
2. **L2 assistance** — The car takes over lane keeping and adaptive cruise. You confront the question of who is actually responsible.
3. **The edge case** — Lane markings vanish in a construction zone and the system demands an instant takeover. How long your window lasts depends on how much attention you have left; choosing to grab the wheel opens a hold-to-take-control interaction that measures your real reaction time. Illustrates "automation-induced complacency" and the long-tail problem.
4. **Choose your car** — Compare L0, L2, and L4 vehicles. Your pick, along with the rest of your run, is saved to `localStorage` (`cytc.v1`) to carry into future chapters.
5. **Debrief** — A personalized recap: a timeline of every choice and its consequence, your final Trust and Attention meters, your takeover reaction time, and a closing verdict written from the specific path you took.

The content is based on interviews with autonomous-driving industry professionals in China and reflects the legal and technical landscape as of 2026.

### Chapter 1 (3D rebuild) — `can_you_trust_your_car_drive.html`

A real 3D WebGL rebuild of the Chapter 1 drive, using [Three.js](https://threejs.org). You sit
in a first-person cockpit modelled after a minimalist EV interior (no brand marks) and drive a
two-carriageway night highway with a median wall, lane markings, and NPC traffic in both
directions. The car holds a constant speed; you change lanes with **A/D** or the **arrow keys**
(a discrete, banked, pre-animated lane switch — you can't drift off the road). Audio is a
synthesized EV powertrain (whine rising with speed + wind bed) plus an adaptive night score. The
incoming message arrives as an **iMessage on the car's central touchscreen**. The full branching
story, takeover (now a 3D lane-dodge that measures your reaction time), and debrief are layered on
as DOM overlays, sharing the same `cytc.v1` save as the canvas version.

> **Portability note:** this file **inlines** Three.js so it stays a single, offline,
> double-clickable page. A `WEBSITE-TODO` comment marks where to swap the inlined library for a
> CDN importmap once the chapters are served as part of a website.

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

> **Note:** The "Continue to Chapter 2" button first tries a `sendPrompt(...)` function intended to be provided by a host environment; when that is absent (a standalone browser), it falls back to navigating directly to `can_you_trust_your_car_chapter2.html`. Audio is synthesized with the Web Audio API and stays silent until your first interaction; a mute toggle (top-right, or the **M** key) persists across reloads.

## Project structure

```
.
├── can_you_trust_your_car_chapter1.html   # Chapter 1 — The Last Human Decision (canvas)
├── can_you_trust_your_car_drive.html      # Chapter 1 — 3D driving-sim rebuild (Three.js, inlined)
├── can_you_trust_your_car_chapter2.html   # Chapter 2 — Inside the Machine
├── can_you_trust_your_car_chapter3.html   # Chapter 3 — The Long Tail
└── README.md
```

## Status

Prototype. Chapters 1–3 are complete; further chapters are planned.
