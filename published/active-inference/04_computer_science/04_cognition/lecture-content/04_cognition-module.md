# Module 04: Cognition — Preferences, Priors, and Habits

## Learning Objectives

1. Construct and interpret the C-vector (log-preferences), D-vector (initial state prior), and E-vector (habit prior).
2. Analyze how precision γ modulates the balance between epistemic and pragmatic behavior.
3. Visualize preference, prior, and habit structures using the `active_inference` visualization functions.

## Introduction

Modules 01–03 covered the environment (generative process), the agent's model structure (A, B matrices), and perception (state inference). This module completes the agent's inner life by examining the three vectors that define its _cognitive stance_: what it wants (C), where it thinks it starts (D), and what it habitually does (E). These vectors don't just parameterize inference — they define the agent's character.

## Key Concepts

### 1. The C-Vector: Log-Preferences Over Observations

The C-vector encodes which observations the agent prefers on a log scale:

$$C[o] = \ln P_{\text{preferred}}(o)$$

```python
import numpy as np

# T-maze: strongly prefer reward, strongly avoid no-reward
C = np.array([0.0, 3.0, -3.0])  # [neutral, reward, no-reward]
```

C enters the Expected Free Energy (EFE) through the **risk** term:

$$\text{risk}(\pi) = D_{KL}[q(o \mid \pi) \| \tilde{P}(o)]$$

where $\tilde{P}(o) = \sigma(C)$ is the preferred observation distribution. When $C$ is all zeros, the risk term vanishes and the agent becomes purely epistemic.

**Visualizing C**:

```python
from active_inference.visualization import plot_C_preferences
plot_C_preferences(model, obs_labels=["neutral", "reward", "no-reward"])
```

This produces a bar chart of log-preferences with a softmax probability overlay.

### 2. The D-Vector: Prior Over Initial States

The D-vector is $P(s_0)$ — the agent's belief about which state it starts in:

```python
D = np.array([1.0, 0.0, 0.0, 0.0])  # certain: start at center
```

D serves as the initial prior for state inference. If D is uniform, the agent begins with maximum uncertainty. If D is peaked, the agent starts confident about its location.

**Visualizing D**:

```python
from active_inference.visualization import plot_D_prior
plot_D_prior(model, state_labels=["center", "left", "right", "cue"])
```

The plot annotates the entropy of D — $H(D) = 0$ means the agent is fully certain about its initial state.

### 3. The E-Vector: Habit Prior Over Policies

The optional E-vector encodes a prior over policies before EFE is considered:

$$q(\pi) = \sigma(-\gamma \cdot G(\pi) + \ln E(\pi))$$

```python
# Strong habit favoring policy 0 (stay)
E = np.array([0.8, 0.1, 0.1])
```

When γ is low, habits dominate — the agent acts according to E regardless of EFE. When γ is high, EFE dominates and habits have little effect. When E is `None`, a uniform habit prior is used.

**Visualizing E**:

```python
from active_inference.visualization import plot_E_habits
plot_E_habits(model, policy_labels=["stay", "go-left", "go-right"])
```

### 4. Precision γ: The Exploration–Exploitation Knob

The precision parameter γ controls how sharply the agent commits to the policy with lowest EFE:

| γ value | Behavior |
|---------|----------|
| γ → 0 | Random policy selection — exploration dominates (or habits dominate if E is set) |
| γ ≈ 1–4 | Balanced — considers both EFE and randomness |
| γ → ∞ | Greedy/exploitative — always picks the policy with lowest G |

**Precision sweep**:

```python
from active_inference.visualization import plot_precision_sweep
from active_inference.math import compute_efe, softmax

gamma_values = [0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
# Compute q(π) for each γ and visualize
plot_precision_sweep(gamma_values, q_pi_matrix,
                     policy_labels=["stay", "go-left", "go-right"])
```

### 5. Interaction Between C, D, E, and γ

These components interact in a principled way:

```
┌──────────────┐     ┌──────────────┐
│  D-vector    │────▶│  State       │
│  P(s₀)      │     │  Inference   │
└──────────────┘     └──────┬───────┘
                            │ q(s)
                            ▼
┌──────────────┐     ┌──────────────┐     ┌───────────┐
│  C-vector    │────▶│    EFE       │────▶│  Policy   │
│  ln P(o)     │     │  G(π)       │     │  q(π)     │
└──────────────┘     └──────────────┘     └─────┬─────┘
                            ▲                     │
┌──────────────┐            │              ┌─────▼─────┐
│  E-vector    │────────────┘              │  Action   │
│  P(π)        │     ┌──────────────┐      │  Selection│
└──────────────┘     │  γ precision │──────┘           │
                     └──────────────┘                   ▼
```

- **D** initializes perception and determines the starting beliefs used for policy evaluation.
- **C** shapes the risk term in EFE — driving **pragmatic** (goal-directed) behavior.
- **A** shapes the ambiguity term in EFE — driving **epistemic** (information-seeking) behavior.
- **E** biases the policy posterior toward habitual actions.
- **γ** controls how much EFE matters relative to habits and randomness.

## Applications

- **Goal-directed vs. curious agents**: By varying C from peaked to flat, you can create agents that are purely exploitative, purely exploratory, or balanced between the two.
- **Habitual behavior**: Setting a strong E-vector can model agents that default to familiar actions unless the situation is clearly novel.
- **Anxiety and avoidance**: A C-vector with very negative entries for certain observations models agents that actively avoid aversive outcomes.

## Conclusion

C, D, E, and γ define the agent's cognitive character: what it values, what it assumes, what it defaults to, and how decisive it is. With all five matrix components (A, B, C, D, E) and precision in hand, Module 05 can now show how these components combine to select actions through Expected Free Energy.
