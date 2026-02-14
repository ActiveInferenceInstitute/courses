# Lab: Building and Analyzing Active Inference Agents

## Objective

Implement, run, and analyze Active Inference agents in Python using the `active_inference` library. Progress from basic environment setup through belief updating, policy selection, parameter learning, and multi-agent simulation.

## Prerequisites

* Python 3.11+ with NumPy and Matplotlib
* The `active_inference` library (located in `src/active_inference/`)
* Jupyter notebook or Python IDE

```python
import sys
sys.path.insert(0, 'src')

import numpy as np
from active_inference.agent import GenerativeModel, ActiveInferenceAgent, DiscreteEnvironment
from active_inference.math import compute_vfe, compute_efe, softmax
from active_inference.math.learning import update_dirichlet_A, update_dirichlet_B, expected_A
```

## Procedure

### Part 1: Environment and Agent Setup (20 minutes)

Create a simple 2-state environment (states: LEFT, RIGHT) with 2 observations (see_left, see_right) and 2 actions (stay, switch):

1. Define the true likelihood matrix `true_A` where observation strongly indicates the current state (0.9 / 0.1 split).
2. Define the true transition matrix `true_B` where "stay" preserves state and "switch" flips it.
3. Create a `DiscreteEnvironment` with initial_state=0.
4. Step through 5 time steps, alternating between stay and switch actions. Record the observations generated.
5. Verify that observations match expectations given the true A matrix.

**Checkpoint**: You should see observations that are consistent with (but not perfectly determined by) the true state, reflecting the stochastic nature of the generative process.

### Part 2: Belief Updating (20 minutes)

1. Define a `GenerativeModel` with the agent's A and B matrices (initially set equal to the true matrices).
2. Create an `ActiveInferenceAgent` with this model.
3. Present a sequence of 10 observations and, after each, inspect the agent's posterior beliefs using `agent.beliefs`.
4. Introduce a model mismatch: set the agent's A matrix to be more uncertain than the true A (e.g., 0.7/0.3 instead of 0.9/0.1). Re-run the same observation sequence and compare how beliefs evolve.
5. Visualize beliefs over time for both the accurate and inaccurate models.

**Discussion**: How does model inaccuracy affect the speed and confidence of belief convergence?

### Part 3: Policy Selection via Expected Free Energy (20 minutes)

1. Define preferences C that strongly prefer observation 0 (e.g., C = [2.0, -2.0]).
2. Compute the expected free energy G for each available action (stay, switch) given the current beliefs.
3. Apply the softmax function with gamma=1.0 to obtain action probabilities.
4. Run a full perception-action loop for 20 timesteps: at each step, the agent observes, updates beliefs, selects a policy, and acts.
5. Plot the agent's state trajectory and EFE components (risk and ambiguity) over time.

**Checkpoint**: The agent should tend to select actions that move it toward the preferred observation, with occasional exploratory actions driven by ambiguity.

### Part 4: Online Parameter Learning (15 minutes)

1. Initialize Dirichlet concentration parameters `pA` with uniform priors: `pA = np.ones((2, 2))`.
2. Start the agent with an inaccurate A matrix (e.g., uniform: [[0.5, 0.5], [0.5, 0.5]]).
3. Run 50 timesteps of the perception-action loop, updating pA after each observation using `update_dirichlet_A`.
4. After each update, recompute the expected A matrix using `expected_A(pA)`.
5. Plot the expected A matrix entries over time and verify convergence toward the true A matrix values.

**Discussion**: How many observations does the agent need before its learned A matrix is close to the true A matrix? What would happen if the true environment changed after the agent had learned?

### Part 5: Visualization and Diagnosis (15 minutes)

Using the visualization module, generate the following plots for your agent's 50-timestep run:

1. Belief trajectory (posterior probability of each state over time)
2. Free energy over time (VFE at each step)
3. EFE components (risk and ambiguity for each action at each step)
4. Learned A matrix heatmap (final concentration parameters)

Interpret each plot: What does the free energy trajectory tell you about the agent's learning? Where do you see the transition from exploration to exploitation?

## Discussion Questions

1. What happens to the agent's behavior when you set gamma very high (e.g., 16.0) versus very low (e.g., 0.1)? Which setting produces more robust behavior in an uncertain environment?
2. If the environment suddenly changes its dynamics (the true B matrix shifts), how long does it take the agent's learned parameters to adapt? What design choices would make the agent more or less adaptive?
3. How would you extend this agent to handle a 3-state, 3-observation, 3-action problem? What changes in computational cost, and what stays the same algorithmically?
