# Lab 04: Preferences, Priors, and Precision Tuning

## Objective

Explore how C, D, E vectors and precision γ shape agent behavior.

## Prerequisites

- Completed Labs 01–03
- Understanding of EFE decomposition (risk + ambiguity)

## Part 1: C-Vector Effects

**Goal**: Compare agent behavior with different preference vectors.

1. Create a T-maze `GenerativeModel` (4 states, 3 obs, 3 actions).
2. Run the perception-action loop for 15 steps with three C-vectors:
   - `C_neutral = [0, 0, 0]` (no preferences)
   - `C_reward = [0, 3, -3]` (prefer reward)
   - `C_explore = [0, 0, 0]` with a noisy A-matrix (epistemic drive)
3. Record and compare the action sequences and states visited.

```python
# TODO: Create models with different C-vectors
# TODO: Run loops and compare
```

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: D-Vector Effects

**Goal**: Investigate how the initial state prior affects early behavior.

1. Fix C and E. Create two agents with:
   - `D_certain = [1, 0, 0, 0]` (confident at center)
   - `D_uncertain = [0.25, 0.25, 0.25, 0.25]` (uniform)
2. Run 5 steps. Compare the first action selected and the VFE trajectory.
3. Visualize both D-vectors using `plot_D_prior()`.

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: E-Vector and Habit Formation

**Goal**: Demonstrate how habits bias action selection.

1. Create an agent with `E = [0.8, 0.1, 0.1]` (strong stay habit) and γ = 0.5.
2. Create an agent with `E = None` and the same γ.
3. Run both for 20 steps. Count how often each agent selects action 0 (stay).
4. Visualize habits using `plot_E_habits()`.

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Precision Sweep

**Goal**: Map the exploration–exploitation tradeoff across γ values.

1. For γ ∈ {0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0}:
   - Run `run_policy_inference()` with the same beliefs and C-vector
   - Record the resulting $q(\pi)$
2. Visualize with `plot_precision_sweep()`.
3. Identify the γ value where the agent transitions from near-random to near-deterministic.

```python
from active_inference.math import run_policy_inference
from active_inference.visualization import plot_precision_sweep

# TODO: Sweep γ and collect q(π) matrix
```

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Analysis Questions

1. Did the agent with `C = [0, 3, -3]` consistently reach the reward arm? If not, what prevented it?
2. How many steps did the habit-biased agent waste on action 0 compared to a habit-free agent?
3. At which γ value did policy selection become effectively deterministic? How does this relate to the magnitude of EFE differences?

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary

| Skill | Library Component | Status |
|-------|------------------|--------|
| Design C-vectors for goal-directed behavior | `GenerativeModel(C=...)` | |
| Visualize preferences, priors, and habits | `plot_C_preferences()`, `plot_D_prior()`, `plot_E_habits()` | |
| Investigate precision effects | `run_policy_inference(gamma=...)` | |
| Map the exploration–exploitation tradeoff | `plot_precision_sweep()` | |
| Compare agents with different cognitive configurations | Multi-agent experiment design | |
