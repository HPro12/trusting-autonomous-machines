# How Should China Build Public Trust in Autonomous Driving?

### A policy white paper on transparency, evidence, and governance

*Version 1 — formal edition. Part of the* Trust the Machine *research initiative.*

*Draft for review. Figures are described in-line as* **[FIGURE]** *blocks and will be produced as final artwork before publication.*

---

## A note on sources and method

This report stands on two bodies of evidence. The first is a set of nine confidential interviews I conducted in 2025 and 2026 with professionals across China's autonomous-driving ecosystem — robotaxi operations and business leads, deployment and data specialists, perception and planning engineers, a technology and product manager, a global test-operations lead, and a commercialization strategist who has worked across several major mobility and mapping firms. I cite each of them by role rather than by name, because candor was the price of usefulness and anonymity was the price of candor. The second body of evidence is desk research on the regulatory and technical landscape as of mid-2026, organized with a knowledge graph built across the interviews and their supporting material.

This document is one of three parts of the *Trust the Machine* initiative. The other two are the interview corpus itself and an interactive public-education experience of the same name. This is the policy part, and its ambition is narrow but deliberate: not to describe the rules China has, but to argue for the rules, evidence, and communication China needs.

---

## 0. Executive Summary

Autonomous driving in China has crossed a threshold, and the crossing has changed the problem. The professionals I interviewed are nearly unanimous that the core technology is now, in one product manager's words, "commercially usable." Robotaxis in Guangzhou and Shenzhen already handle roughly 80 percent of what a human ride-hailing driver handles, and the curve is steep. Yet deployment stays cautious, public understanding stays thin, and adoption trails what the engineering alone would permit. The binding constraint has moved. It is no longer capability. It is trust.

The argument of this report is that trust is not manufactured by safety, and it is not manufactured by claims. It is built by a chain: transparency creates trust, evidence sustains it, and governance protects it. Technology creates capability, policy creates accountability, and education creates trust — and none of the three substitutes for the others. Autonomous driving scales responsibly only when all three rise together.

The report also reframes the question everyone asks. "Is autonomous driving safe?" is the wrong question, because safety is not a property a car either has or lacks. The right question is institutional: what evidence, disclosure, and understanding let a society decide whether autonomous driving is *safe enough*? That distinction runs through everything that follows.

The report's central contribution is the **TRUST Framework for Autonomous Driving Governance**, built on five reinforcing pillars — **T**ransparency, **R**esponsibility, **U**nderstanding, **S**afety Validation, and **T**rustworthy Governance. From the framework flow five recommendations, one for each pillar, each specified by who acts, what benefits follow, and what it costs: a standardized disclosure regime anchored by a two-tier autonomy label; clear liability by level, made enforceable by event-data reconstruction; a national public-understanding program built on a shared vocabulary, of which *Trust the Machine* is one model; independent validation before and after deployment; and adaptive regulation on a stable safety floor.

China does not begin this work from behind. It begins from a decisive deploy-first posture, a disciplined whitelist-and-rings rollout, and unusually high public trust in its own institutions. The recommendations here are built to fit that starting point, not to import a foreign one.

---

## 1. Introduction — Reframing the Question

Is autonomous driving safe? It is the question every passenger, journalist, and official reaches for first, and it is almost useless. Safety is not a switch that a vehicle flips on or off. It is a probabilistic, conditional, contested claim about how a vast system behaves across a range of circumstances so wide that most of them are rare. Ask an honest engineer whether a car "is safe," and the honest answer is another question: safe where, safe when, and safe compared to what?

So the useful question is a different one entirely:

> **What institutions, evidence, and communication allow society to determine whether autonomous driving is *safe enough*?**

The move matters because it turns an unanswerable technical question into a chain of answerable institutional ones. "Safe enough" implies a threshold. A threshold implies someone who decides. A decision implies evidence, evidence implies disclosure, disclosure implies a public able to read it, and reading it implies someone who can be held to account. Each link in that chain is a policy lever, and the rest of this report pulls on them one by one.

Beneath the argument sits a simple equation. Technology creates capability — it sets what a system *can* do. Policy creates accountability — it sets who is *answerable* when the system acts. Education creates trust — it sets whether the public can *judge* the first two. These are not interchangeable. A capable system with no accountability collapses at its first serious crash. Accountability with no public understanding produces rules the public neither values nor believes. And enthusiasm with no real capability produces the most dangerous outcome of all, which is misplaced trust. The three must climb together, or whatever is built on one of them alone will not hold weight.

