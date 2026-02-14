# Study Questions: The Mathematics of Active Inference

1. State Bayes' theorem and explain each term (prior, likelihood, evidence, posterior) in the context of an Active Inference agent updating its beliefs about hidden states given an observation.

2. Define the Kullback-Leibler divergence D_KL(q || p) and explain why it is always non-negative. What does it mean for D_KL to equal zero?

3. Derive the variational free energy F as an upper bound on surprise. Show the decomposition into complexity and accuracy terms and explain the intuition behind each.

4. What is the relationship between variational free energy and the Evidence Lower Bound (ELBO)? Prove that minimizing F is equivalent to maximizing the ELBO.

5. Write the Langevin equation for a system with Markov Blanket partition. Explain each term: the flow field, the random fluctuations, and the constraint imposed by the Blanket structure.

6. Describe the Fokker-Planck equation and explain how it governs the evolution of probability density over time. What is the significance of the nonequilibrium steady-state solution?

7. Derive the expected free energy G for a discrete-state-space agent. Show how it decomposes into risk (pragmatic value) and ambiguity (epistemic value).

8. Explain how the softmax function converts expected free energy values into a probability distribution over policies. What role does the precision parameter gamma play?

9. Describe the fixed-point iteration scheme for state inference (belief updating). What conditions guarantee convergence, and how does precision weighting affect the dynamics?

10. Define a hierarchical generative model with two levels. Write the message passing equations for precision-weighted prediction errors flowing between levels.

11. Explain Bayesian Model Reduction. How does it allow comparison of nested models without refitting, and what is the role of the Occam factor?

12. What is the Dirichlet distribution, and how is it used for parameter learning in Active Inference? Show how Dirichlet concentration parameters are updated after observing a state-observation pair.

13. Define mutual information I(X; Y) in terms of entropy and conditional entropy. How does mutual information relate to the epistemic component of expected free energy?

14. Describe generalized synchrony between two coupled dynamical systems. How does Active Inference formalize communication as the mutual minimization of free energy between coupled agents?

15. Derive the recursive belief updating equations for sophisticated inference (planning). How does the tree search over policies extend single-step expected free energy to multi-step horizons?
