# Study Questions: Agents

1. Write the general form of a generative model as a joint distribution p(o, s, θ). Identify each component.
2. What is the difference between a generative model and a discriminative model? Why does Active Inference use generative models?
3. Define the recognition density q(s, θ). How does it relate to the true posterior p(s, θ | o)?
4. What is the mean-field approximation q(s, θ) = q(s) · q(θ)? When is it appropriate and when does it fail?
5. Define sufficient statistics for an exponential family distribution. Give examples for Gaussian, Categorical, and Dirichlet distributions.
6. How do sufficient statistics correspond to the internal states of an Active Inference agent?
7. State the Free Energy Principle precisely. What does it claim, and what does it *not* claim?
8. Write the generative model for a Hidden Markov Model with discrete states. What are the sufficient statistics of q(s)?
9. Write the generative model for a linear Gaussian state-space model. What are the sufficient statistics of q(s)?
10. Why is exact Bayesian inference intractable for most interesting models? What is the computational barrier?
11. How does the variational approach convert an intractable integration problem into a tractable optimization problem?
12. What is the evidence lower bound (ELBO)? How does it relate to model comparison?
13. Derive the optimal q*(s) under mean-field variational inference for a conjugate model.
14. What is the natural gradient? How does it relate to updating sufficient statistics efficiently?
15. How does a Partially Observed Markov Decision Process (POMDP) extend the basic HMM to include actions?
16. What is the difference between state estimation (inferring s given o) and parameter estimation (inferring θ given o)?
17. How does the concept of "model evidence" ln p(o) relate to model selection in Active Inference?
18. Compare variational inference with Markov Chain Monte Carlo (MCMC) sampling. What are the trade-offs?
19. How does amortized inference (training a neural network to approximate q) relate to the recognition density?
20. Derive the free energy for a two-level hierarchical model: p(o|s₁)p(s₁|s₂)p(s₂). How do the sufficient statistics at each level interact?
