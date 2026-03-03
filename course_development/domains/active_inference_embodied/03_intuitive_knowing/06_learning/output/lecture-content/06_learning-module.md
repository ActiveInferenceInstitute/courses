# Module 06: Learning in Embodied Cognition — Somatic Learning

## Learning Objectives

1. Define **somatic learning** as the updating of the embodied generative model through physical practice, contemplative training, and experiential engagement.
2. Analyze how **practice, repetition, and corrective feedback** implement Dirichlet parameter learning in the somatic domain.
3. Apply the Active Inference framework to explain the **stages of embodied skill acquisition** and the role of plateaus, breakthroughs, and regressions.

## Introduction

You cannot learn to swim from a textbook. You cannot learn to cook by reading recipes. You cannot learn to feel empathy by studying psychology. Embodied learning requires *doing* — engaging the body in repeated cycles of prediction, action, and error correction that progressively refine the somatic generative model.

This module examines how the embodied agent learns — not through symbolic instruction alone but through the iterative process of somatic prediction error minimization.

## Key Concepts

### 1. Motor Learning as Parameter Updating

When learning a new physical skill (juggling, typing, a yoga pose), the embodied agent's generative model undergoes systematic refinement:

- **Early learning** (high prediction error): The proprioceptive predictions are rough — the body doesn't yet know where to move. Each attempt generates large prediction errors. Learning rate is high.
- **Intermediate learning** (declining prediction error): The predictions become more accurate. The agent can perform the basic pattern but still generates errors on precision demands (timing, force calibration). Learning rate is moderate.
- **Late learning** (minimal prediction error): The predictions are precise and habitual. The policy prior is strongly shaped. Learning rate is low — the agent is resistant to change.

This trajectory mirrors Dirichlet parameter learning: early observations (with small concentration parameters) produce large updates; later observations (with large concentration parameters) produce small updates. The "10,000 hours" heuristic for expertise corresponds to the accumulation of sufficient concentration parameters to generate high-precision predictions.

### 2. Learning Plateaus and Phase Transitions

Embodied learning is not linear — it involves **plateaus** (periods of no apparent improvement) and **breakthroughs** (sudden competence jumps):

- **Plateaus** occur when the current generative model structure is being optimized locally — the parameters are being fine-tuned within the existing model architecture
- **Breakthroughs** occur when the model undergoes a **structural change** — a new level of hierarchy is added, a new latent variable is discovered, or a previously unsuspected relationship is recognized
- Example: A piano student may plateau for weeks while refining finger technique (parameter learning), then suddenly "break through" when they discover that phrasing is about breathing, not just notes (structural learning — a new variable enters the model)

### 3. Contemplative Practices as Precision Training

Meditation, breathwork, yoga, and body scanning are **systematic precision training** for the embodied generative model:

- **Mindfulness meditation**: Increases precision on present-moment interoceptive and exteroceptive observations while decreasing precision on self-referential narrative predictions (the "default mode network")
- **Yoga**: Increases precision on proprioceptive observations at extreme ranges of motion — expanding the domain over which the body-model makes accurate predictions
- **Breathwork**: Increases precision on respiratory interoception — training the agent to detect and modulate autonomic states through voluntary control of a normally automatic system

These practices don't add new information — they *change the precision structure* of the embodied generative model, making the agent more sensitive to signals that were previously below the attention threshold.

### 4. Trauma as Maladaptive Learning

Trauma can be understood as **maladaptive embodied learning** — a single high-impact experience (or repeated exposure) creates pathologically high-precision priors that distort ongoing inference:

- The traumatized agent's generative model overfits to the traumatic context → neutral stimuli generate threat prediction errors
- The body's interoceptive model becomes locked in a defensive state (hypervigilance, freeze, dissociation) → the learned prior overwhelms current evidence
- Somatic trauma therapies (EMDR, somatic experiencing, yoga therapy) work by gradually reducing the precision on traumatic priors — decoupling the somatic alarm signals from the current safe context

## Applications

- **Rehabilitation after injury**: A patient relearning to walk after a stroke is updating their motor generative model to accommodate new neural pathways — the old B matrix (pre-stroke motor transitions) no longer holds, and the patient must build a new one through thousands of repetitions. Early sessions generate massive proprioceptive prediction errors; later sessions show progressive refinement.
- **Contemplative education**: Integrating mindfulness training into medical education systematically trains interoceptive precision in future clinicians — increasing their capacity for empathic resonance with patients and improving clinical decision-making through enhanced somatic awareness.

## Conclusion

Somatic learning refines the embodied generative model through practice, contemplative training, and experiential engagement. The process involves parameter updating, structural phase transitions, precision training, and — when things go wrong — maladaptive learning that requires therapeutic intervention. The next module explores embodied communication — how somatic knowledge is shared between bodies.
