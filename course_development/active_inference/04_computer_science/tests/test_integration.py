"""Integration tests — end-to-end perception-action-learning loops.

Tests cross-module interactions using real computations (no mocks).
"""

import numpy as np
import pytest

from active_inference.agent.agent import ActiveInferenceAgent
from active_inference.agent.environment import DiscreteEnvironment
from active_inference.math.learning import (
    update_dirichlet_A, update_dirichlet_B, expected_A,
)
from active_inference.math.inference import run_state_inference, run_policy_inference


class TestPerceptionActionLoop:
    """Full perception-action loop integration tests."""

    def test_simple_loop_10_steps(self, simple_model):
        """Run 10 steps of perception-action loop."""
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)

        obs = env.reset(initial_state=0)
        for _ in range(10):
            action = agent.step(obs)
            obs = env.step(action)

        assert len(agent.history["observations"]) == 10
        assert len(env.history["actions"]) == 10

    def test_tmaze_loop(self, tmaze_model):
        """Run perception-action loop on T-maze."""
        np.random.seed(42)
        env = DiscreteEnvironment(tmaze_model.A, tmaze_model.B, initial_state=0)
        agent = ActiveInferenceAgent(tmaze_model, gamma=4.0)

        obs = env.reset(initial_state=0)
        for _ in range(5):
            action = agent.step(obs)
            obs = env.step(action)

        assert len(agent.history["observations"]) == 5


class TestLearningLoop:
    """Perception-action-learning loop tests."""

    def test_learning_improves_model(self, simple_model):
        """After learning, expected A should be more informative."""
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)
        pA = np.ones((2, 2))

        obs = env.reset(initial_state=0)
        for _ in range(30):
            action = agent.step(obs)
            pA = update_dirichlet_A(pA, obs, agent.q_s)
            obs = env.step(action)

        A_learned = expected_A(pA)
        assert A_learned.max() > 0.5  # more peaked than uniform

    def test_learning_B_matrix(self, simple_model):
        """B-matrix learning should track transitions."""
        np.random.seed(42)
        env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
        agent = ActiveInferenceAgent(simple_model, gamma=2.0)
        pB = np.ones((2, 2, 2))

        obs = env.reset(initial_state=0)
        prev_q = agent.q_s.copy()
        for _ in range(20):
            action = agent.step(obs)
            pB = update_dirichlet_B(pB, prev_q, agent.q_s, action)
            prev_q = agent.q_s.copy()
            obs = env.step(action)

        # pB should have accumulated counts beyond uniform
        assert pB.max() > 1.0


class TestStandaloneInference:
    """Tests for standalone inference functions in integration context."""

    def test_standalone_vs_agent_inference(self, simple_model):
        """Standalone state inference should match agent inference."""
        agent = ActiveInferenceAgent(simple_model, gamma=1.0)
        agent.infer_states(0)
        agent_beliefs = agent.q_s.copy()

        result = run_state_inference(
            prior=simple_model.D.copy(),
            observation=0,
            A=simple_model.A,
        )

        assert np.allclose(agent_beliefs, result["q_s"], atol=1e-6)

    def test_standalone_policy_inference(self, simple_model):
        """Standalone policy inference should return valid results."""
        result = run_state_inference(
            prior=simple_model.D.copy(),
            observation=0,
            A=simple_model.A,
        )
        policy_result = run_policy_inference(
            q_s=result["q_s"],
            A=simple_model.A,
            B=simple_model.B,
            C=simple_model.C,
            policies=[[0], [1]],
            gamma=2.0,
        )
        assert np.isclose(policy_result["q_pi"].sum(), 1.0)


class TestThreeStateModel:
    """Tests using the three_state_model fixture for broader coverage."""

    def test_loop_three_state(self, three_state_model):
        """Should work with 3-state models."""
        np.random.seed(42)
        env = DiscreteEnvironment(
            three_state_model.A, three_state_model.B, initial_state=0
        )
        agent = ActiveInferenceAgent(three_state_model, gamma=2.0)

        obs = env.reset(initial_state=0)
        for _ in range(10):
            action = agent.step(obs)
            obs = env.step(action)

        assert len(agent.history["observations"]) == 10
