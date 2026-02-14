# Lab: Control System Architectures

## Objective

Analyze robotic control system architectures through state-space representations and system identification. You will model a robotic system in state-space form, perform system identification experiments, and compare open-loop and closed-loop architectures from an Active Inference perspective.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Mathematical Formulation

Formulate the systems problem mathematically:

1. Define the state-space representation relevant to this module.
2. Specify the cost function or objective for classical approaches.
3. Specify the free energy functional for the Active Inference formulation.
4. Under what assumptions do these formulations yield equivalent solutions?

{fill:textarea}

## Part 2: Algorithm Implementation

Design the algorithm in pseudocode:

1. Write the classical systems algorithm step-by-step.
2. Write the Active Inference equivalent step-by-step.
3. Identify shared computational steps (e.g., matrix inversions, prediction steps).
4. Where do the algorithms diverge? What does Active Inference add?

{fill:textarea}

## Part 3: Robotic Application

Apply both algorithms to a concrete robotic scenario:

1. Define a specific robot (e.g., 2-DOF arm, mobile robot, quadrotor).
2. Specify numerical parameters (masses, inertias, sensor noise).
3. Trace through 5 timesteps of each algorithm.
4. Compare the resulting state estimates, control actions, or plans.

{fill:textarea}

## Part 4: Performance Comparison

Compare the approaches systematically:

| Metric | Classical Approach | Active Inference Approach |
| --- | --- | --- |
| Computational cost | {fill} | {fill} |
| Robustness to noise | {fill} | {fill} |
| Adaptability | {fill} | {fill} |
| Theoretical guarantees | {fill} | {fill} |
| Ease of tuning | {fill} | {fill} |

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
