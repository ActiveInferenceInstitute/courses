# Lab: Clinical Translation and Computational Psychiatry

> **Learning Goal:** Apply Active Inference models to clinical disorders, design translational studies, and evaluate therapeutic implications.

## Part 1: Disorder Modeling

**Exercise**: For each disorder, identify the primary computational dysfunction and design a behavioral task to measure it:

| Disorder | Primary Dysfunction | Predicted Behavioral Pattern | Proposed Task |
|----------|--------------------|-----------------------------|---------------|
| Schizophrenia | Aberrant sensory precision (too high) | Over-reliance on sensory input, resistance to perceptual priors | Force-fusion task: present ambiguous stimuli with varying prior probability — patients should be less influenced by manipulated priors |
| Depression | Pessimistic priors + reduced reward PE precision | Win-stay reduced, loss-shift increased, negative expectation bias | Probabilistic reward task with positive/negative feedback — patients should show blunted learning from positive feedback |
| GAD | Elevated threat PE precision | Hypervigilance, excessive threat detection, safety signal insensitivity | Threat/safety conditioning with reversal — patients should show persistent threat response despite safety signals |
| Autism | High sensory precision, low social precision | Excellent perceptual discrimination, difficulty with social inference | Visual search (high accuracy expected in ASD) + social inference task (reduced accuracy expected) |

For one disorder of your choice, expand the model: specify all parameter values and generate predictions for 200 simulated trials.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Translational Pipeline

> **Learning Goal:** Design a complete translational study.

**Exercise**: Take the schizophrenia model through all 5 pipeline steps:

**Step 1 — Computational theory**: Schizophrenia involves aberrant precision in the sensory hierarchy. Specifically, NMDA receptor hypofunction reduces the precision of top-down predictions, making sensory prediction errors disproportionately influential.

**Step 2 — Behavioral validation**: Design a task (e.g., hollow mask illusion — do patients fail to see the illusion because their strong sensory PEs override the top-down "face" prior?)

**Step 3 — Neural validation**: Measure MMN in patients — reduced MMN suggests impaired prediction error generation (or is it increased PE due to aberrant precision? The direction of the prediction matters).

**Step 4 — Pharmacological validation**: Administer ketamine (NMDA antagonist) to healthy controls. Does it reproduce the computational profile seen in patients?

**Step 5 — Treatment**: If the dysfunction is NMDA-related, would NMDA agonists (e.g., glycine site agonists) restore normal precision? What computational parameters would you monitor?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Clinical Trial Design

> **Learning Goal:** Design a Bayesian adaptive clinical trial.

**Exercise**: Design a trial for a novel anxiety treatment targeting threat precision:

1. **Primary outcome**: Reduction in threat PE precision (measured computationally from threat/safety task)
2. **Secondary outcome**: Clinical symptom reduction (GAD-7 scale)
3. **Enrichment**: Only enroll patients with computational phenotype showing elevated threat precision (top quartile on baseline computational assessment)
4. **Adaptive design**: After every 10 patients, update the posterior on treatment effect. If Pr(treatment effective) > 0.95, stop for efficacy. If Pr(treatment effective) < 0.05, stop for futility.
5. **Sample size**: Estimate needed N for 80% power

What advantages does this computational enrichment + adaptive design offer over standard parallel-group RCT?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Digital Phenotyping Scenario

> **Learning Goal:** Design a digital phenotyping system.

**Exercise**: Design a smartphone-based monitoring system for depression:

1. **Daily task**: 2-minute probabilistic learning task on smartphone (takes 50 trials)
2. **Parameters tracked**: Learning rate (α), reward precision (ω_reward), loss precision (ω_loss), policy precision (β)
3. **Passive measures**: Activity level (accelerometer), social interaction (communication app usage), sleep (phone usage patterns)
4. **Predictive model**: Use changes in computational parameters to predict relapse 1-2 weeks before clinical symptoms emerge

Design the alert system: What parameter changes trigger a clinical alert? How do you balance sensitivity (catching relapses) vs. specificity (avoiding false alarms)?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 300 words, reflect: Computational psychiatry promises to transform diagnosis and treatment by identifying precise computational dysfunctions. But psychiatric disorders are enormously complex — involving genetic, developmental, social, and environmental factors. Can a computational model capture enough of this complexity to be clinically useful? Where is the boundary between useful simplification and harmful reductionism?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Disorder modeling | Mapping dysfunction to parameters |
| 2 | Pipeline design | Translational validation |
| 3 | Clinical trial | Bayesian adaptive design |
| 4 | Digital monitoring | Real-time computational tracking |
| 5 | Critical evaluation | Reductionism vs. utility |
