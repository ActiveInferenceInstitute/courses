# Unit 04: Autonomous Agents — Overview

## Learning Objectives

1. Define **autonomous agency** as the capacity of a robotic system to perform sustained, goal-directed behavior without human intervention across the full Active Inference loop.
2. Analyze the **key challenges** of autonomous operation: perception in open environments, decision-making under deep uncertainty, long-horizon planning, and graceful degradation.
3. Apply the concept of **autonomy levels** to assess the maturity and reliability of autonomous robotic systems.

## Introduction

An autonomous agent is the most complete instantiation of Active Inference in robotics — a system that perceives, infers, plans, acts, learns, communicates, and recovers from errors entirely on its own. This unit brings together all the concepts from the previous three units (Robotic Systems, Bio-Inspired Design, Control & Estimation) and asks: what does it take to build a robot that can function independently in unstructured, dynamic, open-ended environments?

The answer involves solving every hard problem in robotics simultaneously: robust perception in adverse conditions, state estimation with incomplete models, decision-making under deep uncertainty, planning over long horizons with limited computation, learning from sparse experience, communicating with other autonomous agents (and humans), and knowing when to ask for help.

## Key Concepts

### 1. The Autonomy Stack

A fully autonomous robot implements a complete **autonomy stack**:

| Layer | Function | AIF Component | Timescale |
|---|---|---|---|
| Sensing | Data acquisition | A matrix input | μs-ms |
| Perception | Feature extraction, detection | State estimation | ms-s |
| World Model | Environment representation | Generative model | s-min |
| Planning | Route/task optimization | EFE evaluation | s-min |
| Decision | Goal selection, mode switching | Policy selection | s-min |
| Execution | Motion control | Action via prediction | ms |
| Monitoring | Health, safety checking | Meta-inference | continuous |

### 2. Open-World Challenge

Unlike controlled laboratory settings, the real world is **open** — the agent encounters situations, objects, and conditions that were not anticipated during design:

- A delivery robot encounters a street performer blocking the sidewalk (novel obstacle type)
- An agricultural robot encounters a crop disease it was not trained to recognize (out-of-distribution observation)
- A search-and-rescue robot encounters structural collapse that changes the environment topology (catastrophic model violation)

Active Inference handles open-world challenge through surprise detection — rising free energy signals model inadequacy, triggering conservative behavior, human assistance requests, or meta-cognitive model revision.

### 3. Long-Duration Autonomy

Sustained operation (hours, days, weeks) introduces challenges that short-duration autonomy doesn't face:

- **Model drift**: The environment changes over time (seasons, construction, furniture rearrangement) → the generative model must continuously update
- **Component degradation**: Sensors drift, batteries degrade, mechanisms wear → the agent must adapt its inference and control to changing hardware capabilities
- **Cumulative error**: Small estimation errors compound over long durations → drift correction and periodic recalibration are essential

### 4. Safety and Ethics

Autonomous agents operating among humans must address safety at the system level:

- **Fail-safe behavior**: When the agent detects unresolvable uncertainty, it should transition to a safe state (stop, retreat, signal) rather than act blindly
- **Predictability**: Humans interacting with autonomous robots need to predict the robot's behavior — erratic robots are unsafe even if individually rational
- **Accountability**: When an autonomous agent causes harm, the chain of responsibility (designer, operator, algorithm, training data) must be traceable

## Applications

- **Autonomous logistics fleet**: A fleet of delivery drones operating autonomously across a city implements the full autonomy stack — SLAM-based perception, learned traffic models, EFE-based route planning, adaptive control for wind compensation, and safety monitoring that triggers landing if any subsystem reports degraded confidence.
- **Deep-sea exploration robot**: An autonomous underwater vehicle exploring ocean trenches operates in the ultimate open-world environment — unknown terrain, no communication with the surface for hours, and environmental conditions (pressure, temperature, currents) that test every aspect of the autonomy stack.

## Conclusion

Autonomous agency integrates every Active Inference component into a self-governing whole. The challenges of open-world operation, long-duration reliability, and safe behavior define the frontier of robotic autonomy. This unit's 8 modules explore each component of the Active Inference spine in the autonomous agent context.
