# Lab: The Complete Active Inference Agent

> **Learning Goal:** Build, run, and analyze the fully integrated Active Inference agent.

## Part 1: Initialize the Complete Agent

```python
# 2-state foraging environment
A_prior = np.ones((2, 2)) * 2.0
B_prior = np.ones((2, 2, 2)) * 2.0
C = np.array([3.0, -1.0])
D = np.array([0.5, 0.5])

agent = CompleteActiveInferenceAgent(A_prior, B_prior, C, D, policy_len=1, gamma=1.0)
print(f"Policies: {agent.policies}")
print(f"Initial A:\n{agent.A.round(3)}")
print(f"Initial habit entropy: {-(agent.policy_prior * np.log(agent.policy_prior + 1e-16)).sum():.3f}")
```


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Run 100 Steps

```python
true_A = np.array([[0.9, 0.1], [0.1, 0.9]])
true_B = np.zeros((2, 2, 2))
true_B[:,:,0] = np.eye(2)
true_B[:,:,1] = np.array([[0, 1], [1, 0]])

env = SimpleEnvironment(true_A, true_B)
agent = run_full_simulation(agent, env, num_steps=100)
```

Analyze: Did the agent learn the environment? Did habits form?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Analyze the Four Subsystems

After 100 steps, examine each subsystem:

1. **Perception**: Compare learned A to true A — how close?
2. **Action**: What is the distribution over policies in the last 10 steps?
3. **Learning**: Plot the learning rate trajectory
4. **Habits**: Print the habit strength and policy prior

```python
print(f"Learned A:\n{agent.A.round(3)}")
print(f"True A:\n{true_A}")
print(f"Final policy prior: {agent.policy_prior.round(3)}")
print(f"Habit strength: {agent.habit_strength.round(1)}")
```


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Goal-Directed vs. Habitual Transition

**Exercise**: Compare early steps (1-10) vs. late steps (90-100):

- How do policy probabilities differ?
- Is the agent more "habitual" by step 100?
- What is the role of EFE vs. policy prior at each phase?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Capstone Reflection

In 200 words, reflect on the entire Implementation unit: You've built an Active Inference agent from scratch — data structures, inference, action selection, learning, communication, and planning. What are the most important insights from translating theory into code? What would you add or change?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Complete initialization | Full agent setup |
| 2 | Extended simulation | 100-step run |
| 3 | Subsystem analysis | Perception + Action + Learning + Habits |
| 4 | Behavioral transition | Goal-directed → Habitual |
| 5 | Capstone reflection | Theory ↔ Implementation synthesis |
