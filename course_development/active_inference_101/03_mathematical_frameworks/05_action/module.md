# Module 05: Action — Expected Free Energy

> **Course**: Active Inference 101 | **Unit**: Mathematical Frameworks | **Audience**: First-semester undergraduates

## Learning Objectives

1. Define **Expected Free Energy (EFE)**, denoted as **$G(\pi)$**, as the ultimate mathematical criterion for policy (action) selection.
2. Formally derive how EFE decomposes strictly into **pragmatic value** (goal-seeking behavior) and **epistemic value** (information-seeking behavior).
3. Walk through a detailed, numeric **Expected Free Energy derivation example** across a discrete state space (e.g., a T-maze).
4. Explain how this elegant mathematical decomposition naturally and automatically resolves the classic reinforcement learning dilemma of **exploration vs. exploitation** without requiring arbitrary tuning parameters.

## Introduction

Modules 01-04 covered how agents infer hidden states from current observations (Perception). But Active Inference is not merely a theory of passive perception—agents must *act* upon the world to survive. How does the mathematics of Free Energy handle future hypothetical action selection?

The answer is **Expected Free Energy**—a quantity the agent evaluates for *each possible policy* (sequence of actions) to decide what to do next. While standard Free Energy ($F$) evaluates the past and present, Expected Free Energy ($G$) evaluates the future.

## Key Concepts

### 1. Expected Free Energy — The Formal Definition

Expected Free Energy $G(\pi)$ evaluates a policy $\pi$ by asking a fundamental question: "If I execute this sequence of actions in the future, how mathematically 'surprised' do I expect to be?"

The base equation for Expected Free Energy evaluated at a future time step $\tau$ under policy $\pi$ is:

**$G(\pi) = E_{\tilde{Q}}[ \log \tilde{Q}(s_\tau) - \log P(o_\tau, s_\tau) ]$**

Where:

- **$\tau$**: A future time step.
- **$\tilde{Q}$**: The posterior predictive distribution—the agent's internal statistical prediction of what states and observations *will* occur if it commits to policy $\pi$.
- **$P(o_\tau, s_\tau)$**: The generative model's joint probability of observations and states.

Just as with standard Free Energy, lower is better. The agent selects the policy that yields the mathematically lowest Expected Free Energy.

### 2. The Key Decomposition — Pragmatic + Epistemic Value

The genius of the Active Inference framework reveals itself when we algebraically decompose the formula for $G(\pi)$ into two distinct, interpretable terms:

**$G(\pi) \approx -E_{\tilde{Q}}[ \log P(o_\tau) ] - E_{\tilde{Q}}[ D_{KL} [ Q(s_\tau|o_\tau, \pi) || Q(s_\tau|\pi) ] ]$**

Or, phrased more simply in information-theoretic terms:
**(Policy Cost) = - (Pragmatic Value) - (Epistemic Value)**

Let's break down these two forces driving all biological behavior:

#### Pragmatic Value (Goal-Seeking / Exploitation)

**Pragmatic value** captures: *"Will this policy result in observations that I prefer?"*
Mathematically: $E_{\tilde{Q}}[ \log P(o_\tau) ]$
Here, $P(o_\tau)$ represents the agent's absolute prior preferences (often stored in the **C-matrix** in discrete state-space models). If the expected observations under policy $\pi$ strongly match the agent's preferred target observations (e.g., a thermostat expects to observe 72 degrees; an animal expects to observe food), pragmatic value is massively positive, lowering the overall $G$. This term mathematically drives **exploitative**, reward-seeking behavior.

#### Epistemic Value (Information-Seeking / Exploration)

**Epistemic value** captures: *"Will this policy resolve my uncertainty about the world?"*
Mathematically, it is the expected Information Gain (or expected reduction in entropy/uncertainty): $E_{\tilde{Q}}[ D_{KL} ]$.
This measures the mutual information between the hidden states $s_\tau$ and the expected observations $o_\tau$. High epistemic value means the policy will generate an observation that wildly updates the agent's prior beliefs into a highly precise posterior. Looking under a rock you've never looked under has high epistemic value; looking under a rock you just checked has zero epistemic value. This term drives **exploratory**, curiosity-driven behavior.

