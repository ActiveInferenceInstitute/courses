# Practice Quiz: Planning / Complete Agent (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** The CompleteActiveInferenceAgent integrates:
A) Only perception
B) Perception, action, learning, and habit formation in one unified class
C) Only reinforcement learning
D) External API calls

**2.** Habit formation in the implementation is achieved by:
A) Hard-coding preferred actions
B) Strengthening the policy prior for successful policies via `update_habits`
C) Removing all but one policy
D) Increasing gamma

**3.** The equation `log_pi = -γG + log(policy_prior)` shows that action selection depends on:
A) Only habits
B) Both EFE evaluation (G) and habitual tendencies (policy_prior)
C) Only EFE
D) Random noise

**4.** Over many time steps, habit entropy:
A) Increases
B) Decreases as certain policies become more habitual
C) Stays constant
D) Oscillates

**5.** The `step` method performs these operations in order:
A) Act, Perceive, Learn, Habituate
B) Perceive → Decide → Learn → Habituate
C) Learn, Act, Perceive
D) Habituate, then everything else

**6.** The `summary` method reports:
A) Only action counts
B) Action distribution, final beliefs, learning rate, strongest habit, and habit entropy
C) The agent's name
D) Memory usage

**7.** Comparing early vs. late behavior reveals:
A) No difference
B) Early behavior is goal-directed (EFE-dominated), late behavior is habitual (prior-dominated)
C) Late behavior is always random
D) Early behavior is always habitual

## Part B: Short Answer

**1.** Trace the `step` method for one time step. List each operation, what it updates, and why.

**2.** How would you implement "dehabituation" — reducing habit strength when the environment changes? Describe the code changes needed and when dehabituation should trigger.

**3.** Reflecting on the entire 101 course: you've studied Active Inference through Cognitive Science, Computational Neuroscience, Mathematical Frameworks, and now Implementation. Identify one concept that became clearer through implementation and explain why.
