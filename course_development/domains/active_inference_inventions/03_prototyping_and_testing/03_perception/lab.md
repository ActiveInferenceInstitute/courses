# Lab: Signal Taxonomy and Failure Analysis

## Objective

Practice reading prototype signals by classifying test data into signal types, interpreting failure modes as informative events, and designing instrumentation to extend your perceptual reach. By the end of this lab, you will have a signal collection plan for your invention project.

## Prerequisites

- Familiarity with observation vs. inference, signal types, and failure interpretation from this module's lecture
- Your invention project prototype or prototype specification from Module 01
- A test scenario (real or simulated) where you can generate or imagine prototype data

## Materials

- Notebook or digital document
- Your prototype (or a detailed description if the physical prototype is not available)
- Colored pens or highlighters (for categorizing signals)

---

## Part 1: Observation Before Inference (10 minutes)

**Goal**: Practice separating raw observations from interpretations.

Conduct a brief test of your prototype (or simulate one by closely examining your prototype specification and imagining a test). Record observations in two columns: what you actually observed (raw data) and what you interpreted (inference).

| Raw Observation (What you saw/measured/heard) | Your Inference (What you think it means) | Could another interpretation be valid? |
|----------------------------------------------|----------------------------------------|---------------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |

Reflect: How easy or difficult was it to separate observation from inference? Did you catch yourself interpreting before recording?

{fill:textarea}

---

## Part 2: Signal Classification (15 minutes)

**Goal**: Classify the signals your prototype could generate using the four-category taxonomy.

For your invention project, brainstorm all the signals a test could produce. Then classify each:

**Quantitative Measurements** — things you could measure with a number:

| Measurement | Unit | What it tells you | How precise does it need to be? |
|-------------|------|-------------------|-------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Qualitative Feedback** — things users or experts might say:

| Possible feedback | What it would suggest about your model | Parameter update or structure update? |
|------------------|---------------------------------------|--------------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Behavioral Observations** — things you would see users do:

| Possible behavior | What it would reveal about the user's generative model | How would you record it? |
|------------------|------------------------------------------------------|------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Potential Failure Events** — ways the prototype could fail:

| Failure mode | What it would reveal | Severity (minor/major/critical) |
|-------------|---------------------|-------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |

---

## Part 3: Failure Mode Deep Dive (15 minutes)

**Goal**: Treat failure as the most informative signal by analyzing a specific failure mode in detail.

Select one potential failure mode from Part 2 (or recall an actual failure if you have tested a prototype). Analyze it thoroughly:

**The failure:** {fill:textarea}

**When it occurs:** Under what conditions does this failure happen? What triggers it? {fill:textarea}

**What your generative model predicted:** What did you expect to happen instead? {fill:textarea}

**The prediction error:** What is the specific discrepancy between prediction and observation? {fill:textarea}

**Root cause analysis — 5 Whys:**

| Level | Why? | Answer |
|-------|------|--------|
| 1 | Why did this failure occur? | {fill:textarea} |
| 2 | Why? (deeper) | {fill:textarea} |
| 3 | Why? (deeper) | {fill:textarea} |
| 4 | Why? (deeper) | {fill:textarea} |
| 5 | Why? (root cause) | {fill:textarea} |

**What this failure teaches you:**
- About the prototype's physics/mechanism: {fill:textarea}
- About the user's expectations: {fill:textarea}
- About your generative model's blind spots: {fill:textarea}

**How to update your model based on this failure:**
- Parameter update (change a value): {fill:textarea}
- Structure update (add a variable or relationship): {fill:textarea}
- Do nothing (failure is outside design scope): {fill:textarea}

---

## Part 4: Instrumentation Design (10 minutes)

**Goal**: Identify hidden states you cannot currently perceive and design instrumentation to access them.

What aspects of your prototype's behavior are currently invisible to you? What hidden states would you like to observe but cannot with your current perceptual capabilities?

| Hidden State | Why it matters | Instrument/method to make it observable | Estimated cost/difficulty |
|-------------|---------------|----------------------------------------|--------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

If your prototype is digital, consider: What user behaviors are you not currently logging? What system states are invisible in your current monitoring setup?

{fill:textarea}

If your prototype is physical, consider: What internal stresses, temperatures, vibrations, or movements are currently unobservable? What sensors could you add?

{fill:textarea}

---

## Part 5: Signal Collection Plan (10 minutes)

**Goal**: Create a structured plan for collecting and recording signals during your next test.

**Signal Collection Plan for:** {fill:textarea}

| Signal Category | Specific Signals to Collect | Collection Method | Recording Format | Who Collects |
|----------------|---------------------------|-------------------|-----------------|-------------|
| Quantitative | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Qualitative | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Behavioral | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Failure Events | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Data separation protocol:** How will you ensure raw observations are recorded before interpretations?

{fill:textarea}

---

## Part 6: Cross-Signal Integration (5 minutes)

**Goal**: Practice combining signals from different categories to form a holistic picture of your prototype's performance.

Look across all the signals you identified in Parts 2-5. Do any signals from different categories tell a consistent story? Do any contradict each other?

| Story / Pattern | Supporting Signals (list category and specific signal) | Contradicting Signals | Your Interpretation |
|----------------|------------------------------------------------------|----------------------|-------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

When signals converge (multiple signal types pointing to the same conclusion), your confidence in the interpretation should increase. When signals diverge (quantitative data says one thing, qualitative feedback says another), this is a flag for deeper investigation — the divergence may reveal that your generative model is structured incorrectly.

What is the single most important signal your testing has produced so far? Which category does it belong to?

{fill:textarea}

---

## Discussion and Debrief

1. **Observation discipline**: Was separating observation from inference harder than expected? What does this tell you about how tightly coupled perception and interpretation are?

2. **Signal priorities**: Of the four signal types, which is most important for your invention at its current stage? Why?

3. **Failure reframing**: Did the failure analysis exercise change how you feel about potential failures? Can you honestly say you would welcome a major failure during testing?

4. **Instrumentation gaps**: What is the most important hidden state you identified that you currently cannot observe? How would access to this state change your testing strategy?

5. **Qualitative vs. quantitative**: If you could collect only one type of data in your next test, which would you choose and why? What would you lose by not collecting the other?

{fill:textarea}
