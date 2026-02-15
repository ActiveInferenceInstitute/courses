# Section Lab: Mathematical Foundations of Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md)

## Objective

This integrative lab synthesizes all eight modules from the Mathematical Frameworks course. You will work through derivations, solve problems involving variational inference, and apply the POMDP formalism to concrete scenarios. This is a problem set format -- show your work for all derivations.

## Prerequisites

- Completion of all eight Mathematical Frameworks modules (01_systems through 08_planning)
- Comfort with probability theory, Bayes' theorem, KL divergence, logarithms, and matrix operations
- Access to pen/paper or a LaTeX editor for derivations

---

## Part 1: Generative Models and Probability (Modules 01-02)

**Problem 1a.** A simple generative model has two hidden states (s1, s2) and three observations (o1, o2, o3). The likelihood matrix A and prior D are:

```
A = [[0.8, 0.1],     D = [0.6, 0.4]
     [0.1, 0.7],
     [0.1, 0.2]]
```

Compute the joint distribution P(o, s) = P(o|s) * P(s) for all six (observation, state) combinations. Verify that the joint distribution sums to 1.

{fill:textarea}

**Problem 1b.** Using the joint distribution from 1a, compute the marginal distribution P(o) for each observation. Then compute the posterior P(s|o1) using Bayes' theorem. Show all steps.

{fill:textarea}

---

## Part 2: Variational Free Energy (Modules 03-04)

**Problem 2a.** Given the generative model from Part 1 and observation o1, compute the variational free energy F for two candidate approximate posteriors:

- q_A(s) = [0.9, 0.1]  (confident in s1)
- q_B(s) = [0.5, 0.5]  (uncertain)

Use the formula: F = E_q[ln q(s)] - E_q[ln P(o,s)]

Which approximate posterior has lower free energy? Explain why in terms of accuracy and complexity.

{fill:textarea}

**Problem 2b.** Derive the optimal variational posterior q*(s) that minimizes F for the observation o1. Show that q*(s) is proportional to exp(ln P(o1|s) + ln P(s)), which gives the softmax form used in Active Inference implementations. Compute the numerical values of q*(s) and verify that F(q*) <= F(q_A) and F(q*) <= F(q_B).

{fill:textarea}

---

## Part 3: Inference and Action (Modules 03-05)

**Problem 3a.** Consider a POMDP with a transition matrix B for two actions (a1=stay, a2=move):

```
B[a1] = [[0.9, 0.1],     B[a2] = [[0.2, 0.8],
          [0.1, 0.9]]               [0.8, 0.2]]
```

Starting from prior belief q(s_0) = [0.7, 0.3], compute the predicted belief after one time step for each action: q(s_1|a) = B[a]^T * q(s_0). Which action produces more uncertainty (higher entropy)?

{fill:textarea}

**Problem 3b.** Now add preferences C = [2.0, -1.0] over observations (the agent prefers o1 over o2). Using the A matrix from Part 1, compute the expected free energy G(pi) for a one-step policy using each action. Decompose G into the pragmatic term (expected utility) and the epistemic term (expected information gain). Which policy does the agent prefer, and why?

Show the computation:
- Pragmatic value: E_q[ln P(o|C)] where P(o|C) = softmax(C)
- Epistemic value: E_q[H[P(o|s)]] - H[E_q[P(o|s)]]

{fill:textarea}

---

## Part 4: Learning and Model Structure (Module 06)

**Problem 4a.** The Dirichlet distribution Dir(alpha) is the conjugate prior for categorical distributions. Given a prior concentration parameter alpha = [2, 1] for a binary hidden state, and a sequence of three observations that indicate state s1, s1, s2:

- Write the posterior concentration parameters after each observation using the Dirichlet update rule
- Compute the expected categorical distribution E[Cat(theta)] = alpha_i / sum(alpha) at each step
- Plot or describe how the expected distribution changes with each observation

{fill:textarea}

**Problem 4b.** Bayesian model reduction (BMR) compares a full model M1 with a reduced model M0 (obtained by setting some parameters to their prior values). The log Bayes factor is:

ln BF = ln P(data | M0) - ln P(data | M1)

If ln BF > 0, the reduced model is preferred (Occam's razor). Explain intuitively why a simpler model can have higher evidence even if it fits the data slightly worse. Connect this to the accuracy-complexity trade-off in variational free energy.

{fill:textarea}

---

## Part 5: Communication and Planning (Modules 07-08)

**Problem 5a.** Two agents share a generative model but have different beliefs: Agent A has q_A(s) = [0.8, 0.2] and Agent B has q_B(s) = [0.3, 0.7]. Compute the KL divergence D_KL(q_A || q_B) and D_KL(q_B || q_A). Explain why KL divergence is asymmetric and what this means for communication -- is it "easier" for Agent A to understand Agent B's perspective, or vice versa?

{fill:textarea}

**Problem 5b.** An agent must plan over a two-step horizon with two actions at each step (4 total policies: a1-a1, a1-a2, a2-a1, a2-a2). Using the B matrices from Part 3 and a preference for being in state s1 at the final time step:

- Compute the predicted belief trajectory q(s_1), q(s_2) for each of the 4 policies
- Compute the expected free energy G for each policy over the full horizon
- Select the optimal policy via softmax with precision gamma = 2.0

Show your work and explain how temporal depth affects the agent's behavior compared to a one-step (myopic) agent.

{fill:textarea}

---

## Part 6: Synthesis

**6a.** The variational free energy F and expected free energy G are the two central quantities in Active Inference. Write a concise mathematical comparison: How are they similar in structure? How do they differ in purpose? When does minimizing F lead to different behavior than minimizing G?

{fill:textarea}

---

## Submission Guidelines

- Show all derivations step by step; final answers without work receive no credit
- Express all probabilities to at least 3 decimal places
- Clearly label each step of multi-part computations
- Total expected effort: 3-5 hours

## Recommended Readings

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapters 2-6. MIT Press.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology*, 99, 102447.
- Beal, M. J. (2003). Variational algorithms for approximate Bayesian inference. *PhD Thesis*, University College London.
