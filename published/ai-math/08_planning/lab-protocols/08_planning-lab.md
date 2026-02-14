# Lab: Derivation Exercise — Policy Evaluation and Sophisticated Inference

## Objective

Derive and compute Expected Free Energy for multi-step policies, extending to sophisticated inference with recursive belief updating.

## Part 1: Two-Step Policy Evaluation

**Goal**: Compute EFE for all policies in a simple POMDP.

**Setup**: 2 states, 2 observations, 2 actions, planning horizon T = 2.

- A matrix: A = [[0.9, 0.1], [0.1, 0.9]]
- B matrix: B₁ = [[0.8, 0.2], [0.2, 0.8]] (action 1), B₂ = [[0.3, 0.7], [0.7, 0.3]] (action 2)
- C vector: C = [ln 2, ln(1/2)] (prefer observation 1)
- Initial belief: q(s₁) = [0.5, 0.5]

There are K^T = 2² = 4 policies: π₁=(a₁,a₁), π₂=(a₁,a₂), π₃=(a₂,a₁), π₄=(a₂,a₂).

**Task**:

1. For each policy, compute q(s₂ | π) = B(π₁) · q(s₁) and q(s₃ | π) = B(π₂) · q(s₂ | π)
2. Compute predicted observations q(o_τ | π) = A · q(s_τ | π) for each timestep
3. Compute the EFE G(π) = ∑_τ [pragmatic_τ + epistemic_τ] for each policy
4. Select the best policy (lowest G)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Sophisticated Inference

**Goal**: Extend Part 1 with future belief updates.

**Task**:

1. For the best policy from Part 1, simulate what happens at timestep 2: the agent observes o₂, then updates its belief using Bayes' rule: q(s₂ | o₂, π) ∝ A(o₂, :) · q(s₂ | π)
2. For each possible observation o₂, compute the updated belief q(s₂ | o₂, π)
3. Evaluate the EFE of the second action using these updated beliefs instead of the prior beliefs
4. Compare the sophisticated EFE with the basic EFE from Part 1. How do they differ?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Hierarchical POMDP

**Goal**: Construct a two-level hierarchical POMDP.

**Setup**:

- Level 1 (fast): 3 states, 2 observations, 2 actions, runs for T₁ = 3 steps per Level 2 step
- Level 2 (slow): 2 states (contexts), determines the initial state distribution and preferences for Level 1

**Task**:

1. Write the generative model for each level
2. Show how Level 2's policy selection sets the D vector (initial state prior) and C vector (preferences) for Level 1
3. Derive the total free energy F_total = F₁ + F₂
4. Explain how optimizing at Level 2 selects which sub-task to pursue, while Level 1 handles moment-to-moment execution


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Computational Complexity Analysis

**Goal**: Analyze the scalability of planning.

**Task**:

1. For a flat POMDP with K actions and planning horizon T, count the number of policies: K^T
2. For K = 4, compute the number of policies for T = 1, 2, 3, 5, 10
3. Propose a pruning strategy based on Expected Free Energy thresholds: at each timestep, keep only the top-N policies
4. Analyze the complexity reduction: from K^T to N·K per timestep
5. Discuss: how does habit formation (defaulting to well-learned policies) further reduce computational demands?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Synthesis

In 200 words, explain how the three planning levels (basic EFE, sophisticated inference, hierarchical POMDPs) provide increasingly powerful but computationally costly planning — and how biological brains manage this trade-off through habits, sub-goals, and selective deliberation.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Numerical computation | Full EFE evaluation for all policies |
| 2 | Recursive reasoning | Sophisticated inference with future belief updates |
| 3 | Hierarchical modeling | Two-level POMDP with context-dependent sub-tasks |
| 4 | Complexity analysis | Scalability and pruning strategies |
| 5 | Conceptual integration | Biological-computational planning trade-offs |
