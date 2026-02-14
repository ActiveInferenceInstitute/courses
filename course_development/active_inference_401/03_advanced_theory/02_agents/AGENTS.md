# Station: Agents (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Agents
- **Subtitle**: POMDPs, Belief MDPs, and Information Geometry
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Formalize the active inference agent as a partially observable Markov decision process (POMDP) with the full tuple $\langle \mathcal{S}, \mathcal{A}, \mathcal{O}, T, \Omega, R, \gamma \rangle$. Derive the belief MDP — the MDP defined over the space of belief states $\Delta(\mathcal{S})$ — and show that optimal policies in the belief MDP correspond to optimal policies in the original POMDP (Kaelbling et al., 1998, Theorem 1). Equip the belief simplex with the Fisher information metric $g_{ij}(\theta) = \mathbb{E}_{p_\theta}\left[\frac{\partial \ln p_\theta}{\partial \theta^i}\frac{\partial \ln p_\theta}{\partial \theta^j}\right]$, making it a Riemannian statistical manifold. Derive the natural gradient $\tilde{\nabla} F = \Gamma^{-1}\nabla F$ and show its relationship to variational free energy minimization. Prove that natural gradient descent is the unique reparameterization-invariant gradient method on statistical manifolds (Amari, 2016, Chapter 7).

## Key Concepts

- POMDP formalization: state space $\mathcal{S}$, action space $\mathcal{A}$, observation space $\mathcal{O}$, transition kernel $T$, observation kernel $\Omega$, preference/reward function
- Belief MDP: the sufficient statistic reduction from POMDPs to MDPs on the belief simplex $\Delta(\mathcal{S})$
- Statistical manifold $(\mathcal{M}, g)$: the space of parameterized probability distributions equipped with the Fisher metric
- Fisher information metric $g_{ij}(\theta)$: the unique (up to scaling) Riemannian metric that is invariant under sufficient statistics (Cencov's theorem)
- Natural gradient: $\tilde{\nabla} F(\theta) = g^{-1}(\theta)\nabla F(\theta)$ — gradient descent that respects the intrinsic geometry of parameter space
- Policy spaces and their geometry: the space of stochastic policies as a statistical manifold
- Connection between VFE minimization and geodesic flow on $\mathcal{M}$

## Key References

- Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1-2), 99-134.
- Ay, N., Jost, J., Le, H. V., & Schwachhofer, L. (2017). *Information Geometry*. Springer.
- Da Costa, L., Sajid, N., Parr, T., Friston, K., & Smith, R. (2020). The relationship between dynamic programming and active inference. *arXiv preprint arXiv:2009.16459*.
- Cencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society.

## Prerequisite Modules

- Module 01 (Systems): The NESS formalism and particular partition provide the dynamical foundation upon which the agent is defined. The Helmholtz decomposition of flow into solenoidal and dissipative components is presupposed.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 02): Debates the philosophical criteria for agency — autonomy, intentionality, and whether the Markov blanket formalism is sufficient for genuine agency. See [../../01_philosophical_foundations/02_agents/module.md](../../01_philosophical_foundations/02_agents/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 02): Maps the POMDP structure onto prefrontal-basal ganglia circuits, with dopamine encoding precision over policies. See [../../02_neuroscientific_frontiers/02_agents/module.md](../../02_neuroscientific_frontiers/02_agents/module.md).
- **Research Methods** (Unit 4, Module 02): Covers computational implementation of POMDP agents in PyMDP, parameter recovery, and model inversion for behavioral data. See [../../04_research_methods/02_agents/module.md](../../04_research_methods/02_agents/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
