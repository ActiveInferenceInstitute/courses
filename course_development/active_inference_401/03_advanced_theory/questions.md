# Study Questions: Advanced Theory

1. Derive the variational free energy functional from Bayes' theorem and Jensen's inequality. Identify the step where the approximation enters and explain what is lost.

2. Compare the three decompositions of free energy — (Energy − Entropy), (Complexity − Accuracy), (Surprise + KL divergence) — and explain which decomposition is most illuminating for perception, learning, and model comparison respectively.

3. How do the mean-field, Bethe, and Laplace approximations differ in their assumptions and applicability? Give a concrete example where each approximation is appropriate and one where each fails.

4. What is the Fisher information matrix, and how does it define the geometry of a statistical manifold? Show that the Fisher metric is the local quadratic approximation to KL divergence.

5. Explain natural gradient descent. Why is parameterization-invariance important for neural implementations of free energy minimization?

6. State the Free Energy Lemma. Under what conditions do the dynamics of internal states (behind a Markov blanket) approximate variational free energy minimization?

7. Explain the Helmholtz decomposition of stochastic dynamical flow into dissipative and solenoidal components. What is the role of each component in maintaining a nonequilibrium steady state?

8. How do deep temporal models implement hierarchical inference across multiple timescales? Describe the architecture, the ascending/descending messages, and how precision weighting determines the balance between bottom-up and top-down influence.

9. Derive the decomposition of expected free energy (EFE) into pragmatic value and epistemic value. Under what conditions does exploration dominate exploitation, and vice versa?

10. What is the renormalization group (RG), and how does it formalize scale-free properties of Active Inference? How does RG coarse-graining correspond to Bayesian Model Reduction?

11. What evidence supports the hypothesis that the brain operates near a critical point? Why would criticality be computationally advantageous for inference?

12. What is Bayesian Model Reduction (BMR)? Derive its formula under the Laplace approximation and explain how it avoids refitting reduced models from scratch.

13. How does structure learning differ from parameter learning? Compare score-based, constraint-based, and BMR-based approaches to structure learning.

14. How does multi-agent Active Inference extend the single-agent framework? Explain recursive modeling (Theory of Mind levels), communication as coupled inference, and Nash equilibrium as mutual expected free energy minimization.

15. How does the formal analogy between thermodynamic free energy (Helmholtz/Gibbs) and variational free energy reflect a deep structural identity or merely a superficial mathematical coincidence?

16. What is the relationship between rate-distortion theory, the complexity cost in free energy, and the brain's coding efficiency?

17. How does "dual aspect monism" in Bayesian mechanics relate internal state dynamics to belief dynamics? What is the role of gauge symmetry in this mapping?

18. Compare Active Inference with reinforcement learning, optimal control theory, and information-theoretic frameworks. What does Active Inference uniquely provide — built-in exploration, Occam's Razor, or unified perception-action?

19. How do the mathematical tools developed across this track (variational calculus, information geometry, Bayesian mechanics, renormalization group, Bayesian model selection, multi-agent theory) interconnect to form a coherent mathematical framework?

20. Critically evaluate: What are the genuine mathematical limitations of Active Inference? Where does the variational approximation fail, and what alternative approaches (e.g., particle methods, amortized inference, Rényi divergences) might extend its reach?
