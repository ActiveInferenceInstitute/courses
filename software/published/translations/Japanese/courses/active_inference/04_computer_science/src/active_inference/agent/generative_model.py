"""Generative Model — A, B, C, D, E matrices for discrete state spaces.

Notation (from resources/notation_table.md):
    A[o, s]       — P(o | s), likelihood mapping         (|o| × |s|)
    B[s', s, a]   — P(s' | s, a), transition model       (|s| × |s| × |a|)
    C[o]          — ln P(o), log-prior preferences        (|o|,)
    D[s]          — P(s_0), prior over initial states     (|s|,)
    E[π]          — P(π), prior over policies (habits)    (|π|,)
    S(o)          — -ln p(o), surprisal                   (scalar)

Cross-course connections (see resources/cross_course_map.md):
    Philosophy M2  — Autopoiesis, agency, self-organizing system
    CogSci M2      — Self-model, interoception, ego boundaries
    Math M2        — Particular partition, Bayesian mechanics
    CS M2          — Agent class, A–E matrix initialization
"""

import numpy as np
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class GenerativeModel:
    """Discrete-state-space generative model for Active Inference.

    Encapsulates the five matrices (A, B, C, D, E) that define how an
    agent models its world.  The generative model specifies the joint
    distribution ``p(o, s, π) = p(o|s) · p(s|π) · p(π) = A · B^π · E``
    (see notation_table.md, Matrix Relationships).

    Glossary terms (see resources/glossary.md):
        Generative Model — probabilistic model of how observations arise
        Likelihood       — A-matrix: P(o|s)
        Transition       — B-matrix: P(s'|s, a)
        Preferences      — C-matrix: ln P(o)
        Prior            — D-vector: P(s_0)
        Habits           — E-vector: P(π)

    Parameters
    ----------
    A : np.ndarray
        Likelihood mapping, shape ``(num_obs, num_states)``.
        Each column must sum to 1: ``Σ_o A[o,s] = 1`` for all *s*.
    B : np.ndarray
        Transition model, shape ``(num_states, num_states, num_actions)``.
        Each column must sum to 1: ``Σ_{s'} B[s',s,a] = 1`` for all *s*, *a*.
    C : np.ndarray
        Log-preferences over observations, shape ``(num_obs,)``.
    D : np.ndarray
        Prior over initial states, shape ``(num_states,)``.  Must sum to 1.
    E : np.ndarray, optional
        Habit prior over policies, shape ``(num_policies,)``.  Must sum to 1.

    Raises
    ------
    ValueError
        If any matrix has an invalid shape or fails normalisation.
    """

    def __init__(
        self,
        A: np.ndarray,
        B: np.ndarray,
        C: np.ndarray,
        D: np.ndarray,
        E: Optional[np.ndarray] = None,
    ):
        self.A = np.asarray(A, dtype=np.float64)
        self.B = np.asarray(B, dtype=np.float64)
        self.C = np.asarray(C, dtype=np.float64)
        self.D = np.asarray(D, dtype=np.float64)

        # Pre-validate ndim before extracting shape indices
        if self.A.ndim != 2:
            raise ValueError(f"A must be 2-D, got {self.A.ndim}-D")

        self.num_obs: int = self.A.shape[0]
        self.num_states: int = self.A.shape[1]
        self.num_actions: int = self.B.shape[2] if self.B.ndim == 3 else 1

        self.E: Optional[np.ndarray] = (
            np.asarray(E, dtype=np.float64) if E is not None else None
        )

        self._validate()
        logger.info(
            "GenerativeModel created: %d obs, %d states, %d actions",
            self.num_obs, self.num_states, self.num_actions,
        )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate(self) -> None:
        """Validate matrix shapes and normalisation.

        Raises
        ------
        ValueError
            On any constraint violation.
        """
        # A — likelihood
        for s in range(self.num_states):
            col_sum = self.A[:, s].sum()
            if not np.isclose(col_sum, 1.0):
                raise ValueError(
                    f"A column {s} sums to {col_sum:.6f}, expected 1.0"
                )

        # B — transitions
        if self.B.ndim == 3:
            if self.B.shape[0] != self.num_states or self.B.shape[1] != self.num_states:
                raise ValueError(
                    f"B shape {self.B.shape} inconsistent with {self.num_states} states"
                )
            for a in range(self.num_actions):
                for s in range(self.num_states):
                    col_sum = self.B[:, s, a].sum()
                    if not np.isclose(col_sum, 1.0):
                        raise ValueError(
                            f"B column s={s}, a={a} sums to {col_sum:.6f}"
                        )
        elif self.B.ndim != 2:
            raise ValueError(f"B must be 2-D or 3-D, got {self.B.ndim}-D")

        # C — preferences
        if self.C.shape != (self.num_obs,):
            raise ValueError(f"C shape {self.C.shape} != ({self.num_obs},)")

        # D — prior
        if self.D.shape != (self.num_states,):
            raise ValueError(f"D shape {self.D.shape} != ({self.num_states},)")
        if not np.isclose(self.D.sum(), 1.0):
            raise ValueError(f"D sums to {self.D.sum():.6f}, expected 1.0")

        # E — habits (optional)
        if self.E is not None and not np.isclose(self.E.sum(), 1.0):
            raise ValueError(f"E sums to {self.E.sum():.6f}, expected 1.0")

        logger.debug("GenerativeModel validation passed")

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def log_likelihood(self, o: int) -> np.ndarray:
        """Compute ln P(o | s) for each state *s*.

        Parameters
        ----------
        o : int
            Observation index.

        Returns
        -------
        np.ndarray
            Log-likelihood vector, shape ``(num_states,)``.

        Raises
        ------
        ValueError
            If *o* is out of range.
        """
        if not 0 <= o < self.num_obs:
            raise ValueError(f"Observation {o} out of range [0, {self.num_obs})")
        return np.log(self.A[o, :] + 1e-16)

    def surprisal(self, o: int, q_s: np.ndarray) -> float:
        """Surprisal S(o) = −ln p(o) = −ln Σ_s P(o|s) q(s).

        Defined in notation_table.md (line 67) and glossary.md
        ("Surprisal").

        Parameters
        ----------
        o : int
            Observation index.
        q_s : np.ndarray
            Belief distribution over states, shape ``(num_states,)``.

        Returns
        -------
        float
            Surprisal in nats.
        """
        if not 0 <= o < self.num_obs:
            raise ValueError(f"Observation {o} out of range [0, {self.num_obs})")
        p_o = float(self.A[o, :] @ q_s)
        return -np.log(p_o + 1e-16)

    def log_joint(self, o: int, s: int) -> float:
        """Compute ln p(o, s) = ln A[o, s] + ln D[s].

        Under the generative model the joint factorises as
        ``p(o, s) = p(o|s) p(s) = A[o,s] · D[s]``.

        Parameters
        ----------
        o : int
            Observation index.
        s : int
            State index.

        Returns
        -------
        float
            Log-joint probability.
        """
        if not 0 <= o < self.num_obs:
            raise ValueError(f"Observation {o} out of range [0, {self.num_obs})")
        if not 0 <= s < self.num_states:
            raise ValueError(f"State {s} out of range [0, {self.num_states})")
        return float(np.log(self.A[o, s] + 1e-16) + np.log(self.D[s] + 1e-16))

    def predict_observation(self, q_s: np.ndarray) -> np.ndarray:
        """Predict observation distribution: q(o) = Σ_s A[o, s] q(s).

        Parameters
        ----------
        q_s : np.ndarray
            Belief distribution over states, shape ``(num_states,)``.

        Returns
        -------
        np.ndarray
            Predicted observation distribution, shape ``(num_obs,)``.
        """
        return self.A @ q_s

    def predict_state(self, q_s: np.ndarray, action: int) -> np.ndarray:
        """Predict next-state distribution: q(s') = B[:, :, a] @ q(s).

        Parameters
        ----------
        q_s : np.ndarray
            Current belief over states.
        action : int
            Action index.

        Returns
        -------
        np.ndarray
            Predicted state distribution, shape ``(num_states,)``.

        Raises
        ------
        ValueError
            If *action* is out of range.
        """
        if not 0 <= action < self.num_actions:
            raise ValueError(
                f"Action {action} out of range [0, {self.num_actions})"
            )
        if self.B.ndim == 3:
            return self.B[:, :, action] @ q_s
        return self.B @ q_s

    # ------------------------------------------------------------------
    # Dunder helpers
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"GenerativeModel(obs={self.num_obs}, states={self.num_states}, "
            f"actions={self.num_actions})"
        )
