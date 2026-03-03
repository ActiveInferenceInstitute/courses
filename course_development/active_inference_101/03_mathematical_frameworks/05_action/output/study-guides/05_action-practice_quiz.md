# Practice Quiz: Action (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** Expected Free Energy G(π) evaluates:
A) How much energy the agent has
B) How good a policy is expected to be — lower G means a better policy
C) How fast the agent moves
D) The agent's current beliefs

**2.** The EFE decomposition shows that policy selection balances:
A) Speed and accuracy
B) Pragmatic value (goal-seeking) and epistemic value (information-seeking)
C) Perception and action
D) Reward and punishment

**3.** Pragmatic value is high when:
A) The agent learns a lot
B) Expected observations match the agent's preferences (C vector)
C) The agent has no preferences
D) Uncertainty is high

**4.** Epistemic value is high when:
A) The agent already knows everything
B) The policy leads to observations that reduce uncertainty about hidden states
C) The agent achieves its goals
D) No exploration occurs

**5.** The softmax function in policy selection:
A) Picks the random policy
B) Converts EFE scores into probabilities, with lower G getting higher probability
C) Eliminates all but one policy
D) Doubles the EFE value

**6.** When uncertainty is high, EFE favors policies with:
A) High pragmatic value only
B) High epistemic value (exploration) because reducing uncertainty is most valuable
C) No value at all
D) Only habitual actions

**7.** Policy precision γ controls:
A) How fast the agent moves
B) How decisive the agent is — higher γ means more commitment to the best policy
C) The number of available policies
D) The length of each policy

## Part B: Short Answer

**1.** Two policies: π₁ has pragmatic value = 5, epistemic value = 1. π₂ has pragmatic value = 2, epistemic value = 6. Compute total value for each (pragmatic + epistemic). Which policy is selected and why?

**2.** Explain why Active Inference does not need a separate "exploration bonus" parameter, unlike many reinforcement learning algorithms. How does exploration emerge naturally from the EFE formulation?

**3.** A robot is exploring a new room. Initially it knows nothing about the room layout. After 10 minutes of exploration, it has mapped most of the room. How does the balance between epistemic and pragmatic value change over time? What drives this shift?
