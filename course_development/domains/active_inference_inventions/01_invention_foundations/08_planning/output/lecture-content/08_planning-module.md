# The Invention Roadmap: Planning Under Uncertainty

## Executive Summary

Invention projects unfold over time under pervasive uncertainty. The inventor does not know which designs will work, which users will adopt, which competitors will emerge, or which regulations will apply. Yet decisions must be made, resources must be allocated, and milestones must be set. Active Inference provides a principled framework for planning under uncertainty through the concept of expected free energy — evaluating future actions based on both their pragmatic value (how much they advance toward the goal) and their epistemic value (how much they reduce uncertainty). This module develops the inventor's planning capabilities: decomposing complex projects into stages, making irreversible decisions at the right time, building contingency into plans, and adapting the roadmap as learning progresses.

## Learning Objectives

1. Explain planning in Active Inference as the selection of action sequences that minimize expected free energy across time.
2. Apply the concept of expected free energy to evaluate invention project plans, balancing information-gathering actions against goal-advancing actions.
3. Design staged development plans that defer irreversible decisions until uncertainty is sufficiently reduced.
4. Construct decision trees for invention projects, identifying branch points where evidence should guide the choice of path.
5. Develop adaptive roadmaps that incorporate learning from each stage to update plans for subsequent stages.

## Key Concepts

### 1. Planning as Expected Free Energy Minimization

In Active Inference, planning means selecting a sequence of future actions that minimizes expected free energy — the agent's best estimate of how much surprise (prediction error) it will encounter if it follows a particular plan. Expected free energy has two components that are particularly relevant for inventors:

**Pragmatic value** measures how much a plan advances the agent toward its preferred states. For an inventor, pragmatic value is progress toward a working, adopted, impactful invention. A plan with high pragmatic value is one that produces tangible results: functional prototypes, validated markets, signed partnerships.

**Epistemic value** measures how much a plan reduces the agent's uncertainty. For an inventor, epistemic value is learning — discovering whether an approach works, what users need, how a material behaves. A plan with high epistemic value resolves critical unknowns early, even if it does not immediately produce a sellable product.

The optimal plan balances both. A plan that is pure pragmatic value (rushing to market without testing) is risky — it may produce a product that fails because critical uncertainties were never resolved. A plan that is pure epistemic value (perpetual research without commercialization) never achieves impact. The Active Inference framework treats this not as a philosophical question but as a computational one: for each candidate plan, estimate the expected free energy (combining pragmatic and epistemic terms), and select the plan with the lowest total.

In practice, this means that early stages of an invention project should weight epistemic value heavily — the primary goal is learning, not selling. As uncertainty decreases through learning, the plan should shift toward pragmatic value — now the primary goal is achieving the preferred outcome. This shift is not a single moment but a gradual reweighting as the project matures.

### 2. Staged Development: Deciding When to Decide

One of the most important planning principles from Active Inference is that irreversible decisions should be deferred until uncertainty is sufficiently reduced. This is the logic behind staged development: breaking the invention project into phases, with each phase generating the information needed to make the decisions in the next phase.

A typical staged plan for an invention might look like:

**Stage 1: Problem Validation** — Is the problem real, widespread, and severe? Actions: observation, user interviews, evidence gathering. Key decision at the end: is this problem worth solving?

**Stage 2: Concept Validation** — Does the proposed mechanism address the problem? Actions: proof-of-concept prototyping, mechanism testing. Key decision: does the core mechanism work?

**Stage 3: User Validation** — Do users interact with the invention as intended? Actions: user experience prototyping, usability testing. Key decision: does the invention deliver value to real users?

**Stage 4: Feasibility Validation** — Can the invention be manufactured, distributed, and supported at scale? Actions: manufacturing prototyping, supply chain investigation. Key decision: can the invention be produced viably?

**Stage 5: Market Validation** — Will the market adopt and pay for the invention? Actions: limited launch, pricing experiments, channel testing. Key decision: should the invention be scaled?

Each stage produces specific information that reduces the uncertainty about a specific dimension of viability. The decisions at stage boundaries are go/no-go decisions — and they should be informed by the evidence gathered in the previous stage, not by enthusiasm or sunk cost.

The Active Inference rationale for staging is that it minimizes total expected free energy across the project. Making a large investment before critical uncertainties are resolved (skipping stages) dramatically increases expected free energy because the agent cannot predict whether the investment will produce the desired outcome. Making the investment after uncertainties are resolved (following stages) reduces expected free energy because the agent's predictions are better calibrated.

### 3. Decision Trees and Branch Points

Invention plans are not linear paths — they are trees with branch points where different evidence leads to different courses of action. A good plan explicitly identifies these branch points and specifies the criteria for choosing each branch.

