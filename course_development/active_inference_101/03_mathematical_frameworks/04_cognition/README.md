# Module 04: Cognition

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Partially Observable Markov Decision Processes

Part of **Mathematical Frameworks** -- this module introduces the POMDP framework as the canonical generative model for Active Inference decision-making.

## Learning Objectives

By the end of this module, students will be able to:

1. **Specify** the complete POMDP generative model by defining A (likelihood), B (transitions), C (preferences), and D (initial prior) matrices
2. **Compute** state inference for one time step in a POMDP given an observation sequence
3. **Analyze** how message passing (forward filtering and backward smoothing) enables inference over time
4. **Calculate** information gain (mutual information) for different possible observations in a POMDP
5. **Synthesize** the POMDP components with the cognitive science concepts of beliefs, preferences, and attention

## Prerequisites

- Mathematical Frameworks Module 03: Perception (belief updating, free energy minimization)

## Key Concepts

- **POMDP**: Partially Observable Markov Decision Process -- the canonical Active Inference generative model
- **A matrix**: P(o|s) -- the likelihood mapping from hidden states to observations
- **B matrix**: P(s_t|s_{t-1}, a) -- transition dynamics conditioned on actions
- **C vector**: Log-preferences over observations, encoding goals as prior expectations
- **D vector**: P(s_1) -- the initial belief about hidden states

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Partially Observable Markov Decision Processes |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Building a POMDP for the T-Maze Task |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 5. MIT Press.
- Kaelbling, L. P. et al. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1-2), 99-134.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces. *Journal of Mathematical Psychology*, 99, 102447.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
