# Lab: Derivation Exercise — Parameter Learning and Model Reduction

## Objective

Derive the parameter learning equations and Bayesian Model Reduction formula, applying them to concrete examples.

## Part 1: Dirichlet-Categorical Conjugacy

**Goal**: Derive the conjugate update from first principles.

**Setup**: Prior: p(θ) = Dir(θ; α₁, α₂, α₃) with α = [2, 3, 1]. Likelihood: p(x|θ) = Cat(x; θ). Data: 10 observations: {1, 1, 2, 1, 3, 2, 1, 1, 2, 1} (category counts: n₁=6, n₂=3, n₃=1).

**Task**:

1. Write Bayes' rule: p(θ|x₁:N) ∝ p(x₁:N|θ) · p(θ)
2. Expand the likelihood as ∏ₖ θₖ^nₖ and the prior as ∏ₖ θₖ^(αₖ-1)
3. Show the posterior is Dir(θ; α₁+n₁, α₂+n₂, α₃+n₃) = Dir(θ; 8, 6, 2)
4. Compute the posterior mean E[θ|data] and compare with the MLE

{fill:textarea}

## Part 2: A-Matrix Learning in a POMDP

**Goal**: Track how the A matrix evolves with experience.

**Setup**: A 2-state, 2-observation POMDP. Initial A matrix concentration:

a = [[10, 1], [1, 10]]  (state 1 → observation 1; state 2 → observation 2)

The agent experiences 20 trials where state 1 produces observation 1 (18 times) and observation 2 (2 times).

**Task**:

1. Apply the Dirichlet update rule: a_ij ← a_ij + n_ij
2. Compute the updated concentration parameters
3. Compute the updated expected A matrix (posterior mean)
4. How has the A matrix changed? How much more confident is the agent?

{fill:textarea}

## Part 3: Bayesian Model Reduction

**Goal**: Apply BMR to decide whether a parameter should be pruned.

**Setup**: After learning, a 3-state POMDP has posterior A matrix concentrations:

a_full = [[50, 2, 1], [2, 48, 1], [1, 1, 45]]

Consider a reduced model where states 2 and 3 are merged (reducing from 3 to 2 states), with reduced prior concentrations:

ã₀ = [[50, 3], [2, 49]]

Original prior: a₀ = [[10, 1, 1], [1, 10, 1], [1, 1, 10]]

**Task**:

1. Compute the BMR evidence ratio using: ΔF ≈ ln B(ã₀) - ln B(a₀) - ln B(ã) + ln B(a)
2. Where ã = a + ã₀ - a₀
3. Determine whether the reduced model is preferred (ΔF < 0)
4. Explain what this means: is the third state "doing work" or can it be pruned?

{fill:textarea}

## Part 4: Learning Rate and Forgetting

**Goal**: Analyze the effect of learning rate and forgetting on parameter trajectories.

**Task**:

1. For the Dirichlet update a ← a + η · n, analyze the effect of η < 1 (slow learning) and η > 1 (fast learning)
2. Consider a forgetting mechanism: a ← λ · a + η · n, where λ < 1 is a decay factor. Show that this implements exponential forgetting
3. Compute the effective "memory window" as a function of λ
4. Discuss: when is forgetting adaptive? When is it maladaptive?

{fill:textarea}

## Part 5: Synthesis

In 200 words, explain how parameter learning (Dirichlet updates) and structure learning (BMR) together enable the agent to both refine and simplify its generative model, and how this maps onto the neuroscience of waking learning and sleep consolidation.

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Bayesian updating | Dirichlet-Categorical conjugate derivation |
| 2 | Matrix learning | A-matrix concentration update tracking |
| 3 | Model comparison | Bayesian Model Reduction evidence ratio |
| 4 | Dynamical analysis | Learning rate and forgetting trade-offs |
| 5 | Conceptual integration | Connecting learning math to neuroscience |
