# Practice Quiz: Action (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Multi-step policies are generated using:
A) Random sampling
B) Cartesian product of actions across time steps
C) Neural networks
D) Manual specification only

**2.** For 4 actions and 3 time steps, the total number of policies is:
A) 12
B) 64 (4³)
C) 7
D) 4

**3.** The pragmatic component of EFE measures:
A) How much the agent will learn
B) How well expected future observations match the agent's preferences (C vector)
C) The speed of action execution
D) The number of states

**4.** The epistemic component of EFE measures:
A) The agent's knowledge level
B) How much mutual information there is between future states and observations under a policy
C) The reward value
D) The prior probability

**5.** In the active inference loop, belief transition is done:
A) Before observing
B) After executing the action — predicting the next state before the next observation
C) Only during learning
D) Never

**6.** The log dictionary in the loop stores:
A) Debug messages
B) Belief, action, observation, and EFE histories for post-hoc analysis
C) Error messages only
D) File paths

**7.** If gamma is very high, the agent:
A) Acts randomly
B) Commits strongly to the policy with lowest EFE
C) Never acts
D) Ignores observations

## Part B: Short Answer

**1.** Explain the computational scaling problem of policy evaluation: how does the number of policies grow with num_actions and policy_length? At what point does this become impractical?

**2.** Write pseudocode for selecting an action in the active inference loop. Include state inference, policy evaluation, softmax, and sampling.

**3.** An agent in a 3-state world has two policies. Policy 1 has pragmatic value 5 and epistemic value 1. Policy 2 has pragmatic value 2 and epistemic value 6. With gamma = 1.0, compute P(π₁) and P(π₂) using softmax.
