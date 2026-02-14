# Active Inference 401: Advanced PhD Seminar — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Philosophical Foundations](./01_philosophical_foundations/) | [Neuroscientific Frontiers](./02_neuroscientific_frontiers/) | [Advanced Theory](./03_advanced_theory/) | [Research Methods](./04_research_methods/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit advanced Active Inference curriculum for PhD students and researchers: 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain research-level rigor in terminology, notation, and argumentation across all units.

The curriculum treats the same 8 topics (Systems, Agents, Perception, Cognition, Action, Learning, Communication, Planning) from four disciplinary perspectives. **Each unit is NOT a repetition — it is a genuinely different intellectual engagement with the topic.** Agents must ensure that content across units is complementary, not duplicative. A student who reads all four treatments of "Perception" should encounter four distinct bodies of literature, four different methodologies, and four different standards of evidence — all converging on the same underlying formalism.

---

## Directory Contents

| Path | Type | Description |
| ---- | ---- | ----------- |
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_philosophical_foundations/` | Directory | Unit 1: Philosophical Foundations of Active Inference (8 modules) |
| `02_neuroscientific_frontiers/` | Directory | Unit 2: Neuroscientific Frontiers (8 modules) |
| `03_advanced_theory/` | Directory | Unit 3: Advanced Mathematical Theory (8 modules) |
| `04_research_methods/` | Directory | Unit 4: Research Methods & Open Problems (8 modules) |

---

## Prerequisites Assumed of the Reader

This is a 401-level course. All content must be written assuming the reader has mastered the following.

### Mathematical Foundations

- **Probability theory**: Measure-theoretic foundations, Bayes' theorem, exponential families, sufficient statistics, conjugate priors, graphical models (Bayesian networks, factor graphs)
- **Information theory**: Shannon entropy, KL divergence, mutual information, data processing inequality, rate-distortion theory
- **Differential geometry**: Smooth manifolds, tangent/cotangent bundles, Riemannian metrics, connections, geodesics, the Fisher information metric as a Riemannian metric on statistical manifolds
- **Dynamical systems**: ODEs, SDEs (Ito and Stratonovich), Langevin dynamics, Fokker-Planck equation, Lyapunov stability, attractors, ergodic theory, non-equilibrium steady states
- **Variational calculus**: Functionals, Euler-Lagrange equations, calculus of variations, Legendre transforms, path integrals (Feynman-Kac)
- **Linear algebra**: Eigendecomposition, positive-definite matrices, matrix calculus, Kronecker products, tensor notation
- **Category theory** (Unit 3 primarily): Functors, natural transformations, adjunctions, monoidal categories, string diagrams

### Domain Knowledge

- **Bayesian inference**: Variational inference (mean-field, structured), Laplace approximation, expectation-maximization, belief propagation, variational message passing
- **Control theory**: Bellman equation, Hamilton-Jacobi-Bellman equation, LQR/LQG, Pontryagin's maximum principle, KL control, linearly solvable MDPs
- **Neuroscience** (Unit 2 primarily): Cortical microcircuits (layers, cell types, connectivity), synaptic plasticity (LTP/LTD, STDP), neuromodulatory systems (dopamine, acetylcholine, noradrenaline, serotonin), neural oscillations (gamma, theta, alpha)
- **Philosophy of mind** (Unit 1 primarily): Functionalism, extended mind thesis (Clark & Chalmers), enactivism (Varela, Thompson, Noë), phenomenology (Husserl, Merleau-Ponty, Heidegger), ecological psychology (Gibson)
- **Active Inference fundamentals**: Generative models, variational free energy, expected free energy, POMDP formulation, Markov blanket formalism, particular partition

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
| -------- | ------- | --------------- |
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any formula, symbol, or equation |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references between courses |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, research-quality content. Every glossary entry must have a formal definition with citations. Every notation entry must have a precise mathematical meaning. Every reference must be a real, citable work.

### 3. Differentiate Units — Do Not Duplicate

This is the single most important rule. The four units treat the same 8 topics from genuinely different perspectives. If content in two different units could be swapped without anyone noticing, something is wrong.

| Unit | Core Question | Method | What "Rigor" Means Here | Characteristic Output |
| ---- | ------------- | ------ | ----------------------- | --------------------- |
| Philosophical Foundations | What does this concept *mean*? What are its ontological and epistemological commitments? | Conceptual analysis, phenomenological description, thought experiments, argumentative essays | Clarity of argument, engagement with philosophical literature, identification of hidden assumptions, dialectical structure | A seminar paper that could appear in *Philosophy of Science* or *Synthese* |
| Neuroscientific Frontiers | What is the *neural evidence*? Which brain mechanisms implement this? | Empirical review, experimental paradigms, neural circuit modeling, quantitative data analysis | Quality of evidence evaluation, specificity of neural claims, linking computational models to neural data, effect sizes | A review article that could appear in *Nature Reviews Neuroscience* or *Neuroscience & Biobehavioral Reviews* |
| Advanced Theory | Can we *prove* this? What is the exact mathematical structure? | Formal derivation, theorem-proof structure, categorical/geometric analysis, constructive proofs | Mathematical correctness, generality of results, identification of necessary and sufficient conditions, explicit statement of assumptions | A technical article that could appear in *Journal of Mathematical Psychology* or *Proceedings of the Royal Society A* |
| Research Methods | How do we *test* this? What experiments would distinguish competing accounts? | Experimental design, model comparison, simulation studies, power analysis, computational benchmarking | Falsifiability, statistical rigor, computational tractability, practical feasibility, replicability | A methods paper that could appear in *NeuroImage*, *PLOS Computational Biology*, or *Frontiers in Computational Neuroscience* |

### 4. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
| ---- | ----------- | -------- | --------------- |
| Philosophical Foundations | Epistemology, phenomenology, 4E cognition | Seminar Discussion | "Reconstruct Clark's (2013) argument that predictive processing vindicates the extended mind thesis. Evaluate Hohwy's (2016) Markov blanket objection. Does the particular partition settle this debate?" |
| Neuroscientific Frontiers | Predictive processing, precision, neural dynamics | Paper Review | "Critically evaluate Bastos et al. (2012) on canonical microcircuits for predictive coding. What specific predictions does the model make about laminar-specific oscillatory coupling? How would you test these with laminar fMRI?" |
| Advanced Theory | Stochastic thermodynamics, Bayesian mechanics, path integrals | Proof Workshop | "Starting from the Fokker-Planck equation for a system at NESS, derive the particular partition. Show that internal states parameterize a density over external states. State all assumptions explicitly." |
| Research Methods | Experimental design, model comparison, open problems | Research Proposal | "Design a study using Dynamic Causal Modeling to compare predictive coding and adaptive resonance accounts of the mismatch negativity. Specify your generative model, inversion scheme, and model comparison criterion." |

### 5. Write for PhD Students and Researchers

- Assume strong foundations in the prerequisites listed above
- Reference primary literature extensively — cite specific theorems, equations, figures, and experimental results (not just papers by name)
- Engage with open questions and unresolved debates in the field
- Present multiple perspectives on contested claims with named proponents
- Include pointers to frontier research, unsolved problems, and active controversies
- Use hedging language appropriately: distinguish established results from conjectures, strong from weak evidence, formal proofs from heuristic arguments
- Flag when an argument depends on assumptions that are themselves debated

### 6. Mathematical Rigor Standards

| Standard | Philosophical Foundations | Neuroscientific Frontiers | Advanced Theory | Research Methods |
| -------- | ------------------------ | ------------------------ | --------------- | ---------------- |
| **Equations** | Illustrative; explain what each term means conceptually and why the formalism matters philosophically | Specify models fitted to neural data; link parameters to measurable quantities (firing rates, BOLD signal) | Derived from first principles with all steps shown; state domain, range, regularity conditions | Define likelihood functions, estimators, test statistics; show computational cost and scaling |
| **Proofs** | Informal arguments showing logical structure; identify hidden premises | Not typically required; focus on model specification and fit to data | Full formal proofs expected: theorem statement, assumptions, proof, corollaries | Proofs of identifiability, convergence, consistency, asymptotic properties as needed |
| **Notation** | Consistent with notation table; conceptual emphasis; explain symbols when first introduced | Consistent with notation table; map symbols to neural quantities explicitly | Consistent with notation table; full generality (indexed, tensorially); define all objects before use | Consistent with notation table; computational implementation; pseudocode where helpful |
| **Figures** | Conceptual diagrams, argument maps, schematic illustrations | Neural circuit diagrams, data plots with error bars, model fits overlaid on data | Commutative diagrams, manifold illustrations, phase portraits | Experimental designs, model comparison plots (BMS, family inference), simulation results |

### 7. Literature Engagement Standards

- **Cite specifically**: "Friston (2010, Eq. 2.3)" not just "Friston (2010)". "Rao & Ballard (1999, Fig. 3)" not just "Rao & Ballard (1999)".
- **Recency**: Include work through 2024 where relevant. Flag preprints explicitly with "preprint" or arXiv ID.
- **Debate representation**: When a claim is contested, present at least two named positions. Example: "Da Costa et al. (2021) argue X, while Bruineberg et al. (2022) counter that Y."
- **Key references by unit** (non-exhaustive — see [resources/references.md](./resources/references.md) for the full list):
  - **Philosophical**: Friston (2010, 2019), Clark (2013, 2016), Hohwy (2013, 2020), Bruineberg et al. (2018), Kirchhoff et al. (2018), Ramstead et al. (2020), Seth (2021), Wiese & Metzinger (2017), Gallagher & Allen (2018), Colombo & Wright (2021)
  - **Neuroscientific**: Rao & Ballard (1999), Bastos et al. (2012), Adams et al. (2013), Kanai et al. (2015), Shipp (2016), Feldman & Friston (2010), Parr & Friston (2018), Keller & Mrsic-Flogel (2018), Heilbron & Chait (2018)
  - **Advanced Theory**: Da Costa et al. (2021), Sakthivadivel (2022), Friston et al. (2023), Parr et al. (2022), Barp et al. (2022), Amari (2016), Ay et al. (2017), Friston (2019, "A free energy principle for a particular physics")
  - **Research Methods**: Stephan et al. (2009), Friston et al. (2007), Smith et al. (2022), Heins et al. (2022), Fountas et al. (2020), Champion et al. (2021), Sajid et al. (2021)

---

## Notation Standards

All units use the notation defined in [resources/notation_table.md](./resources/notation_table.md). The key symbols are:

### Variational and Free Energy Quantities

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| $F$ | Variational Free Energy | `$F$` | Functional of recognition density $q$ and observations $o$; upper bound on surprisal |
| $G$ | Expected Free Energy | `$G$` | Functional of policies $\pi$; decomposes into Risk + Ambiguity or Pragmatic + Epistemic value |
| $\tilde{F}$ | Generalized Free Energy | `$\tilde{F}$` | Combines VFE and EFE under a single functional |
| $\mathbb{F}$ | Free energy functional (path integral) | `$\mathbb{F}$` | Path integral formulation over trajectories |
| $D_{KL}$ | Kullback-Leibler Divergence | `$D_{KL}$` | $D_{KL}[q \| p] = \mathbb{E}_q[\ln q - \ln p]$ |
| $\mathcal{L}$ | ELBO / Negative VFE | `$\mathcal{L}$` | Evidence lower bound; $\mathcal{L} = -F$ |

### Generative Model Components

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| $p(o, s)$ | Generative model (joint) | `$p(o,s)$` | Joint distribution over observations and hidden states |
| $p(o \mid s)$ | Likelihood | `$p(o \mid s)$` | Observation model |
| $p(s' \mid s, a)$ | Transition model | `$p(s' \mid s, a)$` | State dynamics conditioned on actions |
| $q(s)$ | Approximate posterior (recognition density) | `$q(s)$` | Variational approximation to $p(s \mid o)$ |
| $\pi$ | Policy (sequence of actions) | `$\pi$` | $\pi = (a_1, a_2, \ldots, a_T)$ |
| $\gamma$ | Policy precision (inverse temperature) | `$\gamma$` | Controls stochasticity of policy selection via $\sigma(\gamma \cdot G(\pi))$ |

### POMDP Matrices (Discrete State-Space)

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| **A** | Likelihood matrix | `$\mathbf{A}$` | $A_{ij} = p(o_i \mid s_j)$; maps hidden states to observations |
| **B** | Transition matrix | `$\mathbf{B}$` | $B_{ij}^{(a)} = p(s_i' \mid s_j, a)$; state transitions under action $a$ |
| **C** | Preference vector | `$\mathbf{C}$` | $C_i = \ln p(o_i)$; log prior preferences over observations |
| **D** | Prior over initial states | `$\mathbf{D}$` | $D_i = p(s_i^{(0)})$; initial state beliefs |
| **E** | Habit vector | `$\mathbf{E}$` | $E_\pi = p(\pi)$; prior over policies before EFE evaluation |

### Markov Blanket and Partition States

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| $\eta$ | External states | `$\eta$` | States outside the Markov blanket |
| $\mu$ | Internal states | `$\mu$` | States inside the blanket; parameterize beliefs about $\eta$ |
| $s$ | Sensory states | `$s$` | Blanket states influenced by $\eta$; input to $\mu$ |
| $a$ | Active states | `$a$` | Blanket states influenced by $\mu$; output to $\eta$ |
| $b = (s, a)$ | Blanket states | `$b$` | Union of sensory and active states |
| $p = (\mu, b)$ | Particular states | `$p$` | Internal states + blanket states = the "agent" |

### Dynamical and Geometric Quantities

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| $\Gamma$ | Fisher information metric | `$\Gamma$` | Riemannian metric on the statistical manifold $\mathcal{M}$ |
| $Q$ | Solenoidal flow matrix | `$Q$` | Antisymmetric; $Q = -Q^T$; generates conservative (non-dissipative) flow |
| $f_\mu$ | Flow of internal states | `$f_\mu$` | $f_\mu = (Q_{\mu\mu} - \Gamma_{\mu\mu}) \nabla_\mu F$ |
| $p^*(\cdot)$ | NESS density | `$p^*(\cdot)$` | Non-equilibrium steady-state distribution |
| $\nabla$ | Gradient operator | `$\nabla$` | With subscript: $\nabla_\mu$ = gradient w.r.t. internal states |
| $\mathcal{M}$ | Statistical manifold | `$\mathcal{M}$` | Space of probability distributions equipped with Fisher metric |

### Information-Theoretic Quantities

| Symbol | Meaning | LaTeX | Notes |
| ------ | ------- | ----- | ----- |
| $H[p]$ | Shannon entropy | `$H[p]$` | $H[p] = -\mathbb{E}_p[\ln p]$ |
| $I(X;Y)$ | Mutual information | `$I(X;Y)$` | $I(X;Y) = D_{KL}[p(x,y) \| p(x)p(y)]$ |
| $\mathfrak{s}(o)$ | Surprisal (self-information) | `$\mathfrak{s}(o)$` | $\mathfrak{s}(o) = -\ln p(o)$; also written $-\ln p(o \mid m)$ |
| $\ln p(o \mid m)$ | Log model evidence | `$\ln p(o \mid m)$` | Marginal likelihood of observations under model $m$ |

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
| -------------- | ----- | ------ |
| Generative Model | World model, internal model | Standard FEP terminology; a probabilistic model $p(o, s \mid \theta)$ with parameters $\theta$ |
| Generative Process | Environment, true world | Distinguishes the data-generating process from the agent's model of it |
| Markov Blanket | Boundary (informal) | Formal term from Bayesian network theory (Pearl, 1988): the set of nodes that d-separate internal from external |
| Precision | Confidence, certainty | Precision = inverse variance $\Pi = \Sigma^{-1}$; has specific algebraic role in message passing |
| Variational Free Energy (VFE) | Free energy (ambiguous) | Distinguishes from Helmholtz/Gibbs free energy in thermodynamics |
| Expected Free Energy (EFE) | Future free energy, anticipated free energy | Functional of policies; decomposes into Risk $D_{KL}[q(o \mid \pi) \| p(o)]$ + Ambiguity $\mathbb{E}_{q(s \mid \pi)}[H[p(o \mid s)]]$ |
| Surprisal | Surprise (colloquial) | Technical: $\mathfrak{s}(o) = -\ln p(o)$; "surprise" invites folk-psychological confusion |
| Recognition Density | Belief distribution, posterior approximation | Standard variational inference term for $q(s)$; emphasizes it is an approximation |
| Blanket States | Boundary states | Formal: union of sensory states $s$ and active states $a$ |
| Active States | Motor states, output states | Formal partition term: blanket states influenced by internal states |
| Sensory States | Input states, observation states | Formal partition term: blanket states influenced by external states |
| Particular Partition | Agent partition, system partition | Formal: the decomposition into particular states $(\mu, b)$ and external states $\eta$ |
| Solenoidal Flow | Rotational flow, conservative flow | Flow component $Qf$ with antisymmetric $Q$; preserves steady-state density |
| Dissipative Flow | Gradient flow | Flow component $-\Gamma \nabla F$; performs gradient descent on $F$ |
| Generative Model Inversion | Inference, perception | Technically: computing $q(s) \approx p(s \mid o)$; "inversion" emphasizes the computational operation |
| Policy | Strategy, plan, action sequence | In active inference: a sequence of actions $\pi = (a_1, \ldots, a_T)$ evaluated by $G(\pi)$ |
| Epistemic Value | Information gain, curiosity | The component of EFE that drives exploration: $I(o; s \mid \pi)$ |
| Pragmatic Value | Reward, utility, preference satisfaction | The component of EFE that drives exploitation: $-D_{KL}[q(o \mid \pi) \| p(o)]$ |
| Model Evidence | Marginal likelihood | $p(o \mid m) = \int p(o, s \mid m) ds$; used for model comparison (Bayesian model selection) |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

This order reflects the logical dependency chain of the FEP:

1. **Systems**: Defining non-equilibrium steady states, random dynamical systems, and the conditions under which a system maintains its existence
2. **Agents**: Identifying which systems qualify as agents via the particular partition, Markov blanket formalism, and the agent-environment boundary
3. **Perception**: How agents perform perceptual inference — inverting the generative model to infer hidden causes of sensory data
4. **Cognition**: How generative models are structured, how beliefs are updated, and how variational methods approximate exact inference
5. **Action**: How agents fulfill predictions and minimize expected free energy through motor control and environmental intervention
6. **Learning**: How agents refine generative model parameters and structure over longer timescales
7. **Communication**: How multiple agents align generative models through shared Markov blankets, language, and cultural affordances
8. **Planning**: How temporal depth, counterfactual reasoning, and sophisticated inference enable long-horizon behavior

---

## Unit-Specific Module Differentiation Guide

Each module must have a **distinct subtitle, distinct key concepts, and distinct references** per unit. The following table specifies what each unit's treatment of each topic must emphasize. **Agents must not produce content that collapses these distinctions.**

### Module 1: Systems

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Ontology of Self-Organizing Systems | Autopoiesis (Maturana & Varela), organizational closure, autonomy, process ontology, the boundary problem | Thompson (2007), Di Paolo (2005), Kauffman (1993), Froese & Ziemke (2009) |
| Neuroscientific Frontiers | Neural Systems as Non-Equilibrium Steady States | Cortical dynamics as NESS, neural oscillations and attractors, criticality hypothesis, power-law scaling | Breakspear (2017), Beggs & Plenz (2003), Deco et al. (2017), Friston et al. (2012) |
| Advanced Theory | Bayesian Mechanics and the Physics of Beliefs | NESS density, Fokker-Planck equation, Langevin dynamics, particular partition, solenoidal vs. dissipative flow | Da Costa et al. (2021), Sakthivadivel (2022), Friston (2019), Pavliotis (2014) |
| Research Methods | Identifying and Modeling Self-Organizing Systems | Testing NESS conditions empirically, Langevin model fitting, parameter estimation for SDEs, model identifiability | Ait-Sahalia (2002), Kessler (1997), Friston & Ao (2012), Crauel & Flandoli (1994) |

### Module 2: Agents

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Autonomy, Intentionality, and the Markov Blanket | Agency and the FEP, minimal cognition, Barandiaran's autonomy conditions, the intentionality debate, agent vs. mere system | Barandiaran et al. (2009), Froese & Di Paolo (2011), Kirchhoff & Froese (2017), Moreno & Mossio (2015) |
| Neuroscientific Frontiers | The Neural Architecture of Active Inference Agents | Prefrontal-basal ganglia circuits, dopamine as precision, cortico-thalamic loops, neural POMDP implementation | Schwartenbeck et al. (2015), FitzGerald et al. (2015), Friston et al. (2017), Parr & Friston (2018) |
| Advanced Theory | POMDPs, Belief MDPs, and Information Geometry | Formal agent models on statistical manifolds, belief-space geometry, policy spaces, natural gradient methods | Amari (2016), Kaelbling et al. (1998), Ay et al. (2017), Da Costa et al. (2020) |
| Research Methods | Building and Validating Agent Models | PyMDP implementation, model inversion for behavioral data, parameter recovery, agent-based simulation | Heins et al. (2022), Smith et al. (2022), Wilson & Collins (2019), Palminteri et al. (2017) |

### Module 3: Perception

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Phenomenology of Perception and the Bayesian Brain | Merleau-Ponty vs. Helmholtz, the compatibility thesis, direct perception (Gibson), the hard problem of perceptual content | Merleau-Ponty (1945/2012), Hohwy (2013), Bruineberg & Rietveld (2014), Gallagher & Allen (2018) |
| Neuroscientific Frontiers | Predictive Coding in Cortical Hierarchies | V1 predictive coding (Rao & Ballard), canonical microcircuit model, MMN and P300 as prediction errors, precision weighting via neuromodulators | Rao & Ballard (1999), Bastos et al. (2012), Shipp (2016), Feldman & Friston (2010) |
| Advanced Theory | Variational Message Passing and Hierarchical Inference | Derivation of predictive coding updates from VFE, convergence of hierarchical message passing, information geometry of perceptual manifolds | Friston & Kiebel (2009), Dauwels (2007), Bogacz (2017), Buckley et al. (2017) |
| Research Methods | Testing Predictive Coding with Neuroimaging | DCM for fMRI/EEG, Bayesian model comparison, designing oddball/roving paradigms, computational phenotyping | Stephan et al. (2009), Friston et al. (2007), Garrido et al. (2009), Adams et al. (2013) |

### Module 4: Cognition

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Extended Cognition, Scaffolded Inference, and the Markov Blanket | Clark's extended mind thesis, cognitive integration, where cognition ends, epistemic actions, the parity principle | Clark & Chalmers (1998), Clark (2016), Kirchhoff (2018), Menary (2007), Hohwy (2016) |
| Neuroscientific Frontiers | Prefrontal Hierarchies, Precision, and Working Memory | Hierarchical generative models in PFC, precision and attention (gain modulation), neural substrates of belief updating, prefrontal-parietal networks | Miller & Cohen (2001), Parr & Friston (2017), Kanai et al. (2015), Bastos et al. (2020) |
| Advanced Theory | Variational Methods: Mean-Field, Bethe, and Message Passing | Variational families, mean-field approximation, Bethe free energy, belief propagation, variational message passing, convergence guarantees | Wainwright & Jordan (2008), Yedidia et al. (2005), Dauwels (2007), Parr et al. (2019) |
| Research Methods | Bayesian Model Comparison and Structure Learning in Practice | Bayesian model selection (BMS), family inference, protected exceedance probability, computational model comparison, cross-validation | Stephan et al. (2009), Rigoux et al. (2014), Friston & Penny (2011), Piray et al. (2019) |

### Module 5: Action

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Enactivism, Affordances, and Active Inference | Enactive approach (Varela, Thompson, Di Paolo), affordances as precision-weighted predictions, motor intentionality, the action-perception cycle | Varela et al. (1991), Bruineberg & Rietveld (2014), Chemero (2009), Engel et al. (2013) |
| Neuroscientific Frontiers | Motor Control and Active Inference in the Brain | Spinal reflexes as prediction error minimization, cerebellar forward models, motor hierarchy, oculomotor control, active sensing | Adams et al. (2013), Friston et al. (2010), Wolpert et al. (1998), Parr & Friston (2018) |
| Advanced Theory | Path Integrals, KL Control, and Optimal Policies | Path integral formulation of control, KL control and linearly solvable MDPs, EFE derivation from first principles, policy selection as inference | Kappen (2005), Todorov (2009), Friston et al. (2015), Millidge et al. (2020) |
| Research Methods | Designing Motor Control and Decision-Making Experiments | Reaching/grasping paradigms, saccade experiments, force field adaptation, drift-diffusion models, fitting active inference models to behavioral data | Shadmehr & Mussa-Ivaldi (1994), Smith et al. (2022), Fountas et al. (2020), Sajid et al. (2021) |

### Module 6: Learning

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Epistemology of Model Revision and Epistemic Virtue | Kuhnian paradigm shifts as structure learning, abductive inference, epistemic virtues, Bayesian epistemology, the problem of induction | Kuhn (1962), Lipton (2004), Williamson (2000), Tenenbaum et al. (2011), Ramstead et al. (2020) |
| Neuroscientific Frontiers | Synaptic Plasticity, Neuromodulation, and Bayesian Learning | Hebbian plasticity as VFE minimization, precision weighting via dopamine/acetylcholine, sleep consolidation, empirical Bayes in cortical hierarchies | Friston (2005), Gershman & Daw (2017), Diekelmann & Born (2010), Friston & Frith (2015) |
| Advanced Theory | Bayesian Mechanics, Structure Learning, and Model Evidence | Variational Laplacian, model evidence bounds (free energy as evidence bound), structure learning algorithms, Bayesian model reduction | Friston et al. (2018), Friston & Penny (2011), Friston et al. (2016, BMR), Ghahramani (2015) |
| Research Methods | Fitting, Comparing, and Validating Generative Models | Parameter estimation (EM, variational Bayes), model evidence computation, parameter recovery, simulation-based calibration, posterior predictive checks | Gelman et al. (2014), Talts et al. (2018), Wilson & Collins (2019), Friston et al. (2007) |

### Module 7: Communication

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Shared Intentionality, Language, and the Social Markov Blanket | Joint attention, shared generative models, Tomasello's shared intentionality, cultural niche construction, regulative vs. constitutive rules | Tomasello (2014), Ramstead et al. (2016), Veissière et al. (2020), Vasil et al. (2020) |
| Neuroscientific Frontiers | Mirror Systems, Mentalizing, and Social Prediction | Mirror neuron system, theory of mind networks, social prediction errors, oxytocin and social precision, hyperscanning evidence | Kilner et al. (2007), Frith & Frith (2006), Koster-Hale & Saxe (2013), Hasson et al. (2012) |
| Advanced Theory | Multi-Agent Active Inference and Coupled Dynamical Systems | Shared Markov blankets (formal construction), multi-agent POMDP, coupled inference, game-theoretic connections, mean-field games | Friston & Frith (2015), Da Costa et al. (2020), Vasil et al. (2020), Lasry & Lions (2007) |
| Research Methods | Studying Social Inference Experimentally | Hyperscanning paradigms (fMRI, EEG, fNIRS), computational phenotyping of social learning, two-player trust games, agent-based social simulation | Hasson et al. (2012), Diaconescu et al. (2014), Mathys et al. (2014), Behrens et al. (2008) |

### Module 8: Planning

| Unit | Subtitle | Key Concepts | Key References |
| ---- | -------- | ------------ | -------------- |
| Philosophical Foundations | Temporal Depth, Imagination, and Counterfactual Reasoning | Imagination as offline policy evaluation, counterfactual reasoning, temporal consciousness, mental time travel, narrative self | Pezzulo (2008), Buckner (2010), Friston et al. (2021), Seth (2021), Gallagher (2000) |
| Neuroscientific Frontiers | Hippocampal Replay, Prospection, and Model-Based Planning | Hippocampal sequence replay, preplay and prospective coding, prefrontal-hippocampal interaction, theta sequences, model-based vs. model-free control | Foster & Wilson (2006), Pfeiffer & Foster (2013), Dolan & Dayan (2013), Mattar & Daw (2018) |
| Advanced Theory | Deep Temporal Models and Sophisticated Inference | Deep POMDP (hierarchical temporal), sophisticated inference (recursive EFE), tree search and planning algorithms, planning as inference | Friston et al. (2021), Da Costa et al. (2020, sophisticated), Botvinick et al. (2009), Attias (2003) |
| Research Methods | Open Problems and Research Frontiers in Active Inference | Scale-free inference, consciousness and the FEP, embodied AI applications, clinical computational psychiatry, AGI and alignment | Ramstead et al. (2023), Seth (2021), Tschantz et al. (2020), Parr et al. (2022), Friston et al. (2022) |

---

## Content Format Standards

| File | Format Requirements |
| ---- | ------------------- |
| `module.md` | `# Title: Subtitle` heading, `> Course:` and `> Audience:` metadata block, `## Overview` (1-2 paragraphs), `## Learning Goals` (3-5 numbered items using Bloom's taxonomy verbs at analysis/synthesis/evaluation level), `## Key Concepts` (3-5 bolded definitions with formal precision), `## Lesson Content` (3-5 subsections, each 2-4 paragraphs with formal rigor appropriate to unit), `## Summary` (1 paragraph), `## Further Reading` (3-6 specific references with full citations) |
| `questions.md` | `# Course — Module — Study Questions` heading + numbered list of exactly 20 questions. Questions must be research-oriented, requiring synthesis across readings, engagement with debates, and formal/technical analysis. Avoid yes/no or definition-only questions. |
| `practice_quiz.md` | `Name/Date` header. `Part A: Multiple Choice` (exactly 7 questions with 4 options each; distractors should represent common misconceptions or competing theoretical positions). `Part B: Free Response` (exactly 3 questions requiring proof, derivation, critical analysis, or experimental design — calibrated to unit type). |
| `lab.md` | `## Objectives` → multi-part exercises with `> **Learning Goal:**` blockquotes → `{fill:textarea}` response fields → `## Summary` table. Lab type must match unit: Seminar Discussion / Paper Review / Proof Workshop / Research Proposal. |
| `dashboard.html` | Interactive HTML5: dark theme with `#a78bfa` purple accent, concept cards with progress meters, quiz section with JS answer checking. Must be self-contained (no external dependencies). |
| `README.md` | Quick Navigation header, overview paragraph, module contents table (linking all files), learning goals (3 items), resources links. |
| `AGENTS.md` | Quick Navigation header, conventions (perspective, topics, lab style, audience, tone), topic-specific content guidance, key references for this module, prerequisite modules, cross-unit connections. |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_philosophical_foundations/03_perception/module.md to the theory version: -->
See the [formal derivation](../../03_advanced_theory/03_perception/module.md) for the
information-geometric treatment of hierarchical inference.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- Cross-course reference to the core curriculum: -->
See the [Core Mathematics course](../../active_inference/03_math/03_perception/module.md)
for the introductory derivation.

<!-- Cross-unit reference within the same module topic: -->
For the philosophical implications, see the
[Philosophical Foundations treatment](../../01_philosophical_foundations/03_perception/module.md).
```

---

## Computational Tools and Frameworks

Content may reference the following tools. When doing so, specify version and cite the tool paper:

| Tool | Language | Purpose | Citation |
| ---- | -------- | ------- | -------- |
| **SPM** (Statistical Parametric Mapping) | MATLAB | DCM, Bayesian model inversion, neuroimaging analysis | Friston et al. (2007) |
| **PyMDP** | Python | Discrete active inference agents (POMDP) | Heins et al. (2022) |
| **RxInfer.jl** | Julia | Reactive message passing, scalable variational inference | Bagaev & de Vries (2023) |
| **SPM DEM Toolbox** | MATLAB | Continuous active inference, generalized filtering | Friston et al. (2010) |
| **ForneyLab.jl** | Julia | Factor graph-based variational inference | Cox et al. (2019) |
| **deep-active-inference** | Python/PyTorch | Deep active inference with neural network function approximation | Fountas et al. (2020) |

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

### Content Quality
- [ ] Content reflects research-level rigor appropriate to the PhD audience
- [ ] Content is genuinely differentiated from the same topic in other units (not duplicative)
- [ ] Primary literature is cited with specific results, theorems, equations, or figures
- [ ] Open questions and frontier problems are highlighted with named researchers/positions
- [ ] Multiple perspectives on contested claims are presented fairly
- [ ] No placeholder brackets `[...]`, `[TODO]`, or circular definitions remain

### Notation and Terminology
- [ ] All notation matches `resources/notation_table.md`
- [ ] All terms match `resources/glossary.md`
- [ ] Symbols are defined on first use within each module
- [ ] Unit-appropriate level of mathematical formalism is maintained

### Structure and Format
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Cross-references use correct relative paths and have been verified
- [ ] Content format matches the standards table above
- [ ] Lab activities match the unit's lab type (Seminar/Paper Review/Proof Workshop/Research Proposal)

### Assessment Quality
- [ ] Study questions (20) engage with current research debates and require synthesis
- [ ] Quiz Part A has exactly 7 MC questions with well-constructed distractors
- [ ] Quiz Part B has exactly 3 questions at proof/analysis/design level (calibrated to unit)
- [ ] Lab exercises require genuine intellectual work, not just recall

### Cross-References
- [ ] Links to other units' treatments of the same topic are present and correct
- [ ] Links to prerequisite modules are present
- [ ] Links to the notation table and glossary are present

---

## Dashboard Color Identity

- **Accent**: Purple `#a78bfa`
- **Gradient**: Purple → Pink
- **Semantic**: Advanced, sophisticated, research-level
