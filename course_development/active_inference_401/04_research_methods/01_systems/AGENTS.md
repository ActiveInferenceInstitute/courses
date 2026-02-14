# Station: Systems (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Systems
- **Subtitle**: Identifying and Modeling Self-Organizing Systems
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must cover the practical methods for empirically determining whether a system is at non-equilibrium steady state (NESS) and for fitting stochastic dynamical models to real data. Students should learn how to estimate parameters of stochastic differential equations (SDEs) from time-series observations using both maximum likelihood methods (Ait-Sahalia, 2002) and Bayesian approaches (Kessler, 1997), how to test for the particular partition in empirical data, and how to diagnose identifiability failures when NESS cannot be distinguished from equilibrium on the basis of finite observations. Concrete examples should be drawn from neuroscience (EEG power spectra, fMRI BOLD dynamics) and should include discussion of criticality testing (power-law fitting, branching ratio estimation) and the methodological pitfalls therein (Clauset et al., 2009).

## Key Concepts

- **NESS testing**: Empirical criteria for determining whether a system maintains a non-equilibrium steady state, including detailed balance violation tests, entropy production estimation, and irreversibility metrics
- **Langevin model fitting**: Parameter estimation for SDEs of the form $dx = f(x)dt + \sigma dW$, including drift and diffusion coefficient estimation from discretely sampled trajectories
- **Parameter estimation for SDEs**: Maximum likelihood estimation via transition density approximation (Ait-Sahalia, 2002), Bayesian estimation using data augmentation (Roberts & Stramer, 2001), and generalized method of moments (Kessler, 1997)
- **Model identifiability**: Conditions under which NESS parameters (solenoidal flow $Q$, dissipative coupling $\Gamma$, steady-state density $p^*$) can be uniquely recovered from observed data; structural vs. practical identifiability
- **Evidence for criticality**: Methods for testing the criticality hypothesis in neural systems — power-law fitting (Clauset et al., 2009), detrended fluctuation analysis, branching ratio estimation, and the distinction between true criticality and quasi-critical dynamics

## Key References

- Ait-Sahalia, Y. (2002). Maximum likelihood estimation of discretely sampled diffusions: A closed-form approximation approach. *Econometrica*, 70(1), 223-262.
- Kessler, M. (1997). Estimation of an ergodic diffusion from discrete observations. *Scandinavian Journal of Statistics*, 24(2), 211-229.
- Friston, K., & Ao, P. (2012). Free energy, value, and attractors. *Computational and Mathematical Methods in Medicine*, 2012, 937860.
- Crauel, H., & Flandoli, F. (1994). Attractors for random dynamical systems. *Probability Theory and Related Fields*, 100(3), 365-393.
- Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. *SIAM Review*, 51(4), 661-703.
- Breakspear, M. (2017). Dynamic models of large-scale brain activity. *Nature Neuroscience*, 20(3), 340-352.

## Prerequisite Modules

- None (entry point for the Research Methods unit)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/01_systems/module.md](../../03_advanced_theory/01_systems/module.md)): Derives the NESS formalism, Fokker-Planck equation, and particular partition from first principles — this module asks how to test those formalisms empirically
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/01_systems/module.md](../../02_neuroscientific_frontiers/01_systems/module.md)): Examines neural systems as NESS with cortical dynamics and oscillatory evidence — this module provides the statistical tools to evaluate that evidence
- **Philosophical Foundations** ([../../01_philosophical_foundations/01_systems/module.md](../../01_philosophical_foundations/01_systems/module.md)): Debates the ontology of self-organizing systems and autopoiesis — this module operationalizes those concepts into testable empirical claims

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
