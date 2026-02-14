# Lab: Designing Your Testing Agent Protocol

## Objective

Design a multi-agent testing strategy for your invention project that deliberately incorporates diverse perspectives, manages creator bias, and includes adversarial testing. By the end of this lab, you will have a testing protocol that specifies who tests, what they look for, and how their observations are collected and interpreted.

## Prerequisites

- Familiarity with the creator-evaluator transition, distributed sensing, and adversarial testing from this module's lecture
- Your invention project and prototype specification from Module 01
- At least one other person available for a brief testing exercise (or the ability to simulate external perspectives)

## Materials

- Your prototype (physical, digital, or conceptual)
- Notebook or digital document for recording observations
- Timer

---

## Part 1: Self-Assessment — Your Agent Configuration (10 minutes)

**Goal**: Map your own generative model as a testing agent, identifying your priors, attention patterns, and potential blind spots.

Answer honestly — the value of this exercise depends on self-awareness:

**Your priors about your invention:**

What do you believe most strongly about your invention? What are you most confident will work?

{fill:textarea}

What are you least sure about? Where is your uncertainty highest?

{fill:textarea}

**Your attention profile:**

When you look at your prototype, what do you naturally focus on first? (Mechanism? Aesthetics? User interface? Materials? Cost?)

{fill:textarea}

What aspects of the prototype do you tend to overlook or check last?

{fill:textarea}

**Your bias risk assessment:**

| Bias | Risk Level (Low/Med/High) | Why? |
|------|--------------------------|------|
| Confirmation bias (interpreting ambiguous results as positive) | {fill:textarea} | {fill:textarea} |
| Sunk cost bias (reluctance to abandon failed approaches) | {fill:textarea} | {fill:textarea} |
| Anchoring bias (over-weighting early test results) | {fill:textarea} | {fill:textarea} |
| Expertise blindness (assuming users share your knowledge) | {fill:textarea} | {fill:textarea} |

---

## Part 2: Design Your Testing Agent Team (15 minutes)

**Goal**: Identify the different types of testing agents your invention needs and what each brings to the evaluation.

For each agent type, specify who they are, what generative model they bring, and what prediction errors they are likely to generate:

**Agent Type 1: The Naive User**
- Who: Someone with no knowledge of your invention's domain or mechanism
- What they test: Basic usability, first impressions, intuitive understanding
- Who specifically could you recruit for this role? {fill:textarea}
- What instructions would you give them? {fill:textarea}

**Agent Type 2: The Domain Expert**
- Who: Someone with deep expertise in the problem your invention solves
- What they test: Technical viability, competitive comparison, unmet needs
- Who specifically could you recruit for this role? {fill:textarea}
- What questions would you ask them? {fill:textarea}

**Agent Type 3: The Adversarial Tester**
- Who: Someone given explicit permission and incentive to break the prototype
- What they test: Failure modes, edge cases, worst-case scenarios
- Who specifically could you recruit for this role? {fill:textarea}
- What constraints would you set (to prevent actual danger while allowing stress testing)? {fill:textarea}

**Agent Type 4: The Target Customer**
- Who: Someone who matches the profile of your intended user
- What they test: Value proposition, willingness to use/buy, integration with existing habits
- Who specifically could you recruit for this role? {fill:textarea}
- What scenario would you set up for their test? {fill:textarea}

---

## Part 3: Run a Mini Test Session (20 minutes)

**Goal**: Conduct a brief test of your prototype with at least one external agent, practicing the skills of observation without intervention.

If you have access to another person, ask them to interact with your prototype (or a description/sketch of it) for 5-10 minutes. If working alone, simulate an external agent by deliberately adopting a different perspective (e.g., imagine you are a complete novice encountering this for the first time).

**Rules for the test:**
1. Give the tester the prototype with minimal explanation
2. Do NOT explain how it works unless they are stuck and frustrated
3. Observe silently — record what they do, not what you expected them to do
4. Note every moment of confusion, surprise, or unexpected behavior

**Observation Record:**

| Time | What the tester did | What you expected them to do | Prediction error (difference) |
|------|-------------------|----------------------------|------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Post-test debrief (ask the tester):**

What did you think this was supposed to do? {fill:textarea}

What was confusing or surprising? {fill:textarea}

What would you change? {fill:textarea}

---

## Part 4: Analyze Agent Divergence (10 minutes)

**Goal**: Compare your own observations of the prototype with the external agent's observations and analyze the differences.

Review the prediction errors from Part 3. For each significant discrepancy between your expectations and the tester's behavior:

| Prediction Error | Was this a surprise to you? | What does it reveal about your generative model? | What should you update? |
|-----------------|---------------------------|------------------------------------------------|----------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Now categorize your updates:

- **Model-confirming observations** (tester did what you expected): {fill:textarea}
- **Parameter-updating observations** (tester struggled with specific details, but the basic approach works): {fill:textarea}
- **Structure-updating observations** (tester's behavior suggests a fundamental assumption is wrong): {fill:textarea}

---

## Part 5: Write Your Testing Protocol (10 minutes)

**Goal**: Compile your analysis into a formal testing protocol document.

**Testing Protocol for:** {fill:textarea}

**Pre-registration statement** (commit to these before testing):
- Hypothesis being tested: {fill:textarea}
- Specific success criteria (quantitative if possible): {fill:textarea}
- Specific failure criteria: {fill:textarea}
- What result would make you change your design? {fill:textarea}

**Agent deployment plan:**

| Phase | Agent Type | Number of Testers | What They Test | How You Collect Data |
|-------|-----------|-------------------|---------------|---------------------|
| 1 | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| 2 | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| 3 | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Bias mitigation measures:**
{fill:textarea}

---

## Discussion and Debrief

1. **The hardest part**: What was most difficult about observing someone else interact with your invention without intervening? What does this reveal about your priors?

2. **Surprise value**: What was the single most surprising observation from your test session? Was it more valuable than the confirming observations?

3. **Agent diversity**: If you could add one more type of testing agent to your protocol, who would it be and why?

4. **Pre-registration challenge**: Was it difficult to commit to specific failure criteria? Why might inventors resist pre-registering what would count as failure?

5. **Adversarial comfort**: How comfortable are you with the idea of someone deliberately trying to break your invention? What does your comfort level reveal about your relationship to your generative model?

{fill:textarea}
