# Module 08: Planning — Prefrontal Cortex, Decision-Making, and Temporal Abstraction

## Learning Objectives

1. Describe the role of the **prefrontal cortex** in planning as hierarchical policy selection over extended timescales.
2. Explain how the brain evaluates Expected Free Energy through interactions between prefrontal cortex, basal ganglia, and dopaminergic systems.
3. Analyze planning deficits (frontal lobe syndrome, impulsivity, addiction) as specific failures of hierarchical temporal inference.

## Introduction

Planning is the brain's most temporally extended form of inference — evaluating what might happen next, and the step after that, and choosing actions accordingly. The **prefrontal cortex (PFC)**, the most recently evolved and most elaborate region of the human brain, is the neural substrate of planning. It maintains hierarchical, temporally extended representations of possible futures — what Active Inference formalizes as policy evaluation through Expected Free Energy.

## Key Concepts

### 1. Prefrontal Cortex and Temporal Abstraction

The PFC is organized along a rostro-caudal gradient of **temporal abstraction**:

- **Posterior PFC** (premotor, dorsolateral): encodes concrete, near-future motor plans
- **Anterior PFC** (frontopolar cortex, BA10): encodes abstract, long-horizon goals and meta-cognitive planning

Badre and D'Esposito (2009) demonstrated this gradient experimentally: progressively more abstract action rules activated progressively more anterior regions of PFC. In Active Inference terms, this gradient corresponds to the hierarchical depth of the generative model — lower levels predict concrete sensorimotor states; higher levels predict abstract, temporally extended outcomes.

### 2. Basal Ganglia and Policy Selection

The **basal ganglia** (striatum, globus pallidus, subthalamic nucleus) implement a selection mechanism for policies. The direct pathway facilitates a chosen policy; the indirect pathway suppresses competing policies. Dopaminergic input from the ventral tegmental area (VTA) and substantia nigra pars compacta (SNc) modulates the precision of policy selection:

- High dopamine → high precision → decisive policy selection
- Low dopamine → low precision → indecisive, slow policy selection (as in Parkinson's disease)

The **Expected Free Energy** of each policy is evaluated through cortico-basal ganglia-thalamic loops, with the ventromedial PFC encoding **pragmatic value** (how well the policy achieves goals) and the dorsolateral PFC and frontopolar cortex encoding **epistemic value** (how much information the policy provides).

### 3. Planning Disorders

- **Frontal lobe syndrome**: Damage to PFC impairs the ability to plan, sequence actions, and inhibit inappropriate responses. Patients may show "utilization behavior" — automatically using objects placed in front of them without a plan. Interpretation: loss of hierarchical policy evaluation above the concrete motor level.
- **Impulsivity**: May reflect low precision on long-horizon policies → the agent selects short-term policies that minimize immediate free energy without considering future consequences. Connects to temporal discounting (preference for immediate over delayed reward).
- **Addiction**: A progressively narrowing policy space — the generative model increasingly predicts that only one policy (drug seeking) minimizes expected free energy, overriding competing policies for health, relationships, and goals.

## Clinical Connections

- **ADHD and impulsivity**: Reduced dopaminergic tone → low precision on policy evaluation → difficulty sustaining long-term plans, shifting attention to whatever provides immediate prediction error reduction.
- **Depression and planning paralysis**: High precision on negative outcome predictions → all policies evaluated as leading to bad outcomes → behavioral inertia and anhedonia (nothing is worth doing).

## Conclusion

Planning is hierarchical, temporally extended policy evaluation implemented by the prefrontal cortex, basal ganglia, and dopaminergic system. Understanding this neural architecture connects Active Inference to clinical conditions involving planning deficits and to the broader question of what makes human cognition uniquely powerful. This concludes the Cognitive Science course's eight-module exploration of the neural implementation of Active Inference.
