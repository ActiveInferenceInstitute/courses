# Module 08: Planning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Deep Temporal Models and Planning as Inference

Part of **Mathematical Frameworks** -- the capstone module formalizes multi-timescale planning, sophisticated inference, and the relationship between habits and deliberation.

## Learning Objectives

By the end of this module, students will be able to:

1. **Derive** the expected free energy over a multi-step planning horizon, summing contributions from each future time step
2. **Analyze** deep temporal models as hierarchical POMDPs with nested timescale predictions
3. **Compare** standard EFE-based planning with sophisticated inference (which accounts for future belief updating)
4. **Evaluate** the computational complexity of planning as a function of horizon length and number of actions
5. **Synthesize** how habit formation (strong policy priors) reduces the computational burden of planning

## Prerequisites

- Mathematical Frameworks Module 05: Action (EFE)
- Mathematical Frameworks Module 06: Learning (parameter learning, BMR)

## Key Concepts

- **Deep temporal model**: Hierarchical generative model with predictions at multiple temporal resolutions
- **Policy tree**: Branching structure of possible future action sequences, evaluated by EFE
- **Planning horizon**: Number of future time steps over which the agent evaluates policies
- **Sophisticated inference**: Recursive planning that accounts for how future beliefs will change
- **Computational complexity of planning**: Exponential growth of policies with horizon, requiring pruning

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Deep Temporal Models and Planning as Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Multi-Step Policy Evaluation and Sophisticated Inference |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2021). Sophisticated inference. *Neural Computation*, 33(3), 713-763.
- Friston, K. J. et al. (2018). Deep temporal models and active inference. *Neuroscience & Biobehavioral Reviews*, 90, 486-501.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 8. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
