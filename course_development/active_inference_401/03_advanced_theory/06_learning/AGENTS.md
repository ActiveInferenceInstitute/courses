# Station: Learning (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Learning
- **Subtitle**: Bayesian Mechanics, Structure Learning, and Model Evidence
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Derive the variational Laplacian — the Laplace approximation to the variational posterior, where $q(s) = \mathcal{N}(\mu, \Sigma)$ with $\mu = \arg\min_s F(s)$ and $\Sigma^{-1} = \nabla^2 F \big|_{s=\mu}$. Show that the variational free energy $F = -\ln p(o \mid m) + D_{KL}[q(s) \| p(s \mid o, m)]$ is an upper bound on negative log model evidence $-\ln p(o \mid m)$, and characterize the tightness of this bound: it is tight if and only if $q(s) = p(s \mid o, m)$, with the gap given exactly by $D_{KL}[q \| p(\cdot \mid o, m)]$. Derive Bayesian model reduction (BMR) as a method for post-hoc model comparison: given a full model posterior $q(s \mid m_{\text{full}})$, show that the evidence for a reduced model $m_{\text{red}}$ (differing only in priors) can be computed analytically as $\ln p(o \mid m_{\text{red}}) \approx \ln p(o \mid m_{\text{full}}) + \ln \mathbb{E}_{q(s \mid m_{\text{full}})}\left[\frac{p(s \mid m_{\text{red}})}{p(s \mid m_{\text{full}})}\right]$ without re-inverting the model. Present structure learning as model evidence optimization over a discrete space of model structures $\{m_1, \ldots, m_K\}$, where each structure specifies the graphical model topology. Prove the asymptotic relationships between information criteria: show that the Bayesian Information Criterion (BIC) approximates $-2\ln p(o \mid m) \approx -2\ln p(o \mid \hat{\theta}, m) + k\ln n$ via Laplace's method, that AIC corresponds to a different asymptotic regime, and that VFE interpolates between these bounds under different regularity conditions.

## Key Concepts

- Variational Laplacian: $q^*(s) = \mathcal{N}(\mu^*, \Sigma^*)$ where $\mu^* = \arg\min_s F$ and $\Sigma^{*-1} = \nabla^2_s F\big|_{\mu^*}$ — conditions for validity (unimodal posterior, sufficient smoothness)
- VFE as evidence bound: $F[q, o] = -\ln p(o|m) + D_{KL}[q(s)\|p(s|o,m)] \geq -\ln p(o|m)$ — tightness controlled by posterior approximation quality
- Bayesian model reduction (BMR): analytic model comparison via prior ratio integration — $\Delta F = \ln \mathbb{E}_q[p(s|m_{\text{red}})/p(s|m_{\text{full}})]$ — applicable when models differ only in priors
- Bayesian model comparison: $p(m|o) \propto p(o|m)p(m)$ — model evidence as the arbiter, Occam's razor as automatic complexity penalization
- Structure learning: search over model topologies $\mathcal{G}$ by comparing $\ln p(o|m_\mathcal{G})$ — greedy algorithms, score-based methods
- Information criteria relationships: BIC $\approx$ VFE (large $n$, regular models), AIC $\approx$ VFE (small $n$ or singular models), DIC for hierarchical models
- Parameter learning timescales: fast inference ($q(s)$ converges within a trial) vs. slow learning ($\theta$ updates across trials via sufficient statistic accumulation)

## Key References

- Friston, K., Parr, T., & Zeidman, P. (2018). Bayesian model reduction. *arXiv preprint arXiv:1805.07092*.
- Friston, K., & Penny, W. (2011). Post hoc Bayesian model selection. *NeuroImage*, 56(4), 2089-2099.
- Friston, K., Litvak, V., Oswal, A., Razi, A., Stephan, K. E., van Wijk, B. C. M., Ziegler, G., & Zeidman, P. (2016). Bayesian model reduction and empirical Bayes for group (DCM) studies. *NeuroImage*, 128, 413-431.
- Ghahramani, Z. (2015). Probabilistic machine learning and artificial intelligence. *Nature*, 521(7553), 452-459.
- Schwarz, G. (1978). Estimating the dimension of a model. *The Annals of Statistics*, 6(2), 461-464.

## Prerequisite Modules

- Module 04 (Cognition): The hierarchy of variational approximations (mean-field, Bethe, structured) provides the computational substrate upon which learning operates. The VMP framework and factor graph formulations from Module 04 are extended here to the model comparison and structure learning setting.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 06): Examines the epistemology of model revision — Kuhnian paradigm shifts as structure learning, abductive inference, and Bayesian epistemology. See [../../01_philosophical_foundations/06_learning/module.md](../../01_philosophical_foundations/06_learning/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 06): Reviews the neural substrates of learning — Hebbian plasticity as VFE minimization, dopaminergic and cholinergic precision weighting, and sleep consolidation as offline model optimization. See [../../02_neuroscientific_frontiers/06_learning/module.md](../../02_neuroscientific_frontiers/06_learning/module.md).
- **Research Methods** (Unit 4, Module 06): Covers practical model fitting — parameter estimation via EM and variational Bayes, parameter recovery studies, simulation-based calibration, and posterior predictive checks. See [../../04_research_methods/06_learning/module.md](../../04_research_methods/06_learning/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
