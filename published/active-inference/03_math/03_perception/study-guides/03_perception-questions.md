# Study Questions: Perception

1. Write the perception equation dμ/dt = -∂F/∂μ. Explain what each term represents.
2. For a single-level Gaussian model p(o|s) = N(s, σ²) with prior p(s) = N(μ₀, σ₀²), derive ∂F/∂μ and the fixed-point solution μ*.
3. What is the prediction error ε in the predictive coding scheme? How is it computed at each level?
4. How does precision weighting modulate the influence of prediction errors on belief updates?
5. Derive the message-passing equations for a two-level hierarchy. Identify the bottom-up and top-down messages.
6. What is the Jacobian ∂g/∂μ in the prediction error propagation? How does it transform errors between levels?
7. How do nonlinear generative mappings g(·) affect the message-passing equations compared to linear models?
8. Show that the fixed point of the predictive coding scheme corresponds to the mode of the posterior (MAP inference).
9. How does the Laplace approximation relate to the Gaussian assumption in predictive coding?
10. What is the difference between the Laplace-encoded form of predictive coding and the full Bayesian approach?
11. Derive the predictive coding update for generalized coordinates of motion (position, velocity, acceleration, ...).
12. How does predictive coding in generalized coordinates achieve temporal prediction (predicting the future of sensory input)?
13. What is the mathematical relationship between predictive coding and the Kalman filter?
14. Show that the Kalman filter is a special case of predictive coding for linear Gaussian models.
15. How does the gradient descent dynamics dμ/dt = -∂F/∂μ ensure convergence? What conditions are needed?
16. What is the role of the step size (learning rate) in the gradient descent for perception?
17. How does hierarchical depth affect the convergence of the message-passing scheme?
18. Derive the prediction error form of free energy for a model with both state and parameter estimation.
19. Compare variational message passing with belief propagation on factor graphs. What is the relationship?
20. Derive the update equations for a binary (categorical) hidden state model. How do the equations differ from the Gaussian case?