An Active Inference decision tree for invention includes:

**Branch points**: Moments where a decision must be made based on evidence. "If user testing shows that 80% of users can complete the task in under 2 minutes, proceed to manufacturing prototyping. If less than 50% can complete it, redesign the interface. If 50-80% can complete it, conduct additional testing with a refined prototype."

**Information-gathering actions**: Steps specifically designed to provide the evidence needed for branch point decisions. "Before choosing between injection molding and 3D printing for production, produce 50 units by each method and compare quality, cost, and time."

**Contingency plans**: Alternative paths for different outcomes. "If the primary material fails environmental testing, we have identified two alternative materials with the following properties..." The inventor who has only one plan — no contingencies — is maximizing expected free energy because they have no response strategy for unexpected outcomes.

The concept of **option value** is relevant here. A plan that keeps multiple options open (even at some cost) may have lower expected free energy than a plan that commits irrevocably to one path. The inventor who develops two parallel approaches and chooses between them after testing both has higher option value than the inventor who bets everything on one approach.

This does not mean that decisions should be avoided indefinitely. At some point, the information gained from maintaining options is outweighed by the cost of not committing. The Active Inference framework provides the criterion: commit when the expected free energy of committing (accounting for the risk of being wrong) is lower than the expected free energy of continuing to explore (accounting for the cost of delay).

### 4. Adaptive Roadmaps: Planning to Replan

Traditional project plans assume that the future is predictable enough to specify in advance. Active Inference recognizes that the future is uncertain and that plans must be updated as new information arrives. An adaptive roadmap is a plan that includes explicit mechanisms for its own revision.

The key principle is that each stage of the plan generates evidence that updates the generative model, and the updated model may require revisions to subsequent stages. An inventor who discovers in Stage 2 that their core mechanism does not work as expected should not proceed to Stage 3 (user testing) — they should loop back and revise their mechanism or explore alternatives.

Adaptive roadmaps include:

**Review points**: Scheduled moments to evaluate progress, compare predictions against observations, and update the plan. "At the end of each month, review the iteration log and assess whether the current plan still reflects our best understanding."

**Pivot criteria**: Pre-specified conditions under which the plan would fundamentally change. "If we cannot achieve cost-per-unit below $X by Stage 4, we will pivot from consumer to industrial application."

**Learning integration**: Mechanisms for incorporating lessons from earlier stages into later plans. "User testing in Stage 3 revealed that the primary value proposition is portability, not precision. Stage 5 marketing should emphasize portability."

The concept of the **planning horizon** is important. Active Inference agents do not plan infinitely far ahead — they plan to the horizon where their generative model can still make useful predictions. Beyond that horizon, the uncertainty is so high that detailed planning is counterproductive. For most invention projects, the planning horizon is one to two stages ahead, with only rough outlines for later stages.

This means that a complete invention roadmap might have detailed plans for the current stage, rough plans for the next stage, and only directional intent for stages beyond that. This is not laziness — it is epistemic humility. Planning details for a stage that may never be reached, or may be reached under completely different conditions than anticipated, is wasted effort that creates false confidence.

### 5. Resource Allocation Under Uncertainty

Planning also involves allocating limited resources — time, money, materials, attention — across competing demands. Active Inference provides a framework for this allocation: invest resources where they will reduce expected free energy the most.

In the early stages of an invention project, the highest-free-energy questions are typically about fundamental viability: "Does the mechanism work?" "Do users want this?" Resources should be concentrated on answering these questions, even if other aspects (branding, packaging, business model) are also important. The other aspects contribute less to uncertainty reduction at this stage.

As fundamental viability questions are resolved, resources should shift to operational questions: "Can we manufacture this affordably?" "What is the right distribution channel?" "How do we comply with regulations?" These questions become the highest-free-energy items as the project matures.

A common planning error is premature optimization — investing heavily in aspects that will only matter if fundamental viability is established. An inventor who spends six months designing packaging before confirming that the product works is misallocating resources. The expected free energy of "does the product work?" is far higher than the expected free energy of "does the packaging look good?"

The countermeasure is to rank all uncertainties by their impact on the project's viability and allocate resources in priority order. This ranking should be updated at each review point as some uncertainties are resolved and others emerge.

## Applications

### Case Study 1: SpaceX's Staged Rocket Development

SpaceX's development of reusable rockets demonstrates staged planning with adaptive roadmaps at an extraordinary scale. Elon Musk's original plan was straightforward: build a cheap rocket, launch payloads to orbit, use the revenue to fund Mars colonization. But the actual development followed a deeply staged, adaptive process.

