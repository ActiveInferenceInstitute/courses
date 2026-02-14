# Lab: The T-Maze

> **Learning Goal:** Build, run, and analyze the canonical T-Maze Active Inference benchmark.

## Part 1: Build the T-Maze

**Exercise**: Using the code from the module:

```python
A, B, C, D = build_tmaze(reward_prob=0.8, cue_reliability=0.9)

# Verify dimensions
for i, a in enumerate(A):
    print(f"A[{i}] shape: {a.shape}, columns sum: {a.sum(axis=0)}")
print(f"B shape: {B.shape}")
print(f"D shape: {D.shape}, sum: {D.sum()}")
```

Verify all matrices are well-formed (columns sum to 1).

{fill:textarea}

## Part 2: Run the Agent

> **Learning Goal:** Observe exploration-exploitation behavior.

**Exercise**: Run 10 trials of the T-Maze and record the agent's behavior:

| Trial | Step 1 Action | Step 2 Action | Got Reward? | Visited Cue? |
|-------|-------------|-------------|------------|-------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

How often does the agent visit the cue before choosing an arm?

{fill:textarea}

## Part 3: Parameter Manipulation

> **Learning Goal:** Explore how parameters affect behavior.

**Experiments**:

1. **Cue reliability = 0.5** (useless cue) — Does the agent still visit the cue?
2. **Cue reliability = 1.0** (perfect cue) — How does behavior change?
3. **C_reward = [0, 0, 0]** (no preferences) — What does the agent do?
4. **C_reward = [10, -10, 0]** (strong preferences) — How does behavior change?

Record results for each experiment.

{fill:textarea}

## Part 4: Analyze EFE Components

> **Learning Goal:** Decompose EFE into pragmatic and epistemic terms.

**Exercise**: For the agent's policy evaluation at the first time step:

```python
# Compute EFE for each action and decompose
for action in range(4):
    # YOUR CODE: compute pragmatic and epistemic value
    print(f"Action {action}: Pragmatic={prag:.3f}, Epistemic={epist:.3f}, Total={total:.3f}")
```

Which action has the highest epistemic value? Why?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: The T-Maze is a simple environment, yet it demonstrates a profound insight — that curiosity and goal-seeking emerge from one objective (EFE). Is this simplicity a strength or limitation of the benchmark?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | POMDP construction | Multi-modal T-Maze |
| 2 | Agent evaluation | Exploration-exploitation behavior |
| 3 | Parameter sensitivity | Cue reliability and preference effects |
| 4 | EFE decomposition | Pragmatic vs. epistemic value |
| 5 | Critical reflection | Benchmark evaluation |
