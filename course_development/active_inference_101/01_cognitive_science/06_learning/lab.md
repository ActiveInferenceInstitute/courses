# Lab: Learning and Model Updating

> **Learning Goal:** Analyze how experience reshapes the generative model.

## Part 1: Tracking Parameter Learning

**Scenario**: You move to a new city. Over 30 days, trace how your generative model updates:

| Day | What You Learn | Which Matrix Updates? | How? |
|-----|---------------|----------------------|------|
| Day 1 | The bus comes at 8:15 AM | B (transitions) | Learning temporal patterns of transportation |
| Day 5 | | | |
| Day 10 | | | |
| Day 20 | | | |
| Day 30 | | | |

Fill in the table with plausible learning events, identifying which aspect of the generative model (A, B, or D) is being updated and how.

{fill:textarea}

## Part 2: Structure Learning in Practice

> **Learning Goal:** Identify cases where simplification (pruning) is adaptive.

**Exercise**: For each of the following, explain what model simplification occurred and why it was beneficial:

1. A medical student learns to distinguish "important" from "irrelevant" symptoms, focusing only on diagnostic information
2. An experienced driver no longer consciously checks mirrors — it becomes automatic
3. A language learner initially translates word-by-word but eventually thinks directly in the new language

{fill:textarea}

## Part 3: The Role of Sleep

> **Learning Goal:** Analyze the relationship between sleep and learning.

**Experiment design**: You want to test whether sleep helps with learning a new musical instrument.

1. Design a simple experiment: What would you measure? What would the control group do?
2. Based on the distinction between slow-wave sleep (parameter consolidation) and REM sleep (structure learning), what specific predictions does Active Inference make about your results?
3. How would you test whether napping is as effective as a full night's sleep?

{fill:textarea}

## Part 4: Skill Acquisition Analysis

> **Learning Goal:** Map the stages of skill learning to prediction error dynamics.

**Exercise**: Choose a skill you've learned (an instrument, a sport, cooking, a language) and describe your journey through three stages:

1. **Beginner stage**: What prediction errors were most prominent? What was effortful?
2. **Intermediate stage**: What became easier? What was still challenging?
3. **Current level**: What is now automatic? Where do you still make prediction errors?

Relate each stage to the concept of prediction error, precision, and model parameters.

{fill:textarea}

## Part 5: Reflection

In 150 words, discuss: Is there such a thing as "too much learning"? When might updating your model too rapidly be harmful? Consider the balance between stability (keeping a good model) and flexibility (adapting to new evidence).

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Temporal analysis | Parameter learning over time |
| 2 | Simplification identification | Structure learning / BMR |
| 3 | Experimental design | Sleep and memory consolidation |
| 4 | Autobiographical analysis | Skill acquisition and prediction error |
| 5 | Critical reflection | Stability-flexibility trade-off |
