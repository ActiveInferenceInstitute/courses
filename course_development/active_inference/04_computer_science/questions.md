# Study Questions: Computational Active Inference

1. Explain the distinction between the generative process and the generative model in computational Active Inference. What Python classes represent each in the `active_inference` library, and what matrices does each contain?

2. Describe the A matrix (likelihood matrix) in detail. What do its rows and columns represent? What constraint must each column satisfy, and why?

3. How is the B matrix (transition matrix) structured when there are multiple actions? Explain the tensor indexing B[s', s, a] and give an example for a 2-state, 2-action system.

4. What role does the C vector play in policy selection? How does changing C from uniform to strongly preferring one outcome alter the agent's behavior?

5. Explain the D vector (initial state prior) and the E vector (habit prior). Under what conditions would the E vector significantly influence policy selection?

6. Walk through one iteration of the variational belief updating (fixed-point iteration) algorithm. Starting from a prior belief and an observation, show how the posterior is computed using the A matrix.

7. Derive the expected free energy G for a single policy in a discrete system. Show how the risk and ambiguity components arise from the A matrix, the C vector, and the current beliefs.

8. How does the softmax precision parameter gamma affect policy selection? What happens as gamma approaches zero (uniform random) and as gamma approaches infinity (greedy selection)?

9. Describe how Dirichlet concentration parameters pA are initialized and updated during online learning. What is the relationship between concentration parameters and the expected likelihood matrix?

10. Explain how Bayesian Model Reduction works computationally. Given a full model and a reduced model, how are the reduced model's parameters derived without refitting?

11. In a multi-agent simulation, how are two Active Inference agents coupled? Specifically, how does one agent's action become another agent's observation?

12. What is a deep temporal model? How does extending the planning horizon from T=1 to T>1 change the computation of expected free energy?

13. Describe the T-maze benchmark task. What are the states, observations, and actions? Why does the optimal agent visit the cue location before choosing an arm?

14. How would you diagnose an agent that consistently chooses suboptimal policies? What parameters (A, B, C, D, E, gamma) would you inspect, and what patterns would indicate specific problems?

15. Explain the role of the `active_inference` visualization module. How do functions like `plot_beliefs`, `plot_free_energy`, and `plot_efe_components` help diagnose agent behavior?
