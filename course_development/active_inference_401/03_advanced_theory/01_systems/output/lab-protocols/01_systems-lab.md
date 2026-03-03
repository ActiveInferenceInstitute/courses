# Lab: Variational Calculus and the Free Energy Functional

> **Learning Goal:** Derive, decompose, and analyze variational free energy through mathematical exercises.

## Part 1: Derivation Exercise

**Exercise**: Starting from the definition of model evidence, derive the variational free energy bound step by step.

Given: A generative model p(o, s) = p(o|s) p(s), observations o, hidden states s, and approximate posterior q(s).

1. Write the log model evidence: ln p(o) = ln ∫ p(o, s) ds
2. Multiply and divide by q(s) inside the integral
3. Apply Jensen's inequality to obtain the ELBO
4. Define F[q] = -ELBO and show F[q] = E_q[-ln p(o, s)] + E_q[ln q(s)]
5. Show F[q] = -ln p(o) + D_KL[q(s) || p(s|o)]
6. Conclude that F[q] ≥ -ln p(o) with equality iff q(s) = p(s|o)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Decomposition Analysis

> **Learning Goal:** Work through all three decompositions and understand their computational significance.

**Exercise**: For a simple model — p(s) = N(0, σ²_p), p(o|s) = N(s, σ²_o), and q(s) = N(μ_q, σ²_q) — compute each decomposition analytically:

**Decomposition 1** (Energy - Entropy):

- Energy = E_q[-ln p(o, s)] = ?
- Entropy = H[q] = ½ ln(2πe σ²_q)
- F = Energy - Entropy

**Decomposition 2** (Complexity - Accuracy):

- Complexity = D_KL[q(s) || p(s)] = ?
- Accuracy = E_q[ln p(o|s)] = ?
- F = Complexity - Accuracy

**Decomposition 3** (Surprise + KL):

- Compute p(o) analytically for this Gaussian model
- Surprise = -ln p(o) = ?
- KL = D_KL[q(s) || p(s|o)] = ?
- Verify F = Surprise + KL


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Mean-Field Updates

> **Learning Goal:** Derive and apply mean-field variational updates.

**Exercise**: Consider a model with two hidden state groups s₁ and s₂:

p(o, s₁, s₂) = p(o | s₁, s₂) · p(s₁) · p(s₂)

Assume mean-field factorization: q(s₁, s₂) = q₁(s₁) · q₂(s₂)

1. Derive the optimal q₁*(s₁) by taking the functional derivative of F with respect to q₁ and setting to zero
2. Show that ln q₁*(s₁) = E_{q₂}[ln p(o, s₁, s₂)] + const
3. Explain why this creates an iterative scheme (q₁ depends on q₂ and vice versa)
4. Under what conditions does this scheme converge? (Are there guarantees?)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Free Energy on a Factor Graph

> **Learning Goal:** Decompose free energy into local contributions on a simple factor graph.

**Exercise**: Consider a Hidden Markov Model with 3 time steps:

p(s₁, s₂, s₃, o₁, o₂, o₃) = p(s₁) · p(s₂|s₁) · p(s₃|s₂) · p(o₁|s₁) · p(o₂|s₂) · p(o₃|s₃)

1. Draw the factor graph (variable nodes and factor nodes)
2. Write the total free energy as a sum of local free energies (one per factor node)
3. What messages need to pass between variable and factor nodes?
4. How does updating beliefs at one node affect neighboring nodes?
5. What is the computational advantage of this decomposition vs. computing F globally?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Approximation Comparison

> **Learning Goal:** Compare variational approximation methods.

**Exercise**: For a bimodal posterior p(s|o) (two well-separated modes), compare:

| Method | Approximation | What It Gets Right | What It Gets Wrong |
|--------|--------------|-------------------|-------------------|
| Mean-field (factorized Gaussian) | Single Gaussian | Captures one mode location | Misses the other mode entirely (mode-seeking) |
| Laplace | Gaussian at MAP | Captures the MAP mode accurately | Misses second mode; underestimates uncertainty |
| Bethe | Pairwise interactions | Better for structured models | Still struggles with multimodality |
| MCMC (for comparison) | Samples from true posterior | Both modes captured | Computationally expensive; convergence unclear |

Write a 300-word analysis: What are the trade-offs between accuracy and computational cost? Why does Active Inference typically use mean-field or Laplace rather than MCMC?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Mathematical derivation | Free energy bound |
| 2 | Analytical computation | Decompositions in Gaussian models |
| 3 | Variational updates | Mean-field optimization |
| 4 | Graphical models | Factor graph decomposition |
| 5 | Method comparison | Approximation trade-offs |
