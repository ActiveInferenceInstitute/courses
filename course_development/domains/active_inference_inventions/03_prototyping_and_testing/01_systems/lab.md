# Lab: Defining Your Prototype's Markov Blanket

## Objective

Design the system boundary of a prototype for your invention project by explicitly mapping internal states, sensory surfaces, active surfaces, and external environment. By the end of this lab, you will have a prototype specification that connects every design decision to a testable hypothesis.

## Prerequisites

- Familiarity with Markov blankets, generative models, and fidelity levels from this module's lecture
- Your invention project concept (at any stage of development)
- Drawing materials (paper, whiteboard, or digital drawing tool)

## Materials

- Large sheet of paper or whiteboard
- Three colors of markers or pens (for internal, blanket, and external states)
- Sticky notes or index cards
- Your invention project notes from prior modules

---

## Part 1: Identify Your Prototype's Purpose (10 minutes)

**Goal**: Clarify what specific hypotheses your prototype needs to test, before deciding what to build.

A prototype is a physical generative model built to test specific predictions. Before drawing boundaries, you must know what questions the prototype is meant to answer.

List your invention's top 3 uncertainties — the things you are most unsure about:

| Rank | Uncertainty | What would resolve it? | Current confidence (1-10) |
|------|-----------|----------------------|--------------------------|
| 1 | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| 2 | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| 3 | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Now select the single most critical uncertainty. This is the hypothesis your prototype must test first. Write it as a prediction:

"If my invention works as I expect, then when [input/condition], the prototype should [observable output]."

{fill:textarea}

---

## Part 2: Draw the Markov Blanket (15 minutes)

**Goal**: Map the system boundary of your prototype using the four-state partition.

On your large sheet of paper, draw a large circle or rectangle. This is your prototype's Markov blanket. Now populate the diagram:

**Inside the blanket (Internal States):** List the components, mechanisms, or logic that must be inside the prototype to generate the predictions you identified in Part 1. These are the hidden states — the causal machinery.

{fill:textarea}

**On the blanket — Sensory Surface:** List the inputs your prototype receives from the testing environment. These are the channels through which the external world influences the prototype's internal states.

{fill:textarea}

**On the blanket — Active Surface:** List the outputs your prototype produces. These are the channels through which the prototype's internal states influence the external world.

{fill:textarea}

**Outside the blanket (External States):** List the environmental conditions, user behaviors, and contextual factors that are relevant to your invention but deliberately excluded from this prototype. These are things you are not testing yet.

{fill:textarea}

Now assess your blanket. Answer the following:

- Does every internal state contribute to generating the prediction from Part 1? If not, can you remove it?
- Does the sensory surface include the input variables needed to trigger the prediction?
- Does the active surface include the output variables you need to observe?
- Are there external states that could confound your test results? Should any of them be brought inside the blanket?

{fill:textarea}

---

## Part 3: Choose Your Fidelity Level (15 minutes)

**Goal**: Match prototype fidelity to your current state of knowledge and available resources.

For each internal state in your prototype, rate the appropriate fidelity level and justify your choice:

| Component / Internal State | Fidelity Level (Low/Med/High) | Justification | Materials/Method |
|---------------------------|------------------------------|---------------|-----------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

Now consider: could you reduce fidelity on any component without losing the ability to test your core hypothesis? Remember, lower fidelity means faster iteration and lower cost.

{fill:textarea}

What is the overall fidelity level of your prototype? What is the primary constraint driving this choice (time, money, materials, knowledge)?

{fill:textarea}

---

## Part 4: Modularity Analysis (10 minutes)

**Goal**: Determine whether your prototype can be decomposed into independently testable sub-systems.

Look at your Markov blanket diagram. Can the internal states be grouped into clusters that interact primarily with each other, with limited connections to other clusters? If so, each cluster is a potential sub-system with its own nested Markov blanket.

List potential sub-systems:

| Sub-system | Internal States | Interface to Other Sub-systems | Could be prototyped independently? |
|-----------|----------------|-------------------------------|-----------------------------------|
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |
| {fill:textarea} | {fill:textarea} | {fill:textarea} | {fill:textarea} |

If your prototype can be decomposed, which sub-system should you build and test first? Why? (Consider: which sub-system carries the most uncertainty? Which is cheapest to test? Which is prerequisite for other sub-systems?)

{fill:textarea}

---

## Part 5: Prototype Specification Document (10 minutes)

**Goal**: Compile your analysis into a one-page prototype specification.

Write a brief prototype specification using the template below:

**Prototype Name:** {fill:textarea}

**Version:** (e.g., v0.1, first prototype) {fill:textarea}

**Core Hypothesis Being Tested:** {fill:textarea}

**System Boundary Summary:**
- Internal states (what is built): {fill:textarea}
- Sensory inputs (what it receives): {fill:textarea}
- Active outputs (what it produces): {fill:textarea}
- Excluded variables (what is not tested): {fill:textarea}

**Fidelity Level:** {fill:textarea}

**Estimated Build Time:** {fill:textarea}

**Estimated Build Cost:** {fill:textarea}

**Success Criteria:** What observation would confirm your hypothesis? {fill:textarea}

**Failure Criteria:** What observation would disconfirm your hypothesis? {fill:textarea}

**Next Prototype:** If this prototype succeeds, what is the next blanket expansion? If it fails, what do you change? {fill:textarea}

---

## Discussion and Debrief

Reflect on the following questions. If working in a group, discuss with your peers:

1. **Scope discipline**: Was it difficult to decide what to exclude from your prototype? What was the strongest temptation to include more than necessary?

2. **Fidelity trade-offs**: If you had unlimited budget and time, would you build a higher-fidelity prototype? Would that actually give you better information, or would it just feel more satisfying?

3. **Blanket surprises**: Did the Markov blanket exercise reveal any assumptions you had not previously made explicit? Were there internal states you assumed were necessary that turned out to be irrelevant to your core hypothesis?

4. **Modularity lessons**: If your prototype is modular, does the order in which you test sub-systems matter? How does sub-system testing order relate to the dependencies in your generative model?

5. **Real-world comparison**: Think of a famous invention. How did its earliest prototype compare to its final form? What was inside the blanket of the first prototype, and what was excluded?

{fill:textarea}
