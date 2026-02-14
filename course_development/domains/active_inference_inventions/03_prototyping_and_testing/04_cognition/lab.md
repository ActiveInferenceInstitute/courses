# Lab: Bayesian Reasoning About Your Test Results

## Objective

Practice structured reasoning about prototype test data by applying Bayesian updating, signal-noise discrimination, and bias mitigation techniques to your own invention project. By the end of this lab, you will have a reasoning protocol that enforces disciplined inference.

## Prerequisites

- Familiarity with Bayesian updating, signal vs. noise, and cognitive biases from this module's lecture
- Test data from your invention project (real or hypothetical)
- Your prototype specification from Module 01 and signal collection plan from Module 03

## Materials

- Test results (quantitative data, qualitative feedback, behavioral observations, and/or failure records)
- Notebook or digital document
- Calculator (for simple probability estimates)

---

## Part 1: Map Your Prior Beliefs (10 minutes)

**Goal**: Make your current beliefs about your invention explicit and quantifiable before examining test data.

Before looking at any test results, write down your beliefs about your prototype's performance. Be specific and honest.

| Performance Variable | Your Prediction (specific value or range) | Your Confidence (1-10) | What evidence formed this belief? |
|---------------------|------------------------------------------|----------------------|--------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Now define your falsification criteria — what results would make you change your design?

"I will consider my current approach failed if: ___"

{fill:textarea}

"I will consider my current approach validated if: ___"

{fill:textarea}

---

## Part 2: Evaluate Evidence Quality (10 minutes)

**Goal**: Assess the precision and reliability of your test data before using it to update beliefs.

Take your test results (real or hypothetical) and evaluate each piece of evidence:

| Evidence | Repeatable? (same result if tested again?) | Consistent? (other data points agree?) | Magnitude (large or small effect?) | Precision Rating (Low/Med/High) |
|----------|-------------------------------------------|---------------------------------------|----------------------------------|-------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Based on this assessment, which evidence should carry the most weight in your reasoning? Which should carry the least?

{fill:textarea}

---

## Part 3: Bayesian Updating Exercise (15 minutes)

**Goal**: Practice proportional belief updating using your actual test data.

Select the single most important test result from your data. Walk through the Bayesian update:

**Prior belief**: Before testing, what did you believe? (State specifically.) {fill:textarea}

**Evidence**: What did you observe? (State the raw data.) {fill:textarea}

**Evidence precision**: How trustworthy is this evidence? (Low/Medium/High, with justification.) {fill:textarea}

**Posterior belief**: After considering this evidence, what do you now believe? {fill:textarea}

**Update magnitude**: How much did your belief change? Was the change proportional to the evidence strength? {fill:textarea}

Now repeat for a second test result:

**Prior belief** (now using the posterior from above as your new prior): {fill:textarea}

**Evidence**: {fill:textarea}

**Evidence precision**: {fill:textarea}

**Posterior belief**: {fill:textarea}

**Cumulative update**: After two pieces of evidence, how far have your beliefs moved from your original prior? {fill:textarea}

---

## Part 4: Analysis of Competing Hypotheses (15 minutes)

**Goal**: Practice evaluating multiple explanations for your test results, rather than defaulting to the most comfortable one.

Take a key test result (especially one that was surprising or ambiguous) and generate multiple competing hypotheses:

**Test result being analyzed**: {fill:textarea}

| Hypothesis | Consistent with this result? | Consistent with other evidence? | Would you have predicted this result from this hypothesis? | Plausibility (1-5) |
|-----------|----------------------------|-------------------------------|----------------------------------------------------------|-------------------|
| H1: {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| H2: {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| H3: {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| H4: {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Which hypothesis best explains the evidence? Is it the one you initially preferred?

{fill:textarea}

What additional test would help discriminate between the top two hypotheses?

{fill:textarea}

---

## Part 5: Bias Audit (10 minutes)

**Goal**: Check your reasoning for common cognitive biases.

Review your reasoning from Parts 1-4 and honestly assess:

| Bias | Evidence of this bias in your reasoning? | How it might be distorting your conclusions | Mitigation step |
|------|----------------------------------------|-------------------------------------------|----------------|
| Confirmation bias (interpreting ambiguous data as supportive) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Anchoring (over-weighting early results) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Motivated reasoning (wanting a specific conclusion) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Base rate neglect (ignoring background rates of failure) | {fill:textarea} | {fill:textarea} | {fill:textarea} |

What is the strongest piece of evidence against your preferred interpretation of the test results?

{fill:textarea}

If you had to argue that your prototype should be abandoned based on the test data, what would your argument be?

{fill:textarea}

---

## Part 6: Build Your Reasoning Protocol (5 minutes)

**Goal**: Design a personal reasoning protocol you will use for all future test data interpretation.

Based on what you learned in this lab, create a checklist you will follow every time you evaluate test results:

My Reasoning Protocol:

Step 1: Before looking at data, write down my predictions and confidence levels: {fill:textarea}

Step 2: Assess evidence quality (repeatability, consistency, magnitude): {fill:textarea}

Step 3: Perform Bayesian update with proportional change: {fill:textarea}

Step 4: Generate at least two alternative explanations for the results: {fill:textarea}

Step 5: Check for biases (confirmation, anchoring, motivated reasoning, base rate neglect): {fill:textarea}

Step 6: Compare my interpretation with at least one other person: {fill:textarea}

Step 7: Document the reasoning process in my lab notebook: {fill:textarea}

Will you actually follow this protocol? What is the most likely reason you might skip steps, and how will you guard against that?

{fill:textarea}

---

## Discussion and Debrief

1. **Prior transparency**: Was it difficult to quantify your beliefs before looking at test data? Why is this exercise valuable even though the numbers are rough estimates?

2. **Proportional updating**: Did you find yourself wanting to either ignore the data or overreact to it? How do you calibrate proportional updates?

3. **Competing hypotheses**: Did generating alternative explanations change your interpretation of the test results? Was there a hypothesis you had not previously considered?

4. **Bias discovery**: Were you surprised to find evidence of any specific bias in your reasoning? Which bias do you think is most dangerous for your project?

5. **Devil's advocate**: Was it emotionally difficult to argue for abandoning your prototype? What does your emotional resistance tell you about the strength of your priors?

{fill:textarea}
