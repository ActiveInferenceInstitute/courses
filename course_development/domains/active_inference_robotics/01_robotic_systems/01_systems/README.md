# Module 01: Systems -- Robotic Systems Architecture

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module introduces the concept of **systems** as the foundational unit of analysis in Active Inference, applied to robotic system architecture. A robotic system is decomposed into internal, sensory, active, and external states using the Markov blanket formalism, providing a principled framework for understanding how robots maintain their organization through interaction with the environment.

## Learning Objectives

1. **Define** the Markov blanket boundary for a robotic system and identify its internal, sensory, active, and external states.
2. **Map** standard robotic components (sensors, actuators, processors) to Active Inference state types.
3. **Analyze** how system boundary choices affect the generative model structure and computational requirements.
4. **Compare** classical robotics system decomposition (sense-plan-act) with the Active Inference perception-action loop.
5. **Evaluate** trade-offs in sensor suite design, actuator selection, and computational architecture through the lens of free energy minimization.
6. **Design** a block diagram of a robotic system that explicitly represents Markov blanket partitioning.

## Key Concepts

- Markov blanket as a system boundary in physical robots
- Sensor-actuator architecture as sensory and active states
- Generative models for robotic state estimation
- The relationship between hardware abstraction layers and conditional independence
- System identification as model structure learning

## Prerequisites

- Basic familiarity with robot components (sensors, actuators, embedded controllers)
- Understanding of state-space representations (state vectors, transition models)
- Introductory probability and statistics (Gaussian distributions, Bayes' rule)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Robotic Systems Architecture |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: System Boundary Analysis |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Next module**: [Agents](../02_agents/README.md) -- from system boundaries to agent identity
- **Related in Course 3**: [Control & Estimation: Systems](../../03_control_estimation/01_systems/README.md) -- mathematical treatment of state estimation
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
