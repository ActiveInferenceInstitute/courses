# Lab: Philosophy of Science Through Active Inference

> **Learning Goal:** Apply the rigorous formalisms of Active Inference to analyze the mechanics of theory change, formalize parsimony (Occam's razor), adjudicate demarcation criteria, and systematically address the problem of induction.

## Part 1: Theory Change & Formal Paradigm Shifts

**Exercise**: Choose a major historical scientific revolution (e.g., Ptolemaic Geocentrism → Copernican Heliocentrism, Phlogiston theory → Oxygen theory, Newtonian Mechanics → General Relativity). Analyze the deep structure of this revolution by mapping it explicitly onto Active Inference mechanics:

| Historical Phase | Philosophy of Science Concept | Active Inference Formalization | Application to your Case Study |
|-------|-------------------|------------------------|--------------------------------|
| Normal Science | Puzzle-solving within a paradigm | Continuous parameter learning (updating the $a$ matrix) | |
| Anomaly | Persistent, unexplained observations | Chronically high sensory prediction errors ($pe$) | |
| Crisis | Loss of faith in the paradigm | Rising expected free energy ($G$), precipitous drop in model evidence ($ln P(y \| m)$) | |
| Revolution | Adoption of a new paradigm | Bayesian model selection (structural update via Bayesian Model Reduction) | |
| Resolution | Return to normal science | Parameter learning within the newly selected, high-evidence model | |

Write a 400-word critical analysis of your chosen case: Does the mathematical concept of Bayesian model selection genuinely capture the *sociological* and *political* dimensions of a Kuhnian paradigm shift, or does it overly intellectualize the messy history of science?

{fill:textarea}

## Part 2: Occam's Razor and Formal Parsimony

> **Learning Goal:** Apply the mathematical necessity of the Complexity-Accuracy trade-off ($F \approx \text{Complexity} - \text{Accuracy}$) to adjudicate between competing models.

**Exercise**: Consider two competing generative models attempting to explain the exact same sensory dataset:

- **Model A (Simple)**: 3 free parameters, Accuracy (log-likelihood) = 8.0, Complexity penalty = 2.0
- **Model B (Complex)**: 30 free parameters, Accuracy (log-likelihood) = 8.5, Complexity penalty = 9.0

1. **Calculation**: Compute the approximate variational free energy for each model.
2. **Adjudication**: Which model does Occam's Razor mathematically favor, and why?
3. **The Complexity Boundary**: At exactly what level of Accuracy would Model B scientifically justify its massive 30-parameter complexity? Show the math.
4. **Machine Learning Parallel**: Explain in detail how this fundamental trade-off perfectly mirrors the concepts of "overfitting" and "regularization" (e.g., L1/L2 penalties) in contemporary deep learning architectures.

{fill:textarea}

## Part 3: The Demarcation Problem

> **Learning Goal:** Apply the Active Inference framework to solve Karl Popper's classic demarcation criterion (distinguishing rigorous science from unfalsifiable pseudoscience).

**Exercise**: Analyze the following claims. Classify each as a scientific hypothesis, a pseudoscientific dogma, or an axiomatic prior using Active Inference criteria. Specifically, analyze the *precision* assigned to the prior belief versus the *precision* assigned to contradictory sensory prediction errors.

| Claim | Classification | Precision Dynamics (Priors vs. Sensory PE) |
|-------|---------------|-----------------|
| "The Earth orbits the Sun in an elliptical path." | | |
| "Your astrological birth chart dictates your personality." | | |
| "Homeopathic remedies work via the 'memory' of water." | | |
| "Evolution proceeds via natural selection." | | |
| "A global, omnipotent conspiracy is secretly hiding the truth of flat earth." | | |

Write a 250-word synthesis: How does "dogmatic belief updating" (where infinite precision is assigned to top-down priors, instantly explaining away all bottom-up evidence) structurally define a conspiracy theory within a belief network?

{fill:textarea}

## Part 4: Induction and Evolutionary Priors

**Exercise**: David Hume's classic problem of induction asks: *By what rational justification can we expect the future to resemble the past?*

1. **The Problem**: State Hume's problem precisely in the language of probability theory.
2. **The Active Inference Solution**: Explain Active Inference's pragmatic, evolutionary response to induction. (Hint: The agent doesn't need a logical guarantee; it simply relies on phylogenetic priors forged by natural selection to minimize surprise).
3. **Philosophical Satisfaction**: Is this evolutionary response philosophically satisfying? Does it actually solve Hume's logical problem, or does it merely explain *why* human brains are forced to make inductive leaps to survive?
4. **Prior Selection**: How does this evolutionary history ultimately solve the infinite regress of prior selection in Bayesian epistemology?

{fill:textarea}

## Part 5: Critical Meta-Reflection

In 350 words, provide a conclusive reflection on the epistemology of the Free Energy Principle: Does Active Inference provide a genuinely novel, mathematically unified account of the scientific method, or is it fundamentally a sophisticated post-hoc "curve-fitting" exercise that forcefully retrofits complex philosophy of science debates into a rigid thermodynamic metaphor?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept Analyzed |
|------|----------------|-------------|
| 1 | Historical formalization | Kuhnian Theory Change / Bayesian Model Selection |
| 2 | Quantitative reasoning | Occam's Razor / The Complexity Penalty |
| 3 | Epistemological mapping | The Demarcation Problem / Dogmatic Precision |
| 4 | Philosophical argumentation | The Problem of Induction / Phylogenetic Priors |
| 5 | Critical reflection | The Limits of Mathematical Formalization |
