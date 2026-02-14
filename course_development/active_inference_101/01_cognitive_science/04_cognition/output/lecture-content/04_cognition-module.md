# Module 04: Cognition — How Agents Organize and Update Beliefs

> **Course**: Active Inference 101 | **Unit**: Cognitive Science | **Audience**: First-semester undergraduates

## Learning Objectives

1. Explain **variational free energy** as a measure of how well the agent's model fits the world.
2. Describe how **attention** works as precision weighting — turning up the volume on relevant information.
3. Analyze how cognitive biases and disorders relate to disrupted belief optimization.
4. Understand the **accuracy-complexity trade-off** as the brain's fundamental design principle.

## Introduction

Perception (Module 03) is about sensing the world. Cognition is about *thinking* — organizing beliefs, paying attention to what matters, and deciding what to make of ambiguous information. In Active Inference, cognition is the ongoing process of optimizing the generative model to minimize **variational free energy**.

> **Key Insight**: The brain isn't a camera that records reality. It's a hypothesis-testing machine that constantly asks "What model of the world best explains what I'm experiencing?" Cognition is this ongoing testing process — updating beliefs, reallocating attention, and choosing the simplest explanation that fits the data.

## Key Concepts

### 1. Variational Free Energy — A Scorecard for Your Model

**Variational free energy (VFE)** is a single number that captures how well your brain's model fits reality. Think of it as a "badness score":

- **High free energy**: Your model is a poor fit — you're confused, surprised, things don't make sense
- **Low free energy**: Your model is a good fit — you understand what's going on, predictions are accurate

Your brain is constantly trying to minimize VFE. It does this in two ways:

1. **Accuracy**: Make your model match the data better (reduce prediction errors)
2. **Simplicity**: Don't make your model unnecessarily complex (prefer simpler explanations)

This balance between accuracy and simplicity is called the **accuracy-complexity trade-off**. The brain doesn't just want to explain everything — it wants to explain things *efficiently*.

> **Real-World Example — Conspiracy Theories**: A conspiracy theory can "explain" almost any evidence — but it does so by adding enormous complexity (secret agents, hidden motives, suppressed information). The brain naturally resists such models because their complexity cost outweighs their accuracy gain. When this trade-off fails — when the brain over-values accuracy at the expense of simplicity — conspiracy thinking emerges.

### 2. Attention as Precision Weighting

**Attention** in Active Inference is precision optimization — adjusting how much weight different sources of information receive:

- When you focus on reading, you increase the precision of visual processing (making text prediction errors louder)
- When you listen for your name at a party, you increase the precision of auditory processing (the **cocktail party effect**)
- When you're driving in fog, you increase the precision of all visual prediction errors (heightened vigilance)

Think of precision as a **volume knob** on each information channel. Attention turns up the volume on what matters and turns it down on what doesn't.

Different neurotransmitters modulate precision:

| Neurotransmitter | Precision Function | Example |
|-----------------|-------------------|---------|
| **Acetylcholine** | Boosts sensory precision | "Pay close attention to what you're sensing" — ACh increases when something needs careful examination |
| **Dopamine** | Boosts prior precision | "Trust your expectations" — DA increases when you're confident in your predictions |
| **Noradrenaline** | Modulates overall alertness | "Something important might happen" — NE increases in uncertain or threatening contexts |

**ADHD** may involve impaired precision weighting — difficulty in boosting relevant signals and suppressing irrelevant ones. The brain's "volume knobs" are poorly calibrated, making it hard to focus on one thing while ignoring distractions.

### 3. The "Dark Room" Problem

If agents minimize surprise, why don't they just sit in a dark room forever? That would be maximally predictable. This is a common objection to Active Inference. There are three answers:

1. **Preferences matter**: A human agent's generative model *expects* variety — food, social interaction, movement. Sitting in a dark room violates these expectations → high prediction error → high free energy
2. **Epistemic value**: Agents are driven to explore and gather information, not just to avoid surprise. A dark room is informationally impoverished
3. **Biological imperative**: Your physiology predicts periodic food, water, and social contact. A dark room would quickly generate massive interoceptive prediction errors (hunger, thirst, loneliness)

> **Key Insight**: The "dark room" objection misunderstands what Active Inference means by "surprise minimization." The model doesn't predict a boring world — it predicts a *rich* world with food, social connection, and meaningful activity. Surprise is minimized by living a life that matches these expectations, not by retreating from experience.

### 4. Cognitive Biases as Model Features

Cognitive biases aren't random flaws — they're consequences of the brain's optimization strategy:

| Bias | Active Inference Explanation | When It Helps | When It Hurts |
|------|----------------------------|--------------|--------------|
| **Confirmation bias** | High prior precision → low weight on disconfirming evidence | Stability, consistency, focus | Resistance to correct updating |
| **Anchoring** | First information sets a strong prior that shapes subsequent inference | Rapid initial estimation | Over-reliance on first data |
| **Overconfidence** | Excessively high precision on one's own model | Quick decisions, commitment | Ignoring valid warnings |
| **Availability bias** | Recent/vivid events increase their precision in memory | Responding to current threats | Overestimating rare dramatic events |
| **Sunk cost fallacy** | Prior commitment increases precision of "stay" policy | Persistence through difficulty | Continuing failing strategies |

### 5. When Cognition Goes Wrong

Disrupted belief optimization can produce cognitive and psychiatric symptoms:

- **Delusions** (e.g., in schizophrenia): Extremely high precision on aberrant prediction errors → bizarre beliefs become "certain." The person isn't being irrational — their precision settings make the delusional belief the best fit for their (distorted) data
- **Anxiety**: Excessively high precision on threat predictions → overestimating danger everywhere. The brain's "threat volume" is stuck on maximum
- **Depression**: Low precision on positive predictions → inability to generate positive expectations about the future. The brain's "hope volume" is turned down
- **OCD**: Extremely high precision on contamination/harm prediction errors → compulsive checking and cleaning to reduce the unresolvable errors

> **Key Insight — Compassionate Understanding**: Notice that in Active Inference, psychiatric symptoms are not "irrational." They are the *rational consequences* of specific precision settings. A person with anxiety is performing perfectly correct inference — given their elevated threat precision. Treatment involves recalibrating these settings, not simply telling the person to "think differently."

### 6. Curiosity and Exploration

Active Inference doesn't just explain why agents avoid surprise — it explains why they *seek information*:

**Epistemic value**: The value of an action that reduces uncertainty about hidden states. When you explore a new city, you're driven by epistemic value — the desire to reduce your uncertainty about what's there.

**Expected free energy**: Combines pragmatic value (getting what you want) and epistemic value (learning about the world). The best policies are ones that both achieve goals AND reduce uncertainty.

This explains why humans are naturally curious — curiosity is the drive to reduce free energy through information gathering.

## Summary

Cognition is the ongoing optimization of the generative model through minimization of variational free energy, balancing accuracy against complexity. Attention is the dynamic adjustment of precision — determining what information gets amplified. Cognitive biases are features of this optimization process, not bugs. Psychiatric symptoms arise from miscalibrated precision settings. Curiosity and exploration reflect the epistemic component of expected free energy — the drive to reduce uncertainty about the world.

## Further Reading

- Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press. (Chapters 4-6)
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Corlett, P. R. et al. (2019). Hallucinations and strong priors. *Trends in Cognitive Sciences*, 23(2), 114-127.
- Schwartenbeck, P. et al. (2019). Computational mechanisms of curiosity and goal-directed exploration. *eLife*, 8, e41703.
