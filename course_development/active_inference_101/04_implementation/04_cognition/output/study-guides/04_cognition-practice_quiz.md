# Practice Quiz: Cognition (Implementation)

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** The T-Maze has how many hidden states?
A) 2
B) 4
C) 8 — (4 locations × 2 reward conditions)
D) 16

**2.** The T-Maze uses 3 observation modalities because:
A) Three is a magic number
B) The agent needs separate channels for location, cue, and reward information
C) Python requires 3 arrays
D) There are 3 states

**3.** The expected behavior of an Active Inference agent in the T-Maze is:
A) Always go left
B) First visit the cue (information-seeking), then go to the rewarded arm (goal-seeking)
C) Never visit the cue
D) Stay in the center forever

**4.** The agent visits the cue because:
A) It's programmed to
B) The cue has high epistemic value — visiting it reduces uncertainty about the reward location
C) The cue has high reward
D) There's no other option

**5.** If cue reliability is 0.5 (random), the agent:
A) Still visits the cue out of habit
B) Has less incentive to visit the cue since it provides no information
C) Always visits the cue
D) Crashes

**6.** The C_reward vector = [3, -3, 0] means:
A) Reward has value 3, loss has penalty -3, neutral is neither
B) There are 3 states
C) The agent prefers 3 rewards
D) The discount factor is 3

**7.** In the B matrix, the reward condition dimension doesn't change because:
A) The code is incomplete
B) The reward is permanently in one location — the agent's actions don't move the reward
C) B only encodes location
D) NumPy doesn't support 4D arrays

## Part B: Short Answer

**1.** Explain why the T-Maze demonstrates the exploration-exploitation balance. What drives the agent to explore (visit cue) vs. exploit (go to reward arm)?

**2.** Design a modification to the T-Maze where there are 3 arms instead of 2, with cues of different reliability for each arm. How would A, B, C, D change?

**3.** What happens to the agent's behavior if you set C_reward = [0, 0, 0]? Why? What is the agent optimizing for in the absence of preferences?
