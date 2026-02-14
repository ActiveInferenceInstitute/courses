# Study Questions: Learning

1. What is parameter learning in the context of a POMDP? Which quantities are updated?
2. Write the Dirichlet distribution Dir(θ; α₁, ..., αK). What is the role of the concentration parameters αₖ?
3. Derive the conjugate Dirichlet update for a Categorical likelihood.
4. How does the A matrix concentration parameter a_ij update with experience? Write the update rule.
5. How does the B matrix concentration parameter b_ijk update with experience? How does it differ from A learning?
6. What is the mean of a Dirichlet distribution? How does it evolve with accumulated evidence?
7. How does the total concentration ∑αₖ relate to the confidence (precision) of the learned parameters?
8. What is Bayesian Model Reduction (BMR)? How does it enable structure learning without re-fitting?
9. Derive the BMR evidence ratio using the multivariate beta function.
10. Why is BMR computationally efficient compared to exhaustive model comparison?
11. How does BMR relate to the synaptic homeostasis hypothesis (synaptic pruning during sleep)?
12. What is the multivariate beta function B(α)? Write its definition in terms of the Gamma function.
13. How does the learning rate η affect the speed and stability of parameter updates?
14. What happens to the A matrix as the concentration parameters a_ij → ∞? How does this represent "crystallized" knowledge?
15. Compare Dirichlet updating with maximum likelihood estimation. When do they converge?
16. What is empirical Bayes? How does it relate to hyperparameter estimation in hierarchical models?
17. How does Active Inference's account of learning differ from classical reinforcement learning (temporal difference learning)?
18. How does the concept of "forgetting" emerge in the Dirichlet framework? (Consider reducing concentration parameters.)
19. What is the relationship between the D vector (initial state prior) and learned context? How does the context update?
20. Derive the free energy contribution from parameter learning: how does uncertainty about parameters increase free energy?
