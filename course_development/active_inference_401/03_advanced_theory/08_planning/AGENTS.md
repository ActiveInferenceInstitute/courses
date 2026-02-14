# Station: Planning (Advanced Theory)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Stochastic thermodynamics, Bayesian mechanics, path integrals
- **Topic**: Planning
- **Subtitle**: Deep Temporal Models and Sophisticated Inference
- **Lab Style**: Proof Workshop
- **Audience**: PhD students and researchers
- **Tone**: Formally rigorous, theorem-proof structure

## Content Guidance

Derive the deep temporal POMDP with hierarchical timescales. Define the generative model as a hierarchy of state-space models operating at nested temporal scales: fast dynamics at level $\ell = 1$ are governed by transition matrices $\mathbf{B}^{(1)}$ that are themselves parameterized by slower states at level $\ell = 2$, which evolve according to $\mathbf{B}^{(2)}$, and so on. Show that this hierarchical construction enables the agent to represent temporally extended regularities — habits, goals, narratives — within a single generative model. Formalize sophisticated inference as recursive expected free energy (EFE) evaluation. In standard active inference, the agent evaluates $G(\pi) = \sum_\tau G(\pi, \tau)$ by marginalizing over future observations. In sophisticated inference, the agent additionally conditions on how each possible future observation would update its beliefs, yielding a recursive structure: $G_{\text{soph}}(\pi) = G(\pi, \tau) + \mathbb{E}_{q(o_\tau|\pi)}[G_{\text{soph}}(\pi, \tau+1 \mid o_\tau)]$ where the inner expectation is taken over the posterior beliefs that would result from observing $o_\tau$. Prove that sophisticated inference subsumes standard active inference: show that when the agent does not condition on counterfactual belief updates, the sophisticated EFE reduces to the standard EFE. Connect to the planning-as-inference framework (Attias, 2003; Botvinick & Toussaint, 2012): show that both frameworks treat future actions as latent variables to be inferred, and identify the precise correspondence — the EFE plays the role of a log-likelihood in the planning-as-inference formulation. Analyze computational complexity: standard active inference scales as $O(|\mathcal{A}|^T \cdot |\mathcal{S}|)$ for horizon $T$ and policy-tree enumeration, while sophisticated inference adds a factor for recursive belief updating. Present approximation schemes — policy pruning, habit learning ($\mathbf{E}$ vector), amortized inference via deep neural networks — and state the conditions under which each approximation preserves optimality guarantees.

## Key Concepts

- Deep temporal POMDP: hierarchical generative model with nested timescales $\ell = 1, \ldots, L$, where slow states $s^{(\ell+1)}$ parameterize the transition dynamics $\mathbf{B}^{(\ell)}(s^{(\ell+1)})$ of fast states $s^{(\ell)}$
- Sophisticated inference: recursive EFE evaluation — $G_{\text{soph}}(\pi) = G(\pi, \tau) + \mathbb{E}_{q(o_\tau|\pi)}[G_{\text{soph}}(\pi, \tau+1 \mid o_\tau)]$ — the agent simulates how future observations would update beliefs and plans accordingly
- Subsumption theorem: standard active inference is a special case of sophisticated inference when counterfactual belief updating is omitted (proof by marginalization)
- Planning as inference (Attias, 2003; Botvinick & Toussaint, 2012): augment the generative model with an optimality variable $\mathcal{O}_t = 1$ such that $p(\mathcal{O}_t = 1 \mid s_t, a_t) \propto \exp(-C(s_t, a_t))$, then infer actions via posterior $p(a_{1:T} \mid \mathcal{O}_{1:T} = 1)$
- Computational complexity: $O(|\mathcal{A}|^T \cdot |\mathcal{S}|)$ for policy-tree enumeration, exponential in horizon — necessitating approximation for practical planning
- Approximation schemes: policy pruning (eliminate low-probability branches early), habit vector $\mathbf{E}$ (prior over policies from past experience), Monte Carlo tree search (stochastic expansion), amortized inference (neural network policy approximation)
- Temporal abstraction: relationship between hierarchical timescales and options/semi-MDPs (Sutton et al., 1999), enabling multi-scale planning

## Key References

- Friston, K., Da Costa, L., Sajid, N., Heins, C., Ueltzhoeffer, K., Pavliotis, G. A., & Parr, T. (2021). The free energy principle made simpler but not too simple. *Physics Reports*, 868, 1-29.
- Da Costa, L., Sajid, N., Parr, T., Friston, K., & Smith, R. (2020). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology*, 99, 102447.
- Botvinick, M., & Toussaint, M. (2012). Planning as inference. *Trends in Cognitive Sciences*, 16(10), 485-488.
- Attias, H. (2003). Planning by probabilistic inference. *Proceedings of the 9th International Workshop on Artificial Intelligence and Statistics*.
- Fountas, Z., Sajid, N., Mediano, P. A., & Friston, K. (2020). Deep active inference agents using Monte-Carlo methods. *Advances in Neural Information Processing Systems*, 33, 11662-11675.

## Prerequisite Modules

- Module 04 (Cognition): The variational methods — mean-field, Bethe, belief propagation — provide the inference machinery that sophisticated inference extends to the temporal domain. Factor graph representations from Module 04 are used to represent the deep temporal generative model.
- Module 05 (Action): The EFE functional and its derivation from first principles are required. The Risk-Ambiguity and Pragmatic-Epistemic decompositions are recursively applied in sophisticated inference.
- Module 06 (Learning): Bayesian model reduction and structure learning provide the mechanisms by which the agent can learn and modify the deep temporal model structure, enabling adaptive planning over changing environments.

## Cross-Unit Connections

- **Philosophical Foundations** (Unit 1, Module 08): Examines the philosophy of imagination, counterfactual reasoning, temporal consciousness, and mental time travel — whether sophisticated inference captures genuine prospection or merely simulates it. See [../../01_philosophical_foundations/08_planning/module.md](../../01_philosophical_foundations/08_planning/module.md).
- **Neuroscientific Frontiers** (Unit 2, Module 08): Reviews hippocampal sequence replay, preplay and prospective coding, prefrontal-hippocampal theta coupling, and the model-based vs. model-free distinction in neural planning circuits. See [../../02_neuroscientific_frontiers/08_planning/module.md](../../02_neuroscientific_frontiers/08_planning/module.md).
- **Research Methods** (Unit 4, Module 08): Covers open problems and research frontiers — scale-free inference, consciousness and the FEP, embodied AI applications, clinical computational psychiatry, and AGI alignment. See [../../04_research_methods/08_planning/module.md](../../04_research_methods/08_planning/module.md).

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
