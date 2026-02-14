# Module 07: Communication -- Multi-Robot Coordination

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module examines **communication** in robotic systems through the Active Inference framework. Inter-robot communication is framed as generative model alignment: robots share beliefs and prediction errors to minimize collective free energy across the multi-agent system. We explore how ROS2 architectures implement this communication, how consensus algorithms achieve distributed coordination, and how communication constraints shape multi-robot behavior.

## Learning Objectives

1. **Frame** inter-robot communication as prediction error sharing that aligns generative models across agents.
2. **Design** ROS2-compatible message-passing architectures for multi-robot teams, mapping topics and services to Markov blanket boundaries.
3. **Implement** precision-weighted consensus algorithms where robots converge on shared beliefs through iterative communication.
4. **Analyze** how communication bandwidth, latency, and reliability affect coordination quality and collective free energy.
5. **Compare** centralized and distributed coordination architectures in terms of scalability, robustness, and Active Inference properties.
6. **Evaluate** communication strategies that balance information sharing costs against coordination benefits.

## Key Concepts

- Communication as generative model alignment
- Prediction error sharing across agent boundaries
- Consensus as collective free energy minimization
- ROS2 topic architectures for multi-robot systems
- Communication bandwidth-coordination quality trade-offs
- Distributed Active Inference

## Prerequisites

- Module 02: Agents (agent boundaries and Markov blankets)
- Module 06: Learning (shared models and parameter transfer)
- Basic networking concepts (publish-subscribe patterns)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Multi-Robot Coordination |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Distributed Communication Protocols |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Learning](../06_learning/README.md) -- learned models that robots share
- **Next module**: [Planning](../08_planning/README.md) -- coordinated multi-robot planning
- **Related in Course 4**: [Autonomous Agents: Communication](../../04_autonomous_agents/07_communication/README.md) -- autonomous communication strategies
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
