# Implementation — Module 08: Planning — Study Questions

1. What are the four subsystems of the CompleteActiveInferenceAgent?
2. How does the constructor initialize learning parameters?
3. What does `policy_prior` represent? How does it start?
4. How does `select_action` combine EFE and habit priors?
5. What does `log_pi = -γG + log(policy_prior)` compute?
6. How does `learn` update both the A and B matrices?
7. What does `update_habits` do? How does it change the policy prior?
8. Walk through `agent.step(observation)` — what happens in order?
9. How does habit entropy change over time? What does low entropy mean?
10. How does the learning rate evolve as the agent gains experience?
11. What is the relationship between habit strength and goal-directed behavior?
12. When does the agent transition from goal-directed to habitual behavior?
13. How would you implement "dehabituation" (breaking a habit)?
14. What is the computational complexity of the complete step?
15. How would you extend this to multi-step planning with deeper policies?
16. What tests would verify that all four subsystems work together correctly?
17. How does this agent compare to a reinforcement learning agent?
18. What are the key advantages of this implementation over traditional RL?
19. How does the logging support understanding agent behavior?
20. Reflecting on the entire Implementation unit: how does writing code deepen understanding of Active Inference compared to reading equations or theory?
