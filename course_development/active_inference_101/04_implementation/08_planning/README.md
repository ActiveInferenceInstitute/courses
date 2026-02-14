# Module 08: Planning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## The Complete Active Inference Agent

Part of **Implementation & Simulation** -- the capstone module integrates all components into a fully functional Active Inference agent with multi-step planning.

## Learning Objectives

By the end of this module, students will be able to:

1. **Implement** multi-step EFE evaluation over a planning horizon of 2-3 time steps
2. **Run** the complete Active Inference agent with perception, action, learning, and planning integrated
3. **Compare** agent performance across different planning depths (1-step, 2-step, 3-step)
4. **Identify** computational bottlenecks in policy tree evaluation and implement pruning strategies
5. **Design** extension projects: new environments, continuous states, or hierarchical models

## Prerequisites

- All previous Implementation modules (01-07)

## Key Concepts

- **Policy tree enumeration**: Generating and evaluating all action sequences up to a planning horizon
- **Sophisticated inference**: Recursive planning accounting for future belief updates
- **Computational budget**: Strategies for limiting policy evaluations (pruning, beam search)
- **Performance benchmarking**: Comparing planning depths, precision settings, and learning configurations
- **Extension projects**: Ideas for expanding the agent beyond the course scope

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: The Complete Active Inference Agent |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: The Complete Active Inference Agent |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. J. et al. (2021). Sophisticated inference. *Neural Computation*, 33(3), 713-763.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 8. MIT Press.
- Heins, C. et al. (2022). pymdp: A Python library for active inference. *JOSS*, 7(73), 4098.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
