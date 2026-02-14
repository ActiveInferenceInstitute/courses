# Module 03: Perception

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing State Inference

Part of **Implementation & Simulation** -- this module implements the belief updating equations for perceptual inference in Python.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** the infer_states() function using the softmax(ln A[o,:] + ln prior) formula
2. **Visualize** belief trajectories showing how the agent's state estimates evolve over time
3. **Experiment** with the precision parameter and observe its effects on inference speed and accuracy
4. **Compare** approximate variational inference with exact Bayesian computation for small state spaces
5. **Analyze** inference failure cases: ambiguous observations, misspecified models, extreme precision

## Prerequisites

- Implementation Module 02: Agents (Agent class, perception-action loop)

## Key Concepts

- **infer_states()**: Core function updating beliefs given an observation and generative model
- **Precision parameter (gamma)**: Temperature parameter controlling inference confidence
- **Belief trajectory**: Time series of belief vectors across simulation steps
- **Exact vs. approximate inference**: Comparing softmax approximation to full Bayesian computation
- **Visualization**: matplotlib plots of belief evolution and free energy

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing State Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Implementing and Visualizing State Inference |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Bogacz, R. (2017). A tutorial on the free-energy framework. *Journal of Mathematical Psychology*, 76, 198-211.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 4. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
