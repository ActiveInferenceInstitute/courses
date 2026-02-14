# Station: Action (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Motor control, PID vs. Active Inference control, proprioceptive inference, action as prediction fulfillment
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, emphasizing the practical advantages of unifying perception and action

## Content Guidelines

All content in this module must:

1. Present action in Active Inference as the process by which motor commands are generated to fulfill proprioceptive predictions, not as a separate planning-then-execution pipeline.
2. Compare classical control approaches (PID, MPC, computed torque) with Active Inference control, highlighting how AI unifies state estimation and control under a single free energy objective.
3. Use concrete robotic actuator examples: DC motors, servos, stepper motors, pneumatic actuators, and their noise/dynamics characteristics.
4. Emphasize the reflex arc model: motor commands arise from proprioceptive prediction errors, analogous to spinal reflexes in biological systems.
5. Address practical concerns: control frequency, actuator saturation, safety constraints, and how these map to the Active Inference formalism.

## Active Inference Integration

- **Sensorimotor loops**: Action is one half of the perception-action loop. The robot acts to change its sensory input so that it matches its predictions (prior preferences).
- **Proprioceptive inference**: Motor commands arise from prediction errors between desired and inferred proprioceptive states (joint angles, end-effector positions).
- **Motor commands as predictions**: In Active Inference, a motor command is a prediction about the next proprioceptive state. The spinal reflex arc (or its robotic equivalent) ensures the body moves to fulfill this prediction.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use u for control/torque inputs, q for joint angles, a for Active Inference actions, F for free energy.
