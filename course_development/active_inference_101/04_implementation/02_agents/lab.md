# Lab: Building and Running an Active Inference Agent

> **Learning Goal:** Implement a complete agent, run it in an environment, and analyze its behavior.

## Part 1: Complete the Agent

**Exercise**: Using the code from the module, create a foraging agent:

```python
import numpy as np

# 3 locations: left, center, right
# Food is in the right location
# 3 observations: food, nothing, wall

A = np.array([
    [0.1, 0.1, 0.8],   # P(see food | state)
    [0.2, 0.8, 0.1],   # P(see nothing | state)
    [0.7, 0.1, 0.1]    # P(see wall | state)
])

B = np.zeros((3, 3, 3))
B[:,:,0] = np.array([[0.9, 0.5, 0.0], [0.1, 0.4, 0.1], [0.0, 0.1, 0.9]])  # go_left
B[:,:,1] = np.array([[0.1, 0.1, 0.0], [0.8, 0.8, 0.2], [0.1, 0.1, 0.8]])  # stay
B[:,:,2] = np.array([[0.0, 0.1, 0.1], [0.1, 0.4, 0.1], [0.9, 0.5, 0.8]])  # go_right

C = np.array([3.0, 0.0, -1.0])  # prefer food, neutral to nothing, avoid wall
D = np.array([0.33, 0.34, 0.33])  # uniform start

# YOUR CODE: Create agent and environment, run simulation
```

{fill:textarea}

## Part 2: Analyze Behavior

> **Learning Goal:** Interpret the agent's belief and action trajectories.

After running 20 steps:

1. Plot or list the agent's belief history — does the agent converge on the true state?
2. Plot or list the action history — does the agent find the food?
3. What does the true_state history show?

{fill:textarea}

## Part 3: Modify Agent Parameters

> **Learning Goal:** Explore how parameters affect behavior.

**Experiments**:

1. Set gamma = 0.1 (low policy precision) — run 20 steps. How does behavior change?
2. Set gamma = 10.0 (high policy precision) — run 20 steps. How does behavior change?
3. Set C = [0, 0, 0] (no preferences) — what does the agent do now?
4. Make A very noisy (nearly uniform) — how does this affect inference?

{fill:textarea}

## Part 4: Add Logging

> **Learning Goal:** Implement better observation and analysis.

**Exercise**: Add a method to the agent class that prints a summary:

```python
def summary(self):
    """Print a summary of the agent's experience."""
    print(f"Steps taken: {len(self.action_history)}")
    print(f"Action distribution: {np.bincount(self.action_history, minlength=self.num_actions)}")
    print(f"Final beliefs: {self.qs.round(3)}")
    print(f"Observation counts: {np.bincount(self.obs_history, minlength=self.num_obs)}")
```

Run the agent for 50 steps and call `summary()`. What do you observe?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: What surprised you about the agent's behavior? Did it always find the food? When did it explore vs. exploit? How does watching the code run deepen your understanding compared to the mathematical description?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Full implementation | Agent + Environment + Loop |
| 2 | Analysis | Belief and action trajectories |
| 3 | Parameter exploration | gamma, C, A effects |
| 4 | Logging | Diagnostic reporting |
| 5 | Reflection | Code ↔ Theory connection |