### 3. A Worked Derivation Example: The T-Maze

Imagine a mouse in a T-maze. Food is randomly placed in either the Left Arm or Right Arm. The mouse is at the bottom (Start). It can go directly to an arm, but it is currently highly uncertain (50/50 prior) about where the food is.

There is a Cue Light at the Start position indicating the food's location, but the mouse must spend a time-step orienting toward the Cue Light to read it.

Let's evaluate two policies:

- **Policy 1: Guess Left Arm Immediately.**
- **Policy 2: Look at Cue Light, then go to the indicated Arm.**

**Evaluating Policy 1 (Guess Left)**:

- *Pragmatic Value*: 0.5 (A 50% chance of observing the preferred "Food" state, 50% chance of observing "Empty").
- *Epistemic Value*: ~0. Going left provides no new information about the maze structure beforehand; if it's wrong, it just fails.
- *Total EFE ($G_1$)*: Moderate/High (Bad).

**Evaluating Policy 2 (Look at Cue)**:

- *Pragmatic Value for Step 1*: 0 (Looking at a light provides zero food reward; it does not satisfy the C-matrix preference).
- *Epistemic Value for Step 1*: VERY HIGH. The observation of the light perfectly resolves the uncertainty of the hidden state (Food Location). The KL divergence between the prior (50/50) and the expected posterior (100/0) is maximum.
- *Total EFE ($G_2$)*: Low (Good).

Because the Epistemic Value of looking at the cue overrides the immediate lack of Pragmatic Value, $G_2$ evaluates lower than $G_1$. The mouse mathematically chooses to explore (look at the cue) before it exploits.

### 4. The Emergent Exploration-Exploitation Balance

In standard Reinforcement Learning, engineers must artificially program an "epsilon-greedy" parameter (e.g., "explore 10% of the time, exploit 90% of the time") to prevent an AI from getting stuck in local minima.

In Active Inference, **this balance is solved analytically without arbitrary tuning parameters**.
Because $G(\pi)$ is the simple sum of Pragmatic and Epistemic value:

- **When uncertainty is high**: The epistemic term mathematically dominates the equation. The agent behaves like a scientist, taking actions solely to reduce uncertainty.
- **When uncertainty is resolved (Epistemic Value approaches 0)**: The pragmatic term mathematically takes over. The agent behaves like a classical reinforcement learner, ruthlessly executing actions that acquire its preferred states.

### 5. Policy Selection via Softmax

Once $G(\pi)$ is calculated for every possible sequence of actions, the agent selects a policy probabilistically using a softmax function:

**$P(\pi) = \sigma(-\gamma \times G(\pi))$**

Where:

- **$\sigma$**: The mathematical softmax function, which converts the raw, negative EFE scores into a clean probability distribution summing to 1.
- **$\gamma$ (Gamma)**: The precision parameter for policy selection. A high $\gamma$ means the agent is highly decisive, almost certainly picking the absolute lowest-EFE policy. A low $\gamma$ means the agent is behaving randomly or sluggishly, flattening the probability distribution.

## Summary

Expected Free Energy $G(\pi)$ is the fundamental engine of decision-making in Active Inference. By rigorously decomposing future action selection into the sum of Pragmatic Value (goal-seeking) and Epistemic Value (information estimation), the framework elegantly unifies classical economic utility with information theory. The agent naturally transitions from curious exploration to ruthless exploitation as its uncertainty about the world evaporates, guided by the softmax transformation and policy precision ($\gamma$).

## Further Reading

- Friston, K. J. et al. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187-214.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press. (Highly recommend Chapter 6 on continuous and discrete time action).
- Sajid, N. et al. (2021). Active inference: Demystified and compared. *Neural Computation*, 33(3), 674-712.
