"""Active Inference Core Library
================================

Modular Python implementations of Active Inference concepts for the
Computer Science course of the Active Inference curriculum.

56 top-level exports: 4 classes, 20 math functions, 28 plot functions,
3 config functions, and 1 constant.

Subpackages
-----------
active_inference.agent
    Generative model, agent, and environment classes.
active_inference.math
    Free energy, inference algorithms, and learning functions.
active_inference.visualization
    Matplotlib-based plotting utilities.

Notation (from resources/notation_table.md)
-------------------------------------------
Core variables:
    F    — Variational Free Energy (VFE; upper bound on surprisal)
    G    — Expected Free Energy (EFE; drives action selection)
    q(s) — Recognition density (approximate posterior over hidden states)
    o    — Observations
    s    — Hidden states
    a    — Actions
    π    — Policy (sequence of actions)
    γ    — Precision of beliefs about policies (inverse temperature)
    β    — Precision of sensory data (inverse variance)
    ω    — Precision of prior beliefs

Generative model matrices:
    A    — Likelihood mapping P(o|s)                  (|o| × |s|)
    B    — Transition model P(s'|s, a)                (|s| × |s| × |a|)
    C    — Log-preferences over observations ln P(o)  (|o|,)
    D    — Prior over initial states P(s₀)            (|s|,)
    E    — Habit prior over policies P(π)             (|π|,)

Learned parameters (Dirichlet concentrations):
    pA   — Concentration parameters for A
    pB   — Concentration parameters for B
    pD   — Concentration parameters for D

Information-theoretic quantities:
    D_KL — KL divergence
    H    — Shannon entropy
    S    — Surprisal = −ln p(o)
    I    — Mutual information = H(X) − H(X|Y)

See also:
    resources/glossary.md          — term definitions
    resources/notation_table.md    — canonical symbols
    resources/cross_course_map.md  — parallel modules across courses
"""

# ── Agent subpackage ──────────────────────────────────────────────────
from .agent import GenerativeModel, ActiveInferenceAgent, DiscreteEnvironment

# ── Math subpackage ───────────────────────────────────────────────────
from .math import (
    compute_vfe,
    compute_vfe_components,
    compute_efe,
    compute_efe_components,
    kl_divergence,
    entropy,
    softmax,
    surprisal,
    mutual_information,
    LOG_ZERO_GUARD,
    run_state_inference,
    run_policy_inference,
    run_mmp,
    update_dirichlet_A,
    update_dirichlet_B,
    update_dirichlet_D,
    expected_A,
    expected_B,
    expected_D,
    dirichlet_entropy,
    bayesian_model_reduction,
)

# ── Visualization subpackage ─────────────────────────────────────────
from .visualization import (
    # config
    VizConfig,
    configure,
    get_config,
    reset_config,
    # plotting
    plot_beliefs,
    plot_free_energy,
    plot_prediction_errors,
    plot_policy_values,
    plot_efe_decomposition,
    plot_learning_progress,
    # matrices
    plot_matrix_heatmap,
    plot_A_matrix,
    plot_B_matrix,
    plot_C_preferences,
    plot_D_prior,
    plot_E_habits,
    plot_model_summary,
    plot_B_transition_graph,
    plot_dirichlet_concentration,
    # diagnostics
    plot_convergence,
    plot_vfe_components,
    plot_efe_components,
    plot_precision_sweep,
    plot_entropy_trajectory,
    plot_surprise_trajectory,
    plot_dirichlet_learning,
    plot_bmr_results,
    # simulation
    plot_simulation_dashboard,
    plot_environment_trajectory,
    plot_agent_vs_environment,
    plot_tmaze,
    plot_gridworld,
)

__all__ = [
    # Agent subpackage
    "GenerativeModel",
    "ActiveInferenceAgent",
    "DiscreteEnvironment",
    # Math / Free energy
    "compute_vfe",
    "compute_vfe_components",
    "compute_efe",
    "compute_efe_components",
    "kl_divergence",
    "entropy",
    "softmax",
    "surprisal",
    "mutual_information",
    "LOG_ZERO_GUARD",
    # Math / Inference
    "run_state_inference",
    "run_policy_inference",
    "run_mmp",
    # Math / Learning
    "update_dirichlet_A",
    "update_dirichlet_B",
    "update_dirichlet_D",
    "expected_A",
    "expected_B",
    "expected_D",
    "dirichlet_entropy",
    "bayesian_model_reduction",
    # Visualization — config
    "VizConfig",
    "configure",
    "get_config",
    "reset_config",
    # Visualization — plotting
    "plot_beliefs",
    "plot_free_energy",
    "plot_prediction_errors",
    "plot_policy_values",
    "plot_efe_decomposition",
    "plot_learning_progress",
    # Visualization — matrices
    "plot_matrix_heatmap",
    "plot_A_matrix",
    "plot_B_matrix",
    "plot_C_preferences",
    "plot_D_prior",
    "plot_E_habits",
    "plot_model_summary",
    "plot_B_transition_graph",
    "plot_dirichlet_concentration",
    # Visualization — diagnostics
    "plot_convergence",
    "plot_vfe_components",
    "plot_efe_components",
    "plot_precision_sweep",
    "plot_entropy_trajectory",
    "plot_surprise_trajectory",
    "plot_dirichlet_learning",
    "plot_bmr_results",
    # Visualization — simulation
    "plot_simulation_dashboard",
    "plot_environment_trajectory",
    "plot_agent_vs_environment",
    "plot_tmaze",
    "plot_gridworld",
]

__version__ = "0.4.0"
