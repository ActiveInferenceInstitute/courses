# Study Questions: Systems

1. Define a Markov Blanket formally. What conditional independence relation does it encode?
2. Write the factorized joint distribution p(η, s, a, μ) for a system with Markov Blanket {s, a}. Explain each factor.
3. What is the Langevin equation? How does it describe the stochastic dynamics of a system?
4. How do the Markov Blanket conditions constrain the flow field f(x) in the Langevin equation?
5. Define variational free energy F. Write the mathematical expression and identify each term.
6. Prove that F = D_KL[q(η) ‖ p(η|s)] - ln p(s). Why is this decomposition important?
7. Why is minimizing F equivalent to maximizing the evidence lower bound (ELBO)?
8. What is the recognition density q(η)? What role does it play in variational inference?
9. Why is exact Bayesian inference (computing p(η|s) directly) typically intractable? How does variational inference address this?
10. What is the KL divergence D_KL[q ‖ p]? Prove that it is always non-negative.
11. Explain the relationship between surprise (-ln p(s)) and entropy. When is surprise high?
12. How does the free energy decompose into accuracy and complexity terms? Write the expression.
13. What is a nonequilibrium steady-state density p*(x)? How does it relate to self-organization?
14. How does the Fokker-Planck equation describe the evolution of the probability density over states?
15. What is the relationship between the flow field f(x) and the gradient of surprise (solenoidal vs. curl-free flow)?
16. How does the Helmholtz decomposition separate the flow into dissipative and conservative components?
17. What happens to variational free energy when q(η) exactly equals the true posterior p(η|s)?
18. Compare the free energy bound with the Helmholtz free energy in statistical thermodynamics. What is the analogy?
19. How does the choice of variational family for q(η) (e.g., mean-field, Gaussian) affect the tightness of the free energy bound?
20. Derive the conditions under which minimizing F with respect to q recovers exact Bayesian inference.
