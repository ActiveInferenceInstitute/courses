# Module 06: Learning — Clinical Translation and Computational Psychiatry

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Apply Active Inference to **computational psychiatry** — using generative models to understand mental illness.
2. Analyze clinical disorders through the lens of **aberrant precision, prediction errors, and model structure**.
3. Evaluate the **translational pipeline** from computational models to clinical interventions.

## Key Concepts

### 1. Computational Psychiatry Framework

Computational psychiatry uses mathematical models to bridge the gap between brain mechanisms and psychiatric symptoms:

**The promise**: Instead of categorizing patients by descriptive symptoms (DSM), characterize them by computational dysfunction — which specific inference process is impaired.

**Active Inference account**: Mental disorders arise from dysfunction in specific components of the generative model or its inversion:

- **Aberrant precision**: Over- or under-weighting prediction errors
- **Dysfunctional model structure**: Incorrect or absent connections in the generative model
- **Maladaptive preferences**: Pathological prior preferences (C vector)
- **Impaired model updating**: Inability to update beliefs despite contradicting evidence

### 2. Disorder-Specific Models

**Schizophrenia**: Characterized by aberrant sensory precision — over-weighting sensory prediction errors relative to prior beliefs:

- Hallucinations: Overly precise sensory priors generate percepts without external stimulation
- Delusions: Aberrant precision on certain belief channels makes them resistant to updating
- Computational biomarker: Abnormal precision parameters recovered from behavioral tasks

**Depression**: Characterized by pessimistic priors and reduced precision on positive prediction errors:

- Negative bias: Generative model expects negative outcomes (pathological C vector)
- Anhedonia: Reduced precision on reward prediction errors → failure to learn from positive outcomes
- Rumination: Deep temporal model with strong negative predictions generates persistent negative counterfactuals

**Anxiety**: Characterized by elevated precision on threat-related prediction errors:

- Hypervigilance: Over-precise threat PE detection → excessive response to ambiguous stimuli
- Intolerance of uncertainty: Pathologically high expected precision → compulsive information seeking
- Avoidance: Actions selected to minimize exposure to high-precision threat PEs

**Autism**: Characterized by altered precision hierarchy:

- Sensory overload: High sensory precision (over-weighted PEs) → difficulty with noisy environments
- Predictability preference: Strong priors → distress when routines are disrupted
- Social inference: Reduced precision on social prediction errors → difficulty with Theory of Mind

### 3. Translational Pipeline

**Step 1: Computational theory** — Formalize the disorder as dysfunction in a specific computational variable
**Step 2: Behavioral validation** — Show that patients differ from controls on the predicted computational parameter (using tasks from Module 04)
**Step 3: Neural validation** — Show that the computational difference maps onto neural differences (using methods from Modules 01, 03)
**Step 4: Pharmacological validation** — Show that drugs known to affect the disorder change the predicted computational variable (dopamine for precision, serotonin for prior beliefs)
**Step 5: Treatment development** — Design interventions targeting the specific computational dysfunction

### 4. Clinical Trial Design for Computational Psychiatry

**Enrichment strategies**: Use computational phenotyping to select patients most likely to respond to a treatment targeting a specific computational variable.

**Bayesian adaptive trials**: Use Active Inference principles in trial design itself — adaptively allocate patients to treatment arms based on accumulating evidence, minimizing the number of patients needed.

**Digital phenotyping**: Collect computational parameters longitudinally using smartphone-based tasks and wearable sensors. Track precision, learning rate, and volatility estimates in real-time to predict relapse.

### 5. Ethical Considerations

Computing on mental states raises ethical concerns: privacy of computational phenotypes, risk of computational discrimination, informed consent for model-based classification, and the danger of reducing complex human experience to a few parameters.

## Summary

Computational psychiatry uses Active Inference to model mental disorders as dysfunction in specific inference variables — precision, model structure, preferences, and updating. Disorder-specific models have been proposed for schizophrenia, depression, anxiety, and autism. The translational pipeline moves from theory through behavioral, neural, and pharmacological validation to intervention design.

## Further Reading

- Friston, K. J. et al. (2014). Computational psychiatry: the brain as a phantastic organ. *The Lancet Psychiatry*, 1(2), 148-158.
- Adams, R. A. et al. (2013). The computational anatomy of psychosis. *Frontiers in Psychiatry*, 4, 47.
- Stephan, K. E. & Mathys, C. (2014). Computational approaches to psychiatry. *Current Opinion in Neurobiology*, 25, 85-92.
