# Module 05: Action -- Active Inference Control

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module covers **action** in robotic systems through the Active Inference framework. Unlike classical control approaches that separate state estimation from control, Active Inference unifies perception and action under a single free energy objective. Motor commands emerge from proprioceptive prediction errors: the robot acts to make its sensory input match its predictions, analogous to biological reflex arcs.

## Learning Objectives

1. **Explain** how action arises in Active Inference as the fulfillment of proprioceptive predictions, contrasting with classical plan-then-execute architectures.
2. **Compare** PID control, Model Predictive Control, and Active Inference control for robotic manipulation tasks.
3. **Design** an Active Inference controller for a multi-joint robot arm, specifying prior preferences, prediction errors, and action update equations.
4. **Analyze** controller robustness under perturbations (external forces, sensor degradation, actuator failure) for each control paradigm.
5. **Implement** pseudocode for a unified perception-action control loop that handles both state estimation and motor command generation.
6. **Evaluate** practical considerations: control frequency requirements, actuator saturation limits, and safety constraints within the Active Inference framework.

## Key Concepts

- Action as proprioceptive prediction error minimization
- The reflex arc model of motor control
- Comparing PID, MPC, and Active Inference control
- Unified perception-action under free energy minimization
- Precision weighting for robust control

## Prerequisites

- Module 03: Perception (prediction errors, precision weighting)
- Module 04: Cognition (world models for action planning)
- Basic control theory (PID, feedback loops, stability)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Active Inference Control |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: PID vs. Active Inference Control |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Cognition](../04_cognition/README.md) -- world models that inform action selection
- **Next module**: [Learning](../06_learning/README.md) -- adapting control parameters over time
- **Related in Course 3**: [Control & Estimation: Action](../../03_control_estimation/05_action/README.md) -- mathematical derivation of AI control
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
