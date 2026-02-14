# Station: Action (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Action
- **Subtitle**: Path Integrals, KL Control, and Optimal Policies
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Derive the path integral formulation of stochastic optimal control following Kappen (2005). Begin with the controlled diffusion $dx = (f(x) + u)\,dt + \sigma\,dW$ and the cost functional $J = \mathbb{E}\left[\Phi(x_T) + \int_0^T \left(V(x_t) + \frac{1}{2}u_t^T R\, u_t\right)dt\right]$. Show that the Hamilton-Jacobi-Bellman (HJB) equation becomes nonlinear in general, but that when the noise-control cost relationship satisfies $\sigma\sigma^T = \lambda R^{-1}$ (Kappen's condition), the Hopf-Cole transformation $\psi = \exp(-\Psi/\lambda)$ linearizes the HJB into a backward Chapman-Kolmogorov equation. Show how this linearization enables path integral computation of the optimal control. Present Todorov's (2009) KL control framework, proving that penalizing policy divergence $D_{KL}[\pi \| \pi_0]$ from a passive dynamics baseline renders the Bellman equation linear in the desirability function. Derive the expected free energy (EFE) functional $G(\pi) = \mathbb{E}_{q(o,s|\pi)}[\ln q(s|\pi) - \ln p(o,s)]$ from first principles. Show its two canonical decompositions: (1) Risk + Ambiguity: $G(\pi) = D_{KL}[q(o|\pi) \| p(o)] + \mathbb{E}_{q(s|\pi)}[H[p(o|s)]]$, and (2) Pragmatic + Epistemic value: $G(\pi) = -\mathbb{E}_{q(o|\pi)}[\ln p(o)] - I(o;s|\pi)$. Prove that policy selection via EFE minimization reduces to optimal control (when ambiguity is zero and preferences are exogenous) and to information gain maximization (when preferences are uniform), thereby unifying exploitation and exploration.

## Key Concepts

- Path integral control: linearization of HJB via Hopf-Cole transform under the condition $\sigma\sigma^T = \lambda R^{-1}$
- KL control (Todorov, 2009): cost = state cost + $\lambda D_{KL}[\pi \| \pi_0]$, linearly solvable MDPs, desirability function $z(x) = \exp(-V(x)/\lambda)$
- Expected free energy: $G(\pi) = \sum_\tau \mathbb{E}_{q(o_\tau, s_\tau|\pi)}[\ln q(s_\tau|\pi) - \ln p(o_\tau, s_\tau)]$
- Risk-Ambiguity decomposition: $G = \underbrace{D_{KL}[q(o|\pi)\|p(o)]}_{\text{Risk}} + \underbrace{\mathbb{E}_{q(s|\pi)}[H[p(o|s)]]}_{\text{Ambiguity}}$
- Pragmatic-Epistemic decomposition: $G = \underbrace{-\mathbb{E}_{q(o|\pi)}[\ln p(o)]}_{\text{Pragmatic value}} - \underbrace{I(o;s|\pi)}_{\text{Epistemic value}}$
- Policy selection as inference: $p(\pi) = \sigma(-\gamma \cdot G(\pi))$ with precision parameter $\gamma$
- Reduction to special cases: optimal control (zero ambiguity), information gain (uniform preferences), risk-sensitive control (non-unit temperature)
- Feynman-Kac formula: connection between stochastic processes and PDE solutions underlying path integral methods

## Key References

- Kappen, H. J. (2005). Path integrals and symmetry breaking for optimal control theory. *Journal of Statistical Mechanics: Theory and Experiment*, 2005(11), P11011.
- Todorov, E. (2009). Efficient computation of optimal actions. *Proceedings of the National Academy of Sciences*, 106(28), 11478-11483.
- Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Millidge, B., Tschantz, A., & Buckley, C. L. (2020). Whence the expected free energy? *Neural Computation*, 33(2), 447-482.
- Levine, S. (2018). Reinforcement learning and control as probabilistic inference: Tutorial and review. *arXiv preprint arXiv:1805.00909*.

## Prerequisite Modules

- Module 03 (Perception): The variational free energy functional and its gradient descent minimization, derived for perceptual inference, are extended here to the action domain. The Laplace approximation and message passing framework carry over directly.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 05): Examines the enactivist interpretation of action — affordances as precision-weighted predictions, motor intentionality, and the action-perception cycle as constitutive of cognition. See [../../01_philosophical_foundations/05_action/module.md](../../01_philosophical_foundations/05_action/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 05): Reviews spinal reflexes as prediction error minimization, cerebellar forward models, motor cortical hierarchies, and oculomotor control as active inference. See [../../02_neuroscientific_frontiers/05_action/module.md](../../02_neuroscientific_frontiers/05_action/module.md).
- **Research Methods** (Unit 4, Module 05): Covers experimental design for motor control and decision-making paradigms — reaching tasks, saccade experiments, force field adaptation — and fitting active inference models to behavioral data. See [../../04_research_methods/05_action/module.md](../../04_research_methods/05_action/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
