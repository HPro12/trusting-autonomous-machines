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
├── can_you_trust_your_car_chapter1.html   # The complete Chapter 1 experience
└── README.md
```

## Status

Prototype. Chapter 1 is complete; further chapters are planned.
