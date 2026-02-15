# Section Lab: Building a Complete Active Inference Agent

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md)

## Objective

This integrative lab brings together all eight modules from the Implementation course. You will build, run, and analyze a complete Active Inference agent in the T-maze environment, implementing the full perception-action-learning loop from scratch and comparing your implementation with pymdp.

## Prerequisites

- Completion of all eight Implementation modules (01_systems through 08_planning)
- Working Python environment with NumPy, Matplotlib, and pymdp installed
- Familiarity with the T-maze task, POMDP matrices (A, B, C, D), and the Active Inference update equations

---

## Part 1: Environment and Generative Model Setup (Modules 01-02)

**Task 1a.** Implement a `TMazeEnvironment` class that manages the true hidden state and generates observations. The T-maze has 4 locations (center, left arm, right arm, cue location) and 2 reward conditions (reward-left, reward-right). Your class should:

- Store the current state (location, reward condition)
- Generate observations given the current state using the A matrix
- Transition the state given an action using the B matrix
- Reset the environment for a new trial

Paste your implementation below:

{fill:textarea}

**Task 1b.** Implement a `GenerativeModel` class that constructs the A, B, C, and D matrices for the T-maze. The A matrix should encode: (1) unambiguous location observations, (2) a cue that indicates reward location with 80% reliability, and (3) reward/no-reward observations in the arm locations. The C vector should encode a strong preference for reward (+4.0) and aversion to no-reward (-4.0).

Paste your matrix definitions and verify dimensions:

{fill:textarea}

---

## Part 2: State Inference (Module 03)

**Task 2a.** Implement the `infer_states()` function that performs one step of variational inference:

```python
def infer_states(observation, A, prior):
    """
    Compute posterior beliefs q(s) given an observation.
    Uses the softmax(ln A[o,:] + ln prior) formula.

    Args:
        observation: integer index of the observation
        A: likelihood matrix (num_obs x num_states)
        prior: prior belief vector over states

    Returns:
        posterior: updated belief vector over states
    """
```

Implement this function, then test it: given a uniform prior and observation o=0 (center location), what posterior does your function produce? Does it match the expected result from the A matrix?

{fill:textarea}

**Task 2b.** Run your `infer_states()` function for a sequence of 5 observations and plot the belief trajectory. Show how the agent's beliefs about its location and the reward condition evolve over time. Use `matplotlib` to create a figure with two subplots: (1) beliefs about location and (2) beliefs about reward condition.

Paste your plotting code and describe the resulting figure:

{fill:textarea}

---

## Part 3: Expected Free Energy and Policy Selection (Modules 04-05)

**Task 3a.** Implement the `compute_efe()` function that evaluates expected free energy for a given policy:

```python
def compute_efe(policy, A, B, C, current_beliefs, T):
    """
    Compute expected free energy G for a policy over T timesteps.

    Args:
        policy: list of action indices [a_0, a_1, ..., a_{T-1}]
        A, B, C: generative model matrices
        current_beliefs: current posterior q(s)
        T: planning horizon

    Returns:
        G: expected free energy (scalar)
        pragmatic: pragmatic component
        epistemic: epistemic component
    """
```

Implement this function with separate pragmatic and epistemic terms. Show the decomposition for the T-maze with two policies: "go to cue then left arm" vs. "go directly to left arm."

{fill:textarea}

**Task 3b.** Implement policy selection via softmax over negative EFE values:

```python
def select_policy(policies, G_values, gamma=16.0):
    """Select a policy using softmax over -G values."""
```

Run the policy selection with gamma values of 1.0, 4.0, and 16.0. How does the precision parameter affect the agent's tendency to explore vs. exploit? Plot the policy probability distribution for each gamma value.

{fill:textarea}

---

## Part 4: The Perception-Action Loop (Modules 02, 04)

**Task 4a.** Combine your components into a complete simulation loop that runs one T-maze trial:

```python
def run_trial(env, model, T=3, gamma=16.0):
    """
    Run one complete T-maze trial.
    Returns: beliefs, actions, observations, free_energies
    """
```

Run 10 trials and report: How often does the agent visit the cue location before choosing an arm? How often does it choose the correct (rewarded) arm?

{fill:textarea}

**Task 4b.** Compute and plot the variational free energy at each timestep within a single trial. Annotate the plot: Where does free energy spike (new observation)? Where does it decrease (successful inference)? How does the free energy trajectory change between the first trial and the tenth trial?

{fill:textarea}

---

## Part 5: Parameter Learning (Module 06)

**Task 5a.** Implement Dirichlet parameter learning for the A matrix:

```python
def update_parameters(A_prior, observations, beliefs, eta=1.0):
    """
    Update concentration parameters after a trial.

    Args:
        A_prior: current Dirichlet concentration parameters
        observations: list of observations from the trial
        beliefs: list of posterior beliefs from the trial
        eta: learning rate

    Returns:
        A_posterior: updated concentration parameters
    """
```

Run 50 trials with learning enabled. Plot the learning curve: reward rate (fraction of correct arm choices) as a function of trial number. Does performance improve?

{fill:textarea}

**Task 5b.** Compare the agent's A matrix before and after 50 trials of learning. Which entries changed the most? Print the initial and final A matrices side by side and explain what the agent has learned about the environment's statistical structure.

{fill:textarea}

---

## Part 6: Comparison with pymdp (Module 01)

**Task 6a.** Replicate your T-maze agent using pymdp's built-in `Agent` class. Set up the same A, B, C, D matrices and run 50 trials. Compare:

- Reward rate curves (your implementation vs. pymdp)
- Belief trajectories for the same observation sequence
- Computation time per trial

Paste your pymdp code and comparison results:

{fill:textarea}

**Task 6b.** Identify and explain any differences between your implementation and pymdp's results. Common sources of divergence include: numerical stability (log-space vs. linear-space computation), normalization conventions, and policy evaluation details. What did you learn from the comparison?

{fill:textarea}

---

## Part 7: Extension and Reflection

**7a.** Modify the T-maze to introduce a new challenge: make the cue reliability decrease over time (start at 90%, decrease by 2% each trial until reaching 50%). How does your agent's behavior change? Does it eventually stop visiting the cue location? Plot the cue-visit rate and reward rate over 100 trials.

{fill:textarea}

**7b.** Reflect on the full implementation experience. Which component was hardest to implement correctly? Where did numerical issues arise? What would you need to add to scale this implementation to more complex environments?

{fill:textarea}

---

## Submission Guidelines

- Submit all Python source files as separate .py attachments or paste code in the text areas
- Include all plots as inline figures or attached image files
- Code must be runnable -- include all imports and helper functions
- Total expected effort: 5-8 hours

## Recommended Readings

- Heins, C. et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *JOSS*, 7(73), 4098.
- Smith, R. et al. (2022). A step-by-step tutorial on active inference and its application to empirical data. *Journal of Mathematical Psychology*, 107, 102632.
- Da Costa, L. et al. (2020). Active inference on discrete state-spaces: A synthesis. *Journal of Mathematical Psychology*, 99, 102447.
