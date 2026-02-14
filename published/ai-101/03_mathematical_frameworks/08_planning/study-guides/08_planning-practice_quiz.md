# Practice Quiz: Planning (Mathematical Frameworks)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** In Active Inference, planning is treated as:
A) A separate search algorithm
B) Inference over policies — the same variational inference applied to action sequences
C) Random action selection
D) Only applicable to robots

**2.** A policy π in the planning framework is:
A) A single action
B) A sequence of actions [a₁, a₂, ..., a_T] evaluated by Expected Free Energy
C) A brain region
D) A probability distribution over states

**3.** Deep temporal models handle planning across multiple timescales by:
A) Running faster
B) Using hierarchical POMDPs where higher levels operate on slower timescales
C) Ignoring short-term actions
D) Only planning for the distant future

**4.** Habits emerge mathematically when:
A) The agent forgets everything
B) The policy prior P(π) becomes so strong that it dominates over EFE evaluation
C) Expected Free Energy is always zero
D) The agent has no preferences

**5.** In the posterior P(π | o) ∝ P(π) × exp(-γG(π)), P(π) represents:
A) The likelihood of observations
B) The prior on policies — encoding habitual tendencies
C) The posterior on hidden states
D) The precision of sensory data

**6.** The complete Active Inference algorithm integrates:
A) Only perception
B) Perception, action, learning, and planning in a single mathematical loop
C) Only motor control
D) Only language processing

**7.** When encountering a novel situation, an Active Inference agent:
A) Freezes and does nothing
B) Shifts from habitual (prior-dominated) to goal-directed (EFE-dominated) behavior
C) Always follows habits
D) Ignores the situation

## Part B: Short Answer

**1.** Compare planning in Active Inference to a traditional AI planning algorithm (like A* search). What are the key differences in how they represent and evaluate plans?

**2.** Explain the transition from goal-directed to habitual behavior using the equation P(π | o) ∝ P(π) × exp(-γG(π)). What happens to the relative influence of P(π) and G(π) as the agent gains experience?

**3.** Design a simple 2-level deep temporal model for studying for an exam. The high level plans the week (which subjects to cover each day) and the low level plans each study session (which techniques to use). Describe the states, actions, and goals at each level.
