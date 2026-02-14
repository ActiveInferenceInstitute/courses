# Lab: Robotic Systems Integration Project

## Objective

Design a complete robotic system that integrates all eight Active Inference modules from this course. You will specify the system architecture, sensor suite, actuator configuration, generative model, control strategy, learning mechanism, communication protocol, and planning algorithm for a mobile manipulation robot.

## Prerequisites

- Completion of Modules 01-08 in this course
- Familiarity with ROS2 concepts (nodes, topics, services)
- Basic understanding of robot system integration

## Part 1: System Architecture (Module 01)

Define the Markov blanket for a mobile manipulator robot with a differential-drive base, a 6-DOF arm, and a parallel-jaw gripper:

1. List all internal states, sensory states, active states, and external states.
2. Draw a block diagram showing information flow between components.

{fill:textarea}

## Part 2: Agent Specification (Module 02)

Define what makes this robot an agent:

1. Specify the generative model (hidden states, observations, actions).
2. Define prior preferences that encode the robot's task goals.
3. Identify at least two levels of hierarchical agency.

{fill:textarea}

## Part 3: Perception Pipeline (Module 03)

Design the sensor fusion architecture:

1. List all sensors, their observation models, and noise characteristics.
2. Specify precision weights for each sensor modality.
3. Describe one active perception strategy the robot should employ.

{fill:textarea}

## Part 4: Integrated Design Summary

Complete the integration table:

| Module | Component | Your Design Choice | Active Inference Mapping |
| --- | --- | --- | --- |
| Systems | Architecture | {fill} | Markov blanket |
| Agents | Agency | {fill} | Self-evidencing |
| Perception | Sensors | {fill} | Likelihood models |
| Cognition | World model | {fill} | Generative model |
| Action | Control | {fill} | Free energy minimization |
| Learning | Adaptation | {fill} | Parameter learning |
| Communication | Coordination | {fill} | Model alignment |
| Planning | Navigation | {fill} | Expected free energy |

{fill:textarea}

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
