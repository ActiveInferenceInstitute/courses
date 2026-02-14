# Module 07: Communication

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Multi-Agent Active Inference

Part of **Mathematical Frameworks** -- this module extends the POMDP to multiple interacting agents, formalizing communication as coupled inference.

## Learning Objectives

By the end of this module, students will be able to:

1. **Construct** a multi-agent generative model where each agent includes the other's states in its hidden state space
2. **Calculate** mutual information between two agents' belief states as a measure of communication success
3. **Analyze** generalized synchrony as the mathematical condition for aligned generative models
4. **Evaluate** how shared priors (language, norms) reduce the computational cost of multi-agent inference
5. **Apply** the multi-agent framework to formalize Theory of Mind as nested inference

## Prerequisites

- Mathematical Frameworks Module 04: Cognition (POMDPs)
- Mathematical Frameworks Module 05: Action (EFE, policy selection)

## Key Concepts

- **Multi-agent generative model**: A model where each agent's hidden states include the other agent's beliefs
- **Generalized synchrony**: Coupled dynamical systems converging to a shared trajectory
- **Mutual information I(X;Y)**: Shared information between two variables; quantifies communication
- **Shared prior**: Common model component enabling efficient inter-agent prediction
- **Nested inference**: Agent A models agent B who is itself modeling agent A

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Multi-Agent Active Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Two-Agent Inference and Mutual Information |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Veissiere, S. P. L. et al. (2020). Thinking through other minds. *Behavioral and Brain Sciences*, 43, e90.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 9. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
