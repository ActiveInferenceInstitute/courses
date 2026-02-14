# Station: Learning (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Learning — CALPHAD Assessment and Machine Learning
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

CALPHAD database assessment is generative model learning in its purest form. The assessor collects experimental data (phase boundaries, enthalpies of mixing, activity measurements), parameterizes Gibbs energy functions, and iteratively adjusts interaction parameters to minimize the residual between model predictions and experimental observations. This is exactly the structure of Bayesian model learning: prior parameters are updated with likelihood from new data to produce a posterior model. Machine learning approaches (neural network potentials, Gaussian process regression for phase stability) extend this learning to higher-dimensional composition spaces where traditional assessment becomes intractable.

## Key Mappings

| FEP Concept | CALPHAD Learning Translation |
|-------------|------------------------------|
| Model Learning | CALPHAD parameter assessment; database optimization |
| Prior | Initial parameter estimates from end-member data and ab initio calculations |
| Likelihood | Experimental phase boundary data, calorimetric measurements, activity data |
| Posterior | Optimized Gibbs energy parameters after assessment |
| Prediction Error | Residual between calculated and experimental phase diagram features |
| Model Complexity | Number of interaction parameters; sublattice model order |

## Content Guidelines

- Frame the CALPHAD assessment cycle (data collection, parameterization, optimization, validation) as a complete Active Inference learning loop
- Connect machine learning for phase prediction to amortized inference — training a neural network to approximate the expensive CALPHAD calculation
- Treat the ICSD (Inorganic Crystal Structure Database) as a repository of crystallographic priors that inform new phase predictions
- Emphasize that good CALPHAD assessment balances model complexity against data fit, directly paralleling the complexity-accuracy trade-off in variational free energy

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
