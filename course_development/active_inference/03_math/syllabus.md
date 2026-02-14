# Course 3: The Mathematics of Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md) | [Resources](../resources/) | [Agent Guidelines](./AGENTS.md)

## Course Description

This course provides the formal mathematical foundations of Active Inference and the Free Energy Principle. The first two modules build a solid prerequisite base, covering matrix operations, probability theory, Bayesian statistics, information theory, graphical models, stochastic processes, and the Langevin/Fokker-Planck formalism. From Module 3 onward, we derive the core equations of variational inference, KL divergence, and the Expected Free Energy decomposition. Topics include precision matrices and hierarchical message passing, Bayesian model reduction, generalized synchrony in coupled systems, and sophisticated inference with tree search over policies. All derivations are presented step-by-step with worked examples.

---

## Prerequisites

- Courses 1-2 (Philosophy and Cognitive Science of Active Inference)
- Calculus: partial derivatives, gradients, optimization
- Basic familiarity with matrices and probability is helpful but formally reviewed in Modules 1-2
- No prior knowledge of information theory or stochastic differential equations is required (covered in Modules 1-2)

---

## Course Schedule

| Week | Module | Topic | Key Results | Mathematical Focus | Deliverables |
|------|--------|-------|-------------|-------------------|-------------|
| 1 | [Module 1](./01_systems/) | **Mathematical Foundations** | Precision-weighted Bayesian update, d-separation | Matrices, probability, Bayes' theorem, entropy, KL divergence, graphical models | Lab 1, Quiz 1 |
| 2 | [Module 2](./02_agents/) | **Stochastic Systems** | Fokker-Planck equation, NESS density, Kramers rate | Dynamical systems, random processes, Langevin equation, ergodicity | Lab 2, Quiz 2 |
| 3 | [Module 3](./03_perception/) | **Perception** | VFE derivation, ELBO | KL divergence, variational calculus | Lab 3, Quiz 3 |
| 4 | [Module 4](./04_cognition/) | **Cognition** | Hierarchical Gaussian filters | Precision matrices, message passing | Lab 4, Quiz 4 |
| 5 | [Module 5](./05_action/) | **Action** | EFE decomposition (G = risk + ambiguity) | Softmax policy selection, expected information gain | Lab 5, Quiz 5 |
| 6 | [Module 6](./06_learning/) | **Learning** | Dirichlet updates, BMR | Gradient descent on F, Occam factor | Lab 6, Quiz 6 |
| 7 | [Module 7](./07_communication/) | **Communication** | Generalized synchrony, MI | Coupled dynamical systems, transfer entropy | Lab 7, Quiz 7 |
| 8 | [Module 8](./08_planning/) | **Planning** | Sophisticated inference equations | Tree search, recursive belief updating | Lab 8, Quiz 8, Final Project |

---

## Learning Objectives

By the end of this course, you should be able to:

1. **Apply** matrices, probability, Bayes' theorem, and information theory as the mathematical language of Active Inference
2. **Analyze** stochastic dynamical systems via the Langevin and Fokker-Planck equations and compute steady-state densities
3. **Derive** the Variational Free Energy (VFE) from first principles and show its decomposition into complexity and accuracy
4. **Prove** that minimizing VFE is equivalent to maximizing the Evidence Lower Bound (ELBO)
5. **Decompose** Expected Free Energy (EFE) into pragmatic value (risk) and epistemic value (ambiguity resolution)
6. **Construct** precision-weighted message passing equations for a hierarchical generative model
7. **Apply** Bayesian Model Reduction to analytically compare nested models
8. **Formalize** communication as generalized synchrony between coupled dynamical systems
9. **Derive** the sophisticated inference update equations for multi-step planning

---

## Assessment Components

| Component | Description | Frequency |
|-----------|-------------|-----------|
| Practice Quizzes | Part A: 7 multiple choice + Part B: 3 free response per module (computations required) | Weekly (8 total) |
| Derivation Labs | Step-by-step proofs, equation manipulation, worked problems | Weekly (8 total) |
| Study Questions | 20 mathematical questions per module | Weekly (8 total) |
| Final Project | Extended derivation or formal proof | End of course |

### Final Project Options

1. **Extended Derivation**: Derive a key result not covered in class (e.g., continuous-time Active Inference, Renormalization Group connection)
2. **Proof Verification**: Formally verify all steps of a published derivation (e.g., Da Costa et al. 2020) and identify any implicit assumptions
3. **Novel Application**: Apply the mathematical framework to a new domain (e.g., ecological modelling, economic decision theory) and derive domain-specific equations

---

## Resources

| Resource | Purpose |
|----------|---------|
| [Notation Table](../resources/notation_table.md) | **Essential**: All symbols used in this course |
| [Glossary](../resources/glossary.md) | Definitions of mathematical and conceptual terms |
| [References](../resources/references.md) | Primary mathematical references (Friston 2019, Da Costa et al. 2020) |
| [Cross-Course Map](../resources/cross_course_map.md) | Navigate to conceptual counterparts in other courses |
