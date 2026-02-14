# Practice Quiz: Planning

## Part A: Multiple Choice

1. A multi-step policy specifies:
A) A single action
B) A sequence of actions over T future timesteps
C) A probability distribution over actions
D) A belief update rule

2. The total EFE of a 3-step policy is computed by:
A) Taking the EFE at the first step only
B) Taking the maximum EFE across steps
C) Summing $G_\tau(\pi)$ for $\tau = 0, 1, 2$
D) Multiplying the three step EFEs

3. Marginal Message Passing differs from single-step inference because it:
A) Uses the C-vector
B) Infers beliefs at multiple time points simultaneously
C) Only works for gridworlds
D) Does not use the A-matrix

4. For a 3-action system with temporal depth T = 4, the number of exhaustive policies is:
A) 12
B) 64
C) 81
D) 256

5. In a gridworld, walls are encoded by:
A) Removing states from the state space
B) Setting the B-matrix to have self-transitions at wall positions
C) Modifying the A-matrix
D) Setting C to zero at wall states

6. Why does the T-maze require T ≥ 2 for reliable performance?
A) The environment has more than 2 states
B) The agent must visit the cue (step 1) before choosing an arm (step 2)
C) The B-matrix requires 2 transitions
D) Precision γ must equal 2

7. `plot_simulation_dashboard()` displays:
A) A single belief plot
B) 5 panels: beliefs, VFE, predictions, prediction errors, and EFE
C) The gridworld state space
D) The A and B matrices

## Part B: Short Answer

1. Write code to define all 2-step policies for a 3-action system. How many policies are there? Display them as a list of lists.

2. Explain why the computational cost of planning scales exponentially with temporal depth T. Describe one strategy to manage this complexity (e.g., pruning, hierarchical policies, or Monte Carlo sampling).

3. Design a delayed-reward gridworld where a greedy (T = 1) agent gets stuck but a planning (T = 3) agent succeeds. Sketch the grid, identify the obstacle, and explain why depth matters.
