"""Output test suite — generates 32 visualization figures + data to output/.

Includes raw data export (CSV/JSON) for every figure to support verification.
Re-ordered to match the curriculum flow:
- 01-09: Systems & Generative Models
- 10-19: Perception & Cognition (Inference)
- 20-29: Action & Learning
- 30+:   Planning & Integrated Simulation
"""

import os
import json
import numpy as np
import pytest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Package imports ───────────────────────────────────────────────────
from active_inference.visualization.config import configure, get_config
from active_inference.agent.generative_model import GenerativeModel
from active_inference.agent.agent import ActiveInferenceAgent
from active_inference.agent.environment import DiscreteEnvironment
from active_inference.math.free_energy import (
    compute_vfe, compute_vfe_components, compute_efe_components, softmax,
)
from active_inference.math.inference import run_state_inference
from active_inference.math.learning import (
    update_dirichlet_A, update_dirichlet_B,
)
from active_inference.visualization import (
    plot_beliefs, plot_free_energy, plot_prediction_errors,
    plot_policy_values, plot_efe_decomposition, plot_learning_progress,
    plot_matrix_heatmap, plot_A_matrix, plot_B_matrix,
    plot_C_preferences, plot_D_prior, plot_E_habits,
    plot_model_summary, plot_B_transition_graph, plot_dirichlet_concentration,
    plot_convergence, plot_vfe_components, plot_efe_components,
    plot_precision_sweep, plot_entropy_trajectory, plot_surprise_trajectory,
    plot_dirichlet_learning, plot_bmr_results,
    plot_simulation_dashboard, plot_environment_trajectory,
    plot_agent_vs_environment, plot_tmaze, plot_gridworld,
)


# ── Constants ─────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "output"
)


# ── Helpers ───────────────────────────────────────────────────────────

def _save_output(name: str, fig: plt.Figure, data: dict = None):
    """Save figure (PNG) and companion data (CSV/JSON)."""
    # 1. Save Figure
    fig_path = os.path.join(OUTPUT_DIR, f"{name}.png")
    fig.savefig(fig_path, bbox_inches="tight")
    plt.close(fig)

    if data is None:
        return

    # 2. Separate arrays (CSV) from metadata (JSON)
    metadata = {}
    
    for key, value in data.items():
        # Handle NumPy arrays -> CSV
        if isinstance(value, np.ndarray):
            csv_path = os.path.join(OUTPUT_DIR, f"{name}_{key}.csv")
            # Flatten >2D arrays for CSV saving, or keep 1D/2D
            if value.ndim <= 2:
                np.savetxt(csv_path, value, delimiter=",", fmt="%.4f")
            else:
                # Save 3D+ arrays as flattened 2D for simplicity or separate files
                # For this curriculum, mostly saving slices or flattened is fine
                # Squelch complex shapes to flattened
                np.savetxt(csv_path, value.reshape(value.shape[0], -1), delimiter=",", fmt="%.4f")
                metadata[f"{key}_shape"] = value.shape
        
        # Handle Lists of arrays (e.g. histories) -> CSV (stacked)
        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], np.ndarray):
            csv_path = os.path.join(OUTPUT_DIR, f"{name}_{key}.csv")
            try:
                # stack row-wise
                arr = np.array(value)
                if arr.ndim <= 2:
                    np.savetxt(csv_path, arr, delimiter=",", fmt="%.4f")
                else:
                    np.savetxt(csv_path, arr.reshape(arr.shape[0], -1), delimiter=",", fmt="%.4f")
                    metadata[f"{key}_shape"] = arr.shape
            except ValueError:
                # Jagged arrays or incompatible shapes
                metadata[key] = "Jagged array list (not saved as CSV)"

        # Handle scalars/strings/lists-of-scalars -> JSON
        else:
            # Convert numpy scalars to native python types for JSON serialization
            if isinstance(value, (np.integer, np.floating)):
                metadata[key] = value.item()
            elif isinstance(value, np.ndarray): # scalar array
                metadata[key] = value.item()
            else:
                metadata[key] = value

    # 3. Save Metadata JSON
    if metadata:
        json_path = os.path.join(OUTPUT_DIR, f"{name}_meta.json")
        with open(json_path, "w") as f:
            json.dump(metadata, f, indent=2)


