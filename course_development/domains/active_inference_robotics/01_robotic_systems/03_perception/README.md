# Module 03: Perception -- Sensor Fusion and State Estimation

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module covers **perception** in robotic systems through the lens of Active Inference. Robotic perception is framed as variational inference: the robot maintains beliefs about hidden states (its pose, the environment, object identities) and updates these beliefs by minimizing the discrepancy between predicted and actual sensor readings. Multi-sensor fusion emerges naturally as precision-weighted prediction error minimization.

## Learning Objectives

1. **Formulate** robotic perception as variational inference over a generative model that maps hidden states to sensor observations.
2. **Specify** observation models for common robotic sensors (LIDAR, cameras, IMUs, encoders) including noise characteristics and failure modes.
3. **Implement** precision-weighted sensor fusion, connecting Kalman filtering to free energy minimization.
4. **Analyze** how sensor precision (reliability) modulates the influence of each modality on the posterior belief.
5. **Design** active perception strategies where the robot selects actions to maximize information gain and reduce perceptual uncertainty.
6. **Distinguish** between exteroceptive and proprioceptive perception and their roles in the Active Inference framework.

## Key Concepts

- Perception as prediction error minimization
- Observation models and likelihood functions for robotic sensors
- Precision weighting and adaptive sensor fusion
- Active perception and epistemic actions
- Proprioceptive vs. exteroceptive inference

## Prerequisites

- Module 01: Systems (Markov blanket, state partitioning)
- Module 02: Agents (generative models, belief states)
- Basic probability theory (Bayes' rule, Gaussian distributions)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Sensor Fusion and State Estimation |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Multi-Sensor Fusion and Active Perception |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Agents](../02_agents/README.md) -- agent architecture that perception supports
- **Next module**: [Cognition](../04_cognition/README.md) -- world models built from perceptual inference
- **Related in Course 3**: [Control & Estimation: Perception](../../03_control_estimation/03_perception/README.md) -- Kalman filter derivation
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
