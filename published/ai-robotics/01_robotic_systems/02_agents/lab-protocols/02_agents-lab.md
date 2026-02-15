# Lab: Defining Robotic Agents as Active Inference Systems

## Objective

Design and analyze a robotic agent by specifying its generative model, belief states, and action repertoire. You will compare how classical control agents and Active Inference agents differ in their architecture, and explore how morphological computation and embodiment shape agency.

## Prerequisites

- Understanding of what constitutes an agent (autonomy, goal-directedness, environmental coupling)
- Familiarity with the Markov blanket formalism from Module 01
- Basic understanding of Bayesian inference

## Part 1: Agent Specification

Consider a warehouse robot that must navigate to pick-up locations, grasp objects, and deliver them to packing stations.

1. Define the agent's **generative model** by specifying:
   - Hidden states: robot pose (x, y, theta), gripper state (open/closed), object location, target station
   - Observations: LIDAR scans, camera images, force-torque readings at the gripper, wheel encoder counts
   - Actions: wheel velocities (v_left, v_right), gripper open/close command

2. What distinguishes this robot as an *agent* rather than merely a *system*? Identify at least three properties that confer agency.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Classical vs. Active Inference Agent Architecture

Compare two designs for the warehouse robot:

| Feature | Classical Agent | Active Inference Agent |
| --- | --- | --- |
| State estimation | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Goal representation | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Action selection | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Error handling | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Adaptation mechanism | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |

For the classical agent, assume a finite state machine with PID controllers. For the Active Inference agent, describe how beliefs, preferences (prior preferences over observations), and expected free energy drive behavior.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Morphological Computation Analysis

Analyze how the robot's physical body contributes to its cognitive processing:

1. A compliant gripper passively conforms to object shapes without explicit shape modeling. How does this reduce the complexity of the generative model?
2. A round-bodied robot deflects off obstacles rather than requiring collision avoidance planning. What generative model states are eliminated?
3. Identify one additional example of morphological computation in robotics and describe its free energy implications.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Belief Dynamics Trace

Trace the agent's belief updates through a scenario where it approaches a shelf but finds the expected object missing:

1. **Prior belief**: Object is at location (3.2, 1.5) on shelf B with high confidence.
2. **Observation**: Camera detects empty shelf at that location.
3. **Prediction error**: Describe the qualitative prediction error (expected vs. observed).
4. **Belief update**: How does the agent revise its beliefs? What happens to uncertainty?
5. **Action consequence**: What action does the agent select to resolve the remaining surprise?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Autonomy Spectrum

Place different robotic systems on an autonomy spectrum based on their Active Inference properties:

| Robot System | Generative Model Depth | Temporal Horizon | Adaptability | Agency Level |
| --- | --- | --- | --- | --- |
| Thermostat | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Roomba vacuum | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Warehouse pick robot | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Surgical robot (da Vinci) | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Self-driving car | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |

## Summary Table

| Agent Property | Formal Definition | Warehouse Robot Implementation |
| --- | --- | --- |
| Autonomy | Self-evidencing via free energy minimization | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Goal-directedness | Prior preferences over observations | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Adaptability | Model parameter updating | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Embodiment | Physical Markov blanket | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Friston, K. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86).
- Pfeifer, R. & Bongard, J. (2006). *How the Body Shapes the Way We Think*. MIT Press.
