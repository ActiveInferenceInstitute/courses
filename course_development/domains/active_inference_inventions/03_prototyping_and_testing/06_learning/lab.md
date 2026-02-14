# Lab: Post-Mortem Analysis and Failure Cataloging

## Objective

Conduct a structured post-mortem analysis of a testing outcome from your invention project and begin building a failure mode catalog. By the end of this lab, you will have extracted transferable lessons from both failures and successes, and created a learning system that grows across projects.

## Prerequisites

- Familiarity with parameter vs. structure learning, post-mortem methods, and failure cataloging from this module's lecture
- At least one testing outcome (positive, negative, or ambiguous) from your invention project
- If you have not yet tested a prototype, you may use a hypothetical scenario based on your design

## Materials

- Test records from prior modules (signal collection plan, reasoning worksheets)
- Notebook or digital document for the failure catalog
- Index cards or sticky notes for the abstraction ladder exercise

---

## Part 1: Structured Post-Mortem (20 minutes)

**Goal**: Analyze a specific testing outcome using the five-step post-mortem framework.

Select a testing outcome from your invention project. It can be a failure, a success, or an ambiguous result.

**Step 1: Establish the facts** (what actually happened, without interpretation)

{fill:textarea}

**Step 2: Compare to predictions** (what did your generative model predict?)

| Aspect | Predicted Outcome | Actual Outcome | Prediction Error (difference) |
|--------|------------------|----------------|------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Step 3: Attribute causes** (for each prediction error, what caused it?)

| Prediction Error | Possible Cause 1 | Possible Cause 2 | Most Likely Cause | Parameter error or Structure error? |
|-----------------|------------------|------------------|-------------------|-------------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

**Step 4: Extract lessons** (what specific updates should be made to your generative model?)

Parameter updates (change values, keep model structure):
{fill:textarea}

Structure updates (add variables, change relationships, remove incorrect assumptions):
{fill:textarea}

**Step 5: Assess transferability** (are these lessons specific to this prototype or applicable to future projects?)

{fill:textarea}

---

## Part 2: Failure Mode Catalog (15 minutes)

**Goal**: Create a structured failure catalog entry for each failure observed in your testing.

If your test outcome was a success, imagine three plausible failure modes that could have occurred and catalog those instead.

| Field | Entry 1 | Entry 2 | Entry 3 |
|-------|---------|---------|---------|
| Date / Prototype Version | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Failure Description (what happened) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Failure Mode (how it failed) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Root Cause (why it failed) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Severity (minor/major/critical) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Detectability (easy/moderate/hard to detect) | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Lesson Learned | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| Countermeasure (how to prevent recurrence) | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Do you see any patterns across your failure entries? Are there common failure modes, common root causes, or common lessons?

{fill:textarea}

---

## Part 3: Success Analysis (10 minutes)

**Goal**: Apply the same rigor to understanding why something worked.

Select a positive test outcome (or the best-performing aspect of an ambiguous outcome):

**What went right?** {fill:textarea}

**Did the generative model predict this success? Was the prediction correct for the right reasons?**

{fill:textarea}

**What factors contributed to the success?**

| Factor | Was this factor part of your model? | Could this factor have been luck or uncontrolled variables? |
|--------|-----------------------------------|-----------------------------------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} |

**What aspects of the success does your model NOT explain?**

{fill:textarea}

**What would happen if you tried to replicate this success in different conditions? Would the same factors still apply?**

{fill:textarea}

---

## Part 4: The Abstraction Ladder (10 minutes)

**Goal**: Practice abstracting specific lessons into transferable principles.

Take the most important lesson from your post-mortem. Climb the abstraction ladder from the specific observation to the meta-principle:

| Level | Abstraction | Your Lesson |
|-------|------------|-------------|
| 1. Specific observation | What you saw | {fill:textarea} |
| 2. Proximate cause | Why it happened in this instance | {fill:textarea} |
| 3. General mechanism | The underlying principle at work | {fill:textarea} |
| 4. Design principle | A rule of thumb for future designs | {fill:textarea} |
| 5. Meta-principle | A general principle about inventing | {fill:textarea} |

Which level of abstraction is most useful for your next prototype iteration? Which is most useful for future projects in different domains?

{fill:textarea}

---

## Part 5: Design Your Learning System (10 minutes)

**Goal**: Create a sustainable system for capturing and applying lessons from every testing cycle.

Design a personal learning system that you will use throughout your invention project:

**Where will you record lessons?** (Format, tool, location)
{fill:textarea}

**When will you conduct post-mortems?** (After every test? After each prototype version? Weekly?)
{fill:textarea}

**How will you ensure you review past lessons before starting new work?** (Checklist? Review ritual? Team discussion?)
{fill:textarea}

**How will you organize lessons for cross-project transfer?** (Categories? Tags? Abstraction levels?)
{fill:textarea}

**Commitment statement:** "Before starting each new prototype iteration, I will..."
{fill:textarea}

---

## Discussion and Debrief

1. **Parameter vs. structure**: In your post-mortem, did you find more parameter errors or structure errors? Which type is harder to identify?

2. **Success blind spots**: Was it harder to analyze success or failure? What did the success analysis reveal that you would have missed without structured analysis?

3. **Pattern recognition**: Do you see any patterns in your failure catalog? Are you consistently weak in the same areas?

4. **Abstraction challenge**: Was it difficult to climb the abstraction ladder? At which level did the lesson stop being useful and start being too vague?

5. **Learning commitment**: Do you believe you will actually use the learning system you designed? What is the biggest obstacle to consistent learning discipline?

{fill:textarea}