**[FIGURE — The Trust Flywheel.** *A circular diagram: Exposure → Evidence → Transparency → Trust → more Exposure. Real-world operation generates evidence; disclosed openly, that evidence builds trust; trust earns wider exposure, which generates more evidence still. Transparency is drawn as the coupling that keeps the wheel turning — remove it, and the loop stalls.]*

The scope here is China, and the landscape is that of mid-2026. Where the report draws on other countries, it treats them as sources of transferable ideas rather than as a ranking. And where it points to the companion *Trust the Machine* experience, it does so because that experience answers the same question from the citizen's side of the chain, while this report answers it from the regulator's.

---

## 2. The Current Landscape

### 2.1 How China governs autonomous driving today

China's approach fits into one phrase that recurred across nearly every interview: deploy first, regulate later (先跑先试). Rather than wait for a finished legal code before allowing operation, regulators permit bounded real-world deployment and let the rules converge on what the evidence reveals. One deployment and data specialist was careful to frame this caution as chosen, not timid, shaped by four pressures at once — law, technology, the cost of industrialization, and public awareness.

The posture runs on three mechanisms, and all three surfaced again and again in the interviews.

The first is a **whitelist**. Nothing is permitted by default; a company must prove a specific capability before its permissions widen. "Nothing is allowed by default," as one business and operations lead put it. "You must prove capability before scope opens." This is the mirror image of the more permissive, default-allow posture common in parts of the United States, and the interviewees were emphatic that the whitelist's direction of travel is toward *more* openness, not less.

The second is **ring-based rollout**. Operators earn scope geographically — they accumulate safe mileage and operating time in outer, lower-density zones, then apply to move inward toward the dense city core. The metaphor several reached for was a video game: clear the outer ring before the inner ring unlocks.

**[FIGURE — The Whitelist Ring Map.** *Concentric governance rings from the outside in: closed test road → open road with safety driver → open-road driverless → core-city districts. An arrow shows operators earning their way inward on accumulated safe mileage. This figure is documentary, not aspirational — it depicts the access-and-pilot model already in force.]*

The third is a **staged ODD progression** within each ring: closed-road testing, then open road with a safety driver, then open road without one, each stage gated by its own technical and safety bar. Incidents are graded by severity — P0 for the most serious, then P1 and P2 — remote operators watch fleets in real time, and every incident triggers a formal review in which vehicle data is uploaded, analyzed centrally, and replayed in simulation.

The system's sensitivity to shock is real, and worth naming early. A global test-operations lead identified changing government policy as the single largest operational challenge he faces, and pointed to how one high-profile episode — the Wuhan robotaxi incident — set off a wave of regulatory tightening that disrupted operations, costs, and business models across the country. Governance here is adaptive. But its adaptations can arrive all at once.

### 2.2 The state of the technology

On capability, the interviews were consistent and unsentimental. A technology and product manager said flatly that the technology "has already reached a commercially usable stage," and that the larger barriers now are regulation, user acceptance, and social trust. A test-operations lead put a figure on it: today's robotaxis handle about 80 percent of what a human ride-hailing driver handles, and the early complaints — too slow, too cautious — have largely given way to driving that feels much more human.

Two distinctions from the interviews carry real policy weight. The first is the gap between assistance and autonomy. Consumer L2 driver-assistance and true L4 robotaxi autonomy are different products with different purposes, and one deployment specialist refused to blur them: L2 "only needs 70 to 80 points; its goal is just to sell cars, not to solve the A-to-B problem." Treat the two as neighboring points on one smooth line — in marketing, or in regulation — and you manufacture exactly the confusion this report exists to fight.

The second distinction is between two technical routes. The industry is split between a sensor-and-map-heavy path (redundant LiDAR, radar, and cameras, with HD maps and cloud coordination) and a data-driven, vehicle-intelligence path (minimal sensors, maximum learned intelligence). A commercialization strategist gave the report its most memorable image, one I return to in Section 7: the first route is "very strong eyes, a five-year-old's brain," and the second is "limited senses, an adult expert driver's brain." Both, he stressed, still carry safety and risk.

