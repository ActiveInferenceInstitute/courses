# Station: Communication (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Multi-robot communication, consensus algorithms, distributed inference, ROS2 architectures
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting distributed systems design to Active Inference theory

## Content Guidelines

All content in this module must:

1. Frame inter-robot communication as generative model alignment: robots share prediction errors and beliefs to minimize collective free energy across the multi-agent system.
2. Connect to practical multi-robot architectures using ROS2 topics, services, and actions as communication primitives.
3. Address consensus algorithms as collective free energy minimization, where precision-weighted belief sharing leads to coordinated behavior.
4. Use concrete multi-robot scenarios: warehouse fleets, search-and-rescue teams, collaborative manipulation, and drone swarms.
5. Discuss communication constraints (bandwidth, latency, packet loss) as factors that shape the expected free energy of communication actions.

## Active Inference Integration

- **Sensorimotor loops**: Communication extends the sensorimotor loop across agent boundaries. Receiving a message from another robot is a form of observation; sending a message is a form of action.
- **Proprioceptive inference**: In multi-robot systems, each robot must model not only its own state but also its beliefs about other robots' states and intentions.
- **Motor commands as predictions**: A communication message is a prediction about what the receiving robot needs to know -- the sender predicts the receiver's information gap and acts to fill it.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use subscript i for robot index, Pi for precision, mu for beliefs, and C for communication channel.
