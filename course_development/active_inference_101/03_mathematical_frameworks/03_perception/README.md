# Module 03: Perception

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Free Energy Minimization

Part of **Mathematical Frameworks** -- this module derives the belief updating equations that formalize perception as free energy minimization.

## Learning Objectives

By the end of this module, students will be able to:

1. **Derive** the optimal belief updating rule by minimizing variational free energy with respect to q(s)
2. **Compute** posterior beliefs given an A matrix, D vector, and observation using the softmax formula
3. **Analyze** how precision weighting enters the belief updating equations through the relative weight of likelihood and prior
4. **Evaluate** the effect of different precision settings on perceptual inference in a worked example
5. **Compare** variational belief updating with exact Bayesian computation for a simple two-state model

## Prerequisites

- Mathematical Frameworks Module 02: Agents (variational inference, free energy, KL divergence)

## Key Concepts

- **Variational free energy F**: F = E_q[ln q(s) - ln P(o, s)] -- minimized during perception
- **Belief updating**: Iteratively adjusting q(s) to minimize F, converging on the best explanation
- **Precision (pi)**: Inverse variance; high precision = confident/narrow, low precision = uncertain/broad
- **Softmax**: The function that converts log-probabilities to a valid probability distribution
- **Gradient descent on F**: The algorithmic implementation of belief updating

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Free Energy Minimization |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Step-by-Step Belief Updating in a Two-State Model |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 4. MIT Press.
- Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology*, 76, 198-211.
- Buckley, C. L. et al. (2017). The free energy principle for action and perception. *Journal of Mathematical Psychology*, 76, 55-79.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
