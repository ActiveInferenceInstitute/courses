# Study Questions: Cognition

1. Define precision mathematically. How does it relate to variance and covariance?
2. Write the Gaussian likelihood with explicit precision matrix: p(o|s) = N(g(s), Π⁻¹). Expand the log-likelihood.
3. Derive ∂F/∂π for a univariate Gaussian model. What is the optimal precision?
4. Explain why the optimal precision equals the inverse expected squared prediction error. What intuition does this provide?
5. What is the Gamma distribution? Why is it used as a prior on precision?
6. Derive the posterior distribution over precision for a Gamma-Gaussian conjugate model.
7. What is the Fisher information matrix? How is it computed for a parametric model?
8. Prove that for a Gaussian model with known mean, the Fisher information equals the precision.
9. How does Fisher information relate to the Cramér-Rao bound on parameter estimation?
10. How does attention modulate precision in the predictive coding hierarchy? What are the mathematical consequences?
11. Derive the precision update equation dγ/dt = -∂F/∂γ where γ = ln π is the log-precision.
12. Why is log-precision (γ) often used instead of raw precision (π) in the update equations?
13. How does the precision-weighted prediction error Π·ε differ from the unweighted prediction error ε in its effect on belief updates?
14. What happens mathematically when precision goes to zero? When it goes to infinity?
15. How does the brain estimate precision separately for each level of the hierarchy?
16. What is the expected free energy contribution from precision? Write the term explicitly.
17. How does type II maximum likelihood (empirical Bayes) relate to precision estimation?
18. Compare Bayesian precision estimation with classical approaches to estimating noise variance.
19. How does the concept of volatility (how rapidly precision changes over time) relate to hierarchical precision learning?
20. Derive the precision update for a model where the precision itself changes over time (volatile environment).
