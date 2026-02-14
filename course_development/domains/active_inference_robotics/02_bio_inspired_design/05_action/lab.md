# Lab: Bio-Inspired Motor Control Systems

## Objective

Design bio-inspired motor control systems by analyzing biological locomotion, central pattern generators (CPGs), and the spinal reflex arc. You will compare biological motor control with robotic control, design a CPG-based locomotion controller, and analyze how Active Inference unifies these biological mechanisms.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Spinal Reflex Arc as Active Inference

Analyze the biological spinal reflex arc as an Active Inference control mechanism:

1. Map the components: muscle spindles (sensors), alpha motor neurons (actuators), spinal interneurons (internal model).
2. How does the gamma motor neuron system set proprioceptive predictions (prior preferences)?
3. How does the stretch reflex implement prediction error minimization?
4. Design a robotic joint controller that mimics this architecture.

{fill:textarea}

## Part 2: Central Pattern Generator Design

Design a CPG-based locomotion controller for a quadruped robot:

1. Define oscillator dynamics for each leg (amplitude, frequency, phase offset).
2. Specify inter-leg coupling to produce walk, trot, and gallop gaits.
3. How does sensory feedback modulate CPG parameters for terrain adaptation?
4. How does the Active Inference framework explain CPG behavior as prediction fulfillment?

{fill:textarea}

## Part 3: Biological vs. Robotic Locomotion

Compare locomotion strategies across biological and robotic systems:

| Feature | Cockroach | Horse | Boston Dynamics Spot | CPG-AI Robot |
| --- | --- | --- | --- | --- |
| Gait patterns | {fill} | {fill} | {fill} | {fill} |
| Terrain adaptation | {fill} | {fill} | {fill} | {fill} |
| Energy efficiency | {fill} | {fill} | {fill} | {fill} |
| Reflex speed | {fill} | {fill} | {fill} | {fill} |
| Learning ability | {fill} | {fill} | {fill} | {fill} |

{fill:textarea}

## Part 4: Reaching and Grasping

Analyze biological reaching and grasping as Active Inference:

1. How does the brain plan a reaching movement (motor cortex -> spinal cord -> muscles)?
2. What role do forward models (cerebellum) play in predicting movement outcomes?
3. How does efference copy (corollary discharge) implement the generative model's prediction of self-generated sensory changes?
4. Design a bio-inspired reaching controller for a robot arm that uses forward models and prediction errors.

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
