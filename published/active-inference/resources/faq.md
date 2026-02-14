# Frequently Asked Questions

> **Quick Navigation**: [Curriculum Home](../README.md) | [Notation Table](./notation_table.md) | [Glossary](./glossary.md) | [References](./references.md) | [Cross-Course Map](./cross_course_map.md) | [Learning Pathways](./learning_pathways.md)

Common questions about Active Inference and this curriculum, with pointers to the relevant modules.

---

## About Active Inference

### What is Active Inference?

Active Inference is a framework stating that organisms act to minimize *expected free energy* — a quantity that unifies perception, action, learning, and planning under a single imperative. It is a corollary of the [Free Energy Principle](./glossary.md) (FEP), which proposes that any self-organizing system at non-equilibrium steady state can be described as minimizing variational free energy.

**Where to start**: [Philosophy Module 1](../01_philosophy/01_systems/module.md) (conceptual) or [Mathematics Module 3](../03_math/03_perception/module.md) (formal).

### How does Active Inference differ from Reinforcement Learning?

| Aspect | Active Inference | Reinforcement Learning |
|--------|-----------------|----------------------|
| Objective | Minimize expected free energy | Maximize expected reward |
| Exploration | Intrinsic (epistemic value in EFE) | Extrinsic (ε-greedy, UCB, etc.) |
| Model | Generative model (required) | Model-free or model-based |
| Perception | Unified with action | Separate from action |

**Detailed treatment**: [CS Module 5](../04_computer_science/05_action/module.md), Reference #74 (Sajid et al., 2021).

### What is the Dark Room Problem?

The objection that if organisms minimize surprise, they should seek maximally predictable environments (a dark, empty room). Active Inference resolves this through the *C-vector* (preferences): organisms have prior expectations about the states they should occupy, and a dark room violates those expectations.

**Full discussion**: [Philosophy Module 4](../01_philosophy/04_cognition/module.md), [Glossary: Dark Room Problem](./glossary.md).

---

## About This Curriculum

### What math do I need?

- **Course 1 (Philosophy)**: No math required — concepts are presented in prose
- **Course 2 (Cognitive Science)**: Basic familiarity with probability and statistics is helpful
- **Course 3 (Mathematics)**: Calculus (partial derivatives, gradients), basic linear algebra, and probability theory. Modules 1-2 review prerequisites
- **Course 4 (Computer Science)**: Python programming with NumPy, basic OOP

### Can I skip courses?

The courses are designed to be taken in order (Philosophy → CogSci → Math → CS), but see [Learning Pathways](./learning_pathways.md) for alternative routes based on your background. Key dependencies:

- Math Course requires philosophical and cognitive context from Courses 1-2
- CS Course requires the mathematical derivations from Course 3
- Each course can be studied independently for a single-disciplinary perspective, but cross-course connections will be missed

### How long does the curriculum take?

Each course is designed for 8 weeks (one module per week). The full 4-course sequence takes approximately 32 weeks. Students with strong backgrounds may work faster through familiar material.

### What are the shared resources?

All four courses reference a common set of resources:

| Resource | Purpose |
|----------|---------|
| [Notation Table](./notation_table.md) | Canonical symbols used across all courses |
| [Glossary](./glossary.md) | 50+ term definitions with per-course usage |
| [References](./references.md) | 82 canonical citations organized by module topic |
| [Cross-Course Map](./cross_course_map.md) | Navigate between parallel modules across courses |
| [Learning Pathways](./learning_pathways.md) | Suggested study orders by background |

---

## Conceptual Questions

### What is a Markov Blanket?

A set of states that renders internal states *conditionally independent* of external states. It formalizes the notion of a system boundary — not as a physical barrier, but as a statistical separation. See [Glossary](./glossary.md), [Philosophy Module 1](../01_philosophy/01_systems/module.md), [Math Module 1](../03_math/01_systems/module.md).

### What is Variational Free Energy?

An upper bound on surprisal (negative log model evidence): `F = E_q[ln q(s) - ln p(o,s)]`. Minimizing VFE with respect to beliefs = perception; with respect to parameters = learning. See [Notation Table](./notation_table.md), [Math Module 3](../03_math/03_perception/module.md).

### What is Expected Free Energy?

The expected value of free energy under a future policy. Decomposes into *risk* (pragmatic value) and *ambiguity* (epistemic value). Drives action selection. See [Math Module 5](../03_math/05_action/module.md), [CS Module 5](../04_computer_science/05_action/module.md).

### What are the A, B, C, D, E matrices?

The components of a discrete state-space generative model:

| Matrix | Name | Role |
|--------|------|------|
| **A** | Likelihood | Maps hidden states to observations |
| **B** | Transition | State transitions under actions |
| **C** | Preferences | Log prior preferences over observations |
| **D** | Prior | Prior beliefs about initial state |
| **E** | Habits | Prior over policies |

See [Notation Table](./notation_table.md), [CS Module 2](../04_computer_science/02_agents/module.md).
