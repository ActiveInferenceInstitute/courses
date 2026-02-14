# Station: Communication (Autonomous Agents)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: SLAM, navigation, multi-robot coordination
- **Topics**: natural language, gesture, multi-robot task allocation, shared autonomy, full autonomy requirements
- **Lab Style**: ROS2 Project
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting fully autonomous robotic systems to Active Inference

## Content Guidelines

All content in this module must:

1. Frame autonomous communication as a system that operates without human intervention, using Active Inference to handle uncertainty, novelty, and failures.
2. Emphasize ROS2 implementation patterns: nodes, topics, services, actions, and lifecycle management.
3. Address real-world deployment challenges: edge cases, safety constraints, computational limits, and graceful degradation.
4. Use concrete autonomous robotics scenarios: warehouse automation, search and rescue, autonomous driving, space exploration.
5. Connect theoretical Active Inference concepts to practical autonomous communication implementation with specific code patterns and architectural decisions.

## Active Inference Integration

- **Sensorimotor loops**: Frame communication as part of the continuous perception-action cycle where the robot generates predictions, computes prediction errors, and updates beliefs or actions to minimize free energy.
- **Proprioceptive inference**: Connect communication to the robot's self-model -- its understanding of its own body, capabilities, and limitations as maintained through proprioceptive prediction errors.
- **Motor commands as predictions**: Relate communication to the Active Inference principle that motor commands are predictions about desired sensory outcomes, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
