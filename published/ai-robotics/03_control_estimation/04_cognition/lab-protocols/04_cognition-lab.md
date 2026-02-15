# Lab: System Identification and Model Learning

## Objective

Perform system identification experiments to learn a robot's dynamics model. You will compare offline identification methods (least squares) with online recursive methods and show how Active Inference naturally incorporates system identification as part of its generative model learning.

## Prerequisites

- Completion of the corresponding module.md lecture material
- Familiarity with Active Inference concepts (generative models, free energy, prediction errors)
- Basic pseudocode and diagram skills

## Part 1: Mathematical Formulation

Formulate the cognition problem mathematically:

1. Define the state-space representation relevant to this module.
2. Specify the cost function or objective for classical approaches.
3. Specify the free energy functional for the Active Inference formulation.
4. Under what assumptions do these formulations yield equivalent solutions?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Algorithm Implementation

Design the algorithm in pseudocode:

1. Write the classical cognition algorithm step-by-step.
2. Write the Active Inference equivalent step-by-step.
3. Identify shared computational steps (e.g., matrix inversions, prediction steps).
4. Where do the algorithms diverge? What does Active Inference add?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Robotic Application

Apply both algorithms to a concrete robotic scenario:

1. Define a specific robot (e.g., 2-DOF arm, mobile robot, quadrotor).
2. Specify numerical parameters (masses, inertias, sensor noise).
3. Trace through 5 timesteps of each algorithm.
4. Compare the resulting state estimates, control actions, or plans.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Performance Comparison

Compare the approaches systematically:

| Metric | Classical Approach | Active Inference Approach |
| --- | --- | --- |
| Computational cost | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Robustness to noise | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Adaptability | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Theoretical guarantees | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Ease of tuning | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary Table

| Concept | Classical Robotics | Active Inference | Your Design |
| --- | --- | --- | --- |
| Core mechanism | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Uncertainty handling | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Adaptation | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Key advantage | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- Pio-Lopez, L., Nizard, A., Friston, K., & Pezzulo, G. (2016). Active Inference and robot control. *Journal of the Royal Society Interface*, 13(122).
