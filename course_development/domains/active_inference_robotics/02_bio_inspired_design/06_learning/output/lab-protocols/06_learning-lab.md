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


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Developmental Learning

Design a developmental learning curriculum for a robot arm inspired by infant motor development:

1. **Stage 1** (random babbling): Uncoordinated movements that build a body model.
2. **Stage 2** (reaching): Directed reaching toward visually detected objects.
3. **Stage 3** (grasping): Coordinated hand shaping based on object properties.
4. **Stage 4** (tool use): Using grasped objects to interact with the environment.

For each stage, what is learned (model parameters, structure, or both)? How does free energy decrease across stages?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Reward, Curiosity, and Intrinsic Motivation

Analyze biological motivation systems for robotic learning:

1. How does dopaminergic reward prediction error relate to Active Inference expected free energy?
2. Design a curiosity-driven exploration system where the robot seeks novel situations (high epistemic value).
3. How does the brain balance exploitation (familiar, rewarding actions) with exploration (novel, uncertain actions)? Design the robotic equivalent.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Learning System Comparison

Compare biological and artificial learning mechanisms:

| Feature | Hebbian Learning | Backpropagation | Active Inference Learning |
| --- | --- | --- | --- |
| Locality | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Supervision required | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Biological plausibility | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Online capability | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Energy efficiency | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |


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
