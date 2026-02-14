# Practice Quiz: Systems (Advanced Theory)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Variational free energy is defined as:
A) The temperature of a system
B) F[q] = E_q[-ln p(o, s)] + E_q[ln q(s)] = Energy + negative Entropy, an upper bound on negative log model evidence
C) The total energy of a physical system
D) The cost of computation

**2.** The Complexity minus Accuracy decomposition shows that:
A) More complex models are always better
B) Free energy minimization automatically balances model complexity (KL from prior) against data fit (expected log-likelihood) — implementing Occam's Razor
C) Accuracy is irrelevant
D) Complexity should be maximized

**3.** The mean-field approximation assumes:
A) All variables interact
B) The approximate posterior factorizes into independent groups: q(s₁, s₂, ...) = ∏ᵢ qᵢ(sᵢ)
C) Variables are deterministic
D) The model is linear

**4.** On a factor graph, free energy decomposes into:
A) A single global quantity
B) Local free energies at each factor node, enabling distributed message-passing optimization
C) Random components
D) Physical energies

**5.** The Laplace approximation:
A) Is always exact
B) Approximates the posterior as a Gaussian centered at the MAP estimate — efficient but misses multimodality
C) Uses sampling
D) Requires infinite computation

**6.** When q(s) = p(s|o) exactly:
A) Free energy is maximized
B) F[q] = -ln p(o) — free energy equals negative log evidence, and the KL approximation error is zero
C) The model is wrong
D) Entropy is zero

**7.** KL divergence's mode-seeking property (D_KL[q||p]) means:
A) q spreads everywhere
B) The variational approximation tends to "lock onto" one mode of p, potentially missing others
C) q is always uniform
D) KL is symmetric

## Part B: Essay Questions

**1.** Derive the free energy functional from first principles for a general generative model p(o, s). Show all three decompositions. For each decomposition, explain the computational significance — what does each term tell the brain (or the modeler) about the quality of inference? (500 words, include mathematical notation)

**2.** Compare mean-field variational inference, the Laplace approximation, and belief propagation (Bethe). For each: state the factorization assumption, derive the update equations, identify when it works well and when it fails. Which is most biologically plausible, and why? (500 words)

**3.** The free energy principle claims that all self-organizing systems minimize variational free energy. But variational free energy requires a generative model, an approximate posterior, and a definition of "observations." Critically examine: what is the justification for applying this mathematical framework to physical systems (not just brains)? Where does the framework break down at the boundaries? (400 words)
