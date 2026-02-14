# Lab 08: Deep Temporal Planning and Gridworlds

## Objective

マルチステップポリシーの評価を実行し、深層推論のためにMMPを実行し、長い時間軸の計画を持つグリッドワールドエージェントを構築します。

## Prerequisites

- Lab 01～07 の完了
- EFE の蓄積とマルチステップポリシーについての理解

## Part 1: Multi-Step Policy Evaluation

**Goal**: 予測された状態軌跡をアンロールすることで、マルチステップポリシーを評価します。

1. 2状態モデルを作成し、アイデンティティA、スワップまたはステイB、C = [2, -2]、一様Dを使用します。
2. ポリシーを定義します: `[[0, 0], [0, 1], [1, 0], [1, 1]]` (すべての2ステップの組み合わせ)。
3. 各ポリシーについて、ステップごとの $G_t$ の蓄積で合計 EFE を計算します。
4. 合計Gに基づいてポリシーをランク付けした表を出力します。

```python
from active_inference.math import compute_efe

policies = [[0, 0], [0, 1], [1, 0], [1, 1]]
for pi in policies:
    total_G = 0
    q = model.D.copy()
    for action in pi:
        G_t = compute_efe(q, model.A, model.B, model.C, action)
        total_G += G_t
        q = model.B[:, :, action] @ q
    print(f"Policy {pi}: G = {total_G:.4f}")
```

**Response**: {fill:textarea}

## Part 2: Marginal Message Passing

**Goal**: 3ステップの観察シーケンスに対してMMPを実行します。

1. Part 1 で使用したモデルを使用して、観察シーケンス [0, 1, 0] を作成します。
2. `run_mmp()` を 3ステップのポリシーとともに実行します。
3. 各時間点での信念を出力します。
4. `plot_convergence()` を使用して収束を視覚化します。

```python
from active_inference.math import run_mmp
from active_inference.visualization import plot_convergence

result = run_mmp(
    prior=model.D, observations=[0, 1, 0],
    A=model.A, B=model.B, policy=[0, 1, 0],
)

for t, beliefs in enumerate(result["beliefs"]):
    print(f"t={t}: q(s) = {beliefs}")

plot_convergence(result["delta_history"],
                 save_path="output/lab08_mmp_convergence.png")
```

**Response**: {fill:textarea}

## Part 3: Gridworld Environment

**Goal**: 4×4 グリッドワールドを作成し、視覚化します。

1. 16状態の環境（4×4 グリッドの平坦化）を作成します。
2. 4 つのアクション（上、下、左、右）を定義し、位置 (1,1) と (1,2) で壁を作成します。
3. C を状態 15（右下隅）を好むように設定します。
4. `plot_gridworld()` を使用して視覚化します。

**Response**: {fill:textarea}

## Part 4: Planning Agent on the Gridworld

**Goal**: グリッドワールド上でマルチステップポリシーを持つエージェントを実行します。

1. すべての 4³ = 64 個の可能な組み合わせのサブセットである 3ステップのポリシーを定義します。
2. これらのポリシーと γ = 4.0 を持つ `ActiveInferenceAgent` を作成します。
3. エージェントを 20 ステップ実行します。
4. `plot_gridworld()` を使用して、パスをオーバーレイした軌跡を視覚化します。

**Response**: {fill:textarea}

## Part 5: T-Maze with Temporal Depth

**Goal**: T-マズのパフォーマンスを T = 1 と T = 2 のポリシーで T = 1 と T = 2 のポリシーで比較します。

1. モジュール 05 から T-マズのモデルを設定します。
2. シングルステップポリシー（T = 1）で実行します：エージェントが報酬に到達する頻度はどれくらいですか？
3. 2ステップのポリシー（T = 2）を実行します：（例：[go-cue, go-left], [go-cue, go-right] など）。
4. 20 回の試行で成功率を比較します。

**Response**: {fill:textarea}

## Summary

| スキル | ライブラリコンポーネント | ステータス |
|-------|------------------|--------|
| マルチステップポリシーを評価する | `compute_efe()` を使用したループ、ポリシーアンロール | |
| 深層時間軸推論を実行する | `run_mmp()` | |
| グリッドワールド環境を構築する | `DiscreteEnvironment` とグリッド B行列 | |
| グリッドワールド上で計画エージェントを実行する | `ActiveInferenceAgent(policies=...)` | |
| 計画の深さを比較する | T=1 と T=2 ポリシーのパフォーマンス | |