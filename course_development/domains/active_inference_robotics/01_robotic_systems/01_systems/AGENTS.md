# Station: Systems (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Systems architecture, Markov blanket boundaries, sensor-actuator partitioning
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, grounded in real hardware considerations

## Content Guidelines

All content in this module must:

1. Frame robotic systems as Markov blankets, clearly distinguishing internal states (computation, beliefs), sensory states (sensor readings), active states (motor commands), and external states (environment).
2. Use concrete robotic hardware examples: differential-drive platforms, manipulator arms, UAVs, or legged robots.
3. Connect system boundary definitions to real engineering decisions such as sensor placement, actuator selection, and computational resource allocation.
4. Emphasize that the system boundary is not merely physical but functional -- defined by conditional independence relationships in the generative model.
5. Reference established robotics frameworks (ROS2 node architectures, hardware abstraction layers) as practical instantiations of Markov blanket decompositions.

## Active Inference Integration

- **Sensorimotor loops**: The system boundary defines what counts as an observation versus an action. Sensor data flows inward across the blanket; motor commands flow outward.
- **Proprioceptive inference**: Internal state estimation (e.g., joint angles from encoders) is itself a form of self-modeling that the system performs to maintain its generative model.
- **Motor commands as predictions**: Actuator outputs are not arbitrary control signals but predictions about the sensory consequences of action, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use standard robotics notation (q for joint angles, u for control inputs, z for observations) alongside Active Inference notation (mu for beliefs, F for free energy).
