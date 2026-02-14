# Module 05: Action — Motor Circuits and Active Inference

> **Course**: Active Inference 101 | **Unit**: Computational Neuroscience | **Audience**: First-semester undergraduates

## Learning Objectives

1. Describe how the **motor cortex** generates actions through descending predictions.
2. Explain the role of the **basal ganglia-thalamo-cortical loop** in policy selection.
3. Describe how the **cerebellum** updates forward models through climbing fiber error signals.

## Introduction

How does the brain move the body? Traditional neuroscience says: the motor cortex sends commands to muscles. Active Inference says something different: the motor cortex sends *predictions* about expected body states, and spinal reflexes act to fulfill those predictions. This module explores the neural circuitry of action.

## Key Concepts

### 1. Motor Cortex — Predictions, Not Commands

The primary motor cortex (M1) doesn't send "commands" — it sends **proprioceptive predictions**:

- M1 predicts what muscle lengths, joint angles, and forces *should* be
- Spinal motor neurons compare these predictions with actual proprioceptive feedback
- The prediction error drives muscles to contract or relax until the prediction is fulfilled

This explains why movement feels effortless when predictions are accurate and clumsy when they're wrong (like walking on an uneven surface in the dark).

### 2. The Basal Ganglia Loop — Selecting What to Do

The cortico-basal ganglia-thalamo-cortical loop selects which policy to execute:

1. **Cortex** → sends current context and candidate policies to the basal ganglia
2. **Striatum** (input of basal ganglia) → evaluates policies using dopaminergic signals
3. **Direct pathway** → "Go!" — releases selected actions through the thalamus
4. **Indirect pathway** → "No-Go!" — suppresses competing actions
5. **Thalamus** → gates the selected policy back to the motor cortex for execution

**Dopamine** tips the balance: more dopamine favors the Go pathway (more action), less dopamine favors the No-Go pathway (less action). This is why Parkinson's (low dopamine) causes difficulty initiating movement.

### 3. The Cerebellum — Learning from Motor Errors

The cerebellum refines motor predictions through a specific error-correction circuit:

- **Parallel fibers** carry the current motor prediction (from mossy fibers via granule cells)
- **Climbing fibers** (from the inferior olive) carry the **error signal** — the mismatch between predicted and actual outcomes
- When climbing fibers fire, they modify the synapses between parallel fibers and Purkinje cells
- Over many repetitions, the cerebellum's predictions become more accurate

This is the neural basis of motor learning — why practicing a skill makes it smoother and more automatic.

### 4. Mirror Neurons and Action Understanding

**Mirror neurons** fire both when you perform an action and when you observe someone else performing the same action:

- Found in premotor cortex and parietal cortex
- In Active Inference, they're the same prediction mechanism: your brain generates a motor prediction whether you're doing or watching
- This connects action to social cognition — understanding others' actions by simulating them internally

### 5. Disorders of Motor Control

| Disorder | Neural Problem | Active Inference Interpretation |
|----------|---------------|-------------------------------|
| **Parkinson's** | Dopamine loss in basal ganglia | Impaired Go pathway → can't select actions |
| **Huntington's** | Loss of indirect pathway neurons | Impaired No-Go pathway → involuntary movements |
| **Cerebellar ataxia** | Cerebellar damage | Broken forward models → uncoordinated movement |
| **Tourette's** | Basal ganglia hyperactivity | Involuntary tic selection → unwanted actions |

## Summary

Action is implemented through motor cortex predictions fulfilled by spinal reflexes, policy selection via the basal ganglia-thalamo-cortical loop, and forward model refinement in the cerebellum. Dopamine modulates the balance between Go (act) and No-Go (suppress) pathways. Motor disorders are disruptions of specific components of this circuit.

## Further Reading

- Adams, R. A., Shipp, S., & Friston, K. J. (2013). Predictions not commands. *NeuroImage*, 76, 294-305.
- Shadmehr, R. & Krakauer, J. W. (2008). A computational neuroanatomy for motor control. *Experimental Brain Research*, 185(3), 359-381.
- Rizzolatti, G. & Sinigaglia, C. (2010). The functional role of the parieto-frontal mirror circuit. *Nature Reviews Neuroscience*, 11(4), 264-274.
