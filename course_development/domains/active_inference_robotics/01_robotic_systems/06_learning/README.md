# Module 06: Learning -- Adaptive Robotics and Online Learning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module explores **learning** in robotic systems as the process of updating generative model parameters to reduce persistent prediction errors. Robots must adapt to changing conditions: sim-to-real gaps, hardware wear, environmental changes, and novel tasks. Active Inference provides a natural framework for online learning, where free energy serves as both the performance metric and the learning signal.

## Learning Objectives

1. **Formulate** robot learning as parameter optimization under the free energy principle, deriving parameter update rules from the free energy gradient.
2. **Distinguish** three timescales of learning: fast precision updates, medium parameter learning, and slow structure learning.
3. **Analyze** sim-to-real transfer challenges and compare domain randomization, system identification, and Active Inference online adaptation.
4. **Design** a hierarchical learning architecture that operates at multiple timescales while maintaining control stability.
5. **Implement** online parameter adaptation algorithms with appropriate learning rates and safety constraints.
6. **Evaluate** the trade-offs between learning speed, stability, and computational cost in deployed robotic systems.

## Key Concepts

- Free energy as a learning signal
- Parameter learning via gradient descent on free energy
- Sim-to-real transfer and domain adaptation
- Hierarchical learning at multiple timescales
- Lifelong learning and continual adaptation
- Safety constraints during online learning

## Prerequisites

- Module 05: Action (Active Inference control, prediction errors)
- Basic optimization concepts (gradient descent, learning rates)
- Familiarity with simulation environments (Gazebo, MuJoCo, or similar)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Adaptive Robotics and Online Learning |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Online Parameter Adaptation |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Action](../05_action/README.md) -- the control loop that learning improves
- **Next module**: [Communication](../07_communication/README.md) -- sharing learned models across robots
- **Related in Course 2**: [Bio-Inspired Design: Learning](../../02_bio_inspired_design/06_learning/README.md) -- biological learning mechanisms
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
