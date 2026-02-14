# Study Questions: Cognition

1. What does each entry of the C-vector represent, and on what scale is it expressed (linear probability, log probability, or utility)?

2. Write the formula for the preferred observation distribution $\tilde{P}(o)$ in terms of the C-vector. What function converts C to a valid probability distribution?

3. If `C = np.zeros(num_obs)`, what does the risk term in EFE evaluate to? What type of behavior results?

4. Construct a C-vector for a 4-observation system where observation 2 is strongly preferred, observations 0 and 1 are neutral, and observation 3 is strongly avoided.

5. Explain the difference between $D$ (prior over initial states) and $q(s)$ (current posterior). When are they equal?

6. If $D = [1, 0, 0]$, the agent starts with zero entropy over initial states. What is the computational implication for the first state inference step?

7. What validation does `GenerativeModel` perform on the D-vector? Write the two conditions that must hold.

8. How does the E-vector enter the policy posterior formula? Write the equation for $q(\pi)$ with and without E.

9. If `E = np.array([0.99, 0.005, 0.005])` and γ = 0.01, which policy will the agent almost certainly select? Why?

10. What happens to policy selection when γ = 0? Does the agent still use EFE, or does it rely entirely on E?

11. Design an experiment that isolates the effect of the C-vector: keep A, B, D, E, and γ fixed, vary only C, and predict how agent behavior changes.

12. Explain precision γ in terms of the inverse temperature of a Boltzmann distribution. What is the policy posterior equation in this form?

13. How would you use `plot_C_preferences()` to verify that your C-vector matches your intended preference structure? What should you look for in the plot?

14. What does `plot_D_prior()` annotate on the bar chart beyond the prior probabilities? Why is this annotation useful?

15. Write code to create two agents with identical A, B, C, D but different E-vectors, run them in the same environment, and compare their action sequences.

16. At what value of γ does the policy posterior transition from near-uniform to near-deterministic? How would you determine this experimentally?

17. Use `plot_precision_sweep()` to visualize $q(\pi)$ across γ values. Describe the expected shape of the curves.

18. If C-vector entries are in log-probability, can negative C values occur? What do they mean?

19. How would you model an agent that prefers to stay in its current state? Which component(s) — C, D, E, or B — would you modify?

20. Explain why an agent with strong C-preferences and low γ might still act randomly. What is the mathematical mechanism?
