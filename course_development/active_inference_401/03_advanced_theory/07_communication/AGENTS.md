# Station: Communication (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Communication
- **Subtitle**: Multi-Agent Active Inference and Coupled Dynamical Systems
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Formally construct shared Markov blankets between coupled agents. Begin with two agents, each possessing a particular partition $(\mu_1, b_1)$ and $(\mu_2, b_2)$, and define the shared blanket as the subset of blanket states that are simultaneously active states of one agent and sensory states of the other: $b_{12} = a_1 \cap s_2$ and $b_{21} = a_2 \cap s_1$. Derive the conditional independence structure this implies and state the conditions under which a well-defined shared blanket exists (non-trivial intersection, NESS over the joint system). Formulate the multi-agent POMDP: each agent $i$ maintains a generative model $p_i(o_i, s_i, \theta_j)$ that includes parameters $\theta_j$ of the other agent's generative model, and inference over $\theta_j$ constitutes "mentalizing" or theory of mind. Show how coupled active inference — where each agent minimizes its own VFE while the other agent's actions constitute part of the environment — reduces to known game-theoretic solutions. Specifically, prove that when generative models are common knowledge and agents minimize EFE, the resulting equilibrium is a Nash equilibrium (under appropriate conditions on preferences and information structure). Connect to mean-field game theory (Lasry & Lions, 2007) for the many-agent limit: show that as $N \to \infty$, the $N$-agent coupled active inference system converges to a mean-field game where each agent interacts with the population distribution rather than with individuals. Prove conditions under which communication — exchange of observations via shared active states — aligns generative models in the sense that $D_{KL}[q_1(s) \| q_2(s)] \to 0$ over time.

## Key Concepts

- Shared Markov blanket: formal construction via intersection of active and sensory states between two particular partitions — existence conditions and topological constraints
- Multi-agent POMDP: each agent's generative model includes latent variables parameterizing the other agent's beliefs — $p_i(o_i, s_i, \theta_j)$ with inference over $\theta_j$
- Coupled active inference: simultaneous VFE minimization by multiple agents where each agent's environment includes the other's actions — fixed-point analysis of the coupled dynamics
- Game-theoretic connections: proof that coupled EFE minimization yields Nash equilibria under common knowledge assumptions; relationship to Bayesian games and correlated equilibria
- Mean-field game theory (Lasry & Lions, 2007): $N \to \infty$ limit of multi-agent systems, mean-field approximation to the population distribution, Hamilton-Jacobi-Bellman-Fokker-Planck system
- Generative model alignment: conditions under which communication reduces $D_{KL}[q_1 \| q_2]$ — convergence rates, information-theoretic bounds on alignment speed
- Cultural niche construction as structure learning: shared priors emerging from coupled inference over generational timescales

## Key References

- Friston, K. J., & Frith, C. D. (2015). Active inference, communication and hermeneutics. *Cortex*, 68, 129-143.
- Da Costa, L., Sajid, N., Parr, T., Friston, K., & Smith, R. (2020). The relationship between dynamic programming and active inference. *arXiv preprint arXiv:2009.16459*.
- Vasil, J., Badcock, P. B., Constant, A., Friston, K., & Ramstead, M. J. D. (2020). A world unto itself: Human communication as active inference. *Frontiers in Psychology*, 11, 417.
- Lasry, J.-M., & Lions, P.-L. (2007). Mean field games. *Japanese Journal of Mathematics*, 2(1), 229-260.
- Huang, M., Malhame, R. P., & Caines, P. E. (2006). Large population stochastic dynamic games: Closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle. *Communications in Information and Systems*, 6(3), 221-252.

## Prerequisite Modules

- Module 02 (Agents): The POMDP formalization and belief-space geometry are required to define each individual agent before constructing the coupled system. The particular partition from Module 01 (via Module 02) provides the formal apparatus for defining Markov blankets, which are composed into shared blankets here.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 07): Examines shared intentionality, Tomasello's cooperative communication hypothesis, and whether the shared Markov blanket formalism captures genuine intersubjectivity. See [../../01_philosophical_foundations/07_communication/module.md](../../01_philosophical_foundations/07_communication/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 07): Reviews mirror neuron systems, theory of mind networks, social prediction errors, and hyperscanning evidence for coupled neural dynamics. See [../../02_neuroscientific_frontiers/07_communication/module.md](../../02_neuroscientific_frontiers/07_communication/module.md).
- **Research Methods** (Unit 4, Module 07): Covers experimental paradigms for studying social inference — hyperscanning, two-player trust games, computational phenotyping of social learning, and agent-based social simulation. See [../../04_research_methods/07_communication/module.md](../../04_research_methods/07_communication/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
