# Module 04: Cognition -- Probabilistic World Models for Robots

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module explores **cognition** in robotic systems as the construction and maintenance of probabilistic world models. A robot's cognitive architecture is its generative model of the environment: a structured representation that enables prediction, planning, and decision-making. We examine SLAM as a canonical example of robotic cognition, factor graphs as computational tools for inference, and hierarchical models that span multiple spatial and temporal scales.

## Learning Objectives

1. **Design** a generative world model for a mobile robot that jointly represents the robot's pose, environment geometry, and object categories.
2. **Implement** a factor graph representation of a SLAM problem and describe how message-passing algorithms perform approximate inference.
3. **Construct** hierarchical world models with metric, topological, and semantic levels, specifying how information flows between levels.
4. **Analyze** the role of model complexity in the free energy objective and explain how Occam's principle prevents overfitting in world models.
5. **Compare** classical SLAM approaches with Active Inference formulations, identifying shared structure and key differences.
6. **Evaluate** when a robot should update its world model structure versus simply updating belief parameters.

## Key Concepts

- Generative world models as the substrate of robotic cognition
- SLAM as joint inference over poses and maps
- Factor graphs and message-passing inference
- Hierarchical representations (metric, topological, semantic)
- Model complexity, Occam's principle, and Bayesian model selection

## Prerequisites

- Module 03: Perception (sensor fusion, observation models)
- Basic graph theory (nodes, edges, adjacency)
- Familiarity with SLAM concepts (optional but helpful)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Probabilistic World Models for Robots |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: World Model Design and SLAM |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Perception](../03_perception/README.md) -- sensory data that feeds world models
- **Next module**: [Action](../05_action/README.md) -- using world models to select actions
- **Related in Course 4**: [Autonomous Agents: Cognition](../../04_autonomous_agents/04_cognition/README.md) -- cognitive architectures for full autonomy
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
