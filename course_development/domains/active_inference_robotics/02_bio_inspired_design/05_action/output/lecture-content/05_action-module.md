# Module 05: Action in Robotics — Bio-Inspired Motor Control

## Learning Objectives

1. Explain how **biological motor control** (Central Pattern Generators, motor synergies, impedance modulation) inspires Active Inference robot control.
2. Analyze motor control as **proprioceptive prediction fulfillment** — the robot acts by predicting the sensory consequences of intended movements and driving its actuators to make those predictions true.
3. Apply bio-inspired motor strategies to achieve **compliant, adaptive manipulation** and locomotion.

## Introduction

Biological motor control is not a command-and-execute pipeline — it is an inference process. When you reach for a coffee cup, your motor cortex generates a prediction of the proprioceptive trajectory your arm should follow. Spinal motor neurons then drive the muscles to fulfill that prediction. If an unexpected perturbation occurs (someone bumps your arm), the prediction error drives an immediate corrective response without waiting for cortical deliberation.

Bio-inspired robotic motor control replicates this architecture: the robot generates proprioceptive predictions and acts to fulfill them, achieving the compliance and adaptiveness that distinguish biological movement from rigid industrial automation.

## Key Concepts

### 1. Active Inference Motor Control

In the Active Inference framework, action arises from **proprioceptive prediction error minimization**:

- The generative model generates a **desired proprioceptive trajectory** (expected joint angles, forces, velocities over time)
- Spinal-level reflexes (or their robotic analog: low-level controllers) minimize the discrepancy between predicted and actual proprioception
- The result is movement that fulfills the prediction — the robot doesn't send explicit motor commands; it sends *desired sensory states* and lets the local controller figure out how to achieve them

This architecture naturally handles unexpected perturbations: if an external force deflects the robot's limb, the proprioceptive prediction error increases, and the local controller automatically corrects.

### 2. Central Pattern Generators (CPGs)

Biological locomotion is driven by **Central Pattern Generators** — neural circuits in the spinal cord that produce rhythmic motor patterns without requiring continuous cortical input. CPG-inspired robot controllers:

- Generate rhythmic limb movements for walking, swimming, or flying through oscillator networks
- Modulate gait parameters (frequency, amplitude, phase relationships) through top-down precision signals from the generative model
- Achieve robust locomotion over uneven terrain because the CPG handles the rhythmic pattern while the Active Inference controller handles the adaptation

Ijspeert's salamander robot demonstrates CPG-based locomotion that transitions smoothly between walking and swimming by modulating oscillator parameters — a bio-inspired gait selection driven by environmental inference.

### 3. Motor Synergies and Dimensionality Reduction

Biological systems don't control each muscle independently — they use **motor synergies** (coordinated muscle groups) that reduce the dimensionality of the control problem. For robots:

- A robotic hand with 20 degrees of freedom might defined 5-6 grasp synergies (power grasp, precision pinch, lateral pinch, etc.)
- The Active Inference controller selects among synergies rather than specifying each joint angle
- This dramatically reduces the policy space, making EFE computation tractable for high-DOF systems

### 4. Impedance Control as Precision Modulation

Biological limbs modulate their **impedance** (the ratio of force to displacement) depending on the task — stiff when holding a heavy object, compliant when exploring a fragile surface. In Active Inference:

- **High precision on proprioceptive predictions** → stiff behavior (joints resist perturbation, trajectory is followed precisely)
- **Low precision on proprioceptive predictions** → compliant behavior (joints yield to external forces, the robot adapts to contact)
- Impedance control is precision modulation on the motor prediction error

## Applications

- **Compliant humanoid grasping**: A humanoid robot grasps a raw egg by setting low proprioceptive precision (compliant grip that conforms to the egg shape) and high tactile precision (sensitive to slip detection). Active Inference automatically balances grip force and fragility.
- **Legged robot on rough terrain**: A quadruped robot uses CPG-based locomotion with Active Inference adaptation — the CPG generates the basic gait pattern while the generative model modulates stride length, ground clearance, and body posture prediction to navigate rocks, slopes, and gaps.

## Conclusion

Bio-inspired motor control is Active Inference in the actuator domain: proprioceptive prediction fulfillment, CPG rhythm generation, synergy-based dimensionality reduction, and impedance as precision. The next module explores how bio-inspired learning enables these motor systems to improve with experience.
