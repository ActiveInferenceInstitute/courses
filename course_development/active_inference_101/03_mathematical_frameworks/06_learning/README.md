# Module 06: Learning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Parameter and Structure Learning

Part of **Mathematical Frameworks** -- this module formalizes learning as inference over model parameters using Dirichlet distributions and Bayesian model reduction.

## Learning Objectives

By the end of this module, students will be able to:

1. **Explain** Dirichlet distributions as conjugate priors for categorical distributions, and how they encode accumulated experience
2. **Compute** updated concentration parameters after a sequence of state-observation pairs
3. **Derive** the Bayesian model reduction criterion for pruning unnecessary model components
4. **Compare** model evidence for two competing models to determine which better explains the data
5. **Synthesize** parameter learning (slow inference) with state inference (fast inference) within a unified framework

## Prerequisites

- Mathematical Frameworks Module 05: Action (EFE, policy selection)
- Mathematical Frameworks Module 03: Perception (belief updating)

## Key Concepts

- **Dirichlet distribution**: Distribution over probability vectors, parameterized by concentration parameters
- **Concentration parameters**: Accumulated counts encoding experience; higher values = more confidence
- **Bayesian Model Reduction (BMR)**: Evaluating and pruning model components based on model evidence
- **Model evidence P(o)**: The probability of observations under a given model; higher = better fit
- **Conjugate prior**: A prior distribution whose posterior has the same functional form

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Parameter and Structure Learning |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Dirichlet Updates and Model Comparison |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2017). Active inference, curiosity and insight. *Neural Computation*, 29(10), 2633-2683.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 7. MIT Press.
- Friston, K. et al. (2018). Bayesian model reduction. *arXiv:1805.07092*.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
