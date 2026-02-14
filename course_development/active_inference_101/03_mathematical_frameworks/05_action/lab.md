# Lab: Expected Free Energy and Policy Selection

> **Learning Goal:** Compute and decompose EFE for simple policies and analyze exploration-exploitation trade-offs.

## Part 1: EFE for Simple Policies

**Scenario**: A foraging agent with two policies:

- π₁: Go to known food source (certain food, no new information)
- π₂: Explore unknown area (uncertain food, high information gain)

Preferences: C = [food: +3, no_food: -1]

1. For π₁: Expected observation = food (100% certain). Compute pragmatic value.
2. For π₁: Information gain = 0 (already knows this area). Compute epistemic value.
3. For π₂: Expected observation = food (50%) or no_food (50%). Compute pragmatic value.
4. For π₂: Information gain = high (will learn about new area). Estimate epistemic value as +2.
5. Compute G(π) for each policy. Which policy is selected?

{fill:textarea}

## Part 2: Exploration-Exploitation Dynamics

> **Learning Goal:** See how the balance shifts with uncertainty.

**Exercise**: The same agent, but now with varying uncertainty about the known food source:

| Certainty about known source | Pragmatic value (π₁) | Epistemic value (π₂) | Which policy wins? |
|-----------------------------|----------------------|---------------------|-------------------|
| 100% certain food there | +3 | +2 | |
| 70% certain food there | +1.8 | +2 | |
| 50% certain food there | +1 | +2 | |

What pattern do you see? How does uncertainty shift the balance?

{fill:textarea}

## Part 3: Policy Precision (γ)

> **Learning Goal:** Understand how γ affects action selection.

**Exercise**: Two policies with G(π₁) = -5 and G(π₂) = -3 (lower is better, so π₁ is preferred).

Compute P(π₁) = softmax(-γ × G(π)) for different γ values:

| γ | P(π₁) | P(π₂) | How decisive? |
|---|-------|-------|--------------|
| 0.1 | | | |
| 1.0 | | | |
| 10.0 | | | |

Hint: softmax(-γ × G) = exp(-γG) / Σexp(-γG)

{fill:textarea}

## Part 4: Flat C Vector — Pure Curiosity

> **Learning Goal:** Analyze what happens when there are no preferences.

**Exercise**: If C = [0, 0, 0] (no preferences), what is the pragmatic value for any policy?

- If pragmatic value is zero, what is the only remaining drive?
- What kind of behavior would this agent exhibit?
- Is this a good model of infant exploration?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: The EFE decomposition shows that a single mathematical quantity (Expected Free Energy) can explain both goal-directed behavior and curiosity. Why is this unification theoretically important? Are there behaviors this framework cannot explain?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | EFE computation | Pragmatic + Epistemic decomposition |
| 2 | Trade-off analysis | Exploration-exploitation dynamics |
| 3 | Softmax computation | Policy precision γ |
| 4 | Edge case analysis | Pure curiosity agents |
| 5 | Theoretical reflection | Unification of goals and curiosity |
