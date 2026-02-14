# Mathematical Frameworks — Module 06: Learning — Study Questions

1. What is parameter learning? What is being updated?
2. What is a Dirichlet distribution? Why is it used for model parameters?
3. What are concentration parameters α? What do they represent?
4. How does updating α work? What happens each time a (state, observation) pair is observed?
5. What is Dirichlet-Categorical conjugacy? Why is it computationally convenient?
6. How does confidence relate to the sum of concentration parameters?
7. Explain why the effective learning rate decreases naturally with experience.
8. Why is it optimal for early observations to have more influence than later ones?
9. What is structure learning? How does it differ from parameter learning?
10. What is Bayesian Model Reduction (BMR)? What does it compare?
11. How does BMR implement Occam's razor?
12. When does BMR typically occur? (Online or offline? Waking or sleeping?)
13. Why is BMR computationally cheap compared to learning the full model from scratch?
14. Explain the timescale separation between perception and learning.
15. Why does the mathematical formulation naturally produce slow learning and fast perception?
16. How do small vs. large concentration parameters affect the agent's flexibility?
17. How does this mathematical framework explain why children learn faster than adults?
18. What happens if α is reset to small values? What does this correspond to biologically?
19. Can the agent's learned model be wrong? How would this manifest mathematically?
20. Connect the mathematical description of learning to the cognitive science (Unit 1) and neuroscience (Unit 2) accounts.
