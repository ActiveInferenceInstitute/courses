# Lab: Sequential Decisions -- Thinking Multiple Steps Ahead

## Objective

Practice **multi-step decision analysis** using decision trees, expected values across time, and the concept of **expected free energy**. In Active Inference, planning means evaluating policies (sequences of actions) by computing their expected free energy over future time steps.

## Prerequisites

- Completed Math Foundations: Communication module (entropy, information gain)
- Expected value calculations, basic tree diagrams

## Part 1: Decision Trees

**Goal**: Evaluate a two-step decision by computing expected values at each branch.

You have a project due in 2 weeks. At week 1, you choose: Start now or Wait.

If you Start now:
- P(finish early) = 0.7, value = 10
- P(need rush) = 0.3, value = 5

If you Wait:
- At week 2, you can Work hard or Wing it
  - Work hard: P(decent grade) = 0.6, value = 7; P(poor grade) = 0.4, value = 3
  - Wing it: P(decent grade) = 0.2, value = 7; P(poor grade) = 0.8, value = 3

1. Draw the decision tree with all branches labeled.
2. E[Start now] = ?
3. E[Wait, then Work hard] = ?
4. E[Wait, then Wing it] = ?
5. If you Wait, which week-2 action is better? What is E[Wait] using the best week-2 choice?
6. Compare E[Start now] vs. E[Wait]. What is the optimal policy (sequence of decisions)?

{fill:textarea}

## Part 2: Discounting Future Rewards

**Goal**: Understand how agents value near vs. distant outcomes.

A discount factor gamma (0 < gamma < 1) reduces the value of future rewards: V = r_now + gamma * r_next + gamma^2 * r_later.

Policy A: rewards = [2, 2, 2] (steady)
Policy B: rewards = [0, 0, 8] (delayed payoff)

1. With gamma = 1.0 (no discounting): V(A) = ? , V(B) = ?
2. With gamma = 0.5: V(A) = 2 + 0.5(2) + 0.25(2) = ? , V(B) = ?
3. With gamma = 0.9: V(A) = ? , V(B) = ?
4. At what discount factor does Policy A become better than Policy B?
5. In Active Inference, the time horizon of planning is related to how far into the future the agent evaluates expected free energy.

{fill:textarea}

## Part 3: Expected Free Energy (Simplified)

**Goal**: Combine expected reward and expected information gain into a single score.

Recall: Expected Free Energy (G) = Expected Loss + Expected Uncertainty (negative of: pragmatic value + epistemic value).

Two study policies for a test next week:

Policy 1 (Review known material):
- Expected grade: 85/100 (pragmatic value = 85)
- Expected information gain: low (epistemic value = 5)

Policy 2 (Practice new problems):
- Expected grade: 75/100 (pragmatic value = 75)
- Expected information gain: high (epistemic value = 25)

1. Score(Policy 1) = pragmatic + epistemic = ?
2. Score(Policy 2) = pragmatic + epistemic = ?
3. Which policy has lower expected free energy (higher combined score)?
4. Why might an Active Inference agent prefer Policy 2 early in studying but switch to Policy 1 the night before the test?

{fill:textarea}

## Part 4: Policy Trees and Evaluation

**Goal**: Enumerate and compare complete policies.

A robot agent at position A can move to B or C, then from there to D or E.

| Policy | Step 1 | Step 2 | P(success) | Reward if success | Info gained |
|--------|--------|--------|-----------|-------------------|-------------|
| pi_1 | A->B | B->D | 0.8 | 10 | 2 |
| pi_2 | A->B | B->E | 0.5 | 15 | 5 |
| pi_3 | A->C | C->D | 0.6 | 12 | 3 |
| pi_4 | A->C | C->E | 0.3 | 20 | 8 |

1. Compute the expected reward for each policy: E[reward] = P(success) * reward.
2. Compute a combined score for each: Score = E[reward] + info_gained.
3. Rank the policies by expected reward alone. Then rank by combined score. Does the ranking change?
4. In Active Inference, the agent assigns a probability to each policy proportional to exp(-G), where G is the expected free energy. Policies with lower G (better combined score) are more likely to be selected.

{fill:textarea}

## Summary Table

| Math Concept | Symbol | Definition |
|-------------|--------|-----------|
| Decision tree | -- | Branching diagram of sequential choices and outcomes |
| Discount factor | gamma | Reduces the weight of future rewards (0 < gamma < 1) |
| Expected free energy | G | Combines expected loss and expected uncertainty over future steps |
| Policy | pi | A complete sequence of planned actions |
| Policy evaluation | E[G(pi)] | Scoring a policy by its expected free energy across time steps |
