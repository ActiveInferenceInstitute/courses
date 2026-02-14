# モジュール 08: 計画 — 深い時間的モデルと長期間の推論

## 学習目標

1. EFE 計算を T の深さを持つ多段階ポリシーに拡張する。
2. `run_mmp()` を使用して、深い時間的推論のためのマルギナルメッセージ伝播 (MMP) を実装する。
3. 長期間の計画を備えたグリッドワールド環境を構築およびシミュレートする。

## 導入

モジュール 01 ～ 07 では、エージェントはシングルステップまたは短期間のスケールで動作していました。 実際の問題では、**計画** が必要であり、多くの将来のステップに及ぶアクションシーケンスを評価する必要があります。 深い時間的モデルは、複数の時間点で状態に関する信念を維持し、アクションシーケンス全体にわたる EFE の累積によってポリシーを評価します。

## 主要な概念

### 1. 多段階ポリシー

$\pi = [a_0, a_1, \ldots, a_{T-1}]$ は、T 個の将来のタイムステップにおけるアクションを指定するポリシーです。 エージェントは、予測された状態軌跡をアンロールすることで、各ポリシーを評価します。

$$q(s_{\tau+1} \mid \pi) = \mathbf{B}_{a_\tau} \cdot q(s_\tau \mid \pi) \quad \text{for } \tau = 0, \ldots, T-1$$

EFE はすべてのステップに累積されます。

$$G(\pi) = \sum_{\tau=0}^{T-1} G_\tau(\pi)$$

```python
# 3アクションシステム用の多段階ポリシーを定義
policies = [
    [0, 0, 0],  # stay, stay, stay
    [1, 0, 0],  # left, stay, stay
    [1, 2, 0],  # left, right, stay
    [2, 1, 0],  # right, left, stay
]

agent = ActiveInferenceAgent(model, gamma=4.0, policies=policies)
```

### 2. マルギナルメッセージ伝播 (MMP)

深い時間的モデルの場合、`run_mmp()` は複数の時間点で信念を同時に推論します。 $q(s_t)$ の推論だけでなく、$\tau \in \{0, 1, \ldots, T\}$ の範囲の $q(s_\tau)$ を推論します。

```python
from active_inference.math import run_mmp

result = run_mmp(
    prior=model.D,
    observations=[0, 1, 0],     # 過去の観測のシーケンス
    A=model.A,
    B=model.B,
    policy=[1, 0, 1],           # アクションシーケンス
    num_iterations=16,
)

print(result["beliefs"])         # 各タイムステップの信念ベクトルのリスト
print(result["converged"])       # 収束ステータス
print(result["delta_history"])   # 収束トレース
```

MMP は、各タイムステップで信念を改善するために、先行 (prior × 遷移) と後方 (尤度) の両方でメッセージを伝播します。

### 3. 時間的深さ T

時間的深さ $T$ は、エージェントが計画する先をどれだけ進めるかを制御します。

| T | 行動 |
|---|----------|
| T = 1 | 反応型 — 次のステップのみを考慮する (モジュール 01–05) |
| T = 2–3 | 短期間 — アクションのシーケンスを実行できる (例: go-to-cue、その後 go-to-reward) |
| T = 5+ | 深い計画 — グリッドワールドをナビゲートし、遅延した報酬を処理できる |

**トレードオフ**: より大きな T はより良い計画を提供しますが、可能なポリシーの数 (N\_a^T for N\_a 行動) を指数関数的に増加させます。

### 4. グリッドワールドの実装

グリッドワールドは計画の自然なテストベッドです。 グリッドワールドには：

- $N \times M$ の状態のグリッド (フラット化された $N \cdot M$ 状態)
- 4 または 5 のアクション (上、下、左、右、待機)
- 壁/障害物がモデルの B 矩阵 (ブロックされた移動に対する自己遷移) にエンコードされている
- 優先観察される目標状態

```python
from active_inference.visualization import plot_gridworld

# 4x4 グリッドワールドを視覚化
grid = np.zeros((4, 4))
obstacles = [(1, 1), (1, 2)]
path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
goal = (3, 3)

plot_gridworld(grid, obstacles=obstacles, path=path, goal=goal,
               save_path="output/lab08_gridworld.png")
```

### 5. T-迷路における遅延報酬

時間的深さ T を備えた T-迷路は、計画の力を示します。

- **T = 1**: エージェントは cue-then-reward のシーケンスを実行できません。 ランダムに選択します。
- **T = 2–3**: エージェントは計画できます: 最初に cue に移動し、次に reward 腕に移動します。 cue 訪問はステップ 1 での曖昧さを減らし、ステップ 2 でリスクを最小化する選択を可能にします。

### 6. 深いモデルに対するポリシー評価

深いモデルの場合、各ポリシーの EFE は次のステップの合計です。

```python
from active_inference.math import compute_efe

total_G = 0
q_current = agent.q_s.copy()
for t, action in enumerate(policy):
    G_t = compute_efe(q_current, model.A, model.B, model.C, action)
    total_G += G_t
    q_current = model.B[:, :, action] @ q_current  # 次の状態を予測
```

### 7. シミュレーションダッシュボード

`plot_simulation_dashboard()` 関数は、完全なシミュレーションの 5 パネルの概要を提供します。

```python
from active_inference.visualization import plot_simulation_dashboard

plot_simulation_dashboard(
    beliefs_history=agent.history["beliefs"],
    vfe_history=agent.history["vfe"],
    observations=env.history["observations"],
    predictions=[model.A @ b for b in agent.history["beliefs"]],
    efe_history=agent.history.get("efe", []),
    save_path="output/lab08_dashboard.png",
)
```

## 応用

- **ロボットナビゲーション**: グリッドワールド計画は、物理ナビゲーションタスクに直接対応します。
- **遅延した報酬**: 将来のより大きな報酬のために、即時の報酬を先延ばしにできるエージェント。
- **階層的な計画**: 複数の時間的深さにより、抽象的な計画 (目標) と具体的なアクションが可能です。

## 結論

計画は、Active Inference を反応型から思索的な行動へと拡張します。 EFE を累積して多段階ポリシーを評価し、深い状態推論のための MMP を使用することで、遅延した報酬と長い時間的範囲を処理できるエージェントになります。 これにより、Computational Active Inference の 8 モジュールコースが完了します—システムとエージェントから、知覚、認知、行動、学習、コミュニケーション、計画まで。