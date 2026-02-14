# Lab: Multi-Agent Inference and Communication

> **Learning Goal:** Model communication as coupled inference and analyze synchrony.

## Part 1: Coupled Generative Models

**Exercise**: Two agents observe the same weather but from different locations.

- Agent A is indoors (observes: room temperature changes)
- Agent B is outdoors (observes: rain, sunshine)
- Hidden state s: actual weather {sunny, rainy, cloudy}

1. Write Agent A's likelihood P_A(o | s) — how weather affects indoor temperature
2. Write Agent B's likelihood P_B(o | s) — how weather is directly observed
3. If they share their observations, how does this improve each agent's inference?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Measuring Generalized Synchrony

> **Learning Goal:** Understand when agents "converge" on shared beliefs.

**Scenario**: Agent A and Agent B discuss whether a movie is good.

- Before conversation: A thinks 70% good, B thinks 30% good
- After sharing reasons: A thinks 60% good, B thinks 55% good

1. Did generalized synchrony increase? How can you tell?
2. What would perfect synchrony look like? (both posteriors identical)
3. What would zero synchrony look like? (beliefs unchanged by interaction)
4. Is synchrony always good? Give an example where maintaining different beliefs is valuable.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Language as Model Compression

> **Learning Goal:** Analyze how sentences compress generative models.

**Exercise**: For each sentence, identify what generative model information is being transmitted:

| Sentence | Hidden states | Transition (B) | Observation (A) | Preferences (C) |
|---------|--------------|----------------|-----------------|-----------------|
| "Watch out for the car!" | | | | |
| "If it rains tomorrow, bring an umbrella" | | | | |
| "The restaurant on Main St. has great pasta" | | | | |


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Shared Priors and Social Norms

> **Learning Goal:** Model cultural norms as shared prior distributions.

**Exercise**: For each cultural norm, express it as a shared prior and explain how it reduces collective prediction error:

1. "Drive on the right side of the road" → Shared D = ?
2. "Be quiet in libraries" → Shared C = ?
3. "Shake hands when meeting" → Shared B = ?

What happens when someone violates the norm? (In terms of prediction error)


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 150 words, reflect: If communication is coupled inference and cultural norms are shared priors, does this mean all disagreement is "failing to minimize joint free energy"? Or is disagreement sometimes adaptive?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Multi-agent modeling | Coupled generative models |
| 2 | Synchrony analysis | Convergence of beliefs |
| 3 | Linguistic analysis | Language as model compression |
| 4 | Norm formalization | Cultural priors |
| 5 | Critical reflection | Disagreement and free energy |
