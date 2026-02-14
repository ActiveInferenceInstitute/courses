# Module 07: Communication

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing Multi-Agent Inference

Part of **Implementation & Simulation** -- this module implements two coupled Active Inference agents communicating through a shared environment.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** a two-agent simulation where each agent's actions are part of the other's observations
2. **Measure** belief alignment between agents using KL divergence over time
3. **Visualize** belief convergence (or divergence) during multi-agent communication
4. **Experiment** with communication noise and its effect on belief alignment
5. **Analyze** the difference between communication with and without shared priors

## Prerequisites

- Implementation Module 06: Learning (multi-trial simulations)
- Implementation Module 02: Agents (Agent class)

## Key Concepts

- **Multi-agent environment**: Simulation managing two agents with coupled observations
- **Communication channel**: Routing one agent's actions as the other's observations
- **Belief alignment metric**: KL divergence between agents' belief states
- **Shared vs. private states**: Distinguishing common and agent-specific hidden states
- **Communication noise**: Adding stochasticity to the observation channel between agents

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing Multi-Agent Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Two Agents Communicating Through a Shared Environment |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 9. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
