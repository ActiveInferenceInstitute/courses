# Station: Learning (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Online parameter adaptation, sim-to-real transfer, hierarchical learning, lifelong learning
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, addressing practical challenges of deploying learning robots

## Content Guidelines

All content in this module must:

1. Frame robot learning as parameter optimization under the free energy principle: updating generative model parameters to reduce persistent prediction errors.
2. Distinguish three learning timescales: fast precision updates (sensor reliability), medium parameter learning (dynamics model), and slow structure learning (model architecture).
3. Address sim-to-real transfer as a core robotics challenge, comparing domain randomization, system identification, and Active Inference online adaptation.
4. Use concrete examples: friction coefficient learning, mass estimation, motor constant calibration, and sensor drift compensation.
5. Emphasize safety constraints: learning must not destabilize the robot or violate physical limits during adaptation.

## Active Inference Integration

- **Sensorimotor loops**: Learning is driven by persistent prediction errors in the sensorimotor loop. If the robot consistently fails to predict its own sensor readings, model parameters need updating.
- **Proprioceptive inference**: The robot learns its own body model -- joint friction, link masses, motor dynamics -- through proprioceptive prediction errors during normal operation.
- **Motor commands as predictions**: As the body model improves through learning, motor commands become better predictions of desired proprioceptive outcomes, leading to more accurate control.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use theta for learnable parameters, eta for learning rate, F for free energy, dF/dtheta for parameter gradients.
