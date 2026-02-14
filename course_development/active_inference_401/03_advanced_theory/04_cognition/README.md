# Module 04: Cognition

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Deep Temporal Models and Hierarchical Inference

Part of **Advanced Theory**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Deep Temporal Models and Hierarchical Inference |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Implementing Hierarchical Message Passing |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Analyze** deep temporal models as hierarchical generative models with multiple temporal scales, where each level generates the sufficient statistics of the level below at a slower timescale
2. **Derive** the variational message passing equations for hierarchical models: ascending messages (prediction errors) and descending messages (predictions), proving that fixed-point iteration converges to the variational minimum under mean-field assumptions
3. **Examine** the role of temporal depth in planning, imagination, and counterfactual reasoning, formalizing how deep models enable prospection by propagating beliefs forward through the temporal hierarchy
4. **Implement** a deep temporal model in generalized coordinates of motion, showing how continuous-time Active Inference handles dynamics through embedding states in a Taylor expansion (position, velocity, acceleration, jerk, etc.)

## Prerequisites

- Graduate-level understanding of graphical models (factor graphs, message passing, variational message passing)
- Familiarity with generalized coordinates of motion and their role in continuous-time inference
- Competence in numerical methods for ODEs and fixed-point iteration

## Key References

- Friston, K. J. et al. (2017). Active inference, curiosity and insight. *Neural Computation*, 29(10), 2633--2683.
- Friston, K. J. et al. (2017). The graphical brain: Belief propagation and active inference. *Network Neuroscience*, 1(4), 381--414.
- Parr, T. & Friston, K. J. (2018). Generalised free energy and active inference. *Biological Cybernetics*, 113(5--6), 495--513.
- Heins, C. et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software*, 7(73), 4098.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
