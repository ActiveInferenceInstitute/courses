# Practice Quiz: Cognition (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** A POMDP adds what to an HMM?
A) More observations
B) Agency — the ability to choose actions that change state transitions
C) Faster computation
D) Fewer states

**2.** The A matrix in Active Inference represents:
A) P(s_t | s_{t-1}) — how states evolve
B) P(o | s) — how hidden states generate observations
C) The agent's preferences
D) The agent's initial beliefs

**3.** The C vector encodes:
A) Transition dynamics
B) Which observations the agent prefers or avoids
C) The number of hidden states
D) The probability of each action

**4.** In the belief update equation q(s_t) ∝ A(o_t, :) × B × q(s_{t-1}), what does A(o_t, :) do?
A) Selects the row of A corresponding to the current observation, providing the likelihood
B) Updates the transition model
C) Changes the agent's preferences
D) Resets the agent's beliefs

**5.** A policy π in this framework is:
A) A single action
B) A sequence of actions to be evaluated for their expected outcomes
C) A brain region
D) A probability distribution over states

**6.** "Partially observable" means:
A) The agent can see everything perfectly
B) The agent cannot directly observe hidden states — observations are noisy/indirect
C) Half the states don't exist
D) The model is incomplete

**7.** The D vector represents:
A) The agent's beliefs about the initial state before any observations
B) The discount factor
C) The dimensionality of the model
D) The agent's actions

## Part B: Short Answer

**1.** Construct an A matrix for a 2-state, 2-observation system where observation is very reliable (90% correct). Write it out and verify columns sum to 1.

**2.** Explain why the C vector replaces the reward function in Active Inference. What's the philosophical difference between "seeking preferred observations" and "maximizing reward"?

**3.** Trace one full step of the perception-action loop: Given D = [0.6, 0.4], A = [[0.9, 0.2], [0.1, 0.8]], and observation o = "obs_1", compute the posterior q(s) (show your work). Which state is most likely?
