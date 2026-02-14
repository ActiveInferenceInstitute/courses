# Lab: Implementing Parameter Learning

> **Learning Goal:** Build a learning agent, track its improvement, and analyze learning dynamics.

## Part 1: Initialize a Learning Agent

```python
# Weak prior (agent knows little about the environment)
A_prior = np.ones((2, 2)) * 1.0  # uniform Dirichlet prior
B_prior = np.ones((2, 2, 2)) * 1.0

C = np.array([2.0, -1.0])
D = np.array([0.5, 0.5])

agent = LearningAgent(A_prior, B_prior, C, D)
print(f"Initial A:\n{agent.A.round(3)}")
print(f"Initial learning rate: {agent.get_effective_learning_rate():.4f}")
```

{fill:textarea}

## Part 2: Learn from Experience

Run the agent for 50 steps and watch A converge:

```python
# True environment
true_A = np.array([[0.9, 0.1], [0.1, 0.9]])
true_B = np.zeros((2, 2, 2))
true_B[:,:,0] = np.eye(2)
true_B[:,:,1] = np.array([[0, 1], [1, 0]])

env = SimpleEnvironment(true_A, true_B)

for t in range(50):
    obs = np.random.choice(2, p=true_A[:, env.state])
    agent.step(obs)
    if t % 10 == 0:
        print(f"t={t}: A =\n{agent.A.round(3)}\n  LR = {agent.get_effective_learning_rate():.4f}")
```

How close is the learned A to the true A after 50 steps?

{fill:textarea}

## Part 3: Learning Rate Tracking

Plot or tabulate the learning rate over time:

```python
lrs = [log['lr'] for log in agent.learning_log]
for t in [0, 10, 20, 30, 40, 49]:
    print(f"t={t}: learning rate = {lrs[t]:.6f}")
```

Does the learning rate decay match the theoretical prediction (1/total_count)?

{fill:textarea}

## Part 4: Strong vs. Weak Priors

**Exercise**: Compare agents with different prior strengths:

- Weak: A_prior = ones * 1.0
- Strong wrong: A_prior = [[10, 1], [1, 10]] (confident but reversed!)

Run both for 100 steps. Which learns faster? Which gets stuck?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: What did you learn about the relationship between prior strength and learning speed? When is a strong prior helpful vs. harmful?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Agent initialization | Dirichlet priors |
| 2 | Learning observation | A matrix convergence |
| 3 | Rate analysis | Learning rate decay |
| 4 | Prior comparison | Strong vs. weak priors |
| 5 | Reflection | Prior-learning trade-off |
