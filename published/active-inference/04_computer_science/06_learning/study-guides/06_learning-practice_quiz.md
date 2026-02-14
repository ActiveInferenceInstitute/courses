# Practice Quiz: Learning

## Part A: Multiple Choice

1. In Active Inference, parameter learning updates the:
A) Hidden states
B) Dirichlet concentration parameters (pA, pB)
C) C-vector preferences
D) Precision γ

2. `expected_A(pA)` computes:
A) The entropy of the Dirichlet distribution
B) The mean of the Dirichlet distribution — the normalized concentrations
C) The maximum likelihood estimate of A
D) The posterior over hidden states

3. After `update_dirichlet_A(pA, obs=0, q_s=[0.8, 0.2], lr=1.0)`, which pA entries increase?
A) pA[0, 0] by 0.8 and pA[0, 1] by 0.2
B) pA[0, 0] by 1.0 only
C) All entries increase equally
D) pA[1, 0] by 0.8 and pA[1, 1] by 0.2

4. With a learning rate of η = 0, the pA update:
A) Sets pA to zero
B) Leaves pA unchanged — no learning occurs
C) Halves all concentrations
D) Resets to uniform

5. `dirichlet_entropy(alpha)` is low when:
A) The concentrations are all 1.0 (uniform prior)
B) The concentrations are very large (peaked distribution)
C) The distribution is flat
D) The entropy is always constant

6. Bayesian Model Reduction returns ΔF < 0 when:
A) The full model is better
B) The reduced model is preferred (simpler and equally good)
C) Both models are identical
D) The computation failed

7. In the online learning loop, when should `agent.model.A` be updated?
A) Before state inference
B) After state inference but before action selection
C) After updating pA with `expected_A(pA)`
D) Only at the end of the episode

## Part B: Short Answer

1. If `pA = [[10, 1], [1, 10]]`, compute `expected_A(pA)` by hand. Show the normalization for each column.

2. Explain why the agent needs both `pA` (concentration parameters) and `model.A` (expected matrix). Why can't it just use pA directly for state inference?

3. Design an experiment to detect catastrophic forgetting: an agent learns environment A for 50 steps, then switches to environment B for 50 steps. Describe what you would measure and what result would indicate forgetting.
