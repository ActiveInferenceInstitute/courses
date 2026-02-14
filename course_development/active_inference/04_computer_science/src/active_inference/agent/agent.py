"""Active Inference Agent — belief updating, policy selection, and action.

Notation (from resources/notation_table.md):
    q(s)  — Recognition density (approximate posterior)
    G(π)  — Expected Free Energy for policy π
    γ     — Precision of beliefs about policies (inverse temperature)
    F     — Variational Free Energy
    π     — Policy (sequence of actions)
    o     — Observations
    ε     — Prediction error: o − E_q[o]

Cross-course connections (see resources/cross_course_map.md):
    Philosophy M5  — Agency as inference, affordances
    CogSci M5      — Motor control as Active Inference
    Math M5        — EFE derivation, policy selection
    CS M5          — Policy selection and EFE calculation (T-maze)
"""

import numpy as np
from typing import Optional, List, Dict
import logging

from .generative_model import GenerativeModel
from ..math.free_energy import compute_vfe, compute_efe, softmax

logger = logging.getLogger(__name__)


class ActiveInferenceAgent:
    """Discrete Active Inference agent with belief updating and policy selection.

    Implements the full perception-action loop (see notation_table.md
    Quick Reference Card):

    1. **Perceive**: observe ``o_t``, update ``q(s)`` by minimising ``F``
    2. **Decide**: evaluate policies via Expected Free Energy ``G(π)``
    3. **Act**: select action via softmax ``P(π) = σ(−γ · G(π))``

    Glossary terms (see resources/glossary.md):
        Recognition Density — q(s), the agent's belief about hidden states
        Policy              — π, a sequence of planned actions
        Precision           — γ, inverse temperature for policy selection
        Prediction Error    — ε = o − E_q[o]

    Parameters
    ----------
    model : GenerativeModel
        The agent's generative model (A, B, C, D, E matrices).
    gamma : float
        Precision of beliefs about policies (γ). Higher → more exploitative.
    policies : list of list of int, optional
        Available policies.  Each policy is a list of action indices.
        Defaults to single-step policies (one per action).

    Raises
    ------
    ValueError
        If *gamma* is negative.
    """

    def __init__(
        self,
        model: GenerativeModel,
        gamma: float = 1.0,
        policies: Optional[List[List[int]]] = None,
    ):
        if gamma < 0:
            raise ValueError(f"gamma must be ≥ 0, got {gamma}")

        self.model = model
        self.gamma = gamma

        # Default: single-step policies
        if policies is None:
            self.policies = [[a] for a in range(model.num_actions)]
        else:
            self.policies = policies

        # Initialise beliefs q(s) to prior D
        self.q_s = model.D.copy()

        # History tracking
        self.history: Dict[str, list] = {
            "observations": [],
            "actions": [],
            "beliefs": [],
            "vfe": [],
            "efe": [],
        }

        logger.info(
            "Agent created: γ=%.2f, %d policies", gamma, len(self.policies)
        )

    def reset(self) -> None:
        """Reset beliefs to prior and clear history."""
        self.q_s = self.model.D.copy()
        self.history = {k: [] for k in self.history}
        logger.info("Agent reset")

    # ------------------------------------------------------------------
    # Perception (minimise F)
    # ------------------------------------------------------------------

    def infer_states(
        self, observation: int, num_iterations: int = 16
    ) -> np.ndarray:
        """Update beliefs q(s) given a new observation by minimising F.

        Uses fixed-point iteration (see glossary: "Predictive Coding"):
            ``q(s) ∝ P(o|s) · q(s)``  →  normalise

        Parameters
        ----------
        observation : int
            Observed index ``o_t``.
        num_iterations : int
            Number of belief-update iterations.

        Returns
        -------
        np.ndarray
            Updated beliefs q(s).

        Raises
        ------
        ValueError
            If *observation* is out of range.
        """
        if not 0 <= observation < self.model.num_obs:
            raise ValueError(
                f"Observation {observation} out of range "
                f"[0, {self.model.num_obs})"
            )

        log_A = np.log(self.model.A[observation, :] + 1e-16)

        for _ in range(num_iterations):
            log_q = log_A + np.log(self.q_s + 1e-16)
            self.q_s = softmax(log_q, tau=1.0)

        vfe = compute_vfe(self.q_s, observation, self.model.A, self.model.D)

        self.history["observations"].append(observation)
        self.history["beliefs"].append(self.q_s.copy())
        self.history["vfe"].append(vfe)

        logger.debug("State inference: o=%d, VFE=%.4f", observation, vfe)
        return self.q_s

    # ------------------------------------------------------------------
    # Action (minimise G)
    # ------------------------------------------------------------------

    def infer_policies(self) -> np.ndarray:
        """Evaluate policies and return posterior q(π).

        For each policy π computes ``G(π) = Σ_τ G_τ(π)`` then applies
        softmax: ``q(π) = σ(−γ · G(π))``.

        Returns
        -------
        np.ndarray
            Posterior over policies q(π), shape ``(num_policies,)``.
        """
        G_values = np.zeros(len(self.policies))

        for i, policy in enumerate(self.policies):
            q_s_current = self.q_s.copy()
            G = 0.0
            for action in policy:
                G += compute_efe(
                    q_s_current,
                    self.model.A,
                    self.model.B,
                    self.model.C,
                    action,
                )
                if self.model.B.ndim == 3:
                    q_s_current = self.model.B[:, :, action] @ q_s_current
                else:
                    q_s_current = self.model.B @ q_s_current
            G_values[i] = G

        q_pi = softmax(-self.gamma * G_values)

        self.history["efe"].append(G_values.copy())
        logger.debug("Policy inference: G=%s, q(π)=%s", G_values, q_pi)
        return q_pi

    def select_action(self) -> int:
        """Sample an action from the policy posterior.

        Returns
        -------
        int
            Selected action index.
        """
        q_pi = self.infer_policies()
        policy_idx = int(np.random.choice(len(self.policies), p=q_pi))
        action = self.policies[policy_idx][0]
        self.history["actions"].append(action)
        logger.debug("Selected action: %d (policy %d)", action, policy_idx)
        return action

    # ------------------------------------------------------------------
    # Prediction errors
    # ------------------------------------------------------------------

    def get_predicted_observation(self) -> np.ndarray:
        """Return predicted observation distribution q(o) = A @ q(s).

        See glossary.md: "Prediction Error" — ε = o − E_q[o].

        Returns
        -------
        np.ndarray
            Predicted observation probabilities, shape ``(num_obs,)``.
        """
        return self.model.predict_observation(self.q_s)

    def prediction_error(self, observation: int) -> np.ndarray:
        """Compute prediction error ε between actual and predicted obs.

        ``ε_i = δ(o, i) − q(o_i)``  where ``q(o) = A @ q(s)``.

        See notation_table.md: "Prediction error ε = o − E_q[o]".

        Parameters
        ----------
        observation : int
            Actual observation index.

        Returns
        -------
        np.ndarray
            Prediction error vector, shape ``(num_obs,)``.
        """
        q_o = self.get_predicted_observation()
        o_onehot = np.zeros(self.model.num_obs)
        o_onehot[observation] = 1.0
        return o_onehot - q_o

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    def step(self, observation: int) -> int:
        """Full perception-action step: observe → infer → act.

        Parameters
        ----------
        observation : int
            Current observation.

        Returns
        -------
        int
            Selected action.
        """
        self.infer_states(observation)
        return self.select_action()

    def __repr__(self) -> str:
        return (
            f"ActiveInferenceAgent(γ={self.gamma}, "
            f"policies={len(self.policies)}, "
            f"model={self.model!r})"
        )
