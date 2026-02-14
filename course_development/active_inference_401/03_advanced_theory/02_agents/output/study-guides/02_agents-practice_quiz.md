# Practice Quiz: Agents / Information Geometry (Advanced Theory)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** A statistical manifold is:
A) Any high-dimensional space
B) The space of all probability distributions parameterized by θ, equipped with the Fisher information metric — a Riemannian manifold where distance reflects distributional difference
C) A physical surface
D) A computational graph

**2.** The Fisher information matrix measures:
A) Brain activity
B) The sensitivity of a distribution to parameter changes — how much the distribution shifts for infinitesimal parameter perturbations
C) Physical energy
D) Computational complexity

**3.** The natural gradient G⁻¹∇F differs from the Euclidean gradient ∇F because:
A) It is always smaller
B) It accounts for manifold curvature — providing the steepest descent direction in distributional space rather than parameter space
C) It ignores the objective
D) It is random

**4.** Dual flatness of exponential families means:
A) The manifold is always flat
B) The manifold is flat in natural parameter coordinates (η) and simultaneously flat in expectation parameter coordinates (m) — with dually flat connections
C) There are two manifolds
D) Parameters are always positive

**5.** Belief updating as geodesic flow means:
A) Beliefs travel in straight lines
B) The optimal belief update follows the shortest path on the statistical manifold — minimizing unnecessary distributional change
C) Beliefs are static
D) The brain uses GPS

**6.** The Fisher metric's connection to KL divergence is:
A) They are unrelated
B) D_KL[q(θ) || q(θ+dθ)] ≈ ½ dθᵀ G(θ) dθ — the Fisher metric is the local quadratic approximation to KL divergence
C) KL is always larger
D) Fisher is always zero

**7.** The Cramér-Rao bound in information geometry establishes that:
A) All estimators are equally good
B) The inverse Fisher information sets a lower bound on the variance of any unbiased estimator — connecting geometry to statistical efficiency
C) Estimation is impossible
D) The bound only applies to Gaussians

**8.** Amari's α-divergences generalize KL divergence by:
A) Making it symmetric
B) Parameterizing a family of divergences with different geometric properties — including KL (α=1), reverse KL (α=-1), and Hellinger (α=0)
C) Removing all divergence
D) Only applying to discrete distributions

## Part B: Short Answer

**1.** A researcher models neural population activity as a multivariate Gaussian. After observing new data, the posterior moves from N(μ₁, Σ₁) to N(μ₂, Σ₂). Explain why the Euclidean distance ‖μ₂ - μ₁‖ is a poor measure of this belief update, while the Fisher-Rao distance captures the true distributional change. (200 words)

**2.** The natural gradient has been called "the steepest descent in Riemannian space." Explain in concrete terms what this means for variational inference: when does the natural gradient disagree most strongly with the Euclidean gradient, and what are the practical consequences for convergence? (200 words)

## Part C: Essay Questions

**1.** Derive the Fisher information matrix for the multivariate Gaussian family N(μ, Σ). Show that the Fisher metric depends on Σ (the manifold is curved). Interpret this geometrically: why do equal parameter steps correspond to unequal distributional changes? (500 words, include derivation)

**2.** Compare natural gradient descent with other optimization methods (Adam, SGD, Newton's method) for variational inference. What are the computational advantages and disadvantages of each? Under what conditions does the natural gradient significantly outperform alternatives? Why might the brain use natural gradients despite the computational cost of inverting G? (400 words)

**3.** How does information geometry connect to thermodynamics? Both involve Riemannian metrics on state spaces (Fisher metric on distributions, thermodynamic metric on equilibrium states). What is the physical meaning of geodesic flow in each context? Can this connection illuminate the Free Energy Principle's relationship between inference and physics? (400 words)
