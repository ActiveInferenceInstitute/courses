# Lab: Robotics and Embodied Active Inference

> **Learning Goal:** Design and analyze Active Inference implementations for robotic systems.

## Part 1: Discrete POMDP Design (pymdp)

**Exercise**: Design a discrete Active Inference agent for a simple grid navigation task:

**Environment**: 4×4 grid, agent starts at (0,0), goal at (3,3), obstacle at (2,2).

**State space**: 16 grid positions (4×4)
**Observation space**: Visual observation of current position (with 10% noise)
**Action space**: {up, down, left, right, stay}

**POMDP specification**:

| Matrix | Dimensions | Description |
|--------|-----------|-------------|
| A (observation) | 16 × 16 | Noisy identity (0.9 on diagonal, 0.1/15 elsewhere) |
| B (transition) | 16 × 16 × 5 | Deterministic grid transitions per action |
| C (preferences) | 16 × 1 | High value at (3,3), negative at (2,2), zero elsewhere |
| D (prior on start) | 16 × 1 | Peaked at (0,0) |

Write the expected free energy G(π) for a policy π = [right, right, down, down, down, right]:

- Pragmatic: Does it reach the goal?
- Epistemic: Does it reduce uncertainty about position?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Continuous Control Design

> **Learning Goal:** Design a continuous Active Inference controller.

**Exercise**: Design a controller for a robotic arm reaching task:

**Generative model**:

- States: joint angles θ = (θ₁, θ₂) and velocities θ̇ = (θ̇₁, θ̇₂)
- Observations: end-effector position (x, y) via forward kinematics
- Desired state: end-effector at target position (x*, y*)

**Free energy**: F = ½ ε_s^T Π_s ε_s + ½ ε_p^T Π_p ε_p

Where:

- ε_s = sensory PE (observed position - predicted position)
- ε_p = prior PE (current position - desired position)
- Π_s, Π_p = precision matrices

**Action generation**: a = -∂F/∂a — motor commands are the gradient of free energy with respect to action

Design the precision parameters Π_s and Π_p for:

1. Normal reaching (balanced vision and proprioception)
2. Vision occluded (low Π_s, rely on proprioception)
3. Novel environment (low Π_p, exploratory behavior)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Framework Comparison

> **Learning Goal:** Compare Active Inference software tools.

**Exercise**: Complete this comparison for implementing a T-maze navigation task:

| Feature | pymdp (Python) | SPM (MATLAB) | RxInfer.jl (Julia) |
|---------|---------------|-------------|-------------------|
| State space | Discrete (POMDP) | Discrete (POMDP) + continuous (DCM) | Discrete + continuous |
| Inference method | Variational message passing | Variational Bayes | Reactive message passing |
| Speed | Moderate | Slower (MATLAB overhead) | Fast (Julia compilation) |
| Scalability | Small-medium state spaces | Small state spaces | Scales to larger models |
| Real-time capability | No (not designed for it) | No | Yes (reactive, streaming) |
| Hierarchical models | Manual construction | Built-in deep temporal | Factor graph composition |
| Community | Growing, open-source | Established, neuroimaging | Growing, probabilistic programming |
| Best for | Prototyping, education | Neuroimaging analysis | Real-time robotics, production |

Which tool would you choose for: (a) a classroom demo? (b) an fMRI study? (c) a real-time robot controller?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Human-Robot Interaction Design

> **Learning Goal:** Design an HRI experiment using multi-agent Active Inference.

**Exercise**: Design a collaborative object sorting task:

1. **Robot's generative model of human**: Models human's preferences (C_human), attention (precision), and action tendencies
2. **Shared task model**: Both agents have models of the sorting rules and object locations
3. **Communication**: Robot infers human's sorting intent from observed actions; adjusts its behavior to complement (not duplicate) human actions
4. **Active Inference prediction**: Robot should anticipate human's next action and prepare complementary action

Describe: What observations does the robot use to model the human? How does it update its model in real-time? What does coordination look like when it succeeds vs. fails?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 300 words, reflect: Active Inference robotics promises a unified perception-action framework, but current implementations are far from human-level dexterity. What are the main bottlenecks? Is the mathematical framework sound but the engineering immature? Or are there fundamental limitations to the approach?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | POMDP design | Discrete Active Inference |
| 2 | Controller design | Continuous generalized coordinates |
| 3 | Tool evaluation | Software framework comparison |
| 4 | Multi-agent robotics | Human-robot interaction |
| 5 | Critical evaluation | Approach limitations |
