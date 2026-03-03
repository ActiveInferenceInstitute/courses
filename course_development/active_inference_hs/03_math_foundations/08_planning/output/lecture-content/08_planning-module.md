# Module 08: Planning — Expected Free Energy and Decision Trees

## Learning Objectives

1. Construct a **decision tree** and calculate the expected value of each branch.
2. Define **Expected Free Energy** as the combination of pragmatic value (reward) and epistemic value (information gain).
3. Apply tree-based reasoning to plan under uncertainty.

## Introduction

Planning is thinking ahead — imagining future possibilities and choosing the path that leads to the best outcome. Mathematically, planning requires evaluating possible futures *before acting*. This module introduces decision trees and connects them to the Active Inference concept of Expected Free Energy.

## Key Concepts

### 1. Decision Trees

A **decision tree** is a branching diagram where each node represents a choice or chance event, and each branch represents a possible outcome with an associated probability and value.

**Example**: You have a free Saturday. Option A: go to the beach (70% chance of sun → great day, 30% chance of rain → miserable). Option B: go to the movies (100% chance of a decent time). Expected value of A = $0.7 \times 10 + 0.3 \times 2 = 7.6$. Expected value of B = $1.0 \times 7 = 7.0$. The beach has higher expected value, but also higher risk.

### 2. Expected Free Energy (EFE)

In Active Inference, planning is formalized as minimizing **Expected Free Energy** (EFE), which has two components:

$$G(\pi) = \underbrace{-\mathbb{E}[\ln P(o \mid C)]}_{\text{Pragmatic Value}} + \underbrace{-\mathbb{E}[\text{information gain}]}_{\text{Epistemic Value}}$$

- **Pragmatic Value**: "Does this plan get me what I want?" (reaching preferred outcomes)
- **Epistemic Value**: "Does this plan help me learn something new?" (reducing uncertainty about hidden states)

An agent with only pragmatic value would always exploit. An agent with only epistemic value would always explore. EFE naturally balances both.

### 3. Multi-Step Planning

Real planning involves chains of decisions. A chess player does not just consider the next move — they simulate sequences of moves and counter-moves, building a tree of possibilities. The deeper the tree, the better the plan, but the more computationally expensive. Active Inference agents plan by mentally simulating policy trajectories and selecting the one with the lowest expected free energy.

## Applications

- **College Applications**: Students can model their college decision as a decision tree with branches for acceptance probability, financial aid, career outcomes, and campus fit.
- **Game Theory**: In a simple negotiation (e.g., splitting $10 with a partner), the ultimatum game shows how planning must incorporate models of *other agents'* decisions.

## Discussion Questions

1. Using the beach vs. movie example, what happens if you are *risk-averse* (you hate bad outcomes more than you love good ones)? How would you change the math?
2. A chess engine plans 20 moves ahead. A human grandmaster plans only 3-5 but picks better positions by "intuition." How does each strategy relate to the exploration-exploitation trade-off?

## Summary

Planning is evaluating future possibilities before acting. Decision trees organize these possibilities. Expected Free Energy combines the desire for good outcomes (pragmatic value) with the drive to learn (epistemic value), providing a unified mathematical account of planning under uncertainty.

## References

- Kahneman, D. (2011). *Thinking, Fast and Slow*. Chapters 25-26.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces. *Journal of Mathematical Psychology*, 99, 102447.
