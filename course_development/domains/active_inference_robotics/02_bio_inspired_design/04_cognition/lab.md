# Lab: Neural-Inspired World Models for Robots

## Objective

Design robotic cognitive architectures inspired by biological neural systems. You will compare hippocampal spatial representations with SLAM algorithms, analyze how the brain builds and updates world models, and design a neural-inspired cognitive architecture for a mobile robot.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Hippocampal Navigation Models

The hippocampus supports spatial navigation through place cells, grid cells, and head direction cells. Design a robotic equivalent:

1. How do place cells (firing at specific locations) map to a robotic localization system?
2. How do grid cells (periodic spatial firing patterns) map to metric position encoding?
3. How do head direction cells map to compass/heading estimation?
4. How does hippocampal replay (replaying past trajectories during rest) relate to planning in Active Inference?

{fill:textarea}

## Part 2: Cortical Hierarchy for Object Recognition

Design a hierarchical object recognition system inspired by the ventral visual stream (V1 -> V2 -> V4 -> IT cortex):

1. Specify what each level represents (edges, textures, parts, whole objects).
2. Define top-down generative predictions at each level.
3. Define bottom-up prediction errors at each level.
4. How does this compare to a standard convolutional neural network? What are the key differences from an Active Inference perspective?

{fill:textarea}

## Part 3: Memory Systems for Robots

Biological cognition relies on multiple memory systems. Design robotic equivalents:

1. **Working memory** (prefrontal cortex): short-term task state, current goals.
2. **Episodic memory** (hippocampus): specific past experiences and locations.
3. **Semantic memory** (temporal cortex): general knowledge about objects and categories.
4. **Procedural memory** (basal ganglia, cerebellum): learned motor skills.

How do these memory systems interact in a hierarchical generative model?

{fill:textarea}

## Part 4: Cognitive Architecture Comparison

Compare three cognitive architectures:

| Feature | Brain-Inspired | Classical AI (SLAM + planner) | Active Inference |
| --- | --- | --- | --- |
| Spatial representation | {fill} | {fill} | {fill} |
| Memory organization | {fill} | {fill} | {fill} |
| Learning mechanism | {fill} | {fill} | {fill} |
| Planning strategy | {fill} | {fill} | {fill} |

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
