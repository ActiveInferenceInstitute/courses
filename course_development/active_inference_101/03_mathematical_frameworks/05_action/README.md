# Module 05: Action

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Expected Free Energy

Part of **Mathematical Frameworks** -- this module derives the mathematics of action selection through expected free energy decomposition.

## Learning Objectives

By the end of this module, students will be able to:

1. **Derive** Expected Free Energy G(pi) from first principles and decompose it into pragmatic and epistemic terms
2. **Compute** EFE for each policy in a simple POMDP with 2-3 actions
3. **Calculate** the policy distribution P(pi) = softmax(-G(pi)) from EFE values
4. **Analyze** how the balance between pragmatic and epistemic value shifts with uncertainty level
5. **Compare** EFE-based action selection with reward-maximization in reinforcement learning

## Prerequisites

- Mathematical Frameworks Module 04: Cognition (POMDP, A/B/C/D matrices, information gain)

## Key Concepts

- **Expected Free Energy G(pi)**: Expected surprise under policy pi, evaluated over future time steps
- **Pragmatic value**: -E_q[ln P(o_tau)] -- alignment of expected outcomes with preferences
- **Epistemic value**: Expected information gain about hidden states under a policy
- **Policy distribution**: P(pi) = softmax(-G(pi)) -- probabilistic policy selection
- **Exploration-exploitation trade-off**: Naturally resolved by the EFE decomposition

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Expected Free Energy |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Computing and Decomposing Expected Free Energy |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 6. MIT Press.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces. *Journal of Mathematical Psychology*, 99, 102447.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
