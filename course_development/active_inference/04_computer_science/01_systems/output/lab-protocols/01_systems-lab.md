# Lab 01: Building and Exploring a Discrete Environment

## Objective

Build a `DiscreteEnvironment` from scratch, step through it, record trajectories, and visualize the generative process.

## Prerequisites

- Python with NumPy and matplotlib installed
- Familiarity with probability distributions and matrix notation
- Access to the `active_inference` library (`src/active_inference/`)

## Part 1: Constructing the Environment

**Goal**: Create a 3-state, 2-observation environment with 2 actions.

1. Define a `true_A` matrix of shape `(2, 3)` where:
   - State 0 produces observation 0 with probability 0.8
   - State 1 produces each observation with equal probability
   - State 2 produces observation 1 with probability 0.9

2. Define a `true_B` tensor of shape `(3, 3, 2)` where:
   - Action 0 is the identity (stay in current state)
   - Action 1 rotates: state 0 → 1, state 1 → 2, state 2 → 0

3. Create a `DiscreteEnvironment` starting in state 0.

```python
import numpy as np
from active_inference.agent import DiscreteEnvironment

# TODO: Define true_A and true_B
# TODO: Create environment
```

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Running a Trajectory

**Goal**: Step the environment for 20 timesteps using a fixed action sequence.

1. Reset the environment to state 0.
2. Alternate between action 0 (stay) and action 1 (rotate) for 20 steps.
3. Record the state, observation, and action at each step.
4. Print the full trajectory.

```python
env.reset(initial_state=0)
for t in range(20):
    action = t % 2  # alternate stay/rotate
    obs = env.step(action)
    print(f"t={t}: action={action}, state={env.state}, obs={obs}")
```

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Visualizing the Trajectory

**Goal**: Use `plot_environment_trajectory` to visualize the state-observation-action sequence.

1. After running Part 2, extract `env.history`.
2. Call `plot_environment_trajectory` to generate a figure.
3. Save the figure to `output/lab01_trajectory.png`.

```python
from active_inference.visualization import plot_environment_trajectory

plot_environment_trajectory(
    states=env.history["states"],
    observations=env.history["observations"],
    save_path="output/lab01_trajectory.png",
)
```

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Empirical Likelihood Estimation

**Goal**: Verify the `true_A` matrix by collecting observations.

1. Reset the environment. Fix the state by using action 0 (identity) from a known starting state.
2. Collect 1000 observations from each state (reset to each state, step with identity action 1000 times).
3. Compute the empirical frequency of each observation per state.
4. Compare with the original `true_A` matrix.

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Analysis Questions

1. When you ran 20 steps with alternating actions, how many unique states did the trajectory visit? Was this predictable from the `true_B` matrix?

2. Did your empirical likelihood estimates in Part 4 converge to the true values? How many samples were needed for 2-decimal accuracy?

3. What would change if you made `true_A = np.eye(3, 2).T` (a non-square identity-like matrix)? Would the environment still be valid?

**Response**: 
<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary

| Skill | Library Component | Status |
|-------|------------------|--------|
| Create environments with custom A and B matrices | `DiscreteEnvironment(true_A, true_B)` | |
| Step through environments and collect trajectories | `env.step(action)`, `env.history` | |
| Visualize state-observation trajectories | `plot_environment_trajectory()` | |
| Empirically verify likelihood matrices | Manual frequency counting vs `true_A` | |
| Understand the generative process abstraction | Generative process ≠ generative model | |
