# Practice Quiz: Systems

## Part A: Multiple Choice

1. A Markov Blanket {s, a} separating internal states μ from external states η means:
A) μ and η are statistically independent
B) μ ⊥ η | {s, a} — internal and external states are conditionally independent given the blanket
C) μ = η at all times
D) s and a are constants

2. The variational free energy F is:
A) Always equal to surprise
B) An upper bound on surprise: F ≥ -ln p(s)
C) A lower bound on surprise: F ≤ -ln p(s)
D) Undefined for continuous distributions

3. The decomposition F = D_KL[q(η) ‖ p(η|s)] - ln p(s) shows that minimizing F:
A) Only minimizes the KL divergence
B) Simultaneously minimizes the KL divergence (bringing q close to the posterior) and maximizes model evidence
C) Maximizes surprise
D) Has no effect on the recognition density q

4. The accuracy-complexity decomposition F = -E_q[ln p(s|η)] + D_KL[q(η) ‖ p(η)] shows that:
A) Accuracy and complexity must both be maximized
B) Good inference balances explaining the data (accuracy) with not deviating too far from priors (complexity)
C) Only accuracy matters for inference
D) Complexity is always zero

5. In the Langevin equation dx/dt = f(x) + ω, the term ω represents:
A) Deterministic dynamics
B) Random fluctuations (Wiener process / Brownian noise)
C) A control signal from the agent
D) The Markov Blanket

6. The KL divergence D_KL[q ‖ p]:
A) Can be negative
B) Is always non-negative and equals zero only when q = p
C) Is symmetric: D_KL[q ‖ p] = D_KL[p ‖ q]
D) Measures the correlation between q and p

7. At nonequilibrium steady state:
A) All variables stop changing
B) The probability density over states converges to a characteristic form p*(x) while individual states continue to fluctuate
C) Free energy equals zero
D) The system is in thermodynamic equilibrium

## Part B: Short Answer

1. Derive the ELBO inequality in three steps: start from F = E_q[ln q(η) - ln p(η, s)], apply Bayes' rule to p(η, s), and use the non-negativity of KL divergence.
2. For a Gaussian generative model p(η) = N(0, 1) and p(s|η) = N(η, 1), compute the optimal recognition density q*(η) after observing s = 2. What are the optimal mean and variance?
3. Explain the physical interpretation of the Helmholtz decomposition of the flow field into solenoidal (curl-free) and dissipative components. Why does this matter for Active Inference?
