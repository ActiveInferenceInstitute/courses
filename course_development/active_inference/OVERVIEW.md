# Active Inference Curriculum Overview

> **Quick Navigation**: [Philosophy](./01_philosophy/) | [Cognitive Science](./02_cognitive_science/) | [Mathematics](./03_math/) | [Computer Science](./04_computer_science/) | [Shared Resources](./resources/)

## Course Mission

This 4-course curriculum provides a comprehensive, multi-disciplinary introduction to **Active Inference** and the **Free Energy Principle (FEP)**. It is designed to take learners from conceptual understanding to mathematical derivation and computational implementation.

The curriculum employs a **Spiral Learning** pedagogy: each of the 4 courses revisits the **same 8 core topics** from a different disciplinary lens, deepening understanding with each pass.

---

## 1. The Structure

### Disciplinary Tracks

1. **[Philosophy](./01_philosophy/README.md)**: Establish the "Why" and "What". Focus on phenomenology, enactivism, and the conceptual foundations.
    * *Key Output*: Conceptual clarity and argumentation.
2. **[Cognitive Science](./02_cognitive_science/README.md)**: Explore the "How" in biological systems. Focus on predictive coding, neural correlates, and clinical applications.
    * *Key Output*: Mapping theory to brain structure and function.
3. **[Mathematics](./03_math/README.md)**: Derive the "Proof". Focus on the formal definitions of VFE, EFE, and belief updating.
    * *Key Output*: Rigorous derivation of the update equations.
4. **[Computer Science](./04_computer_science/README.md)**: Build the "Mechanism". Focus on Python implementation using `pymdp` and custom agents.
    * *Key Output*: Working simulations of active inference agents.

### The 8 Core Topics

All courses follow this sequence:

1. **Systems**: Markov Blankets, boundaries, and self-organization ([Map](./resources/cross_course_map.md#module-1-systems)).
2. **Agents**: Autopoiesis, interoception, and the self-model ([Map](./resources/cross_course_map.md#module-2-agents)).
3. **Perception**: Inferred states, predictive coding, and VFE minimization ([Map](./resources/cross_course_map.md#module-3-perception)).
4. **Cognition**: Beliefs, precision weighting, and attention ([Map](./resources/cross_course_map.md#module-4-cognition)).
5. **Action**: Policy selection, affordances, and EFE minimization ([Map](./resources/cross_course_map.md#module-5-action)).
6. **Learning**: Parameter updates, structure learning, and model reduction ([Map](./resources/cross_course_map.md#module-6-learning)).
7. **Communication**: Theory of mind, coupled inference, and language ([Map](./resources/cross_course_map.md#module-7-communication)).
8. **Planning**: Deep temporal models and sophisticated inference ([Map](./resources/cross_course_map.md#module-8-planning)).

---

## 2. Resource Hub

Crucial for maintaining consistency across the curriculum.

* **[Notation Table](./resources/notation_table.md)**: The **canonical** source for all mathematical symbols (e.g., $F$, $G$, $\pi$, $\mathbf{A}$).
* **[Glossary](./resources/glossary.md)**: Definitions for 50+ key terms (e.g., "Markov Blanket", "Epistemic Value").
* **[References](./resources/references.md)**: 82+ foundational citations organized by topic.
* **[Cross-Course Map](./resources/cross_course_map.md)**: A grid view of every module across all 4 courses.
* **[Learning Pathways](./resources/learning_pathways.md)**: Suggested routes through the material based on your background.

---

## 3. Deep Linking Map

### Course 1: Philosophy

* [01_systems](./01_philosophy/01_systems/module.md)
* [02_agents](./01_philosophy/02_agents/module.md)
* [03_perception](./01_philosophy/03_perception/module.md)
* [04_cognition](./01_philosophy/04_cognition/module.md)
* [05_action](./01_philosophy/05_action/module.md)
* [06_learning](./01_philosophy/06_learning/module.md)
* [07_communication](./01_philosophy/07_communication/module.md)
* [08_planning](./01_philosophy/08_planning/module.md)

### Course 2: Cognitive Science

* [01_systems](./02_cognitive_science/01_systems/module.md)
* [02_agents](./02_cognitive_science/02_agents/module.md)
* [03_perception](./02_cognitive_science/03_perception/module.md)
* [04_cognition](./02_cognitive_science/04_cognition/module.md)
* [05_action](./02_cognitive_science/05_action/module.md)
* [06_learning](./02_cognitive_science/06_learning/module.md)
* [07_communication](./02_cognitive_science/07_communication/module.md)
* [08_planning](./02_cognitive_science/08_planning/module.md)

### Course 3: Mathematics

* [01_systems](./03_math/01_systems/module.md)
* [02_agents](./03_math/02_agents/module.md)
* [03_perception](./03_math/03_perception/module.md)
* [04_cognition](./03_math/04_cognition/module.md)
* [05_action](./03_math/05_action/module.md)
* [06_learning](./03_math/06_learning/module.md)
* [07_communication](./03_math/07_communication/module.md)
* [08_planning](./03_math/08_planning/module.md)

### Course 4: Computer Science

* [01_systems](./04_computer_science/01_systems/module.md)
* [02_agents](./04_computer_science/02_agents/module.md)
* [03_perception](./04_computer_science/03_perception/module.md)
* [04_cognition](./04_computer_science/04_cognition/module.md)
* [05_action](./04_computer_science/05_action/module.md)
* [06_learning](./04_computer_science/06_learning/module.md)
* [07_communication](./04_computer_science/07_communication/module.md)
* [08_planning](./04_computer_science/08_planning/module.md)

---

## 4. How to Contribute

This repository is maintained by a team of AI agents. Humans and agents must follow strict guidelines:

1. **Read First**: Check [AGENTS.md](./AGENTS.md) at the root level.
2. **Verify**: Ensure all new content adheres to the [Notation Table](./resources/notation_table.md).
3. **Audit**: Run `./audit_modules.sh` before submitting changes.

---

> *Minimize surprise. Maximize evidence.*
