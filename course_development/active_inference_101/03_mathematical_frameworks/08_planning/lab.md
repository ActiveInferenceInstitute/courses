# Lab: Planning and Deep Temporal Models

> **Learning Goal:** Trace policy evaluation, analyze habit formation, and explore hierarchical planning.

## Part 1: Policy Evaluation

**Scenario**: An agent in a 2-state world (left, right) with 2 actions (go_left, go_right) and time horizon T=2. Food is on the right.

Policies:

- π₁ = [go_right, go_right]
- π₂ = [go_left, go_right]
- π₃ = [go_left, go_left]

C = [left: -1, right: +3]

1. For each policy, trace the expected trajectory (what state at each time step)
2. Compute pragmatic value for each policy
3. Rank the policies. Which has lowest EFE?

{fill:textarea}

## Part 2: Habit Formation Dynamics

> **Learning Goal:** See how policy priors P(π) strengthen with experience.

**Exercise**: An agent has 3 policies. Track how P(π) evolves:

| Phase | P(π₁) | P(π₂) | P(π₃) | Behavior Type |
|-------|--------|--------|--------|--------------|
| Day 1 (no experience) | 0.33 | 0.33 | 0.33 | Goal-directed |
| After 10 successes with π₁ | | | | |
| After 100 successes with π₁ | | | | |
| After 1000 successes with π₁ | | | | |

At what point does behavior become "habitual"? How can you tell?

{fill:textarea}

## Part 3: Deep Temporal Model Design

> **Learning Goal:** Build a 2-level hierarchical planning model.

**Scenario**: Planning a trip to a conference.

| Level | Timescale | States | Actions | Goal |
|-------|-----------|--------|---------|------|
| High | Days | {home, airport, conference, hotel} | {travel, attend, rest} | Attend and present |
| Low | Hours | {packing, driving, checking_in, presenting} | {pack, drive, register, speak} | Execute high-level plan |

1. How does the high level set goals for the low level?
2. What happens if the low level encounters an unexpected obstacle (flight cancelled)?
3. How does prediction error propagate between levels?

{fill:textarea}

## Part 4: The Complete Algorithm Trace

> **Learning Goal:** Walk through the full Active Inference algorithm for one time step.

**Setup**: Simple 2-state, 2-action POMDP. Current beliefs: q(s) = [0.3, 0.7]. Observation: o₁.

Trace each step:

1. **Observe**: o₁ received
2. **Infer states**: How does q(s) update? (given A matrix)
3. **Evaluate policies**: Compute G(π) for 2 policies
4. **Select policy**: Apply softmax with γ = 1
5. **Act**: Which action is executed?
6. **Learn**: What parameters are updated?

Show your reasoning at each step (use simple placeholder numbers if needed).

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: Active Inference unifies perception, action, learning, communication, and planning under one mathematical framework. Is this unification a strength (elegant and powerful) or a weakness (too abstract, loses meaningful distinctions)? What does unification gain us as scientists?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Policy evaluation | EFE computation and ranking |
| 2 | Dynamics analysis | Habit formation and policy priors |
| 3 | Hierarchical design | Deep temporal models |
| 4 | Algorithm tracing | Complete Active Inference loop |
| 5 | Theoretical reflection | Value of theoretical unification |
