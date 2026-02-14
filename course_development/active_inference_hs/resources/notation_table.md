# Notation Table

> **Quick Navigation**: [Resources Home](./README.md) | [Glossary](./glossary.md) | [Curriculum Home](../README.md)

This table defines all mathematical symbols used across the Active Inference for High School curriculum. Each symbol includes a **plain English** explanation first, then its formal meaning.

---

## Probability Basics

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| `P(A)` | How likely is event A? | Probability of A, a number between 0 and 1 | Math M1 |
| `P(A\|B)` | How likely is A, knowing B happened? | Conditional probability of A given B | Math M3 |
| `P(A,B)` | How likely are A and B together? | Joint probability of A and B | Math M3 |
| `P(A\|B) = P(B\|A)·P(A)/P(B)` | How to update your beliefs with evidence | Bayes' theorem | Math M4 |

---

## Active Inference Core

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| `F` | Overall prediction error | Variational Free Energy — measures how wrong your mental model is | Math M3 |
| `G` | Expected future prediction error | Expected Free Energy — guides action selection | Math M5 |
| `π` | A plan or strategy | Policy — a sequence of actions (a₁, a₂, ..., aₜ) | Math M5 |
| `q(s)` | What you currently believe about the world | Approximate posterior — your brain's best guess | Math M3 |
| `p(o,s)` | Your brain's model of how the world works | Generative model — joint distribution over observations and states | Math M3 |
| `−ln p(o)` | How surprising something is | Surprisal — negative log probability of an observation | Math M3 |

---

## Matrices (Computer Science Notation)

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| **A** | How observations connect to hidden states | Likelihood matrix: `P(observation \| state)` | Tech M3 |
| **B** | How states change over time | Transition matrix: `P(state_next \| state_now, action)` | Tech M3 |
| **C** | What outcomes the agent prefers | Preference vector: log-probabilities of preferred observations | Tech M4 |
| **D** | What the agent believes at the start | Prior distribution over initial states | Tech M4 |
| **E** | The agent's habits | Habit vector: prior over policies | Tech M5 |

---

## Markov Blanket Partition

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| `η` (eta) | Everything outside the system | External states | Life M1 |
| `μ` (mu) | Everything inside the system | Internal states | Life M1 |
| `σ` (sigma) | How the outside affects the boundary | Sensory states — influenced by external states | Life M1 |
| `α` (alpha) | How the system affects the outside | Active states — influence external states | Life M1 |
| `b = (σ, α)` | The boundary itself | Blanket states — the union of sensory and active states | Life M1 |

---

## Information Theory

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| `H(X)` | How uncertain or random X is | Entropy — average surprisal | Math M7 |
| `D_KL(q \|\| p)` | How different two probability distributions are | KL Divergence — measures distance between q and p | Math M3 |
| `I(X;Y)` | How much X tells you about Y | Mutual Information | Math M7 |

---

## Prediction Error Decomposition

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| `F = E_q[−ln p(o,s)] − H[q(s)]` | Prediction error = model mismatch + uncertainty | VFE decomposition: energy minus entropy | Math M3 |
| `G = Risk + Ambiguity` | Future error = bad outcomes + unclear signals | EFE decomposition | Math M5 |
| Risk | Likelihood of outcomes you don't want | `D_KL[q(o\|π) \|\| p(o)]` — divergence from preferred outcomes | Math M5 |
| Ambiguity | Unclear or noisy signals | `E_q[H[p(o\|s)]]` — expected observation entropy | Math M5 |
| Epistemic Value | Value of learning something new | Information gain — expected reduction in uncertainty | Math M5 |
| Pragmatic Value | Value of getting what you want | Expected utility — closeness to preferred outcomes | Math M5 |

---

## Conventions

1. **Bold capital letters** (**A**, **B**, **C**, **D**, **E**) denote matrices or vectors in the generative model.
2. **Greek letters** (η, μ, σ, α) denote Markov Blanket partition states.
3. **Lowercase** `p` is the generative model (true distribution); `q` is the approximate posterior (the brain's guess).
4. **Subscripts** indicate time: `s_t` is the state at time t.
5. **Superscripts** indicate the index: `s^(i)` is the i-th state.
6. All notation is consistent with Parr, Pezzulo & Friston (2022) *Active Inference* (MIT Press).
