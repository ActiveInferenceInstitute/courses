# Station: Learning (Philosophical Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Epistemology, phenomenology, 4E cognition
- **Topic**: Learning
- **Subtitle**: Epistemology of Model Revision and Epistemic Virtue
- **Lab Style**: Seminar Discussion
- **Audience**: PhD students and researchers
- **Tone**: Argumentative, dialectical, historically informed

## Content Guidance

This module must treat learning as an epistemological phenomenon — a process of rational belief revision — and evaluate the FEP's contribution to the classical problems of epistemology. Content must address whether Bayesian model comparison (the mechanism by which the FEP formalizes structure learning) constitutes a formal account of Kuhnian paradigm shifts, whether variational free energy minimization embodies recognizable epistemic virtues (accuracy, simplicity, coherence), and whether the FEP offers a solution to the problem of induction. The module must also engage with abductive inference (inference to the best explanation) and ask whether the FEP's preference for models with higher evidence (lower VFE) formalizes abduction or replaces it with something else. Throughout, the treatment must distinguish between learning as parameter estimation (updating beliefs within a fixed model), learning as model selection (choosing among competing models), and learning as structure learning (discovering new model architectures) — each of which has different epistemological implications.

## Key Concepts

- **Kuhnian paradigm shifts as structure learning**: Kuhn's (1962) account of scientific revolutions — the shift from one paradigm to another through anomaly accumulation, crisis, and revolution — can be read as a process of structure learning in which the generative model itself is revised, not just its parameters. Does Bayesian model reduction (Friston et al., 2016) formalize this process, or does it miss the sociological and hermeneutic dimensions that Kuhn considered essential?
- **Abductive inference (inference to the best explanation)**: Lipton's (2004) account of abduction as selecting the explanation that, if true, would provide the most understanding. In FEP terms, model selection via free energy scoring selects the model that best balances accuracy (fit to data) and complexity (prior divergence). Is this the same thing as abduction, or does abduction involve irreducibly qualitative judgments of explanatory virtue that resist formalization?
- **Epistemic virtues and VFE minimization**: Variational free energy decomposes into accuracy minus complexity (equivalently, energy minus entropy). This decomposition can be read as encoding epistemic virtues: empirical adequacy (accuracy) and theoretical parsimony (complexity). Does the FEP thereby provide a formal theory of epistemic rationality, or does it reduce epistemic rationality to a single optimization criterion that collapses distinctions between genuinely different virtues (simplicity, unification, fruitfulness)?
- **The problem of induction**: Hume's challenge — how can past observations justify expectations about the future? — has no universally accepted solution. The FEP's answer appears to be that organisms that persist must have generative models whose predictions are sufficiently accurate, and that free energy minimization is a process that tends to produce such models. Does this solve the problem of induction (by grounding inductive success in self-organization) or merely describe how induction happens without justifying it?
- **Bayesian epistemology and the problem of priors**: In Bayesian inference, priors shape the posterior. In the FEP, priors are baked into the generative model. Who chose the priors? Evolution, development, learning? The regress of priors is a core epistemological challenge for any Bayesian framework, including the FEP.

## Key References

- **Kuhn, T. (1962)**: *The Structure of Scientific Revolutions*. The classic account of scientific theory change. Essential for evaluating whether the FEP's structure learning mechanisms capture the qualitative character of paradigm shifts or merely approximate a sanitized, rational reconstruction.
- **Lipton, P. (2004)**: *Inference to the Best Explanation* (2nd ed.). The standard philosophical account of abduction. Provides the framework for asking whether Bayesian model comparison is a formalization of abduction or a replacement for it.
- **Williamson, T. (2000)**: *Knowledge and Its Limits*. Develops an externalist epistemology that bears on the FEP's treatment of learning: if knowledge is a mental state that is factive and anti-luminous, what are the implications for understanding the recognition density as a form of knowledge?
- **Tenenbaum, J., Kemp, C., Griffiths, T., & Goodman, N. (2011)**: "How to grow a mind: Statistics, structure, and abstraction." Provides the computational-level account of learning as Bayesian inference over hierarchical, compositional models — the framework that the FEP generalizes and that this module must critically evaluate.
- **Ramstead, M., Kirchhoff, M., & Friston, K. (2020)**: "A tale of two densities: Active inference is enactive inference." Argues that the FEP's treatment of learning — updating generative models to maintain adaptive fit — is continuous with the enactive tradition's emphasis on sense-making and structural coupling, not merely a Bayesian add-on to enactivism.

## Prerequisite Modules

Module 04 (Cognition) must be completed first. The analysis of cognition as approximate inference — including the debate about where cognition ends and the role of variational methods — provides the conceptual foundation for asking how generative models change over time. Learning is cognition on a longer timescale, and the philosophical issues raised by the cognition module (internalism vs. externalism, the status of the generative model, the role of variational families) recur in transformed guise when applied to learning.

## Cross-Unit Connections

- **Advanced Theory (Module 06)**: The theory treatment covers Bayesian model reduction, variational Laplacian, and the formal computation of model evidence. The philosophical treatment here should interrogate the epistemological significance of these formal operations: does Bayesian model reduction (which prunes model parameters under a complexity cost) formalize Occam's razor, and if so, is it the right formalization (complexity in information-theoretic terms vs. simplicity in explanatory terms)?
- **Neuroscientific Frontiers (Module 06)**: The neuroscience treatment examines synaptic plasticity as VFE minimization and the role of neuromodulators in precision weighting. The philosophical module should ask whether neural learning mechanisms (Hebbian plasticity, dopamine-modulated learning) are best understood as implementing Bayesian inference, or whether the Bayesian description is an idealization that obscures the messy, contingent character of actual neural learning.
- **Research Methods (Module 06)**: The methods treatment covers parameter estimation, model fitting, and simulation-based calibration. The philosophical module should address the epistemology of model fitting itself: when we fit a generative model to behavioral data, are we discovering the subject's actual generative model or constructing a useful fiction? This connects to broader debates about scientific realism and instrumentalism.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
