# Cross-Course Module Map

> **Quick Navigation**: [Curriculum Home](../README.md) | [Notation Table](./notation_table.md) | [Glossary](./glossary.md) | [Key References](./references.md)

This map shows how each of the 8 topics connects across the 4 courses, enabling interdisciplinary cross-referencing and spiral learning. Each module directory contains: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`.

---

## How to Use This Map

- **Students**: When studying a topic, follow the row across to see how Philosophy, Cognitive Science, Mathematics, and Computer Science each illuminate the same concept from different angles.
- **Content authors**: When writing a module, check its row to ensure your content complements (not duplicates) the other courses' treatments.
- **Cross-references**: Use relative paths from any module to link to its parallel in another course. Example: from `01_philosophy/03_perception/module.md`, link to `../../03_math/03_perception/module.md`.

---

## Module 1: Systems

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/01_systems/) | Boundaries, Markov Blankets, and the Philosophy of Biology | What is a system? Boundary problem. Autopoiesis. Self-organization. | `01_philosophy/01_systems/` |
| [Cognitive Science](../02_cognitive_science/01_systems/) | Neural Assemblies, Cortical Organization, and Self-Environment Distinction | Neural assemblies. Cortical columns. Brain-body-environment boundaries. | `02_cognitive_science/01_systems/` |
| [Mathematics](../03_math/01_systems/) | Mathematical Foundations: Matrices, Probability, and Bayesian Reasoning | Matrix operations. Probability distributions. Bayes' theorem. KL divergence. Graphical models. d-separation. | `03_math/01_systems/` |
| [Computer Science](../04_computer_science/01_systems/) | Generative Process vs Generative Model | Environment setup. Generative process vs model distinction. Simulation loop basics. | `04_computer_science/01_systems/` |

---

## Module 2: Agents

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/02_agents/) | Autopoiesis, Agency, and the Self-Organizing System | What is agency? Self-model. Intentionality naturalized. Minimal cognition. | `01_philosophy/02_agents/` |
| [Cognitive Science](../02_cognitive_science/02_agents/) | Self-Model, Interoception, and Ego Boundaries | Interoception. Insular cortex. Self-model development. Clinical disruptions. | `02_cognitive_science/02_agents/` |
| [Mathematics](../03_math/02_agents/) | Stochastic Systems: Random Processes, SDEs, and Steady States | Dynamical systems. Stochastic processes. Langevin equation. Fokker-Planck equation. NESS density. Ergodicity. | `03_math/02_agents/` |
| [Computer Science](../04_computer_science/02_agents/) | The Agent Class: States, Observations, and A-E Matrices | GenerativeModel class. A-E matrix initialization. T-maze benchmark. | `04_computer_science/02_agents/` |

---

## Module 3: Perception

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/03_perception/) | Direct Perception, Inferentialism, and the User-Interface Theory | Veil of perception. Helmholtz's unconscious inference. User-interface theory. Perception as hypothesis testing. | `01_philosophy/03_perception/` |
| [Cognitive Science](../02_cognitive_science/03_perception/) | Predictive Coding, Sensory Attenuation, and Hallucinations | Predictive coding in visual cortex. Sensory attenuation. Hallucinations in schizophrenia. | `02_cognitive_science/03_perception/` |
| [Mathematics](../03_math/03_perception/) | Variational Free Energy, KL Divergence, and Recognition Density | VFE derivation. KL divergence. Recognition density q(s). Prediction error minimization. Hierarchical inference. | `03_math/03_perception/` |
| [Computer Science](../04_computer_science/03_perception/) | State Estimation with A-Matrix and B-Matrix | A-matrix likelihood. B-matrix transitions. Belief update implementation. Posterior visualization. | `04_computer_science/03_perception/` |

---

## Module 4: Cognition

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/04_cognition/) | Beliefs as Physical States, the Embodied Mind, and Consciousness | What are beliefs? Embodied mind. Precision and attention. Dark room problem. Hard problem of consciousness. | `01_philosophy/04_cognition/` |
| [Cognitive Science](../02_cognitive_science/04_cognition/) | Precision Weighting, Neuromodulation, and Attention | Neural attention. Dopamine, acetylcholine, norepinephrine. Working memory. ADHD and autism. | `02_cognitive_science/04_cognition/` |
| [Mathematics](../03_math/04_cognition/) | Precision Matrices, Hierarchical Gaussian Filters, Message Passing | Precision weighting formalism. Hierarchical models. Message passing algorithms. Attentional selection. | `03_math/04_cognition/` |
| [Computer Science](../04_computer_science/04_cognition/) | C-Matrix (Preferences), D-Matrix (Priors), E-Matrix (Habits) | C-vector preferences. D-vector priors. E-vector habits. Precision parameter γ. | `04_computer_science/04_cognition/` |

---

## Module 5: Action

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/05_action/) | Agency as Inference, Affordances, and Active Exploration | Action as inference. Affordances. Pragmatism. Free will. Epistemic action. | `01_philosophy/05_action/` |
| [Cognitive Science](../02_cognitive_science/05_action/) | Motor Control as Active Inference; Habits vs Goals | Motor inference. Habitual vs goal-directed. Basal ganglia. Cerebellum. Movement disorders. | `02_cognitive_science/05_action/` |
| [Mathematics](../03_math/05_action/) | Expected Free Energy (G): Risk and Ambiguity Decomposition | EFE derivation. Policy selection. Risk-ambiguity decomposition. Active exploration. Motor inference. | `03_math/05_action/` |
| [Computer Science](../04_computer_science/05_action/) | Policy Selection and Expected Free Energy Calculation | G(π) computation. Pragmatic and epistemic components. T-maze implementation. | `04_computer_science/05_action/` |

---

## Module 6: Learning

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/06_learning/) | Epistemic Growth, Niche Construction, and Self-Transformation | Learning vs inference. Epistemic growth. Niche construction. Developmental change. Evolution as learning. | `01_philosophy/06_learning/` |
| [Cognitive Science](../02_cognitive_science/06_learning/) | Synaptic Plasticity, Dopamine, and Sleep Consolidation | Synaptic plasticity. Dopamine as precision signal. Sleep and model reduction. Computational psychiatry. | `02_cognitive_science/06_learning/` |
| [Mathematics](../03_math/06_learning/) | Gradient Descent on VFE, Bayesian Model Reduction | Parameter learning. BMR. Gradient descent on VFE. Concentration parameters. Structure learning. | `03_math/06_learning/` |
| [Computer Science](../04_computer_science/06_learning/) | Parameter Learning: Updating Dirichlet Concentrations | pA/pB updates. Online learning. Multi-episode learning. Behavioral adaptation visualization. | `04_computer_science/06_learning/` |

---

## Module 7: Communication

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/07_communication/) | Intersubjectivity, Theory of Mind, and Shared Inference | Problem of other minds. Coupled inference. Intersubjectivity. Theory of mind. Language. | `01_philosophy/07_communication/` |
| [Cognitive Science](../02_cognitive_science/07_communication/) | Mirror Neurons, Mentalizing, and Social Cognition | TPJ and mentalizing. Mirror neuron system. Social cognition development. Autism spectrum. | `02_cognitive_science/07_communication/` |
| [Mathematics](../03_math/07_communication/) | Generalized Synchrony, Mutual Information, Coupled Systems | Generalized synchrony. Mutual information. Coupled dynamical systems. Social generative models. | `03_math/07_communication/` |
| [Computer Science](../04_computer_science/07_communication/) | Multi-Agent Simulation and Signaling Games | Multi-agent simulation. Lewis signaling games. Mutual information tracking. | `04_computer_science/07_communication/` |

---

## Module 8: Planning

| Course | Subtitle | Key Concepts | Directory |
|--------|----------|-------------|-----------|
| [Philosophy](../01_philosophy/08_planning/) | Teleology, Phenomenology of Time, and Sophisticated Inference | What is planning? Teleology. Phenomenology of time. Sophisticated inference. Course synthesis. | `01_philosophy/08_planning/` |
| [Cognitive Science](../02_cognitive_science/08_planning/) | Prefrontal Cortex, Default Mode Network, and Executive Function | PFC temporal abstraction. Default mode network. Episodic future thinking. Executive function development. | `02_cognitive_science/08_planning/` |
| [Mathematics](../03_math/08_planning/) | Recursive Belief Updating, Sophisticated Inference, Tree Search | Deep temporal models. Sophisticated inference equations. Tree search complexity. Temporal abstraction. | `03_math/08_planning/` |
| [Computer Science](../04_computer_science/08_planning/) | Deep Temporal Models, Gridworlds, and Long-Horizon Planning | Deep temporal models. Gridworld implementation. Sophisticated vs. naive inference. Capstone integration. | `04_computer_science/08_planning/` |
