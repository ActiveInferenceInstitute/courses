# Lab: Policy Selection and Active Inference Loop

> **Learning Goal:** Implement and analyze multi-step policy selection with EFE decomposition.

## Part 1: Generate and Inspect Policies

```python
policies = generate_policies(num_actions=3, policy_length=2)
print(f"Total policies: {len(policies)}")
for i, p in enumerate(policies):
    print(f"  π_{i}: {p}")
```

How does the number of policies scale with num_actions and policy_length?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: EFE Decomposition

**Exercise**: Using a simple 2-state, 2-action model, compute EFE for each policy and decompose:

```python
A = np.array([[0.9, 0.1], [0.1, 0.9]])
B = np.zeros((2, 2, 2))
B[:,:,0] = np.eye(2)  # stay
B[:,:,1] = np.array([[0, 1], [1, 0]])  # switch
C = np.array([2.0, -1.0])
qs = np.array([0.5, 0.5])  # uncertain

policies = generate_policies(2, 1)
for i, p in enumerate(policies):
    G, prag, epist = compute_efe_decomposed(A, B, C, qs, p)
    print(f"π={p}: G={G:.3f}, Pragmatic={prag:.3f}, Epistemic={epist:.3f}")
```

Which policy wins and why?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Run the Full Loop

Run the active inference loop for 20 steps and analyze:

```python
log = active_inference_loop(A, B, C, D, env, num_steps=20, gamma=1.0)
print(f"Action frequencies: {np.bincount(log['actions'], minlength=2)}")
```

Does the agent converge on the preferred state?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Gamma Sweep

Run with gamma = 0.1, 1.0, and 10.0. Compare action selection behavior.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 150 words, reflect: How does watching the EFE decomposition evolve over time help you understand the agent's decision-making? When was epistemic value highest vs. pragmatic?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Policy generation | Combinatorial policy space |
| 2 | EFE analysis | Pragmatic vs. epistemic decomposition |
| 3 | Loop execution | Full active inference cycle |
| 4 | Parameter sweep | Gamma and decisiveness |
| 5 | Behavioral analysis | Understanding agent decisions |
