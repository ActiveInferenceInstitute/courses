# Module 01: The Prototype as a System — Building Generative Models You Can Touch

## Executive Summary

A prototype is not merely a rough draft of a product; it is a **physical generative model** — a tangible instantiation of the inventor's beliefs about how a system should work. This module examines prototypes through the lens of Active Inference systems theory, revealing that every design choice about what to include or exclude in a prototype is a decision about the prototype's **Markov blanket**. By understanding prototypes as simplified systems with internal states, sensory surfaces, and active capabilities, inventors can make principled decisions about fidelity levels, material choices, and testing scope. The transition from mental model to physical prototype is the transition from implicit inference to explicit, testable prediction.

## Learning Objectives

1. Characterize a prototype as a generative model made physical, identifying its internal states, sensory states, active states, and external environment.
2. Apply the concept of the Markov blanket to determine what a prototype should include and what it should deliberately exclude.
3. Distinguish between fidelity levels (low, medium, high) as different degrees of model resolution and evaluate which level minimizes expected free energy for a given testing purpose.
4. Analyze how the boundary between a prototype system and its testing environment determines what can and cannot be learned from testing.
5. Design a prototype specification for your own invention project that explicitly maps system boundaries to learning goals.

## Key Concepts

### 1. The Prototype as an Embodied Generative Model

In Active Inference, a generative model is an internal representation that an agent uses to predict sensory observations and guide action. The model encodes beliefs about the causal structure of the world — what causes what, what depends on what, and what to expect under various conditions. When an inventor builds a prototype, they are literally constructing a physical version of this generative model. The prototype embodies the inventor's hypotheses about how components interact, what materials will behave in what ways, and how users will engage with the system.

Consider James Dyson's development of the bagless vacuum cleaner. His first prototype was built from cardboard and duct tape attached to an existing vacuum. This cardboard cyclone was not the product — it was a physical generative model encoding his hypothesis that centrifugal separation could replace filter bags. The prototype generated predictions: air entering at a specific angle and velocity should separate dust particles of a certain size. When he tested it, the discrepancy between prediction and observation (the prediction error, or surprise) told him exactly which parameters of his model needed updating. Over 5,127 prototypes, Dyson was not simply "trying things" — he was systematically reducing the free energy of his generative model by making it progressively more accurate.

The crucial insight is that a prototype does not need to be a complete product to be a complete generative model for a specific hypothesis. A cardboard mock-up is a perfectly adequate generative model for testing spatial relationships. A 3D-printed shell is a perfectly adequate generative model for testing ergonomics. The prototype's purpose determines its required fidelity.

### 2. Markov Blankets and Prototype Boundaries

Every prototype has a boundary — a Markov blanket that separates its internal workings from its external testing environment. This boundary consists of **sensory surfaces** (where the prototype receives inputs from testers, power sources, or environmental conditions) and **active surfaces** (where the prototype produces outputs, effects, or responses). The internal states of the prototype — its mechanisms, circuits, algorithms, structural elements — are shielded from the external world by this blanket.

Deciding where to draw this boundary is one of the most consequential decisions in prototyping. Include too much within the blanket, and you build something expensive and slow that tests too many variables simultaneously. Include too little, and your prototype cannot generate the predictions you need to test your core hypotheses.

Consider the development of the original iPhone. Apple's earliest prototypes separated the Markov blanket into distinct subsystems: one prototype tested only the multi-touch screen (sensory surface), another tested only the antenna and radio components (communication subsystem), and a third tested the user interface software running on a desktop computer. Each prototype had a tightly defined blanket that isolated specific internal states for testing. Only in later stages were these subsystems integrated into a unified blanket.

This is the **modularity principle** in Active Inference prototyping: a complex system's Markov blanket can often be decomposed into nested sub-blankets, each of which can be prototyped and tested independently before integration.

### 3. Fidelity Levels as Model Resolution

Prototype fidelity — the degree to which a prototype resembles the final product in appearance, materials, functionality, and interaction — maps directly onto the concept of **model resolution** in Active Inference. A low-fidelity prototype is a coarse-grained generative model with few parameters and broad priors. A high-fidelity prototype is a fine-grained model with many parameters and tighter priors.

**Low fidelity** (paper sketches, cardboard models, wireframes): These prototypes encode only the most essential structural hypotheses — spatial relationships, basic user flow, overall form factor. They are cheap to produce and disposable, which makes them ideal for the early stages of invention when the inventor's uncertainty is highest. In Active Inference terms, when your priors are very broad (you are unsure about many things), you need a model that can be updated quickly and cheaply. The Wright brothers built hundreds of low-fidelity wing models for their wind tunnel, each testing a single hypothesis about lift coefficients.