Stage 1 was the Falcon 1 — a small, simple rocket designed to demonstrate that a startup could reach orbit. This was primarily epistemic: could SpaceX build and launch a rocket at all? The first three Falcon 1 launches failed, each generating specific prediction errors (turbopump failure, fuel slosh, stage separation timing). Each failure updated the generative model, and the fourth launch succeeded.

Stage 2 was the Falcon 9 — a much larger rocket designed for commercial payloads. This shifted toward pragmatic value (generating revenue) while still pursuing epistemic goals (testing landing legs for reusability). The decision to attempt rocket landings added epistemic value to every commercial launch — even if the landing failed, SpaceX learned something about its reusability model.

Stage 3 was reusable operations — proving that reflown boosters could be reliable and economically beneficial. This required extensive parameter learning about refurbishment costs, re-flight reliability, and turnaround time.

The adaptive element is evident throughout. SpaceX's original plan did not include the Falcon Heavy (added when a market for heavy-lift emerged) or Starship (a structural redesign when the original Mars architecture proved inadequate). Each plan revision was driven by prediction errors from previous stages updating the generative model.

### Case Study 2: The Invention of the Microwave Oven

Percy Spencer's invention of the microwave oven illustrates how an adaptive roadmap can navigate from an accidental discovery to a consumer product through multiple stages with radically different uncertainty profiles.

Spencer's initial observation — a chocolate bar in his pocket melting near a magnetron — was an unplanned prediction error that suggested a new causal relationship: microwave radiation could heat food. Stage 1 was a simple experiment: directing a magnetron at popcorn kernels (which popped) and an egg (which exploded). The epistemic value was high: does microwave heating work on food?

Stage 2 shifted to feasibility: Raytheon built a prototype microwave oven called the Radarange. The first version was 6 feet tall, weighed 750 pounds, and cost $5,000 (in 1947 dollars). The prediction errors from this stage were clear: while the mechanism worked, the form factor and cost were completely wrong for consumer adoption. The plan had to adapt — the consumer market would need to wait for miniaturization.

Stage 3 involved decades of parameter learning: shrinking the magnetron, reducing power consumption, finding food-safe enclosure materials, and lowering cost through manufacturing innovation. Each of these was a parameter optimization within the established structural model (magnetron heats food in an enclosed cavity).

Stage 4 reached the consumer market in the late 1960s, but adoption was slow because of a communication problem (Module 7) — consumers did not understand what a microwave oven was for and feared radiation. The plan adapted again: marketing shifted from "cook meals" to "reheat leftovers and make snacks," reducing the prediction error gap for consumers whose model of cooking was firmly centered on conventional ovens.

The microwave oven roadmap spanned 20 years from discovery to consumer adoption, with multiple plan revisions driven by prediction errors at each stage. No linear, fixed plan could have navigated this journey.

## Cross-References

- **Module 5 (Action)**: Planning selects which actions to take and in what order
- **Module 6 (Learning)**: Planning must incorporate learning from past stages into future plans
- **Module 2 (Agents)**: The inventor's goals (preferred states) drive planning priorities
- **Module 1 (Systems)**: System boundaries determine the scope of what must be planned for

## Summary Table

| Concept | Definition | Invention Example |
|---------|-----------|-------------------|
| Expected Free Energy | The predicted surprise from a future action, balancing pragmatic and epistemic value | Choosing to test user response before investing in manufacturing |
| Pragmatic Value | How much a plan advances toward preferred states (goals) | A working prototype that can be demonstrated to investors |
| Epistemic Value | How much a plan reduces uncertainty about the world | A user test that reveals whether people need the product |
| Staged Development | Breaking projects into phases where each phase generates information for the next | Problem validation, concept validation, user validation, feasibility, market launch |
| Decision Tree | A plan with explicit branch points where evidence determines the path | "If testing shows X, proceed; if Y, redesign; if Z, pivot" |
| Adaptive Roadmap | A plan with built-in mechanisms for revision based on new evidence | SpaceX adding Starship after Falcon 9 results updated their Mars architecture model |
| Planning Horizon | The temporal distance at which the generative model can still make useful predictions | Detailed plans for the current stage, rough plans for the next, directional intent beyond |
| Option Value | The benefit of keeping multiple paths open before committing | Developing two approaches in parallel before choosing one |

## References

1. Friston, K. J., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). Active Inference: A process theory. *Neural Computation*, 29(1), 1-49.
2. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
3. McGrath, R. G., & MacMillan, I. C. (1995). Discovery-driven planning. *Harvard Business Review*, 73(4), 44-54.
4. Ries, E. (2011). *The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses*. Crown Business.
5. Vance, A. (2015). *Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future*. Ecco.
