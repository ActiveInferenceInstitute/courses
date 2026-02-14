# Lab 05: Policy Selection and the T-Maze

## Objective

Compute EFE, decompose it into risk and ambiguity, select policies, and analyze T-maze exploration–exploitation behavior.

## Prerequisites

- Completed Labs 01–04
- Understanding of EFE formula and softmax function

## Part 1: Computing EFE for Individual Actions

**Goal**: Compute and compare EFE values for each action in a 2-state system.

1. Create a `GenerativeModel` with `A = [[0.9, 0.1], [0.1, 0.9]]`, identity B for action 0, swap B for action 1, `C = [2, -2]`, uniform D.
2. Set $q(s) = [0.8, 0.2]$.
3. Compute `compute_efe()` and `compute_efe_components()` for both actions.
4. Print a table of risk, ambiguity, and total G for each action.

```python
from active_inference.math import compute_efe, compute_efe_components

# TODO: Compute and compare EFE for action 0 vs action 1
```

**Response**: {fill:textarea}

## Part 2: Policy Inference with Varying Precision

**Goal**: Run `run_policy_inference()` across γ values and observe policy posterior changes.

1. Use the model from Part 1. Create policies `[[0], [1]]`.
2. Run policy inference for γ ∈ {0.1, 0.5, 1, 2, 4, 8, 16}.
3. Record $q(\pi)$ for each γ.
4. Plot results using `plot_precision_sweep()`.

**Response**: {fill:textarea}

## Part 3: T-Maze Simulation

**Goal**: Build and run a full T-maze agent-environment loop.

1. Set up the T-maze model (4 states, 3 obs, 3 actions) from Module 02.
2. Create the corresponding `DiscreteEnvironment` and `ActiveInferenceAgent`.
3. Run 8 steps. Record states, observations, actions, and EFE values.
4. Did the agent visit the cue location before choosing an arm?

**Response**: {fill:textarea}

## Part 4: EFE Decomposition Over Time

**Goal**: Track risk and ambiguity across the simulation.

1. At each step of the T-maze loop, compute `compute_efe_components()` for the selected action.
2. Store risk and ambiguity values.
3. Plot with `plot_efe_decomposition()`.
4. Identify when ambiguity dominates (information-seeking phase) and when risk dominates (goal-seeking phase).

**Response**: {fill:textarea}

## Part 5: Analysis Questions

1. In the 2-state system, which action had lower G? Does this match your intuition given the C-vector?
2. At what γ value did the T-maze agent become reliably goal-directed?
3. Did the agent's EFE decomposition show an ambiguity-driven phase followed by a risk-driven phase?

**Response**: {fill:textarea}

## Summary

| Skill | Library Component | Status |
|-------|------------------|--------|
| Compute EFE and its components | `compute_efe()`, `compute_efe_components()` | |
| Run policy inference | `run_policy_inference()` | |
| Visualize EFE decomposition | `plot_efe_decomposition()` | |
| Build and run a T-maze simulation | T-maze model + agent-env loop | |
| Analyze exploration vs exploitation | Risk vs ambiguity over time | |
