# Station: Action (Bio-Inspired Design)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Biomimicry & neural architectures
- **Topics**: Biological motor control, CPGs, spinal reflexes, forward models, efference copy, locomotion
- **Lab Style**: Design Challenge
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting biological inspiration for robotic design to Active Inference

## Content Guidelines

All content in this module must:

1. Frame biological motor control as Active Inference: the spinal reflex arc implements prediction error minimization where alpha motor neurons act to fulfill proprioceptive predictions set by gamma motor neurons.
2. Present central pattern generators (CPGs) as embodied generative models that predict and produce rhythmic movement patterns.
3. Use the cerebellum's forward model as the biological implementation of the generative model's prediction of action outcomes.
4. Connect efference copy (corollary discharge) to the Active Inference mechanism of predicting self-generated sensory changes.
5. Include concrete biological locomotion examples: insect walking, fish swimming, bird flight, mammalian gait transitions.

## Active Inference Integration

- **Sensorimotor loops**: Frame action as part of the continuous perception-action cycle where the robot generates predictions, computes prediction errors, and updates beliefs or actions to minimize free energy.
- **Proprioceptive inference**: Connect action to the robot's self-model -- its understanding of its own body, capabilities, and limitations as maintained through proprioceptive prediction errors.
- **Motor commands as predictions**: Relate action to the Active Inference principle that motor commands are predictions about desired sensory outcomes, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
