# Module 02: Agents

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Implementing the Active Inference Agent

Part of **Implementation & Simulation** -- this module builds the Agent class and perception-action loop in Python.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** an Agent class that maintains beliefs q(s) and performs the perception-action loop
2. **Design** an Environment class that manages the true hidden state and generates observations
3. **Execute** a basic simulation running the agent for multiple timesteps, recording beliefs and actions
4. **Compare** a custom agent implementation with pymdp's built-in Agent class
5. **Debug** common simulation issues: incorrect belief initialization, observation indexing errors, action mapping bugs

## Prerequisites

- Implementation Module 01: Systems (NumPy toolkit, GenerativeModel class)

## Key Concepts

- **Agent class**: Python object with generative model, beliefs, and inference/action methods
- **Perception-action loop**: observe -> infer states -> select action -> act -> repeat
- **Belief vector**: NumPy array representing q(s), the current state estimate
- **Environment class**: Separate object managing the true world state
- **pymdp Agent**: The library's reference implementation for comparison

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Implementing the Active Inference Agent |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Building and Running an Active Inference Agent |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Heins, C. et al. (2022). pymdp: A Python library for active inference. *JOSS*, 7(73), 4098.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapters 4-5. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
