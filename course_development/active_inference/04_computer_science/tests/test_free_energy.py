"""Tests for free_energy.py — VFE, EFE, KL divergence, entropy, surprisal, MI.

Verifies mathematical properties (non-negativity, decompositions, bounds)
using real computations.  No mocks.
"""

import numpy as np
import pytest

from active_inference.math.free_energy import (
    softmax, entropy, kl_divergence,
    surprisal, mutual_information,
    compute_vfe, compute_vfe_components,
    compute_efe, compute_efe_components,
)


class TestSoftmax:
    """Tests for the softmax function σ(x)."""

    def test_normalisation(self):
        """Output must sum to 1."""
        assert np.isclose(softmax(np.array([1, 2, 3])).sum(), 1.0)

    def test_ordering_preserved(self):
        """Larger input → larger output."""
        r = softmax(np.array([1.0, 2.0, 3.0]))
        assert r[0] < r[1] < r[2]

    def test_high_temp_uniform(self):
        """High temperature → near-uniform."""
        r = softmax(np.array([1.0, 2.0, 3.0]), tau=100.0)
        assert np.allclose(r, 1 / 3, atol=0.05)

    def test_low_temp_peaked(self):
        """Low temperature → peaked at max."""
        r = softmax(np.array([1.0, 2.0, 3.0]), tau=0.01)
        assert r[2] > 0.99

    def test_constant_input_uniform(self):
        """Equal inputs → uniform output."""
        r = softmax(np.array([5.0, 5.0, 5.0]))
        assert np.allclose(r, 1 / 3, atol=1e-10)

    def test_numerical_stability_large(self):
        """Should not overflow with large values."""
        r = softmax(np.array([1000, 1001, 1002]))
        assert np.isclose(r.sum(), 1.0)


class TestEntropy:
    """Tests for Shannon entropy H(p)."""

    def test_uniform_is_maximum(self):
        """Uniform distribution has maximum entropy for given support."""
        uniform = np.array([0.25, 0.25, 0.25, 0.25])
        peaked = np.array([0.9, 0.05, 0.03, 0.02])
        assert entropy(uniform) > entropy(peaked)

    def test_deterministic_is_zero(self):
        """δ-distribution has zero entropy."""
        assert np.isclose(entropy(np.array([1.0, 0.0, 0.0])), 0.0, atol=1e-10)

    def test_binary_entropy_at_half(self):
        """H([0.5, 0.5]) = ln(2)."""
        assert np.isclose(entropy(np.array([0.5, 0.5])), np.log(2), atol=1e-10)

    def test_non_negative(self):
        """Entropy is always ≥ 0."""
        for _ in range(10):
            p = np.random.dirichlet(np.ones(5))
            assert entropy(p) >= -1e-10


class TestKLDivergence:
    """Tests for D_KL[q ‖ p]."""

    def test_same_dist_zero(self):
        """D_KL[p ‖ p] = 0."""
        p = np.array([0.3, 0.5, 0.2])
        assert np.isclose(kl_divergence(p, p), 0.0, atol=1e-10)

    def test_non_negative(self):
        """Gibbs' inequality: D_KL ≥ 0."""
        q = np.array([0.7, 0.2, 0.1])
        p = np.array([0.33, 0.33, 0.34])
        assert kl_divergence(q, p) >= 0

    def test_asymmetric(self):
        """D_KL[q ‖ p] ≠ D_KL[p ‖ q] in general."""
        q = np.array([0.7, 0.2, 0.1])
        p = np.array([0.33, 0.33, 0.34])
        assert not np.isclose(kl_divergence(q, p), kl_divergence(p, q))

    def test_known_value(self):
        """D_KL[[0.5, 0.5] ‖ [0.25, 0.75]] = known value."""
        q = np.array([0.5, 0.5])
        p = np.array([0.25, 0.75])
        expected = 0.5 * np.log(0.5 / 0.25) + 0.5 * np.log(0.5 / 0.75)
        assert np.isclose(kl_divergence(q, p), expected, atol=1e-10)


