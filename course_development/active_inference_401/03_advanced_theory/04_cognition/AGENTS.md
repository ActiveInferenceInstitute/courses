# Station: Cognition (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Cognition
- **Subtitle**: Variational Methods: Mean-Field, Bethe, and Message Passing
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Present the hierarchy of variational approximations in order of decreasing tightness: exact inference $\to$ structured mean-field (tree-structured) $\to$ naive mean-field (fully factored) $\to$ Laplace approximation. For each level, state the variational family, the resulting free energy functional, and the gap between the approximation and the exact log model evidence. Derive the Bethe free energy $F_{\text{Bethe}}$ as a relaxation of the exact variational free energy, showing that it replaces the global entropy $H[q]$ with a sum of local entropies corrected by counting numbers. Prove the central result of Yedidia, Freeman, and Weiss (2005): that the fixed points of loopy belief propagation are stationary points of the Bethe free energy — i.e., $\nabla_{b_\alpha, b_i} \mathcal{L}_{\text{Bethe}} = 0$ if and only if the BP messages have converged. Derive variational message passing (VMP) for conjugate-exponential models, showing that each VMP update corresponds to a natural gradient step. State convergence guarantees: BP is guaranteed to converge on tree-structured graphs (exactness of junction tree algorithm), may diverge on loopy graphs (provide counterexamples), and VMP converges for models in the conjugate-exponential family. Present factor graph representations and the relationship between the graphical model structure and the form of the variational approximation.

## Key Concepts

- Variational families: mean-field $q(\mathbf{s}) = \prod_i q_i(s_i)$, structured $q(\mathbf{s}) = \prod_\alpha q_\alpha(s_\alpha)$, Laplace (Gaussian centered at MAP)
- Bethe free energy: $F_{\text{Bethe}} = \sum_\alpha \sum_{\mathbf{s}_\alpha} b_\alpha(\mathbf{s}_\alpha)\ln\frac{b_\alpha(\mathbf{s}_\alpha)}{f_\alpha(\mathbf{s}_\alpha)} - \sum_i (d_i - 1) \sum_{s_i} b_i(s_i)\ln b_i(s_i)$ with counting numbers and local beliefs
- Belief propagation (BP): message update rules $m_{f \to x}(x) \propto \sum_{\sim x} f(\mathbf{x})\prod_{y \neq x} m_{y \to f}(y)$, convergence on trees, potential divergence on loopy graphs
- Yedidia-Freeman-Weiss theorem: BP fixed points $\Leftrightarrow$ stationary points of $F_{\text{Bethe}}$
- Variational message passing (VMP): update rule $\ln q_i^*(s_i) = \mathbb{E}_{q_{\setminus i}}[\ln p(\mathbf{s}, \mathbf{o})] + \text{const}$ for conjugate-exponential models
- Convergence theory: sufficient conditions (convexity of $F_{\text{Bethe}}$, tree structure, damping), failure modes (multimodal posteriors, strong loops)
- Factor graphs: Forney-style (edges = variables, nodes = factors) vs. bipartite (two node types), and the mapping between graph structure and variational approximation quality

## Key References

- Wainwright, M. J., & Jordan, M. I. (2008). Graphical models, exponential families, and variational inference. *Foundations and Trends in Machine Learning*, 1(1-2), 1-305.
- Yedidia, J. S., Freeman, W. T., & Weiss, Y. (2005). Constructing free-energy approximations and generalized belief propagation algorithms. *IEEE Transactions on Information Theory*, 51(7), 2282-2312.
- Dauwels, J. (2007). On variational message passing on factor graphs. *IEEE International Symposium on Information Theory*, 2546-2550.
- Parr, T., Markovic, D., Kiebel, S. J., & Friston, K. J. (2019). Neuronal message passing using mean-field, Bethe, and marginal approximations. *Scientific Reports*, 9(1), 1889.
- Minka, T. P. (2001). Expectation propagation for approximate Bayesian inference. *Proceedings of the 17th Conference on Uncertainty in Artificial Intelligence*, 362-369.

## Prerequisite Modules

- Module 03 (Perception): The derivation of predictive coding as VFE minimization provides the foundational example of variational inference in hierarchical models. The Laplace approximation and its limitations, introduced in Module 03, are generalized here to the full hierarchy of variational methods.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 04): Examines extended cognition and whether variational approximations constitute genuine cognitive processes, engaging with the parity principle and cognitive integration debates. See [../../01_philosophical_foundations/04_cognition/module.md](../../01_philosophical_foundations/04_cognition/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 04): Reviews prefrontal hierarchies, precision-weighted attention as gain modulation, and neural implementations of belief propagation in cortical circuits. See [../../02_neuroscientific_frontiers/04_cognition/module.md](../../02_neuroscientific_frontiers/04_cognition/module.md).
- **Research Methods** (Unit 4, Module 04): Covers practical Bayesian model comparison — BMS, family inference, protected exceedance probability — and structure learning in applied settings. See [../../04_research_methods/04_cognition/module.md](../../04_research_methods/04_cognition/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
