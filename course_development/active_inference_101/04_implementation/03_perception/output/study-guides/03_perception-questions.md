# Implementation — Module 03: Perception — Study Questions

1. What is variational message passing? How does it differ from a single Bayesian update?
2. What are the three messages combined at each time step? (observations, past, future)
3. Why does the algorithm iterate multiple times (num_iter)?
4. What does `ln_A + ln_prior + ln_future` represent?
5. Why do we work in log space and then convert with softmax?
6. What is a prediction error in this implementation?
7. How is the observation prediction error computed?
8. How is the state prediction error computed?
9. What does precision weighting do to prediction errors?
10. What happens to beliefs when precision is very high?
11. What happens to beliefs when precision is very low?
12. Write the free energy decomposition: F = Complexity - Accuracy. What does each term mean in code?
13. How is accuracy computed? What does it measure?
14. How is complexity computed? What does it penalize?
15. What value of F indicates perfect inference?
16. How does the future message enable smoothing (using later observations to improve earlier estimates)?
17. What is the convergence criterion for message passing? How do you know when to stop?
18. How does this code relate to predictive coding in the brain?
19. What is the computational cost of message passing vs. exact inference?
20. How would you visualize belief updating to gain insight into the algorithm?
