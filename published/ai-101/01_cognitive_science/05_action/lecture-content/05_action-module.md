# Module 05: Action — How Agents Change the World

> **Course**: Active Inference 101 | **Unit**: Cognitive Science | **Audience**: First-semester undergraduates

## Learning Objectives

1. Explain how action in Active Inference works: agents act to fulfill their predictions, not to seek reward.
2. Define **Expected Free Energy (EFE)** as the agent's guide for choosing what to do next.
3. Distinguish **epistemic actions** (exploring to learn) from **pragmatic actions** (exploiting to achieve goals).

## Introduction

Modules 03-04 covered how agents *perceive* and *think*. But perception alone isn't enough — agents must also *act*. In traditional psychology, action is usually explained by reward: you do things because they feel good. Active Inference offers a different perspective: you act to make the world match your predictions. This is a subtle but powerful shift.

## Key Concepts

### 1. Action as Prediction Fulfillment

In Active Inference, **action** is the process of changing the world so that sensory inputs match the agent's predictions:

- Your brain predicts your hand should be on the coffee cup → your muscles move to grasp the cup
- Your body predicts it should be warm → you put on a jacket
- Your social model predicts a greeting → you say "hello"

This is the complement of perception. Perception changes the model to fit the world; action changes the world to fit the model. Together, they form the **perception-action loop**.

### 2. Expected Free Energy (EFE)

How does an agent decide what to do *next*? By evaluating **Expected Free Energy (EFE)** for each possible action (or policy — a sequence of actions):

**EFE = How much surprise will I expect in the future if I take this action?**

The agent selects actions that minimize expected future surprise. EFE has two components:

- **Pragmatic value** (exploitation): "Will this action bring me closer to my preferred outcomes?" — e.g., going to the fridge when hungry
- **Epistemic value** (exploration): "Will this action reduce my uncertainty about the world?" — e.g., looking around a corner to see what's there

### 3. Exploration vs. Exploitation

Active Inference naturally solves the **exploration-exploitation dilemma** — one of the biggest problems in psychology and AI:

- **Exploit**: Choose the action you know will lead to a good outcome (go to your favorite restaurant)
- **Explore**: Choose an action that reduces uncertainty (try a new restaurant to learn if it's better)

In Active Inference, both are captured by a single quantity (EFE). When uncertainty is high, epistemic value dominates → the agent explores. When uncertainty is low, pragmatic value dominates → the agent exploits.

### 4. Motor Control as Inference

Even basic motor control works through Active Inference:

- Your brain generates a **proprioceptive prediction**: "My arm should be in *this* position"
- Your muscles are "reflexes" that minimize the prediction error between predicted and actual position
- Movement happens because the body acts to fulfill the brain's predictions

This explains why spinal reflexes are so fast — they're the body's most basic mechanism for fulfilling predictions about body position.

### 5. When Action Goes Wrong

Disrupted action selection can produce clinical symptoms:

- **Parkinson's disease**: Difficulty initiating movements due to dopamine loss → impaired precision on action predictions
- **Impulsivity**: Acting on the first option without evaluating alternatives → insufficient deliberation over EFE
- **Compulsions (OCD)**: Repetitive actions driven by inability to resolve prediction errors about safety/cleanliness

## Summary

Action in Active Inference is the process of changing the world to match predictions. Agents evaluate Expected Free Energy to select actions, naturally balancing exploration (reducing uncertainty) and exploitation (achieving goals). Motor control itself is a form of inference — the body acts to fulfill the brain's proprioceptive predictions.

## Further Reading

- Friston, K. J. et al. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Pezzulo, G. & Cisek, P. (2016). Navigating the affordance landscape. *Philosophical Transactions of the Royal Society B*, 371(1693).
- Adams, R. A., Shipp, S., & Friston, K. J. (2013). Predictions not commands. *NeuroImage*, 76, 294-305.
