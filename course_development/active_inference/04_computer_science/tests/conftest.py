"""Shared pytest fixtures for the Active Inference test suite.

Provides reusable model fixtures used across all per-module test files.
All fixtures use real matrix computations — no mocks.
"""

import numpy as np
import pytest
import sys
import os

# Add src to path so `import active_inference` works
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from active_inference.agent.generative_model import GenerativeModel  # noqa: E402


@pytest.fixture
def simple_model():
    """Simple 2-state, 2-obs, 2-action generative model.

    A — 90% accurate likelihood
    B — action 0 = stay, action 1 = swap
    C — prefer observation 0
    D — uniform prior
    """
    A = np.array([[0.9, 0.1],
                  [0.1, 0.9]])
    B = np.zeros((2, 2, 2))
    B[:, :, 0] = np.eye(2)
    B[:, :, 1] = np.array([[0, 1], [1, 0]])
    C = np.array([1.0, -1.0])
    D = np.array([0.5, 0.5])
    return GenerativeModel(A=A, B=B, C=C, D=D)


@pytest.fixture
def tmaze_model():
    """T-maze model: 4 states, 3 observations, 3 actions.

    States:       center, left, right, cue
    Observations: null, reward, no-reward
    Actions:      move-left, move-right, stay
    """
    A = np.array([
        [1.0, 0.0, 0.0, 1.0],
        [0.0, 0.8, 0.2, 0.0],
        [0.0, 0.2, 0.8, 0.0],
    ])
    B = np.zeros((4, 4, 3))
    B[1, 0, 0] = 1.0; B[1, 1, 0] = 1.0; B[2, 2, 0] = 1.0; B[3, 3, 0] = 1.0
    B[2, 0, 1] = 1.0; B[1, 1, 1] = 1.0; B[2, 2, 1] = 1.0; B[3, 3, 1] = 1.0
    B[:, :, 2] = np.eye(4)
    C = np.array([0.0, 2.0, -2.0])
    D = np.array([1.0, 0.0, 0.0, 0.0])
    return GenerativeModel(A=A, B=B, C=C, D=D)


@pytest.fixture
def three_state_model():
    """3-state, 3-obs, 2-action model for broader coverage.

    Provides a slightly more complex environment than simple_model.
    """
    A = np.array([
        [0.8, 0.1, 0.1],
        [0.1, 0.8, 0.1],
        [0.1, 0.1, 0.8],
    ])
    B = np.zeros((3, 3, 2))
    B[:, :, 0] = np.eye(3)
    B[:, :, 1] = np.array([
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ])
    C = np.array([2.0, 0.0, -1.0])
    D = np.array([1.0 / 3, 1.0 / 3, 1.0 / 3])
    return GenerativeModel(A=A, B=B, C=C, D=D)
