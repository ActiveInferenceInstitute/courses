# Lab: Implementing Perceptual Inference

> **Learning Goal:** Run variational message passing, compute prediction errors, and visualize belief dynamics.

## Part 1: Run Message Passing

**Exercise**: Set up a simple 2-state model and run variational inference:

```python
import numpy as np

A = np.array([[0.9, 0.1], [0.1, 0.9]])  # reliable observation
B = np.zeros((2, 2, 2))
B[:,:,0] = np.eye(2)  # action 0: stay
B[:,:,1] = np.array([[0, 1], [1, 0]])  # action 1: switch
D = np.array([0.5, 0.5])

# Sequence of observations and actions
observations = [0, 0, 1, 1, 0]  # observe state 0, then 1, then 0
actions = [0, 0, 1, 0]  # stay, stay, switch, stay

qs = variational_inference(A, B, D, observations, actions)
for t, q in enumerate(qs):
    print(f"t={t}: beliefs = {q.round(3)}, obs = {observations[t]}")
```

Do the beliefs track the observations? How quickly?

{fill:textarea}

## Part 2: Prediction Error Analysis

> **Learning Goal:** Compute and interpret prediction errors.

**Exercise**: Using the results from Part 1:

```python
state_pe, obs_pe = compute_prediction_errors(A, B, qs, observations, actions)
for t in range(len(observations)):
    print(f"t={t}: obs_PE = {obs_pe[t].round(3)}, state_PE = {state_pe[t].round(3)}")
```

1. At which time step is the observation prediction error largest? Why?
2. Does the prediction error decrease over time? Why or why not?

{fill:textarea}

## Part 3: Precision Effects

> **Learning Goal:** Explore how precision changes inference.

**Exercise**: Modify the A matrix to be less precise:

```python
A_noisy = np.array([[0.6, 0.4], [0.4, 0.6]])  # unreliable observation
qs_noisy = variational_inference(A_noisy, B, D, observations, actions)

# Compare beliefs from reliable vs. unreliable observations
for t in range(len(observations)):
    print(f"t={t}: reliable = {qs[t].round(3)}, noisy = {qs_noisy[t].round(3)}")
```

How do noisier observations affect belief certainty?

{fill:textarea}

## Part 4: Free Energy Tracking

> **Learning Goal:** Monitor free energy during inference.

**Exercise**: Compute free energy at each time step:

```python
for t in range(len(observations)):
    if t == 0:
        prior = D
    else:
        prior = B[:,:,actions[t-1]] @ qs[t-1]
    F, acc, comp = compute_free_energy(A, qs[t], observations[t], prior)
    print(f"t={t}: F = {F:.3f}, Accuracy = {acc:.3f}, Complexity = {comp:.3f}")
```

Is free energy lower when observations match predictions?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: How does watching prediction errors and free energy evolve over time deepen your understanding of perception as inference?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Running VMP | Message passing beliefs |
| 2 | Error analysis | Prediction error computation |
| 3 | Parameter effects | Precision and observation noise |
| 4 | Free energy tracking | F = Complexity - Accuracy |
| 5 | Reflection | Perception as inference |