class TestSurprisal:
    """Tests for surprisal S(o)."""

    def test_non_negative(self, simple_model):
        """Surprisal is always ≥ 0."""
        q_s = np.array([0.5, 0.5])
        assert surprisal(0, simple_model.A, q_s) >= 0

    def test_likely_obs_low_surprisal(self, simple_model):
        """Likely observations should have lower surprisal."""
        q_s = np.array([0.99, 0.01])
        s0 = surprisal(0, simple_model.A, q_s)
        s1 = surprisal(1, simple_model.A, q_s)
        assert s0 < s1


class TestMutualInformation:
    """Tests for mutual information I(X; Y)."""

    def test_independent_zero(self):
        """MI = 0 for independent variables."""
        joint = np.array([[0.25, 0.25], [0.25, 0.25]])
        assert np.isclose(mutual_information(joint), 0.0, atol=1e-10)

    def test_perfectly_correlated(self):
        """MI = H(X) for perfectly correlated variables."""
        joint = np.array([[0.5, 0.0], [0.0, 0.5]])
        mi = mutual_information(joint)
        assert np.isclose(mi, np.log(2), atol=1e-10)

    def test_non_negative(self):
        """MI is always ≥ 0."""
        joint = np.array([[0.3, 0.1], [0.2, 0.4]])
        assert mutual_information(joint) >= -1e-10


class TestVFE:
    """Tests for Variational Free Energy F."""

    def test_finite_at_prior(self):
        """VFE should be finite when q(s) = D."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        D = np.array([0.5, 0.5])
        assert np.isfinite(compute_vfe(D, 0, A, D))

    def test_components_sum(self):
        """VFE components: F = complexity − accuracy."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        D = np.array([0.5, 0.5])
        q_s = np.array([0.7, 0.3])
        c = compute_vfe_components(q_s, 0, A, D)
        assert np.isclose(c["F"], c["complexity"] - c["accuracy"], atol=1e-10)

    def test_components_energy_entropy(self):
        """VFE = energy − entropy (decomposition 3)."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        D = np.array([0.5, 0.5])
        q_s = np.array([0.7, 0.3])
        c = compute_vfe_components(q_s, 0, A, D)
        assert np.isclose(c["F"], c["energy"] - c["entropy_q"], atol=1e-10)

    def test_vfe_matches_components(self):
        """compute_vfe and compute_vfe_components.F should match."""
        A = np.array([[0.9, 0.1], [0.1, 0.9]])
        D = np.array([0.5, 0.5])
        q_s = np.array([0.7, 0.3])
        F_scalar = compute_vfe(q_s, 0, A, D)
        F_dict = compute_vfe_components(q_s, 0, A, D)["F"]
        assert np.isclose(F_scalar, F_dict, atol=1e-10)


class TestEFE:
    """Tests for Expected Free Energy G."""

    def test_finite(self, simple_model):
        """EFE should be finite."""
        q_s = np.array([0.5, 0.5])
        g = compute_efe(q_s, simple_model.A, simple_model.B, simple_model.C, 0)
        assert np.isfinite(g)

    def test_components_sum(self, simple_model):
        """G = risk + ambiguity."""
        q_s = np.array([0.5, 0.5])
        c = compute_efe_components(q_s, simple_model.A, simple_model.B,
                                   simple_model.C, 0)
        assert np.isclose(c["G"], c["risk"] + c["ambiguity"], atol=1e-10)

    def test_efe_matches_components(self, simple_model):
        """compute_efe and compute_efe_components.G should match."""
        q_s = np.array([0.5, 0.5])
        G_scalar = compute_efe(q_s, simple_model.A, simple_model.B,
                               simple_model.C, 0)
        G_dict = compute_efe_components(q_s, simple_model.A, simple_model.B,
                                         simple_model.C, 0)["G"]
        assert np.isclose(G_scalar, G_dict, atol=1e-10)


class TestEFE2D:
    """Tests for EFE with 2D B-matrix (static/simple transition)."""

    def test_efe_2d_matrix(self):
        """Should handle 2D B-matrix (single action implicit)."""
        A = np.eye(2)
        B = np.eye(2)  # 2D transition
        C = np.zeros(2)
        q_s = np.array([0.9, 0.1])
        
        # scalars
        g = compute_efe(q_s, A, B, C, action=0)
        assert np.isfinite(g)

        # components
        comps = compute_efe_components(q_s, A, B, C, action=0)
        assert np.isfinite(comps["G"])
