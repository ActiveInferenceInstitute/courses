# Module 04: Cognition — Deep Temporal Models and Hierarchical Inference

> **Course**: Active Inference 401 | **Unit**: Advanced Theory | **Audience**: Graduate students / researchers

## Learning Objectives

1. Analyze **deep temporal models** — hierarchical generative models with multiple temporal scales.
2. Evaluate the mathematical structure of **hierarchical message passing** — ascending and descending messages across levels.
3. Examine the role of **temporal depth** in planning, imagination, and counterfactual reasoning.

## Key Concepts

### 1. The Problem of Temporal Depth

Simple generative models update beliefs moment-by-moment. But intelligent behavior requires modeling the past and future over long horizons:

**Temporal abstraction**: The world operates at multiple timescales simultaneously — from millisecond neural events to decadal life plans. A flat model treating all time points equally is computationally intractable. Deep temporal models address this through hierarchy.

**The key architecture**: A deep temporal model has L levels, each operating at a progressively slower timescale:

- Level 1: Fast dynamics (sensory fluctuations, milliseconds)
- Level 2: Medium dynamics (events, seconds to minutes)
- Level 3: Slow dynamics (contexts, hours to days)
- Level L: Slowest dynamics (life narratives, years)

Each level generates predictions about the level below, and receives prediction errors from it.

### 2. Hierarchical Generative Model Structure

The mathematical structure of a deep temporal model:

**State at level l, time t**: s_t^(l)

**Transition model**: s_{t+1}^(l) ~ p(s_{t+1}^(l) | s_t^(l), s_t^(l+1))

States at level l transition based on their own dynamics AND the contextual influence of the level above.

**Observation model**: Only the lowest level generates observations:

o_t ~ p(o_t | s_t^(1))

**Key property**: Higher levels evolve more slowly because they represent more abstract, temporally stable features. The "clock speed" decreases with level — higher levels change less frequently.

### 3. Hierarchical Message Passing

Inference in deep temporal models involves message passing between levels:

**Ascending messages** (bottom-up): Prediction errors from level l to level l+1. These carry information about what the lower level's predictions got wrong, compressed into summary statistics that inform the higher level's context estimation.

**Descending messages** (top-down): Predictions from level l+1 to level l. These carry the higher level's expectations about what should be happening at the lower level, constraining lower-level inference.

**Update equations**: At each level l, the belief update integrates:

- Prediction error from below (ascending): ε^(l-1) = o - g(s^(l)) or s^(l-1) - f(s^(l))
- Contextual prior from above (descending): p(s^(l) | s^(l+1))
- Lateral dynamics: p(s_t^(l) | s_{t-1}^(l))

The precision weighting determines how much weight each message receives.

### 4. Planning as Inference in Deep Temporal Models

Planning in Active Inference is formalized as inference about future actions (policies). Deep temporal models extend this:

**Multi-scale planning**:

- Level 1: "Should I move my hand left or right" (motor-level policy)
- Level 2: "Should I reach for the cup or the phone" (action-level policy)
- Level 3: "Should I have coffee or tea" (goal-level policy)
- Level L: "Should I pursue career A or career B" (life-level policy)

Higher-level policies constrain lower-level policies through descending messages.

**Expected free energy at multiple scales**: Each level evaluates its own expected free energy:

G^(l)(π) = E_q[ln q(s^(l)_τ | π) - ln p(o_τ, s^(l)_τ | π)]

Higher levels consider outcomes over longer horizons, using more abstract representations.

### 5. Imagination and Counterfactual Reasoning

Deep temporal models enable imagination — the generative model can be "run forward" without sensory input:

**Generative replay**: The model generates predicted future trajectories by sampling from the transition model at each level. This is mental simulation — evaluating what would happen under different policies.

**Counterfactual reasoning**: By "clamping" different policy choices and running the model forward, the agent can evaluate what *would* happen if it did X vs. Y. This corresponds to the expected free energy calculation — comparing G(π₁) vs. G(π₂).

**Dreaming and creativity**: During sleep or rest, the model can be run in "generative mode" without constraining observations. This produces novel combinations of states — the basis for creativity and insight.

## Summary

Deep temporal models address the challenge of multi-scale temporal inference through hierarchical generative models with ascending (bottom-up prediction error) and descending (top-down prediction) messages. Planning at multiple scales is implemented as inference about nested policies. Imagination and counterfactual reasoning emerge from running the generative model forward without sensory constraint.

## Further Reading

- Friston, K. et al. (2017). Deep temporal models and active inference. *Neuroscience & Biobehavioral Reviews*, 77, 388-402.
- Hesp, C. et al. (2021). Deeply felt affect. *Psychological Review*, 128(4), 723-760.
- Parr, T. & Friston, K. (2018). The anatomy of inference: Generative models and brain structure. *Frontiers in Computational Neuroscience*, 12, 90.
