# Practice Quiz: Advanced Theory

## Part A: Multiple Choice

1. Which decomposition of free energy directly implements automatic Occam's Razor?
A) Energy − Entropy
B) Complexity − Accuracy
C) Surprise + KL divergence
D) Pragmatic value + Epistemic value

2. What is the key assumption of the mean-field approximation?
A) The posterior is a Gaussian distribution
B) The posterior factorizes into independent marginals: q(s₁,s₂,...,sₙ) = ∏ᵢ qᵢ(sᵢ)
C) The generative model is a linear dynamical system
D) All hidden states have the same prior

3. What does the Fisher information matrix measure on a statistical manifold?
A) The distance between two probability distributions
B) The local curvature of the manifold — how sensitively distributions change with parameter perturbations
C) The entropy of the maximum likelihood estimate
D) The variance of the posterior distribution

4. What is the role of solenoidal flow in the Helmholtz decomposition of stochastic dynamics?
A) It performs gradient descent on the log-density, driving the system toward equilibrium
B) It creates circulation that maintains the system away from equilibrium (nonequilibrium steady state)
C) It adds noise to the system to enable exploration
D) It implements action selection by the agent

5. What does Bayesian Model Reduction (BMR) achieve computationally?
A) It refits all candidate models from scratch and compares their evidence
B) It evaluates the evidence for reduced (simpler) models from the posterior of a full model, without refitting
C) It increases model complexity to improve predictive accuracy
D) It eliminates the need for model comparison altogether

6. In the expected free energy (EFE) decomposition, what determines whether an agent explores or exploits?
A) The temperature parameter alone
B) The relative magnitude of epistemic value (information gain) vs. pragmatic value (preference satisfaction)
C) Whether the agent is in a high-reward or low-reward state
D) The number of available policies

7. How does the renormalization group (RG) formalize the scale-free property of Active Inference?
A) By showing that physical constants do not change with scale
B) By demonstrating that the same free energy minimization structure is preserved under coarse-graining transformations
C) By proving that all systems have the same number of degrees of freedom at every scale
D) By eliminating the need for Markov Blankets at macroscopic scales

## Part B: Short Answer

1. Derive the variational free energy for a Gaussian recognition density q = N(μ, Σ) paired with a Gaussian generative model. Express F in terms of the sufficient statistics and identify the accuracy and complexity terms.

2. Compare multi-agent Active Inference with classical game theory. How does Nash equilibrium appear as mutual expected free energy minimization, and what does Active Inference add beyond the classical account (e.g., recursive modeling, communication as coupled inference)?

3. Explain how deep temporal models implement hierarchical inference across timescales. Describe the architecture, the ascending/descending messages, and how precision weighting determines the relative influence of bottom-up evidence vs. top-down context.
