# Station: Perception (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Perception
- **Subtitle**: Variational Message Passing and Hierarchical Inference
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Derive predictive coding update rules as gradient descent on variational free energy under a hierarchical Gaussian generative model. Begin with the generative model specification: $v^{(i)} = g^{(i)}(v^{(i+1)}) + z^{(i)}$ where $z^{(i)} \sim \mathcal{N}(0, \Pi^{(i)-1})$, and show that VFE minimization with respect to the recognition density yields the canonical prediction error equations. Establish the formal equivalence between predictive coding and variational message passing on a hierarchical factor graph (Dauwels, 2007; Friston & Kiebel, 2009). Prove convergence conditions for the hierarchical message passing scheme — conditions on the step size, the spectral properties of the precision matrices, and the curvature of the VFE landscape. Derive the information-geometric interpretation: perceptual inference as movement along a geodesic on the statistical manifold $\mathcal{M}$ equipped with the Fisher metric, where each prediction error correction corresponds to a step in the natural gradient direction. Specify precisely when the Laplace approximation is exact (Gaussian posteriors from log-quadratic likelihoods) versus approximate, and characterize the approximation error in terms of higher-order cumulants.

## Key Concepts

- Hierarchical Gaussian generative model: $v^{(i)} = g^{(i)}(v^{(i+1)}) + z^{(i)}$ with precision-weighted prediction errors $\xi^{(i)} = \Pi^{(i)}(v^{(i)} - g^{(i)}(\mu^{(i+1)}))$
- Predictive coding update rules derived as $\dot{\mu}^{(i)} = D\mu^{(i)} + \kappa \frac{\partial F}{\partial \mu^{(i)}}$ with gradient descent on VFE
- Equivalence between predictive coding and variational message passing (VMP) on factor graphs: messages as sufficient statistics, factors as local generative model components
- Convergence of hierarchical message passing: contraction mapping conditions, Lyapunov stability of fixed points
- Information geometry of perceptual inference: inference as geodesic motion on $(\mathcal{M}, g)$, natural gradient interpretation
- Laplace approximation: exactness conditions (exponential family likelihoods), error characterization via Edgeworth expansion
- Gaussian assumptions and their limitations: when non-Gaussian posteriors require particle methods or normalizing flows

## Key References

- Friston, K. J., & Kiebel, S. (2009). Predictive coding under the free-energy principle. *Philosophical Transactions of the Royal Society B*, 364(1521), 1211-1221.
- Dauwels, J. (2007). On variational message passing on factor graphs. *IEEE International Symposium on Information Theory*, 2546-2550.
- Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology*, 76, 198-211.
- Buckley, C. L., Kim, C. S., McGregor, S., & Seth, A. K. (2017). The free energy principle for action and perception: A mathematical review. *Journal of Mathematical Psychology*, 81, 55-79.
- Winn, J., & Bishop, C. M. (2005). Variational message passing. *Journal of Machine Learning Research*, 6, 661-694.

## Prerequisite Modules

- Module 02 (Agents): The POMDP formalization and belief-space geometry provide the agent framework within which perceptual inference is formalized. The Fisher metric and natural gradient are used throughout this module.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 03): Examines the phenomenology of perception — Merleau-Ponty's embodied perception vs. Helmholtz's unconscious inference, and whether predictive coding vindicates either tradition. See [../../01_philosophical_foundations/03_perception/module.md](../../01_philosophical_foundations/03_perception/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 03): Reviews cortical evidence for predictive coding — V1 (Rao & Ballard, 1999), canonical microcircuits (Bastos et al., 2012), mismatch negativity, and precision weighting via neuromodulation. See [../../02_neuroscientific_frontiers/03_perception/module.md](../../02_neuroscientific_frontiers/03_perception/module.md).
- **Research Methods** (Unit 4, Module 03): Covers Dynamic Causal Modeling (DCM) implementation, Bayesian model comparison for testing predictive coding architectures, and computational phenotyping of perceptual inference. See [../../04_research_methods/03_perception/module.md](../../04_research_methods/03_perception/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
