# Module 02: Agents in Robotics — Autonomous Agent Architectures

## Learning Objectives

1. Define the **autonomous agent architecture** as the computational structure that implements the full Active Inference loop: perceive, infer, plan, act, learn.
2. Analyze the major agent architectures (reactive, deliberative, hybrid, behavior-based) and their Active Inference interpretations.
3. Apply architecture selection principles to real autonomous robot design decisions.

## Introduction

An autonomous agent architecture specifies *how* the perception-action loop is implemented in software and hardware. Different architectures make different trade-offs between reactivity (responding quickly to immediate sensory input) and deliberation (planning over extended time horizons). Active Inference provides a unified framework that explains why different architectural choices are appropriate for different operating conditions.

## Key Concepts

### 1. Reactive Architectures: Reflex Agents

**Reactive architectures** (Brooks' Subsumption Architecture) implement direct sensor-motor mappings without explicit world models:

- Simple behaviors (avoid obstacles, follow walls, track targets) are layered, with higher-priority behaviors suppressing lower-priority ones
- In Active Inference terms, reactive behaviors implement low-level prediction error minimization with very shallow generative models — the "prediction" is simply "maintain this sensor state," and the action is whatever achieves it
- **Strengths**: Fast response, robust to model error, computationally lightweight
- **Limitations**: Cannot plan ahead, cannot reason about novel situations, limited to behaviors that can be specified reactively

### 2. Deliberative Architectures: Model-Based Planning

**Deliberative architectures** maintain an explicit world model and plan by simulating future consequences:

- The agent constructs a state representation, generates candidate action sequences, evaluates them using the generative model, and selects the best
- In Active Inference terms, this is full Expected Free Energy minimization over a policy tree
- **Strengths**: Can handle novel situations, can optimize over long horizons, can reason about unseen states
- **Limitations**: Computationally expensive, slow to respond, sensitive to model errors ("the world changes while you're thinking")

### 3. Hybrid Architectures: The Three-Layer Model

Most real autonomous robots use **hybrid architectures** that combine reactive and deliberative elements:

- **Layer 1 (Reactive)**: Fast sensor-motor loops that handle immediate safety (collision avoidance, emergency stops). Timescale: milliseconds.
- **Layer 2 (Executive)**: Middle-level behaviors that sequence actions and manage mode transitions. Timescale: seconds.
- **Layer 3 (Deliberative)**: High-level planning, mission management, and complex reasoning. Timescale: minutes to hours.

In Active Inference terms, this is **hierarchical inference** at different temporal scales — fast, shallow inference at the bottom; slow, deep inference at the top. The hierarchy naturally handles the reactivity-deliberation trade-off.

### 4. Behavior-Based Architectures: Distributed Agency

**Behavior-based architectures** (Arkin) distribute agency across multiple concurrent behaviors:

- Each behavior is an Active Inference sub-agent with its own generative model, observations, and preferred outcomes
- Behaviors run concurrently and their outputs are combined (summed, voted, priority-selected)
- The overall agent behavior **emerges** from the interaction of sub-agent behaviors — no single behavior "plans" the global action

This parallels the multi-agent interpretation of Active Inference: an autonomous robot is itself a society of inference agents, each responsible for a different aspect of behavior.

## Applications

- **Self-driving car architecture**: A modern autonomous vehicle uses a hybrid architecture: reactive safety systems (automatic emergency braking, lane-keeping assist), executive behavior management (lane change sequencing, intersection protocols), and deliberative route planning (mission-level GPS navigation with traffic optimization).
- **Domestic service robot**: A home assistant robot uses behavior-based architecture — concurrent behaviors for obstacle avoidance, person following, object recognition, and task execution run simultaneously, with a priority arbitration system resolving conflicts between behaviors.

## Conclusion

Autonomous agent architectures implement the Active Inference loop at different levels of depth and reactivity. Reactive, deliberative, hybrid, and behavior-based architectures are complementary approaches, each suited to different aspects of autonomous operation. The next module examines perception in the autonomous agent context.
