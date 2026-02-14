# Module 06: Learning — Philosophy of Science and Model Selection

> **Course**: Active Inference 401 | **Unit**: Philosophical Foundations | **Audience**: Advanced undergraduates / graduate students

## Learning Objectives

1. Connect Active Inference's learning mechanisms to **philosophy of science** — theory change, paradigm shifts, and model selection.
2. Analyze **Bayesian Model Reduction** as a formalization of Occam's Razor and scientific parsimony.
3. Evaluate the FEP's implications for the **demarcation problem** and the nature of scientific progress.

## Key Concepts

### 1. Theory Change as Bayesian Learning

Active Inference's parameter and structure learning formalize how belief systems evolve:

**Kuhn's paradigm shifts** → **Bayesian model selection**: Normal science = parameter learning within a fixed model structure. Paradigm crisis = accumulation of prediction errors that the current model cannot reduce. Paradigm shift = Bayesian model comparison selects a new model structure with higher evidence.

**Lakatos's research programmes** → **Hierarchical model structure**: The "hard core" = deep structural priors. The "protective belt" = peripheral parameters that are adjusted first. Model comparison only touches the hard core when the protective belt can no longer absorb anomalies.

**Popper's falsification** → **Model evidence decline**: A model is "falsified" when its evidence (marginal likelihood) drops below competitors. This is Bayesian falsification — softer than Popper's but formally precise.

### 2. Occam's Razor as Free Energy Minimization

The free energy bound F = Complexity - Accuracy formalizes Occam's Razor:

- **Accuracy**: The model should explain the data well
- **Complexity**: The model should not be more complex than necessary (KL divergence from the prior)
- **Occam's Razor**: The best model balances accuracy and simplicity — this emerges automatically from free energy minimization

Bayesian Model Reduction (BMR) goes further: it actively *simplifies* models by pruning unnecessary parameters — a formal implementation of the principle that simpler explanations are preferred.

### 3. The Demarcation Problem

What distinguishes science from non-science? Active Inference offers a formal criterion:

- **Scientific models** are generative models that make testable predictions and update on evidence
- **Pseudoscientific models** are models that minimize free energy by maximizing complexity rather than accuracy — they explain everything post-hoc but predict nothing
- **Dogmatic models** are models with extremely strong priors that resist updating — they refuse to learn

This connects to the sociology of knowledge: scientific communities can be modeled as multi-agent systems with shared generative models that undergo collective updating.

### 4. Induction and the Problem of Under-determination

Hume's problem of induction: we cannot logically justify generalization from past to future. Active Inference's response:

- Induction is **not** logical justification — it's pragmatic survival strategy
- The generative model's priors encode the agent's inductive assumptions
- These assumptions are shaped by evolution and learning — they "work" because agents with bad inductive priors don't survive
- Under-determination is resolved by model comparison: when data under-determine the model, free energy minimization selects the simplest compatible model

### 5. Scientific Realism and the FEP

Does science discover reality, or just build useful models?

- **Scientific realism**: Mature scientific theories approximately describe reality
- **Constructive empiricism** (van Fraassen): Science aims for empirical adequacy, not truth about unobservables
- **FEP position**: Generative models aim at predictive accuracy bounded by complexity — this is closer to constructive empiricism but with a formal criterion (model evidence) for theory choice

### 6. Dewey's Pragmatist Learning Theory

John Dewey's philosophy of education anticipated key Active Inference insights about learning:

**Learning by doing**: Dewey insisted that learning is not passive reception of information but active inquiry — the organism encounters a problem, generates hypotheses, tests them through action, and updates beliefs. Active Inference formalizes this: the agent encounters prediction errors, generates policies to resolve them, acts, and updates its generative model based on the outcome.

**Inquiry as prediction error resolution**: Dewey's five stages of inquiry (situation → problem → hypothesis → reasoning → testing) map directly onto Active Inference: ambiguous situation → prediction error → policy proposal → mental simulation → active testing. The parallel is not metaphorical — both describe the same cycle of prediction, error, and model updating.

**Education as model enrichment**: Dewey argued that education should expand the child's *field of experience* — encounter more diverse situations, develop richer generative models. Active Inference: education is the systematic expansion of the learner's state space and the calibration of priors through guided exposure to prediction errors.

### 7. Development, Habit, and the Plasticity-Stability Trade-off

The philosophical dimensions of developmental learning reveal key tensions:

**Critical periods as precision transitions**: The philosophical puzzle of critical periods — why does language learning become harder after puberty? — receives an Active Inference interpretation: early development features high precision on prediction errors (learning rates are high, priors are weak), while maturation gradually shifts precision toward priors (learning slows, the model stabilizes). This plasticity-stability trade-off is not a bug but a rational strategy: early flexibility enables model acquisition; later rigidity enables efficient inference.

**Habit as crystallized inference**: Ravaisson's and Dewey's philosophy of habit converges with Active Inference: habits are policies whose priors have been so strongly reinforced that they are executed automatically, without deliberation. Habit formation is the progressive accumulation of evidence for a particular policy until its expected free energy is so low that it is selected by default. The philosophical question — are habits "mindless"? — is reframed: habits are not mindless but *transparently minded*, like Heidegger's ready-to-hand.

> **Cross-Track Connection — Neuroscientific Frontiers (Module 06)**: The philosophical plasticity-stability distinction corresponds directly to the neural mechanisms of synaptic pruning and dopaminergic/cholinergic modulation described in the neuroscience track — providing a rare case of genuine philosophy-neuroscience convergence.

## Summary

Active Inference formalizes key philosophy of science concepts: theory change as Bayesian updating, Occam's Razor as the complexity-accuracy trade-off, and falsification as model evidence decline. BMR implements formal parsimony. Dewey's pragmatist education theory anticipates Active Inference's emphasis on learning through action and prediction error. The plasticity-stability trade-off in development reflects a rational precision optimization, and habit formation is the crystallization of well-evidenced policies. The FEP offers a criterion for demarcation and addresses the problem of induction pragmatically rather than logically.

## Further Reading

- Friston, K. J. et al. (2017). Active inference, curiosity and insight. *Neural Computation*, 29(10), 2633-2683.
- Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press, Ch. 9-10.
- Van de Cruys, S. et al. (2014). Precise minds in uncertain worlds. *Psychological Review*, 121(4), 649-675.
- Dewey, J. (1938). *Logic: The Theory of Inquiry*. Henry Holt and Company.
- Carlisle, C. (2014). *On Habit*. Routledge.
