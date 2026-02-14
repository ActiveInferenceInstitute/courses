"""Visualization subpackage — matplotlib-based plotting utilities.

Modules
-------
plotting    — Time-series plots (beliefs, VFE, prediction errors, policies).
matrices    — Matrix heatmaps, model summaries, transition graphs.
diagnostics — Convergence, VFE/EFE components, precision sweeps, BMR.
simulation  — Simulation dashboards, environment trajectories, T-maze, gridworld.

Re-exports all public plot functions and configuration:
    from active_inference.visualization import plot_beliefs, configure, ...
"""

# ── Configuration ───────────────────────────────────────────────────
from .config import VizConfig, configure, get_config, reset_config

# ── Time-series plots ────────────────────────────────────────────────
from .plotting import (
    plot_beliefs,
    plot_free_energy,
    plot_prediction_errors,
    plot_policy_values,
    plot_efe_decomposition,
    plot_learning_progress,
)

# ── Matrix / model structure ─────────────────────────────────────────
from .matrices import (
    plot_matrix_heatmap,
    plot_A_matrix,
    plot_B_matrix,
    plot_C_preferences,
    plot_D_prior,
    plot_E_habits,
    plot_model_summary,
    plot_B_transition_graph,
    plot_dirichlet_concentration,
)

# ── Diagnostics ──────────────────────────────────────────────────────
from .diagnostics import (
    plot_convergence,
    plot_vfe_components,
    plot_efe_components,
    plot_precision_sweep,
    plot_entropy_trajectory,
    plot_surprise_trajectory,
    plot_dirichlet_learning,
    plot_bmr_results,
)

# ── Simulation ───────────────────────────────────────────────────────
from .simulation import (
    plot_simulation_dashboard,
    plot_environment_trajectory,
    plot_agent_vs_environment,
    plot_tmaze,
    plot_gridworld,
)

__all__ = [
    # config
    "VizConfig",
    "configure",
    "get_config",
    "reset_config",
    # plotting
    "plot_beliefs",
    "plot_free_energy",
    "plot_prediction_errors",
    "plot_policy_values",
    "plot_efe_decomposition",
    "plot_learning_progress",
    # matrices
    "plot_matrix_heatmap",
    "plot_A_matrix",
    "plot_B_matrix",
    "plot_C_preferences",
    "plot_D_prior",
    "plot_E_habits",
    "plot_model_summary",
    "plot_B_transition_graph",
    "plot_dirichlet_concentration",
    # diagnostics
    "plot_convergence",
    "plot_vfe_components",
    "plot_efe_components",
    "plot_precision_sweep",
    "plot_entropy_trajectory",
    "plot_surprise_trajectory",
    "plot_dirichlet_learning",
    "plot_bmr_results",
    # simulation
    "plot_simulation_dashboard",
    "plot_environment_trajectory",
    "plot_agent_vs_environment",
    "plot_tmaze",
    "plot_gridworld",
]