# ── Fixtures ──────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def _setup_output():
    """Configure visualisation to output to the project output/ dir."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    configure(output_dir=OUTPUT_DIR, dpi=150, save_format="png")
    yield
    plt.close("all")


@pytest.fixture
def tmaze_model():
    """Analytically accurate T-maze generative model."""
    A = np.array([
        [1.0, 0.0, 1.0, 0.0],   # o=nothing
        [0.0, 1.0, 0.0, 0.0],   # o=reward
        [0.0, 0.0, 0.0, 1.0],   # o=cue_signal
    ])
    B = np.zeros((4, 4, 4))
    B[:, :, 0] = np.eye(4) # stay
    B[:, :, 1] = np.eye(4); B[1, 0, 1] = 1.0; B[0, 0, 1] = 0.0; B[1, 3, 1] = 1.0; B[3, 3, 1] = 0.0 # left
    B[:, :, 2] = np.eye(4); B[2, 0, 2] = 1.0; B[0, 0, 2] = 0.0; B[2, 3, 2] = 1.0; B[3, 3, 2] = 0.0 # right
    B[:, :, 3] = np.eye(4); B[3, 0, 3] = 1.0; B[0, 0, 3] = 0.0 # cue
    
    C = np.array([0.0, 2.0, 0.5])
    D = np.array([1.0, 0.0, 0.0, 0.0])
    return GenerativeModel(A=A, B=B, C=C, D=D)


@pytest.fixture
def simple_model():
    """Minimal 2-state, 2-obs model."""
    A = np.array([[0.9, 0.1], [0.1, 0.9]])
    B = np.zeros((2, 2, 2))
    B[:, :, 0] = np.eye(2)
    B[:, :, 1] = np.array([[0, 1], [1, 0]])
    C = np.array([1.0, -1.0])
    D = np.array([0.5, 0.5])
    return GenerativeModel(A=A, B=B, C=C, D=D)


@pytest.fixture
def sim_data(simple_model):
    """Run a 15-step simulation."""
    np.random.seed(42)
    env = DiscreteEnvironment(simple_model.A, simple_model.B, initial_state=0)
    agent = ActiveInferenceAgent(simple_model, gamma=4.0)
    obs = env.reset(initial_state=0)
    for _ in range(15):
        action = agent.step(obs)
        obs = env.step(action)
    return {"agent": agent, "env": env, "model": simple_model}


# =====================================================================
# 1. SYSTEMS & GENERATIVE MODELS (01-09)
# =====================================================================

class TestGroup01_Systems:
    
    def test_01_model_summary(self, tmaze_model):
        """Generative model overview."""
        name = "01_model_summary"
        fig = plot_model_summary(
            tmaze_model,
            obs_labels=["Nothing", "Reward", "Cue"],
            state_labels=["Center", "Left", "Right", "Cue"],
            title="T-Maze Generative Model Summary"
        )
        _save_output(name, fig, {
            "num_states": 4, "num_obs": 3, "num_actions": 4
        })

    def test_02_A_matrix(self, tmaze_model):
        """Likelihood matrix."""
        name = "02_A_matrix"
        fig = plot_A_matrix(
            tmaze_model,
            obs_labels=["Nothing", "Reward", "Cue"],
            state_labels=["Center", "Left", "Right", "Cue"],
            title="A-Matrix: P(o|s)"
        )
        _save_output(name, fig, {"A": tmaze_model.A})

    def test_03_B_matrix(self, tmaze_model):
        """Transition dynamics."""
        name = "03_B_matrix_grid"
        fig = plot_B_matrix(
            tmaze_model,
            state_labels=["Ctr", "L", "R", "Cue"],
            action_labels=["Stay", "Left", "Right", "Cue"],
            title="B-Matrix Grid"
        )
        _save_output(name, fig, {"B": tmaze_model.B})

    def test_04_transition_graph(self, tmaze_model):
        """Graph view of dynamics."""
        name = "04_transition_graph"
        fig = plot_B_transition_graph(
            tmaze_model, action=1,
            state_labels=["Center", "Left", "Right", "Cue"],
            title="Transition Graph (a=go_left)"
        )
        _save_output(name, fig, {"action_idx": 1, "action_name": "go_left"})

    def test_05_C_vector(self, tmaze_model):
        """Preferences."""
        name = "05_C_preferences"
        fig = plot_C_preferences(
            tmaze_model,
            obs_labels=["Nothing", "Reward", "Cue"],
            title="C-Vector Preferences"
        )
        _save_output(name, fig, {"C": tmaze_model.C})

    def test_06_D_vector(self, tmaze_model):
        """Priors."""
        name = "06_D_prior"
        fig = plot_D_prior(
            tmaze_model,
            state_labels=["Center", "Left", "Right", "Cue"],
            title="D-Vector Prior"
        )
        _save_output(name, fig, {"D": tmaze_model.D})

    def test_07_E_vector(self, tmaze_model):
        """Habits."""
        name = "07_E_habits"
        tmaze_model.E = np.array([0.4, 0.3, 0.2, 0.1])
        fig = plot_E_habits(
            tmaze_model,
            policy_labels=["Stay", "Go Left", "Go Right", "Go Cue"],
            title="E-Vector Habits"
        )
        _save_output(name, fig, {"E": tmaze_model.E})

    def test_08_tmaze_env(self):
        """Environment Layout."""
        name = "08_tmaze_env"
        fig = plot_tmaze(
            agent_state=0, reward_location="left",
            state_labels=["Center", "Left", "Right", "Cue"],
            title="T-Maze Environment"
        )
        _save_output(name, fig, {"agent_state": 0, "reward_side": "left"})

    def test_09_gridworld_env(self):
        """Gridworld Layout."""
        name = "09_gridworld_env"
        grid_shape = (5, 5)
        obstacles = [(1, 1), (1, 2), (2, 3), (3, 1)]
        path_example = [(0, 0), (0, 1), (0, 2)]
        fig = plot_gridworld(
            grid_shape=grid_shape, agent_pos=(0, 0), goal_pos=(4, 4),
            obstacles=obstacles, path=path_example,
            title="Gridworld Environment"
        )
        _save_output(name, fig, {
            "grid_h": 5, "grid_w": 5, "obstacles": obstacles
        })


# =====================================================================
# 2. PERCEPTION & COGNITION (10-19)
# =====================================================================

class TestGroup10_Perception:

    def test_10_beliefs(self, sim_data):
        """Belief traces."""
        name = "10_beliefs"
        fig = plot_beliefs(
            sim_data["agent"].history["beliefs"],
            state_labels=["Safe", "Risky"],
            title="Belief Trajectories"
        )
        _save_output(name, fig, {
            "beliefs": sim_data["agent"].history["beliefs"]
        })

    def test_11_vfe_trajectory(self, sim_data):
        """VFE Minimization."""
        name = "11_vfe_trajectory"
        fig = plot_free_energy(
            sim_data["agent"].history["vfe"],
            title="Variational Free Energy"
        )
        _save_output(name, fig, {
            "vfe": sim_data["agent"].history["vfe"]
        })

    def test_12_vfe_decomposition(self, simple_model):
        """Complexity vs Accuracy."""
        name = "12_vfe_decomposition"
        A = simple_model.A
        D = np.array([0.8, 0.2])
        obs_seq = [0, 0, 1, 1, 0, 1]
        comps = []
        q_s = D.copy()
        
        for o in obs_seq:
            res = run_state_inference(q_s, o, A, num_iterations=3)
            q_s = res["q_s"]
            comps.append(compute_vfe_components(q_s, o, A, D))
            
        fig = plot_vfe_components(comps, title="VFE Decomposition")
        
        # Export component timeseries
        data_export = {
            "F": [c["F"] for c in comps],
            "complexity": [c["complexity"] for c in comps],
            "accuracy": [c["accuracy"] for c in comps],
        }
        _save_output(name, fig, data_export)

    def test_13_prediction_errors(self, sim_data):
        """Predictive Coding errors."""
        name = "13_prediction_errors"
        agent = sim_data["agent"]
        model = sim_data["model"]
        preds = [model.A @ q for q in agent.history["beliefs"]]
        
        fig = plot_prediction_errors(
            agent.history["observations"], preds,
            title="Prediction Errors"
        )
        _save_output(name, fig, {
            "observations": agent.history["observations"],
            "predictions": preds
        })

    def test_14_surprisal(self, sim_data):
        """Information theoretic surprise."""
        name = "14_surprisal"
        agent = sim_data["agent"]
        fig = plot_surprise_trajectory(
            agent.history["observations"],
            sim_data["model"].A,
            agent.history["beliefs"],
            title="Surprisal S(o)"
        )
        _save_output(name, fig, {"observations": agent.history["observations"]})

    def test_15_entropy(self, sim_data):
        """Uncertainty reduction."""
        name = "15_entropy"
        fig = plot_entropy_trajectory(
            sim_data["agent"].history["beliefs"],
            title="Belief Entropy H[q]"
        )
        # Calculate entropies for export
        entropies = [sum(-q*np.log(q+1e-16)) for q in sim_data["agent"].history["beliefs"]]
        _save_output(name, fig, {"entropy": np.array(entropies)})

    def test_16_convergence(self, simple_model):
        """Inference loop convergence."""
        name = "16_convergence"
        res = run_state_inference(simple_model.D, 0, simple_model.A, num_iterations=16)
        fig = plot_convergence(
            res["delta_history"],
            title="Inference Convergence"
        )
        _save_output(name, fig, {"deltas": np.array(res["delta_history"])})


# =====================================================================
# 3. ACTION & LEARNING (20-29)
# =====================================================================

class TestGroup20_ActionLearning:

    def test_20_policy_efe(self, sim_data):
        """EFE values over time."""
        name = "20_policy_efe"
        agent = sim_data["agent"]
        model = sim_data["model"]
        
        # Recompute EFEs for export
        efe_trace = []
        for q in agent.history["beliefs"][:5]:
            p_efes = [compute_efe_components(q, model.A, model.B, model.C, a)["G"] for a in range(model.num_actions)]
            efe_trace.append(p_efes)
            
        fig = plot_policy_values(efe_trace, title="Policy EFE Values")
        _save_output(name, fig, {"efe_values": efe_trace})

    def test_21_efe_decomposition(self, simple_model):
        """Risk vs Ambiguity."""
        name = "21_efe_decomposition"
        q_seq = [np.array([0.9, 0.1]), np.array([0.5, 0.5]), np.array([0.1, 0.9])]
        risks, ambigs = [], []
        for q in q_seq:
            c = compute_efe_components(q, simple_model.A, simple_model.B, simple_model.C, 0)
            risks.append(c["risk"]); ambigs.append(c["ambiguity"])
            
        fig = plot_efe_decomposition(risks, ambigs, title="EFE Decomposition")
        _save_output(name, fig, {"risk": risks, "ambiguity": ambigs})

    def test_22_efe_components_detail(self, simple_model):
        """Detailed stack plot."""
        name = "22_efe_components"
        # Similar data to above but structured for component plot
        comps = []
        for q in [np.array([0.9, 0.1]), np.array([0.5, 0.5])]:
            comps.append(compute_efe_components(q, simple_model.A, simple_model.B, simple_model.C, 0))
            
        fig = plot_efe_components(comps, title="EFE Component Details")
        _save_output(name, fig, {
            "G": [c["G"] for c in comps],
            "risk": [c["risk"] for c in comps]
        })

    def test_23_precision_gamma(self):
        """Softmax temperature."""
        name = "23_precision_gamma"
        gammas = [0.5, 1.0, 4.0, 16.0]
        efe = np.array([-1.0, -0.5])
        q_pi = np.array([softmax(efe, tau=1/g) for g in gammas])
        
        fig = plot_precision_sweep(gammas, q_pi, policy_labels=["A", "B"], title="Precision Gamma Sweep")
        _save_output(name, fig, {"gammas": gammas, "q_pi": q_pi})

    def test_24_learning_trajectory(self, simple_model):
        """Dirichlet updates."""
        name = "24_learning_trajectory"
        pA = np.ones((2, 2))
        hist = [pA.copy()]
        # Fake learning trace
        for i in range(10):
            pA[0, 0] += 0.5
            hist.append(pA.copy())
            
        fig = plot_dirichlet_learning(hist, true_A=simple_model.A, title="Learning Convergence")
        # Save just the (0,0) element evolution for brevity in CSV
        pA00 = [h[0,0] for h in hist]
        _save_output(name, fig, {"pA_00_trace": np.array(pA00)})

    def test_25_learning_concentrations(self):
        """Before/After concentrations."""
        name = "25_learning_concentrations"
        pA_prior = np.ones((3, 3))
        pA_post = pA_prior + np.eye(3) * 5
        
        fig = plot_dirichlet_concentration(
            pA_post, pA_prior=pA_prior, 
            row_labels=["O1","O2","O3"], col_labels=["S1","S2","S3"],
            title="Learned Concentrations"
        )
        _save_output(name, fig, {"pA_posterior": pA_post})

    def test_26_learning_curve(self):
        """KL divergence decrease."""
        name = "26_learning_curve"
        kl = [1.0 * (0.8**t) for t in range(10)]
        fig = plot_learning_progress(kl, title="KL Divergence Learning Curve")
        _save_output(name, fig, {"D_KL": np.array(kl)})

    def test_27_bmr_comparison(self):
        """Model Reduction."""
        name = "27_bmr_comparison"
        dF = np.array([1.5, -0.2, 0.8])
        prune = dF > 0
        fig = plot_bmr_results(dF, prune, state_labels=["S1","S2","S3"], title="BMR Pruning")
        _save_output(name, fig, {"delta_F": dF, "should_prune": prune.astype(int)})


# =====================================================================
# 4. PLANNING & SIMULATION (30+)
# =====================================================================

class TestGroup30_Simulation:

    def test_30_simulation_dashboard(self, tmaze_model):
        """Integrated dashboard."""
        name = "30_simulation_dashboard"
        np.random.seed(99)
        env = DiscreteEnvironment(tmaze_model.A, tmaze_model.B, initial_state=0)
        agent = ActiveInferenceAgent(tmaze_model, gamma=4.0)
        obs = env.reset(0)
        for _ in range(10):
            obs = env.step(agent.step(obs))
            
        fig = plot_simulation_dashboard(
            agent.history["beliefs"], agent.history["vfe"],
            agent.history["observations"], agent.history["actions"],
            env.history["states"], state_labels=["C","L","R","Cue"],
            title="Simulation Dashboard"
        )
        _save_output(name, fig, {
            "actions": agent.history["actions"],
            "observations": agent.history["observations"],
            "states_true": env.history["states"]
        })

    def test_31_env_trajectory(self, sim_data):
        """Environment states."""
        name = "31_env_trajectory"
        env = sim_data["env"]
        fig = plot_environment_trajectory(
            env.history["states"], [], [], title="Environment States"
        )
        _save_output(name, fig, {"states": env.history["states"]})

    def test_32_agent_performance(self, sim_data):
        """Accuracy check."""
        name = "32_agent_performance"
        agent = sim_data["agent"]
        env = sim_data["env"]
        fig = plot_agent_vs_environment(
            agent.history["beliefs"], env.history["states"],
            title="Agent Accuracy"
        )
        _save_output(name, fig, {"accuracy_plot": "generated"})

