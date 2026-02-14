# Lab: Advanced Theory of Active Inference

## Objective

Perform original mathematical work that extends, generalizes, or rigorously analyzes a core formal result in the Active Inference literature. This lab demands facility with variational calculus, information geometry, category theory, or stochastic analysis as appropriate to the chosen problem.

## Prerequisites

- Graduate-level proficiency in variational calculus (functional derivatives, Euler-Lagrange equations)
- Working knowledge of information geometry (Fisher metric, statistical manifolds, natural gradients)
- Familiarity with category theory (functors, natural transformations, lenses) or willingness to acquire it
- Competence in stochastic differential equations and Fokker-Planck dynamics
- Facility with a computational algebra system (SymPy, Mathematica) or probabilistic programming language (Julia/Turing.jl, Python/NumPyro)

## Part 1: Formal Derivation

Choose **one** of the following derivation exercises:

### Option A: Variational Free Energy Decomposition
1. Starting from the joint density p(o, s) and a variational density q(s), derive the variational free energy F = E_q[ln q(s) - ln p(o, s)].
2. Prove the decomposition F = D_KL[q(s) || p(s|o)] - ln p(o), establishing that F is an upper bound on negative log model evidence.
3. Extend the derivation to the **Bethe free energy** on a factor graph. Show under what graphical conditions the Bethe approximation is exact (trees) and characterize the error on loopy graphs.

### Option B: Path Integral Formulation
1. Starting from the Langevin equation dx = f(x)dt + sigma dW, derive the path integral representation of the transition density.
2. Show that the most likely path satisfies a variational principle (Hamilton's principle with dissipation).
3. Connect this to the Active Inference formulation: demonstrate that free energy minimizing trajectories correspond to solutions of a particular Hamilton-Jacobi-Bellman equation under KL control cost.

### Option C: Category-Theoretic Formulation
1. Formalize Bayesian updating as a morphism in the category **Stoch** of Markov kernels.
2. Show that the composition of Bayesian updates satisfies the lens laws (get/put coherence) in the category of dependent lenses.
3. Formalize the Markov blanket partition as a structured decomposition in polynomial functors and discuss how Active Inference arises as a natural transformation between appropriate functors.

## Part 2: Numerical Verification

1. Implement the derived equations numerically in Python or Julia.
2. For Option A: Compare variational, Bethe, and exact posteriors on a benchmark factor graph (e.g., Ising model, hidden Markov model).
3. For Option B: Numerically integrate the path integral and compare the most likely path with direct simulation of the Langevin equation.
4. For Option C: Implement compositional Bayesian inference using a categorical programming framework (e.g., CatLab.jl or custom implementation) and verify lens coherence laws.
5. Quantify numerical accuracy: report convergence rates, approximation errors, and computational cost.

## Part 3: Open Problem Exploration

1. Identify an **open problem** connected to your derivation (e.g., convergence guarantees for loopy belief propagation, path integral approximations for high-dimensional systems, functorial semantics for hierarchical generative models).
2. State the problem precisely in mathematical terms.
3. Outline a research strategy: what tools, techniques, or new results would be needed?
4. Provide at least one partial result, conjecture, or numerical observation.

## Deliverables

- A formal mathematical document (LaTeX-quality, 10--20 pages) containing all derivations with complete proofs
- Annotated source code for numerical verification
- A 1-page research prospectus for the open problem identified in Part 3

## Discussion Requirements

- Present your derivation at the blackboard (or digital equivalent) with full mathematical rigor
- Be prepared to justify each step and respond to requests for alternative proof strategies
- Discuss connections between your chosen option and the other two options (e.g., how the category-theoretic formulation relates to the variational and path integral approaches)
