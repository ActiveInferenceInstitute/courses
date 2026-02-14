# The Mathematics of Active Inference

> **Quick Navigation**: [Curriculum Home](../README.md) | [Syllabus](./syllabus.md) | [Agent Guidelines](./AGENTS.md) | [Resources](../resources/)

## Overview

Provides the formal mathematical foundations of Active Inference and the Free Energy Principle. Covers state-space formulations, Langevin dynamics, variational inference, KL divergence, Expected Free Energy decomposition, precision matrices, Bayesian model reduction, and sophisticated inference. All derivations are presented step-by-step.

---

## Modules

| # | Topic | Subtitle | Description |
|---|-------|----------|-------------|
| 1 | [Systems](./01_systems/) | Mathematical Foundations: Matrices, Probability, and Bayesian Reasoning | Vectors and matrices for state spaces. Probability distributions. Bayes' theorem. Information theory (entropy, KL divergence). Graphical models. |
| 2 | [Agents](./02_agents/) | Stochastic Systems: Random Processes, Differential Equations, and Steady States | Deterministic dynamical systems. Stochastic processes. Langevin equation. Fokker-Planck equation. Steady states and ergodicity. |
| 3 | [Perception](./03_perception/) | Variational Free Energy, KL Divergence, and Recognition Density | VFE derivation and decompositions. Variational inference. KL divergence properties. Recognition density q(s). |
| 4 | [Cognition](./04_cognition/) | Precision Matrices, Hierarchical Gaussian Filters, Message Passing | Precision-weighted prediction errors. Hierarchical generative models. Belief propagation. Attentional selection. |
| 5 | [Action](./05_action/) | Expected Free Energy (G): Risk and Ambiguity Decomposition | EFE derivation. Risk-ambiguity decomposition. Policy selection via softmax. Epistemic and pragmatic value. |
| 6 | [Learning](./06_learning/) | Gradient Descent on VFE, Bayesian Model Reduction | Parameter learning via gradient descent. Dirichlet concentration updates. BMR and structure learning. Occam's window. |
| 7 | [Communication](./07_communication/) | Generalized Synchrony, Mutual Information, Coupled Systems | Coupled dynamical systems. Mutual information. Generalized synchrony. Social generative models. |
| 8 | [Planning](./08_planning/) | Recursive Belief Updating, Sophisticated Inference, Tree Search | Deep temporal models. Sophisticated inference equations. Tree search over policies. Temporal abstraction. |

---

## Module Contents

Each module folder contains 7 files:

| File | Description |
|------|-------------|
| `module.md` | Full lecture content from a mathematical perspective |
| `questions.md` | 20 study questions (mathematical focus) |
| `practice_quiz.md` | Quiz: Part A Multiple Choice (7 questions) + Part B Free Response (3 questions) |
| `lab.md` | Derivation Exercise lab: proof construction, equation manipulation, and worked examples |
| `dashboard.html` | Interactive HTML5 dashboard with concept cards and quiz |
| `README.md` | Module overview with cross-references |
| `AGENTS.md` | Agent guidelines for content generation |

---

## Prerequisites

Courses 1-2 (Philosophy and Cognitive Science). Familiarity with linear algebra (matrices, vectors), probability theory (Bayes' theorem, distributions), and calculus (derivatives, expectations). Knowledge of information theory (entropy, KL divergence) is helpful.

---

## Key References

- Friston (2019) A free energy principle for a particular physics
- Da Costa et al. (2020) Active inference on discrete state-spaces: A synthesis
- Parr, Pezzulo, & Friston (2022) *Active Inference* (MIT Press, Chapters 3-8)
- Friston & Penny (2011) Post hoc Bayesian model selection
- Smith et al. (2022) A step-by-step tutorial on active inference

See [resources/references.md](../resources/references.md) for the complete reference list with 82 canonical citations.

---

## Cross-References

This course is part of a 4-course sequence. Each row below covers the same topic from a different angle:

| Course | Perspective | Lab Type |
|--------|-------------|----------|
| [Philosophy](../01_philosophy/) | Philosophical foundations | Thought Experiment |
| [Cognitive Science](../02_cognitive_science/) | Neural and behavioral correlates | Case Study Analysis |
| [Mathematics](../03_math/) | Formal derivation and proof | Derivation Exercise |
| [Computer Science](../04_computer_science/) | Python implementation with pymdp | Coding Lab |

See [resources/cross_course_map.md](../resources/cross_course_map.md) for the full cross-course navigation map with links to all 32 modules.

---

## Shared Resources

| Resource | Description |
|----------|-------------|
| [Notation Table](../resources/notation_table.md) | Canonical notation used across all courses |
| [Glossary](../resources/glossary.md) | 50+ term definitions with per-course usage |
| [References](../resources/references.md) | 82 canonical citations organized by topic |
| [Cross-Course Map](../resources/cross_course_map.md) | Links to parallel modules in other courses |

---

## Documentation

| Document | Description |
|----------|-------------|
| [syllabus.md](./syllabus.md) | Full course syllabus with schedule, learning objectives, and assessment |
| [AGENTS.md](./AGENTS.md) | Agent guidelines for this course |
| [../README.md](../README.md) | Curriculum overview and learning pathway |
| [../AGENTS.md](../AGENTS.md) | Curriculum-wide conventions and standards |
