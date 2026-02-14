"""Math subpackage — free energy, inference algorithms, and learning.

Re-exports all public functions and constants:
    from active_inference.math import compute_vfe, run_state_inference, update_dirichlet_A, ...
"""

from .free_energy import (
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
)
from .inference import (
    run_state_inference,
    run_policy_inference,
    run_mmp,
)
from .learning import (
    update_dirichlet_A,
    update_dirichlet_B,
    update_dirichlet_D,
    expected_A,
    expected_B,
    expected_D,
    dirichlet_entropy,
    bayesian_model_reduction,
)

__all__ = [
    # Free energy
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
    # Inference
    "run_state_inference",
    "run_policy_inference",
    "run_mmp",
    # Learning
    "update_dirichlet_A",
    "update_dirichlet_B",
    "update_dirichlet_D",
    "expected_A",
    "expected_B",
    "expected_D",
    "dirichlet_entropy",
    "bayesian_model_reduction",
]
