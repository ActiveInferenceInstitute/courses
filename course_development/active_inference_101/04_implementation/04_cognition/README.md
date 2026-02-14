# Module 04: Cognition

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing the T-Maze

Part of **Implementation & Simulation** -- this module implements the T-maze, the canonical Active Inference demonstration task.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** the complete T-maze environment with states, observations, and actions
2. **Set up** the A, B, C, D matrices for the T-maze scenario
3. **Trace** through a complete T-maze trial computing beliefs and free energy at each step
4. **Compute** variational free energy and plot its trajectory over a trial
5. **Modify** the T-maze to test different scenarios: ambiguous cue, no cue, reversed contingencies

## Prerequisites

- Implementation Module 03: Perception (infer_states, belief trajectories)

## Key Concepts

- **T-maze**: Standard Active Inference benchmark with cue location and reward arms
- **Free energy computation**: F = E_q[ln q(s) - ln P(o, s)] evaluated at each timestep
- **Multi-step inference**: Running belief updating across multiple time steps within a trial
- **Environment configuration**: Setting up state-observation-action mappings for the T-maze
- **Trial visualization**: Plotting agent position, beliefs, and free energy over time

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing the T-Maze |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Running the T-Maze Agent |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 5. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
