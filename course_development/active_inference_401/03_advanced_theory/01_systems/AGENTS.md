# Station: Systems (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Systems
- **Subtitle**: Bayesian Mechanics and the Physics of Beliefs
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Derive the Bayesian mechanics formalism from the Fokker-Planck equation for a system at non-equilibrium steady state (NESS). Show the Helmholtz decomposition of the flow field into solenoidal ($Q$) and dissipative ($\Gamma$) components. Derive the particular partition from the NESS density's conditional independence structure, proving that internal states parameterize a density over external states. State all regularity conditions — smoothness of the drift, ellipticity of the diffusion, existence and uniqueness of the NESS density — and specify the function spaces in which these results hold.

## Key Concepts

- NESS density $p^*(\eta, s, a, \mu)$ and its existence conditions (ergodicity, irreducibility)
- Fokker-Planck equation: $\partial_t p = -\nabla \cdot (fp) + \nabla \cdot (D \nabla p)$ and its stationary solutions
- Langevin dynamics on the full state space: $dx = f(x)\,dt + \sigma(x)\,dW$ with state-dependent diffusion
- Particular partition: decomposition into external ($\eta$), sensory ($s$), active ($a$), and internal ($\mu$) states
- Helmholtz decomposition: $f(x) = (Q(x) - \Gamma(x))\nabla \ln p^*(x)$ with antisymmetric $Q$ and positive-definite $\Gamma$
- Solenoidal flow (divergence-free, entropy-preserving) vs. dissipative flow (gradient descent on surprisal)
- Conditional independence structure: $\eta \perp\!\!\!\perp \mu \mid b$ where $b = (s, a)$ are blanket states

## Key References

- Da Costa, L., Parr, T., Sajid, N., Vesber, S., Ryan, V., & Friston, K. (2021). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology*, 99, 102447.
- Sakthivadivel, D. A. R. (2022). Bayesian mechanics of perceptual inference and motor control. *arXiv preprint arXiv:2211.XXXXX*.
- Friston, K. (2019). A free energy principle for a particular physics. *arXiv preprint arXiv:1906.10184*.
- Pavliotis, G. A. (2014). *Stochastic Processes and Applications*. Springer.
- Risken, H. (1996). *The Fokker-Planck Equation: Methods of Solution and Applications*. Springer.

## Prerequisite Modules

None — this is the entry point for Unit 3. Students should have completed the prerequisites specified in the curriculum-level AGENTS.md, particularly: measure-theoretic probability, stochastic differential equations (Ito calculus), and the Fokker-Planck equation.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 01): Examines the ontological status of self-organizing systems — autopoiesis, organizational closure, and the boundary problem. See [../../01_philosophical_foundations/01_systems/module.md](../../01_philosophical_foundations/01_systems/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 01): Reviews cortical dynamics as NESS, neural oscillations and attractors, and the criticality hypothesis. See [../../02_neuroscientific_frontiers/01_systems/module.md](../../02_neuroscientific_frontiers/01_systems/module.md).
- **Research Methods** (Unit 4, Module 01): Covers empirical identification of NESS conditions, Langevin model fitting, and SDE parameter estimation. See [../../04_research_methods/01_systems/module.md](../../04_research_methods/01_systems/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
