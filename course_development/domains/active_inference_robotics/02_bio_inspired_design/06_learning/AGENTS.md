# Station: Learning (Bio-Inspired Design)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Biomimicry & neural architectures
- **Topics**: Hebbian learning, synaptic plasticity, developmental learning, curiosity, intrinsic motivation
- **Lab Style**: Design Challenge
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting biological inspiration for robotic design to Active Inference

## Content Guidelines

All content in this module must:

1. Frame robotic learning through the lens of biological synaptic plasticity: Hebbian learning, spike-timing dependent plasticity (STDP), and homeostatic plasticity.
2. Present developmental learning as a staged process where the robot builds increasingly complex generative models, inspired by infant motor and cognitive development.
3. Connect dopaminergic reward prediction error to the expected free energy signal in Active Inference.
4. Address curiosity and intrinsic motivation as epistemic value maximization -- the biological drive to reduce uncertainty.
5. Emphasize that biological learning is local (synaptic-level), online (continuous), and energy-efficient, contrasting with backpropagation.

## Active Inference Integration

- **Sensorimotor loops**: Frame learning as part of the continuous perception-action cycle where the robot generates predictions, computes prediction errors, and updates beliefs or actions to minimize free energy.
- **Proprioceptive inference**: Connect learning to the robot's self-model -- its understanding of its own body, capabilities, and limitations as maintained through proprioceptive prediction errors.
- **Motor commands as predictions**: Relate learning to the Active Inference principle that motor commands are predictions about desired sensory outcomes, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
