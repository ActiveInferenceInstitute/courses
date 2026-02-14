# Lab: Building a POMDP

> **Learning Goal:** Construct and analyze a simple POMDP from scratch.

## Part 1: Constructing the A Matrix

**Scenario**: A foraging agent in a 2-location world. States: {food_left, food_right}. Observations: {see_food, see_nothing}.

1. Design an A matrix where the agent can partially observe the food location (occasionally gets it wrong).
2. Verify each column sums to 1.
3. What would the A matrix look like if observation were perfect? Noisy?

| | food_left | food_right |
|---|-----------|------------|
| see_food | | |
| see_nothing | | |


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Constructing the B Matrix

> **Learning Goal:** Build transition dynamics with agency.

**Same scenario**: Actions: {go_left, go_right, stay}.

Design the B matrix for each action. The agent is currently at the right location.

For action "go_left":

| | food_left | food_right |
|---|-----------|------------|
| food_left | | |
| food_right | | |

Do the same for "go_right" and "stay."


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Setting Preferences (C Vector)

> **Learning Goal:** Translate goals into the C vector.

**Exercise**: Define C vectors for different types of agents:

1. A hungry agent that wants food: C = ?
2. A scared agent that avoids everything: C = ?
3. A curious agent that wants novelty (any observation is fine): C = ?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Running the Perception-Action Loop

> **Learning Goal:** Manually trace one cycle of belief updating and action selection.

**Setup**:

- D = [0.5, 0.5] (no initial preference for food location)
- A, B, C as you defined above
- Agent observes: see_food

1. Update beliefs: q(s) ∝ A(see_food, :) × D
2. Normalize q(s) so it sums to 1
3. Based on updated beliefs, which action should the agent take?
4. How would your answer change if the observation were "see_nothing"?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Reflection

In 150 words, reflect: The POMDP framework uses just 5 components (A, B, C, D, π) to describe an agent's entire decision-making system. What is gained by this simplicity? What might be lost?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Matrix construction | A matrix (observation model) |
| 2 | Matrix construction | B matrix (transition model) |
| 3 | Preference encoding | C vector (preferences/values) |
| 4 | Loop tracing | Perception-action cycle |
| 5 | Framework reflection | Strengths and limits of POMDPs |