**Medium fidelity** (3D prints, functional breadboards, clickable mock-ups): These encode more detailed hypotheses about material properties, component interactions, and user experience. They narrow the prior distributions on specific parameters while maintaining flexibility on others.

**High fidelity** (pre-production units, beta software, working mechanical assemblies): These approach the resolution of the final product and test near-complete system integration. They are expensive but generate the most realistic prediction errors, because the model's predictions are now close enough to reality that subtle discrepancies become visible.

The inventor's task is to choose the fidelity level that minimizes **expected free energy** — the combination of information gain (epistemic value) and practical utility (pragmatic value) — given current constraints on time, money, and knowledge.

### 4. What to Include and What to Exclude

The question of what to include in a prototype is fundamentally a question about the **generative model's scope**. In Active Inference, a generative model does not need to represent everything about the world — it needs to represent enough to make useful predictions about the variables of interest. Similarly, a prototype does not need to include every feature of the final product — it needs to include enough to test the hypotheses that currently carry the most uncertainty.

This principle yields a concrete prototyping heuristic: **include components that are causally upstream of your test variables; exclude components that are causally independent.** If you are testing whether a new latch mechanism is strong enough, you need the latch, the mounting surface, and the load — but you do not need the product's color scheme, packaging, or branding. These variables are outside the prototype's relevant Markov blanket for this test.

The pharmaceutical industry applies this principle rigorously. In early drug development, the "prototype" is a molecular compound tested in cell cultures (an extremely simplified system). The Markov blanket includes only the drug molecule and its target receptor — everything else about the human body is excluded. As the compound advances through animal testing and clinical trials, the blanket expands to include more of the biological system, but always in a controlled, deliberate manner. Each expansion of the blanket corresponds to a new set of hypotheses being brought under test.

A common failure mode is the **kitchen sink prototype** — a prototype that tries to include everything, resulting in a system so complex that when it fails, you cannot determine which component caused the failure. This is the prototyping equivalent of an overfitted generative model: it has so many parameters that it cannot generate clear prediction errors for any specific hypothesis.

### 5. The Prototype-Environment Interface

The Markov blanket of a prototype defines not only what is inside the prototype but also what constitutes its testing environment — and therefore what can be learned from testing. The **sensory surface** of the prototype determines what environmental inputs it responds to: does it respond to temperature? To user force? To electrical signals? To verbal commands? The **active surface** determines what outputs it produces: does it move? Light up? Produce sound? Display information?

Designing the prototype-environment interface is designing the experiment. If the prototype's sensory surface does not include temperature sensitivity, then testing will not reveal temperature-related failure modes, even if temperature is critical to the final product's performance. This is why prototype design and test design are inseparable — they are two aspects of the same act of inference.

The development of Gore-Tex provides an instructive example. Bob Gore discovered that rapidly stretching PTFE created a microporous membrane. But the initial "prototype" — the stretched PTFE film — had a minimal Markov blanket: it interacted with water and air, and its outputs were water transmission rate and air permeability. Only when Gore expanded the prototype's blanket to include real-world conditions (rain, wind, body heat, perspiration, mechanical stress from movement) did the full performance profile of the material become testable. Each expansion of the blanket brought new environmental variables into the prototype's sensory surface and generated new prediction errors that guided further development. The lesson from Gore-Tex is that the prototype-environment interface is not fixed — it should expand deliberately as earlier, simpler tests are passed. An inventor who tests only under ideal conditions has a prototype whose sensory surface excludes exactly the variables most likely to cause real-world failures.

The principle extends to digital prototypes as well. A software prototype's Markov blanket includes its user interface (sensory/active surface), its backend logic (internal states), and the user plus network environment (external states). A "wizard of Oz" prototype, where a human operator simulates the backend, has the same sensory surface as the real system but different internal states — allowing the team to test user interaction hypotheses without building the actual algorithm.

## Applications

### Case Study 1: The Dyson Cyclone Vacuum — 5,127 Prototypes as Iterative Model Refinement

James Dyson's development of the DC01 vacuum cleaner is one of the most documented cases of systematic prototyping in invention history. Beginning in 1979, Dyson spent fifteen years building over 5,000 prototypes, each one a physical generative model encoding specific hypotheses about cyclonic air separation.

