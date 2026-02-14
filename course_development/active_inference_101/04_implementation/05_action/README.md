# Module 05: Action

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing Policy Selection and EFE

Part of **Implementation & Simulation** -- this module implements expected free energy computation and policy selection in the T-maze.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** the compute_efe() function that evaluates expected free energy for each policy
2. **Decompose** EFE into pragmatic and epistemic components and visualize each separately
3. **Demonstrate** the exploration-exploitation shift in the T-maze as uncertainty changes
4. **Conduct** a parameter sweep over precision and analyze its effect on action selection
5. **Compare** EFE-based policy selection with random and greedy baselines

## Prerequisites

- Implementation Module 04: Cognition (T-maze, free energy computation)

## Key Concepts

- **compute_efe()**: Function returning expected free energy for a given policy
- **Policy evaluation loop**: Iterating over all policies, computing EFE, selecting via softmax
- **Pragmatic component**: Computed from preferences (C vector) and expected observations
- **Epistemic component**: Computed from expected information gain
- **Precision sweep**: Varying gamma/alpha and measuring exploration-exploitation balance

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing Policy Selection and EFE |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: EFE Computation and Policy Selection |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces. *Journal of Mathematical Psychology*, 99, 102447.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
