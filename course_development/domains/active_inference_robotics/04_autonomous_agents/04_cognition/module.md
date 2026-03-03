# Module 04: Cognition in Robotics — Autonomous Reasoning

## Learning Objectives

1. Define **autonomous cognition** as the capacity of a robot to reason about its situation, assess its own competence, and make strategic decisions without human guidance.
2. Analyze how **situation assessment, meta-cognition, and goal management** implement higher-order Active Inference in autonomous systems.
3. Apply cognitive architectures to explain how autonomous robots handle novel situations.

## Introduction

Autonomous cognition goes beyond state estimation (where am I?) to include situation assessment (what is happening?), self-assessment (am I capable of handling this?), and strategic reasoning (what should I prioritize?). This is the "thinking" that distinguishes a truly autonomous agent from a mere reactive system.

## Key Concepts

### 1. Situation Assessment

**Situation assessment** constructs a high-level interpretation of the environment:

- **Scene classification**: Is this a normal operating environment, a hazardous zone, or an emergency?
- **Event detection**: Has something significant happened (object collision, human fall, door opening)?
- **Temporal reasoning**: How has the situation evolved over time? Is it getting better or worse?

In Active Inference terms, situation assessment is inference at a **high level of the generative model hierarchy** — abstracting from low-level percepts to categorical state descriptions that support strategic decision-making.

### 2. Meta-Cognition: Monitoring One's Own Model

Autonomous agents need **meta-cognition** — the ability to assess the reliability of their own inference:

- **Confidence monitoring**: How certain am I about the current state estimate? If confidence drops below a threshold, the agent should switch to more conservative behavior.
- **Novelty detection**: Is the current situation similar to anything in the training data? If not, the generative model may be unreliable and the agent should seek information or request help.
- **Competence assessment**: Can I achieve this goal with my current capabilities? If the EFE for all available policies exceeds a threshold, the task may be beyond the agent's competence.

Meta-cognition is Active Inference about Active Inference — a higher-order generative model that predicts the reliability of the lower-order model.

### 3. Goal Management and Priority

Autonomous agents typically have multiple concurrent goals that require prioritization:

- **Safety goals** (don't collide, don't damage, don't harm) always take highest priority
- **Task goals** (deliver packages, assemble widgets, patrol area) are the agent's primary mission
- **Maintenance goals** (recharge battery, calibrate sensors, update map) ensure continued operability
- **Social goals** (don't block hallways, don't startle people, communicate status) enable coexistence

Goal management requires a **priority architecture** where higher-priority goals can preempt lower-priority actions — precisely the hierarchical policy selection of Active Inference.

### 4. Anomaly Detection and Explanation

When something unexpected happens, autonomous agents should both detect the anomaly and generate an explanation:

- **Detection**: A spike in prediction error across multiple channels simultaneously signals an anomaly — something the generative model did not predict
- **Classification**: Is this anomaly dangerous (obstacle in path), benign (new decoration in office), or informative (clue about environmental change)?
- **Explanation generation**: For human-supervised systems, the robot should communicate *why* it detected an anomaly — providing interpretable reasoning that enables human oversight

## Applications

- **Hospital delivery robot**: An autonomous hospital robot uses situation assessment to navigate complex social environments — classifying hallway traffic as "normal flow," "emergency rush," or "patient transport" and adjusting its behavior accordingly. Meta-cognition monitors localization confidence, triggering map recalibration when the hospital reconfigures.
- **Inspection drone with anomaly reporting**: A drone inspecting infrastructure detects anomalies (cracks, corrosion, deformation) through prediction error on its structural model, classifies severity, and generates explanatory reports with annotated images for human engineers.

## Conclusion

Autonomous cognition — situation assessment, meta-cognition, goal management, and anomaly detection — implements higher-order Active Inference that enables strategic, self-aware robotic behavior. The next module examines autonomous action.
