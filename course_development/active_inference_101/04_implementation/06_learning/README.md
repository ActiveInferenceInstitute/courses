# Module 06: Learning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing Parameter Learning

Part of **Implementation & Simulation** -- this module implements Dirichlet parameter updates and multi-trial learning in Python.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** the Dirichlet update rule for the A matrix after each observation
2. **Run** multi-trial simulations tracking how the agent's model improves with experience
3. **Generate** learning curves plotting reward rate and free energy across trials
4. **Implement** basic Bayesian model reduction to prune unnecessary model parameters
5. **Compare** agent performance with and without parameter learning enabled

## Prerequisites

- Implementation Module 05: Action (EFE computation, policy selection)

## Key Concepts

- **Concentration parameter array**: NumPy array storing accumulated observation counts
- **Learning rate (eta)**: Scalar controlling update magnitude per observation
- **Multi-trial simulation**: Running the agent across many episodes with persistent learning
- **Learning curve**: Performance metric plotted as a function of trial number
- **Model pruning**: Removing low-evidence parameters using BMR

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing Parameter Learning |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Learning Curves and Parameter Updates |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2017). Active inference, curiosity and insight. *Neural Computation*, 29(10), 2633-2683.
- Heins, C. et al. (2022). pymdp: A Python library for active inference. *JOSS*, 7(73), 4098.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
