# Study Questions: Action

1. Write the action equation da/dt = -∂F/∂a. Explain the chain rule decomposition through sensory states.
2. Why does action minimize the *same* objective function (free energy) as perception? What is the difference in mechanism?
3. Define Expected Free Energy G(π). How does it differ from variational free energy F?
4. Derive the decomposition of G into pragmatic value and epistemic value (ambiguity).
5. Derive the alternative decomposition of G into information gain and pragmatic value.
6. What is the C vector in the POMDP framework? How does it encode preferences?
7. Explain the softmax policy selection P(π) = σ(-γ · G(π)). What is the role of the inverse temperature γ?
8. How does the exploration-exploitation trade-off emerge naturally from the EFE decomposition?
9. What happens when epistemic value dominates pragmatic value? When pragmatic value dominates?
10. Define the A, B, C, D matrices of the POMDP. How does each correspond to a component of the generative model?
11. How does Active Inference differ from reinforcement learning in its treatment of action selection?
12. What is the relationship between Expected Free Energy and the KL control framework?
13. Derive the EFE for a simple two-state, two-action, two-observation POMDP.
14. How does temporal depth (planning horizon T) affect the Expected Free Energy computation?
15. What is the computational complexity of evaluating G(π) for all possible policies? How can this be managed?
16. How does the concept of habits relate to policies with consistently low EFE?
17. What is the relationship between EFE and the value function in reinforcement learning?
18. How does risk sensitivity emerge from the pragmatic value component of EFE?
19. Compare EFE with the concept of empowerment (maximum mutual information between actions and future states).
20. Derive the update equations for the inverse temperature γ as a precision parameter on policy selection.
