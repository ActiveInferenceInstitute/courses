# Advanced Theory — Module 01: Systems — Study Questions

1. Why is variational calculus (optimization over function spaces) necessary for Active Inference, rather than ordinary calculus (optimization over parameter spaces)?
2. Derive the free energy functional from Bayes' theorem and Jensen's inequality. At which step does the approximation enter, and what is lost?
3. Why is ln p(o|m) generally intractable? Give a concrete example where the marginal likelihood integral cannot be computed in closed form.
4. What is the Euler-Lagrange equation? How does it apply to finding the distribution q*(s) that minimizes free energy?
5. Explain the three decompositions of free energy: (Energy − Entropy), (Complexity − Accuracy), (Surprise + KL). Which decomposition is most useful for understanding (a) perception, (b) learning, (c) model comparison?
6. Why does the complexity−accuracy decomposition implement automatic Occam's Razor? Show mathematically that a model with unnecessarily many parameters will have higher free energy.
7. When does minimizing free energy equal exact Bayesian inference? What is the KL divergence term, and when is it exactly zero?
8. What is the mean-field approximation? What does the assumption q(s₁,s₂,...,sₙ) = ∏ᵢ qᵢ(sᵢ) gain and lose? Give a concrete example where mean-field fails badly.
9. Compare the Bethe approximation with mean-field. Why does allowing pairwise interactions improve the approximation? How does this relate to belief propagation?
10. What is the Laplace approximation? When is it appropriate and when does it fail? Why is it the basis of DCM (Dynamic Causal Modelling)?
11. How does variational message passing on factor graphs implement distributed free energy minimization? What are the "messages" in neural terms?
12. Derive the fixed-point equation for the mean-field update: qᵢ*(sᵢ) ∝ exp(E_{q₋ᵢ}[ln p(o,s)]). Why is this an iterative scheme?
13. What is the relationship between free energy and thermodynamic free energy (Helmholtz/Gibbs)? Is the analogy merely formal or does it reflect deep structural identity?
14. How does the evidence lower bound (ELBO) in machine learning relate to variational free energy in Active Inference? Are they the same quantity?
15. How does natural gradient descent differ from standard gradient descent for free energy minimization? Why might it be a better model of neural dynamics?
16. What is the free energy of a Gaussian recognition density q = N(μ, Σ)? Express F in terms of the mean and covariance of q and the sufficient statistics of the generative model.
17. How does expected free energy (EFE) differ from variational free energy (VFE)? Why is EFE needed for action selection while VFE suffices for perception?
18. Derive the decomposition of EFE into pragmatic value and epistemic value. Under what conditions does exploration dominate? Under what conditions does exploitation dominate?
19. How does the C vector (preferences) enter the EFE? What happens to policy selection when C is flat (no preferences)?
20. Critically evaluate: Are there alternative variational bounds (e.g., Rényi divergence, χ²-divergence) that might be tighter or more biologically plausible than the KL-based ELBO? What would change if Active Inference used a different divergence?
