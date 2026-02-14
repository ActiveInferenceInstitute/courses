# Module 04: Cognition — Partially Observable Markov Decision Processes

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Define the **POMDP** (Partially Observable Markov Decision Process) as the mathematical framework for decision-making under uncertainty.
2. Identify the five components of a POMDP: **A** (observation), **B** (transition), **C** (preferences), **D** (initial state), and **policies π**.
3. Explain how cognition involves jointly inferring hidden states and selecting actions.

## Introduction

The brain doesn't just perceive — it also decides and acts. To formalize this, we need a framework that handles both uncertainty (partial observability) and decision-making. This is the POMDP.

## Key Concepts

### 1. From HMMs to POMDPs

An HMM (Module 01) models passive observation. A **POMDP** adds agency — the ability to choose actions that change the world:

**HMM**: P(o₁:T, s₁:T) — states evolve on their own
**POMDP**: P(o₁:T, s₁:T | π) — states evolve depending on the agent's policy π

### 2. The Five Components of a POMDP

Active Inference uses five matrices/vectors (the "A, B, C, D" formulation):

| Symbol | Name | What It Encodes | Size |
|--------|------|----------------|------|
| **A** | Observation model | P(o \| s) — how states generate observations | observations × states |
| **B** | Transition model | P(s_t \| s_{t-1}, a) — how actions change states | states × states × actions |
| **C** | Preference vector | log P(o) — which observations the agent prefers | observations × 1 |
| **D** | Initial state prior | P(s₁) — beliefs about the initial state | states × 1 |
| **π** | Policies | Sequences of actions to evaluate | time × policies |

### 3. The A Matrix — Observation Model

The **A matrix** maps hidden states to observations:

**Example** (simple weather):

```
         sunny   rainy
umbrella [ 0.1    0.9 ]
no_umb   [ 0.9    0.1 ]
```

This says: if it's sunny, 90% chance of no umbrella; if it's rainy, 90% chance of umbrella. Each column sums to 1.

### 4. The B Matrix — Transition Model

The **B matrix** determines how states change under each action:

**Example** (thermostat with actions: heat, cool, nothing):

```
B[:,:,heat] =   cold  warm  hot        B[:,:,cool] =   cold  warm  hot
         cold  [0.0   0.0   0.0]                cold  [0.7   0.6   0.1]
         warm  [0.8   0.5   0.2]                warm  [0.3   0.3   0.3]
         hot   [0.2   0.5   0.8]                hot   [0.0   0.1   0.6]
```

### 5. The C Vector — Preferences

The **C vector** encodes which observations the agent prefers (what it values):

**Example**: C = [preferred temperature = warm]

```
C = [cold: -2, warm: +2, hot: -1]
```

Positive values = preferred observations. Negative = avoided. This replaces the reward function in traditional decision-making.

### 6. Putting It Together — Belief Updating

At each time step t:

1. **Observe** o_t
2. **Update beliefs**: q(s_t) ∝ A(o_t, :) × B(:, :, a_{t-1}) × q(s_{t-1})
3. **Evaluate policies**: Score each policy π based on Expected Free Energy (Module 05)
4. **Select action**: Choose the best policy and execute its next action
5. **Repeat**

This is the perception-action loop formalized mathematically.

## Summary

The POMDP provides the complete mathematical framework for Active Inference agents. Five components (A, B, C, D, π) specify everything the agent needs: how observations are generated, how actions change states, what's preferred, and what's believed initially. Cognition is the joint process of updating beliefs and evaluating policies.

## Further Reading

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press. (Chapter 5)
- Smith, R. et al. (2022). A step-by-step tutorial on active inference. *Journal of Mathematical Psychology*, 107, 102632.
- Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101, 99-134.
