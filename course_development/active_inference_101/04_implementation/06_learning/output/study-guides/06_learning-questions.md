# Implementation — Module 06: Learning — Study Questions

1. What are Dirichlet concentration parameters? How do they differ from the A/B matrices themselves?
2. How does `_dirichlet_mean` compute the expected value of the A matrix?
3. What does `update_A` do? What is the outer product computing?
4. What does `update_B` do? Why does it need both previous and current beliefs?
5. How does `get_effective_learning_rate` work? What determines the rate?
6. Why does the learning rate decrease with more experience?
7. What initialization of concentration parameters gives a uniform prior?
8. What initialization gives a strong prior (confident initial model)?
9. How does the agent's performance change across episodes?
10. What is the relationship between A_prior and the initial A matrix?
11. How would you implement "forgetting" (resetting concentration parameters)?
12. What is the computational cost of learning updates?
13. How does learning interact with inference (state estimation)?
14. Can the agent learn a wrong model? What would cause this?
15. How does this compare to gradient-based learning in neural networks?
16. What tests would verify that learning is working correctly?
17. How would you implement B matrix learning for the T-Maze?
18. What is the difference between online and offline learning in this framework?
19. How would you implement Bayesian Model Reduction in code?
20. How does this code relate to synaptic plasticity in the brain?