His earliest prototypes had minimal Markov blankets: a cardboard cyclone cone attached to an existing vacuum motor. The internal states were the cone geometry (angle, diameter, length); the sensory surface was the airflow input; the active surface was the dust output. Each prototype generated a prediction (dust of size X will be captured at efficiency Y) and an observation (actual capture rate). The prediction error drove parameter updates — slight changes to cone angle, entry port size, and cyclone diameter.

As his model became more refined, the blanket expanded to include dual-cyclone architecture, motor integration, filtration stages, and eventually user ergonomics. The key insight from an Active Inference perspective is that Dyson did not attempt to build a complete vacuum from the start. He systematically expanded the generative model's scope as his uncertainty about core mechanisms decreased, always matching prototype fidelity to the current state of knowledge.

### Case Study 2: The Mars Rover Test Beds — Prototyping for Unreachable Environments

NASA's Jet Propulsion Laboratory faced a unique prototyping challenge with the Mars rovers: the prototype's testing environment (Earth) was fundamentally different from its operating environment (Mars). JPL's solution was to build **environmental simulants** — physical models of the Martian environment that could serve as the external states in the prototype's Markov blanket.

The Mars Yard at JPL replicates Martian terrain features: sand traps, rocky slopes, loose regolith. But it cannot replicate Martian gravity (38% of Earth's), atmosphere (95% CO2 at 0.6% of Earth's pressure), or temperature extremes (-80C to +20C). JPL therefore built separate test rigs for each environmental variable: a gravity offload rig to simulate reduced weight, thermal vacuum chambers for atmospheric conditions, and the Mars Yard for terrain navigation.

Each test rig defined a different Markov blanket around the rover prototype, allowing engineers to isolate specific environmental interactions. This modular approach to prototype-environment interfaces is a textbook application of the principle that prototype design and test design are two aspects of the same inference problem.

The Mars Yard approach also illustrates the concept of **environmental fidelity** — the degree to which the testing environment matches the operating environment. Perfect environmental fidelity is often impossible or prohibitively expensive. The inventor's task is to identify which environmental variables are most critical (highest expected free energy reduction) and prioritize environmental fidelity for those variables. For the Mars rovers, terrain interaction was the highest priority (driving over rocks is mechanically complex), so the Mars Yard received the most investment. Gravity simulation was second priority (0.38g affects mobility but is partially predictable through analysis). Atmospheric simulation was lower priority for mobility testing (thin atmosphere has minimal direct effect on driving). This prioritization of environmental fidelity mirrors the prioritization of prototype fidelity — allocate resolution where uncertainty and consequence are highest.

## Cross-References

- **Module 02 (The Testing Agent)**: The inventor must shift from building the prototype system to evaluating it — becoming an observer of the system rather than its creator.
- **Module 03 (Reading the Prototype's Signals)**: The prototype-environment interface determines what signals the inventor can perceive; this module explores how to interpret those signals.
- **Module 05 (Iterative Refinement)**: Each prototype iteration is an action in the Active Inference loop; systems thinking determines what the next iteration should change.
- **Module 08 (Test Planning Under Uncertainty)**: The choice of what to include in a prototype is determined by test planning; planning determines which Markov blanket will minimize expected free energy.

## Summary Table

| Concept | Definition | Prototype Application |
|---------|-----------|----------------------|
| Generative Model | Internal representation predicting observations | Prototype embodies inventor's hypotheses about how the system works |
| Markov Blanket | Statistical boundary separating internal from external states | Prototype boundary determining what is included and what is left to the test environment |
| Sensory States | States mediating environmental influence on internal states | Prototype inputs: user interactions, environmental conditions, power/data feeds |
| Active States | States mediating the system's influence on the environment | Prototype outputs: movements, displays, sounds, effects |
| Model Resolution | Granularity of the generative model | Fidelity level: low (coarse, broad priors) to high (fine, narrow priors) |
| Expected Free Energy | Combined epistemic and pragmatic value of an action | Choosing fidelity that maximizes information gain per unit cost |
| Modularity | Decomposition of a complex blanket into nested sub-blankets | Building separate prototypes for separate subsystems before integration |

## References

1. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
2. Dyson, J. (1997). *Against the Odds: An Autobiography*. Orion Publishing Group.
3. Ulrich, K. T., & Eppinger, S. D. (2016). *Product Design and Development* (6th ed.). McGraw-Hill Education.
4. Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
5. Hoover, S. P., Rinderle, J. R., & Finger, S. (1991). Models and abstractions in design. *Design Studies*, 12(4), 237-245.
