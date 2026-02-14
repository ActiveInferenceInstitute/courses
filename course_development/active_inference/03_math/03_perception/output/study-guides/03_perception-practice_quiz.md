# Practice Quiz: Perception

## Part A: Multiple Choice

1. The perception equation dμ/dt = -∂F/∂μ describes:
A) Motor control
B) Gradient descent on free energy — internal states flow to minimize prediction error
C) Random exploration of state space
D) A static equilibrium condition

2. In a two-level predictive coding hierarchy, the update at level l depends on:
A) Only bottom-up prediction errors from level l-1
B) Only top-down predictions from level l+1
C) Both bottom-up precision-weighted prediction errors and top-down predictions
D) Neither — each level is independent

3. The prediction error εₗ = μₗ - g(μₗ₊₁) represents:
A) The noise in observations
B) The discrepancy between the current estimate and the prediction from the level above
C) The learning rate
D) The prior probability

4. Precision weighting in message passing determines:
A) The color of neural signals
B) How strongly a prediction error drives updates — high precision errors matter more
C) The speed of neural transmission
D) The number of neurons involved

5. The fixed point of the predictive coding dynamics (dμ/dt = 0) corresponds to:
A) Maximum free energy
B) The MAP (maximum a posteriori) estimate of the hidden states
C) Random guessing
D) The prior mean only

6. The Laplace approximation:
A) Assumes all distributions are uniform
B) Approximates the posterior as Gaussian centered on the MAP estimate, enabling tractable nonlinear inference
C) Is exact for all distributions
D) Only applies to discrete distributions

7. Generalized coordinates extend predictive coding by:
A) Adding more spatial dimensions
B) Including temporal derivatives (velocity, acceleration, etc.), enabling prediction of how sensory input will change
C) Removing the hierarchical structure
D) Replacing continuous states with discrete states

## Part B: Short Answer

1. For a Gaussian model with prior p(s) = N(0, 4) and likelihood p(o|s) = N(s, 1), compute the posterior mean after observing o = 3. Show that it is a precision-weighted average.
2. In a three-level hierarchy (observations → level 1 → level 2 → level 3), describe the messages passed between levels. Why must prediction errors from below AND predictions from above both contribute to each level's update?
3. Explain why the Kalman filter is a special case of predictive coding for linear Gaussian models. What additional capability does predictive coding in generalized coordinates provide beyond the standard Kalman filter?
