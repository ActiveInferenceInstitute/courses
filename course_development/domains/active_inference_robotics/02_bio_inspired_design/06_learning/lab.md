# Lab: Hebbian Learning and Synaptic Plasticity for Robots

## Objective

Design robotic learning systems inspired by biological synaptic plasticity. You will compare Hebbian learning rules with backpropagation, analyze biological developmental learning, and design a learning architecture inspired by the brain's multiple learning systems.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Hebbian Learning for Sensor Calibration

Design a Hebbian learning rule for a robot that must calibrate its sensors from experience:

1. The robot has a camera and a LIDAR. Hebbian learning strengthens the association between co-occurring visual and range measurements.
2. Write the update rule: w_ij += eta * x_i * x_j (correlation-based learning).
3. How does this compare to supervised calibration? What are the advantages of unsupervised Hebbian learning?
4. How does this relate to free energy minimization? (Hint: Hebbian learning minimizes prediction errors between modalities.)

{fill:textarea}

## Part 2: Developmental Learning

Design a developmental learning curriculum for a robot arm inspired by infant motor development:

1. **Stage 1** (random babbling): Uncoordinated movements that build a body model.
2. **Stage 2** (reaching): Directed reaching toward visually detected objects.
3. **Stage 3** (grasping): Coordinated hand shaping based on object properties.
4. **Stage 4** (tool use): Using grasped objects to interact with the environment.

For each stage, what is learned (model parameters, structure, or both)? How does free energy decrease across stages?

{fill:textarea}

## Part 3: Reward, Curiosity, and Intrinsic Motivation

Analyze biological motivation systems for robotic learning:

1. How does dopaminergic reward prediction error relate to Active Inference expected free energy?
2. Design a curiosity-driven exploration system where the robot seeks novel situations (high epistemic value).
3. How does the brain balance exploitation (familiar, rewarding actions) with exploration (novel, uncertain actions)? Design the robotic equivalent.

{fill:textarea}

## Part 4: Learning System Comparison

Compare biological and artificial learning mechanisms:

| Feature | Hebbian Learning | Backpropagation | Active Inference Learning |
| --- | --- | --- | --- |
| Locality | {fill} | {fill} | {fill} |
| Supervision required | {fill} | {fill} | {fill} |
| Biological plausibility | {fill} | {fill} | {fill} |
| Online capability | {fill} | {fill} | {fill} |
| Energy efficiency | {fill} | {fill} | {fill} |

{fill:textarea}

## Summary Table

| Concept | Classical Robotics | Active Inference | Your Design |
| --- | --- | --- | --- |
| Core mechanism | {fill} | {fill} | {fill} |
| Uncertainty handling | {fill} | {fill} | {fill} |
| Adaptation | {fill} | {fill} | {fill} |
| Key advantage | {fill} | {fill} | {fill} |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- Pio-Lopez, L., Nizard, A., Friston, K., & Pezzulo, G. (2016). Active Inference and robot control. *Journal of the Royal Society Interface*, 13(122).