### 2.3 Where trust currently comes from

China's model of trust is, for now, managed and state-mediated. There is no mandatory public disclosure of safety-incident data. Instead, the government acts as a trusted intermediary that manages the flow of information and the pace of rollout according to its own reading of public readiness. A commercialization strategist described the logic without flinching, and reached for a precedent: the transition to new-energy vehicles went smoothly even though early battery-fire incidents were never fully publicized, because trust in the institutions managing that transition was high.

The model has genuine strengths, and Section 4 gives them their due. It also has one structural weakness that the rest of this report circles. Trust that rests on confidence in an intermediary, rather than on evidence the public can see for itself, is efficient in calm weather and brittle in a storm. Wuhan was the storm warning. The task ahead is not to tear down the managed model — it is to give it an evidentiary spine.

---

## 3. Key Challenges — The Trust Deficit

Why, if the technology is already "commercially usable," does trust lag so far behind? Because the trust deficit is not one problem but five, and they are braided together. Weak evidence makes disclosure hollow. Opacity makes accountability impossible. Confusion about capability makes every other problem worse. Each of the five below maps to one pillar of the framework in Section 5, and each is presented alongside the others precisely because none of them can be solved alone.

**[FIGURE — The Trust Gap.** *A chart setting measured autonomous-vehicle safety performance against the near-perfect standard the public demands of a machine. Because China publishes no official disengagement or incident dataset, the chart is plotted on published international figures — operator safety data, and RAND's analysis of the mileage needed to demonstrate safety statistically — with an explicit note that comparable Chinese figures are not public. The distance between the two bars is the trust gap. That the Chinese data is missing is itself part of the argument.]*

### 3.1 The Evidence Problem (→ Safety Validation)

Proving an autonomous system safe is a statistical ordeal. RAND's much-cited analysis suggests that demonstrating a meaningful improvement over human drivers, with real statistical confidence, could take hundreds of millions of miles — an amount no company can accumulate on public roads before deployment. This is the long tail: the events that matter most for safety are precisely the ones that happen least often.

The engineers I spoke with live inside this problem rather than around it. Systems are built to cover the common 90 to 99 percent of situations well, then extended to edge cases as those cases appear. Rare scenarios are filled in with synthetic and simulated data, and near-miss events are flagged automatically and fed back into training. One deployment specialist set a sober ceiling on the whole enterprise: of one hundred genuinely hard cases, a system might solve ninety-eight and still fail the last two — and a human would fail those two as well. The evidence problem, in other words, is permanent, not transitional. Policy cannot dissolve it. Policy can only insist that the residual risk be measured, disclosed, and watched, rather than quietly assumed away.

### 3.2 The Transparency Problem (→ Transparency)

Two gaps compound the first. One is disclosure — incident data, as noted, is not systematically public. The other is deeper and more technical. An algorithm developer named model interpretability as the single biggest technical bottleneck in the field. Traditional rule-based, modular systems are mathematically traceable; modern deep-learning models are not. When an accident happens, it can be extraordinarily hard to reconstruct why the system did what it did — which strikes directly at any attempt to assign liability.

A quieter opacity is the undefined ceiling. A deployment specialist noted that the industry advertises improvement from one model generation to the next, "but nobody ever tells you what 100 looks like." Without a defined target for "safe enough," neither the public nor the regulator can judge how far down the road the technology has actually traveled.

### 3.3 The Communication Problem (→ Understanding)

The public learns about capability mostly through marketing, and marketing is built to blur the very distinctions that matter. The assistance-versus-autonomy conflation from Section 2.2 is the clearest case. A product and operations manager pointed to a sharper hazard still: because firms today each define edge-case behavior differently, and describe their systems in non-standardized language, there is no shared vocabulary in which a consumer — or a regulator — can compare two products side by side. He judged this a latent public-safety problem in its own right.

Two human patterns make the communication problem worse. A commercialization strategist observed that a driver's real comfort zone is far narrower than the marketed envelope — people use "four or five centimeters of a claimed ten" — so one unsettling moment sends them back to manual control and erases the convenience entirely. And an operations lead named the asymmetry at the center of the whole trust gap: people accept human error as fate, but cannot accept a machine erring, and so demand something close to perfection before they will extend any trust at all.

### 3.4 The Accountability Problem (→ Responsibility)

When something goes wrong, who is responsible? The answer swings sharply across L2, L3, and L4 — and the public rarely knows which product it is sitting in. In an L2 system, the human remains the legal driver even while the system steers, so the handover of control, and of blame, is instantaneous and badly understood. In an L4 robotaxi, responsibility rests with the operator and the technology provider, but the black-box problem of Section 3.2 makes fault hard to establish even when the will to assign it is there. Accountability that cannot be traced is accountability in name only.

### 3.5 The Human-Factors Problem (cross-cutting)

Some challenges sit across all the pillars at once, because they are about people rather than machines.

- **Automation complacency.** A system good enough to trust is a system easy to stop watching — which is dangerous at exactly the levels, L2 and L3, that still need a human ready to act.
- **The exposure gap.** This is the single most important adoption fact in the interviews. Robotaxi supply is tiny against conventional transport — a commercialization strategist estimated under a thousand robotaxis against more than a hundred thousand taxis in one major city. Most people have never ridden in one, so social awareness has not formed, and ridership numbers do not yet reflect genuine preference. Trust cannot grow out of an experience almost no one has had.
- **Friction that is not about safety.** A business lead reported that the most common complaints are not about crashes at all, but about fixed pickup and drop-off points, since riders are used to human drivers who improvise. Trust is shaped by the mundane as much as by the catastrophic.
- **Public fears.** Two anxieties recurred: losing the option of human intervention in an emergency, and losing driving jobs.
- **Induced behavior.** A perception engineer described a striking second-order effect — pedestrians at some uncontrolled crossings, having learned that autonomous vehicles yield reliably, now step out on purpose. The technology reshapes the very environment it then has to survive in.

---

## 4. Comparative Analysis

Other countries appear here as case studies, not as a scoreboard. Each has placed a characteristic bet, and each bet carries both a lesson and a limit for China.

The **United States** bets on disclosure through intermediaries. Federal authorities require incident reporting for vehicles with automated systems, several states publish operator disengagement data, and a dense layer of media, insurers, and advocacy groups translates that data for the public. A commercialization strategist drew the contrast with China directly: in the US, "safety reports are public, and media, NGOs, and insurers serve as intermediaries." The strength is resilience — trust rests on visible evidence rather than on a single institution. The limit, for China, is institutional: the interpreter ecosystem that makes American disclosure meaningful does not exist in the same form, so importing the requirement without the interpreters would yield raw numbers that few could actually use.

**Germany** bets on law first, at L3. It legislated a framework for higher automation relatively early and aligned with international type-approval standards for L3 highway and traffic-jam systems. The strength is clarity — responsibility at L3 is defined before mass deployment, not after a crash forces the question. The limit is pace: a type-approval culture built for a mature, standards-driven auto industry moves deliberately, which sits in tension with China's deploy-first speed.

**Singapore** bets on standards and structured sandboxes, pairing national technical standards for autonomous vehicles with well-defined testbeds and phased expansion. The strength is that standardization and experimentation were designed together, not bolted onto each other later. The limit is scale — a compact city-state does not generalize to a country of China's size, though the *mechanism* of a formal sandbox travels well.

**Japan** bets on caution, advancing L3 and limited L4 through careful legal amendment and close industry-government coordination, with public confidence as the explicit priority. The strength is deliberate trust-building; the limit, again, is speed.

So what could China realistically adopt? The transferable ideas are the mechanisms, pried loose from the institutions that produced them — standardized ODD and safety-reporting formats from the US and Singapore, clear ex-ante liability rules by level from Germany, and formal regulatory sandboxes from Singapore. What does not transfer is the assumption of a Western-style intermediary layer. Because China's trust runs through the state rather than through NGOs and insurers, disclosure should be designed to flow first to regulators and qualified third parties, with a deliberate, staged path toward public reporting — not a sudden switch to full openness. That adaptation is exactly what the framework in Section 5 is built to support.

---

## 5. The TRUST Framework for Autonomous Driving Governance

Here is the core claim of this report, stated plainly: the five challenges of Section 3 cannot be solved separately, because every partial fix is undone by the gaps around it. Disclosure without validated data discloses noise. Validation without disclosure convinces no one. Accountability without interpretability cannot be enforced. And none of it builds trust if the public cannot understand what is disclosed. The framework therefore couples five pillars that are designed to hold each other up.

**[FIGURE — The TRUST Framework.** *The five pillars as a pentagon or wheel, with connecting edges drawn to show the reinforcement relationships described below.]*

**T — Transparency.** Companies should communicate capabilities, operational design domains, known limitations, disengagement performance, and safety data through standardized reporting, not through marketing language. Transparency is the pillar that converts private engineering knowledge into public and regulatory knowledge.

**R — Responsibility.** Legal responsibility across L2, L3, and L4 should be defined in advance, and expressed in terms a consumer can actually understand. Responsibility is what makes transparency bite — disclosure matters because someone can be held to it.

**U — Understanding.** Governments, schools, companies, and media should raise public technological literacy, using experiential tools rather than technical lectures. The *Trust the Machine* experience, the companion to this report, is one such tool: it lets a person feel the reaction-time limits of a human takeover, see what the machine sees, and face the statistics of the long tail head-on. Understanding is what gives transparency an audience.

**S — Safety Validation.** The field should adopt standardized testing methodologies, simulation benchmarks, third-party audits, and post-deployment monitoring, treating safety as a property under continuous evaluation rather than a gate passed once. Validation is what produces the evidence that transparency discloses.

**T — Trustworthy Governance.** Regulation should be adaptive — evolving with the technology while holding a stable safety floor, and balancing innovation against accountability and public confidence. Governance is the pillar that keeps the other four current as the technology moves beneath them.

The pillars are a cycle, not a list. Validation generates evidence; transparency discloses it; understanding makes the disclosure legible; responsibility makes it binding; governance keeps the loop adaptive and shields it from both capture and panic. This is the institutional form of the Trust Flywheel from Section 1 — exposure produces evidence, evidence disclosed produces trust, and trust earns wider exposure. Thus the framework's real claim is not that any single reform will work, but that this loop is what lets a society decide whether autonomous driving is safe enough, and keep deciding as the answer changes underneath it.

---

## 6. Recommendations

Five recommendations turn the framework into action — one for each pillar, each absorbing the measures that serve it. Each is specified by five questions: why it matters, who implements it, what benefits are expected, what the tradeoffs are, and what will make it hard. The first carries the report's signature proposal, the two-tier autonomy label.

**R1 — Transparency: Standardized disclosure, anchored by a two-tier autonomy label.**
- *Why it matters.* Three gaps close at once. Incompatible marketing vocabularies leave consumers and regulators unable to compare systems (Section 3.3); the operational design domain — where and when a system actually works — is the single most decision-relevant fact about it; and disengagement and incident data are the raw material of any trust built on evidence rather than assurance. One disclosure regime addresses all three.
- *Who implements.* The industry regulator (MIIT is the natural lead) sets a mandatory label format and a machine-readable ODD schema; manufacturers and operators populate them; a certification body verifies; and a qualified third party aggregates the disengagement and incident reporting.
- *Expected benefits.* Consumers and regulators can compare systems at a glance, a national evidence base supports enforcement and defensible decisions to widen or narrow scope, and the label becomes the public face of both the Transparency and Responsibility pillars.
- *Tradeoffs.* A fully public label showing raw disengagement rates cuts against the managed-disclosure model. The two-tier design resolves the tension: a **regulator tier** carries the full data — level, ODD, disengagement rate, incident history, limitations, handover behavior — while a **consumer tier** carries a legible subset: level, ODD, key limitations, and what the driver must be ready to do. Firms may also treat ODD detail as competitively sensitive, and disclosure timing must be managed to avoid panic.
- *Implementation challenges.* Defining metrics precise enough to resist gaming, keeping the label current as systems update over the air, building an ODD schema expressive enough to capture real conditions yet still readable, agreeing on what counts as a disengagement, and sequencing the path from regulator-only toward graduated public reporting.

**[FIGURE — The Autonomy Label.** *A standardized card in two tiers. The consumer tier states level (L2/L3/L4), ODD in plain language ("daytime, mapped urban roads, up to 60 km/h, clear or light rain"), key limitations, and what the driver must be ready to do. The regulator tier adds disengagement rate, incident history, and detailed operating bounds. It is meant to be read, like an energy or nutrition label, in seconds.]*

**R2 — Responsibility: Clear liability by level, made enforceable by reconstructable evidence.**
- *Why it matters.* Section 3.4 showed that accountability is most ambiguous exactly where products differ most, across L2, L3, and L4 — and liability cannot be enforced if the decision cannot be reconstructed, the black-box problem an algorithm developer called the field's biggest bottleneck.
- *Who implements.* Legislators and courts, informed by the regulator and building on local pilots such as Shenzhen's, define liability by level; the regulator mandates a standardized event data recorder and retention rules that industry builds to.
- *Expected benefits.* Predictability for victims, operators, and insurers — the precondition for an insurance market that can price the risk — together with investigable incidents and a feedback loop straight into validation.
- *Tradeoffs.* Rules set too early may not fit technologies that do not yet exist, and event recording brings data-volume, privacy, and cost burdens.
- *Implementation challenges.* Harmonizing across jurisdictions, keeping the rules legible to consumers and not only to lawyers, standardizing what an opaque model must log, and holding sensitive data securely.

**R3 — Understanding: A national public-understanding program built on a shared vocabulary.**
- *Why it matters.* Transparency is worthless without an audience able to read it, and the exposure gap means most people have no direct experience to reason from. A shared language across manufacturers is the precondition for every disclosure, answering the product manager's warning that divergent, non-standardized edge-case definitions are a latent public-safety problem in their own right.
- *Who implements.* Government and educators, with industry support, run the program, drawing on experiential tools including *Trust the Machine*; the regulator and a standards body, with industry participation, fix the terminology.
- *Expected benefits.* A public that calibrates trust rather than swinging between hype and panic, a steadier response when incidents occur, and coherent labels, marketing rules, and public understanding all built on one vocabulary.
- *Tradeoffs.* If it is industry-led, the program risks being read as promotion rather than education, and firms lose branded terminology they have invested in.
- *Implementation challenges.* Reaching non-specialists and measuring whether understanding genuinely improves, enforcing the shared terminology against marketing drift, and aligning it with international vocabulary.

**R4 — Safety Validation: Independent validation, before and after deployment.**
- *Why it matters.* Self-attestation alone cannot carry public trust once the stakes climb, and safety is a continuous property — systems change with every update, and the long tail reveals itself only in operation. Validation also fits China's context precisely: interviewees noted that third-party data services already exist, from battery monitoring run by a leading institute to insurance-linked services that triangulate operators, insurers, and users.
- *Who implements.* Accredited certification bodies and qualified third parties under regulator oversight, with operators supplying data and running the real-time P0/P1/P2 monitoring they already operate, reporting into a regulator-supervised system.
- *Expected benefits.* Credible, comparable assurance and a gate that scales with capability; independent verification without full public disclosure, a middle path suited to the managed model; and early warning that gives a factual basis for adaptive scope decisions, lowering the odds of another abrupt, incident-driven clampdown.
- *Tradeoffs.* Cost, potential slowdown, and the risk of a checkbox culture; third parties see the analysis, not the full data superset the operators own; and continuous monitoring raises surveillance concerns.
- *Implementation challenges.* Building certifier competence for AI systems and avoiding conflicts of interest, governing the third parties themselves and setting data-access terms, and turning firm-internal monitoring into comparable national data.

**R5 — Trustworthy Governance: Adaptive regulation on a stable safety floor, learned through sandboxes.**
- *Why it matters.* Formal regulatory sandboxes give the deploy-first instinct a controlled, evidence-generating structure and lower the chance that one incident forces a blunt, system-wide reaction. And governance here is an inter-departmental balance — tech and economic bodies pushing, safety and labor bodies holding back, the state guarding the floor — which adaptive rules institutionalize instead of leaving to crisis.
- *Who implements.* National and municipal regulators, extending the existing ring model into formal sandboxes and coordinating adaptive rules across departments.
- *Expected benefits.* Faster learning at bounded risk and a smoother path from pilot to scale, plus rules that evolve with the technology while the safety floor stays fixed — and far less whiplash after incidents.
- *Tradeoffs.* Fragmentation if every city runs an incompatible sandbox, and adaptivity that can slide into unpredictability if it is not disciplined.
- *Implementation challenges.* National coordination and clear, evidence-based criteria for graduating from sandbox to open operation, defining the immovable floor precisely, and resisting both capture and overreaction.

Two notes across the set. Explainability requirements should be applied where they are proportionate, not everywhere, given the interpretability limits the engineers described — the practical near-term lever is the reconstruction standards within R2, not a blanket demand that models explain themselves. And the recommendations are sequenced: the disclosure and shared-vocabulary reforms (R1 and R3) come first, because a common language and comparable data are what every later reform stands on.

---

## 7. Future Outlook

The strategist interviews suggest the road ahead is less straight than public debate assumes.

The first surprise is that L4 to L5 is not a smooth upgrade. L5 — operation in all conditions, with no ODD restriction — may not be reachable by scaling today's four-wheeled robotaxi at all. Off-road, flooded, or unstructured environments may demand entirely different physical platforms. No one holds full-scenario data, and, as more than one interviewee noted, the industry has no agreed definition of "100 percent ready." Policy should therefore treat L4-within-defined-ODDs as the operative regime for the foreseeable future, and resist framing L5 as an imminent inevitability.

The second is that geography and jurisdiction will shape deployment more than raw capability will. Commercial viability concentrates in dense, high-frequency urban demand; rural service is navigable but not viable. Inter-city service runs into competition from high-speed rail, the complexity of cross-jurisdiction approval, and jurisdiction-bound fleet economics. The Greater Bay Area is a favorable exception, not a template.

The third is that the floor-versus-ceiling tension will not resolve soon. The two technical routes of Section 2.2 embody a genuine dilemma. The sensor-heavy route offers a high safety floor and a lower ceiling — strong eyes, a young child's brain. The data-driven route offers a lower floor and a higher ceiling — few senses, an expert's brain. Governments prize the floor, which is why sensor-heavy operators have generally been let into more complex environments first. But the public wants maximum safety and maximum capability at the same time, and that wish does not resolve into a single answer. Governance should hold the floor while leaving room for the ceiling to rise, which is exactly what adaptive regulation with a fixed floor (R5) is designed to do.

The last is the most hopeful. China does not have to choose abruptly between its managed-trust model and a Western disclosure model. The framework's staged path — regulator-tier data first, qualified third parties next, graduated public reporting over time — lets trust migrate from resting on an institution to resting on visible evidence, at a pace the institution can control. That migration is what justified trust at scale would actually look like.

---

## 8. Conclusion

Autonomous driving in China is no longer held back mainly by what the technology can do. It is held back by whether society can tell how safe it is, hold someone answerable when it fails, and understand it well enough to trust it for the right reasons. Those are not engineering problems. They are problems of transparency, evidence, and governance.

The argument compresses to a few lines. Safety alone does not create trust, and claims alone do not create trust. Transparency creates trust, evidence sustains it, and governance protects it. Technology creates capability, policy creates accountability, education creates trust — and the three must climb together or not at all. The TRUST Framework and its five recommendations are an attempt to make that shared climb concrete, and to make it fit inside China's own institutions rather than someone else's.

The right question was never whether autonomous driving is safe. It is whether we are building the evidence, the accountability, and the shared understanding that let a society decide — and keep deciding — whether it is safe enough. Getting the vehicles right is a matter of engineering. Getting that decision right is the work of policy. Ultimately, this report is a proposal that China take the second task as seriously as it is already taking the first.

---

## Appendices

**Appendix A — Methodology.** Nine semi-structured interviews conducted in 2025 and 2026 with professionals across operations, deployment and data, perception and planning engineering, product management, test operations, and commercialization strategy. Cited by role to protect candor. Supported by desk research on the mid-2026 regulatory and technical landscape, organized with a knowledge graph across the interview corpus and its supporting material.

**Appendix B — The TRUST Framework at a glance.** A one-page reference: the five pillars, the reinforcement cycle, and the mapping from each of the five challenges in Section 3 to its pillar and its recommendations.

**Appendix C — Signature visuals.** Full-size versions of the Trust Flywheel, the Whitelist Ring Map, the Trust Gap chart, the TRUST Framework diagram, and the two-tier Autonomy Label.

**Appendix D — Glossary.** ODD (Operational Design Domain); SAE levels L2–L5; disengagement; corner case and long tail; 先跑先试 (deploy-first, regulate-later); whitelist and ring-based rollout; P0/P1/P2 incident grading; safety floor versus ceiling.
