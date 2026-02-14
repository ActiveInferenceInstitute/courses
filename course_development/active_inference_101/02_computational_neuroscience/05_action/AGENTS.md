# Station: Action (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Motor cortex, basal ganglia, cerebellum, spinal reflexes as active inference, dopamine and action selection
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module maps action selection and motor control onto neural motor circuits. Content should:

1. **Present motor control as active inference**: The motor cortex generates proprioceptive predictions; spinal motor neurons act as reflex arcs that minimize the error between predicted and actual body position.
2. **Define key terms precisely**:
   - **Motor cortex**: The cortical region that generates predictions about body state (proprioceptive predictions)
   - **Basal ganglia**: Subcortical nuclei that evaluate competing action policies via expected free energy, selecting the best policy
   - **Cerebellum**: A structure that maintains a forward model predicting the sensory consequences of actions, enabling rapid error correction
   - **Spinal reflex arc**: The simplest implementation of active inference -- a prediction error minimizer that adjusts muscle tension to match cortical predictions
3. **Connect dopamine to action selection**: The basal ganglia use dopaminergic signals to weight competing policies. Parkinson's disease results from dopamine loss disrupting this process.
4. **Distinguish habitual from goal-directed action**: Dorsolateral striatum supports habitual policies; dorsomedial striatum supports goal-directed EFE evaluation.

## Active Inference Integration

- Motor commands are proprioceptive predictions, not direct muscle commands (Adams, Shipp, & Friston, 2013)
- The basal ganglia implement policy selection by evaluating expected free energy of competing actions
- The cerebellum implements a forward model for rapid prediction of action consequences

## Assessment Alignment

Questions should test the ability to:
- Explain how a simple reaching movement works as active inference through the motor system
- Describe how Parkinson's disease disrupts action selection via impaired precision weighting
- Compare the roles of basal ganglia (policy selection) and cerebellum (forward model) in action

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
