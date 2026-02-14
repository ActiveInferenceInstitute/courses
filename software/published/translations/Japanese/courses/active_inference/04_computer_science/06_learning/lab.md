# Lab 06: パラメータ学習におけるディレクトリ更新

## 目的

オンラインパラメータ学習を実行し、真のモデルへの収束を追跡し、BMRを使用してモデルの品質を評価します。

## 前提条件

- Lab 01～05 の完了
- ディリクレ分布と共役事前分布の理解

## 第1部：ディリクレ濃度の初期化

**目標**: 2状態システムに対して pA および pB 事前濃度を設定します。

1. `DiscreteEnvironment` を既知の `true_A` および `true_B` で作成します。
2. `pA = np.ones((2, 2))` (一様ディリクレ事前分布) を初期化します。
3. `expected_A(pA)` を使用して初期期待される A 行列を計算します。
4. 各列について KL 分散を使用して `true_A` と比較します。

```python
import numpy as np
from active_inference.math import expected_A, kl_divergence

pA = np.ones((2, 2))
A_initial = expected_A(pA)

for s in range(2):
    kl = kl_divergence(A_initial[:, s], true_A[:, s])
    print(f"初期 KL for state {s}: {kl:.4f}")
```

**応答**: {fill:textarea}

## 第2部：オンライン学習ループ

**目標**: 認識と行動の学習を100ステップ実行し、モデルの収束を追跡します。

1. 初期期待される A 行列を持つエージェントを作成します。
2. 各ステップにおいて：状態を推論し、行動を選択し、pA を更新し、pB を更新し、期待される行列を再計算します。
3. `expected_A(pA)` と `true_A` の間の KL 分散を各ステップで記録します。

```python
from active_inference.math import update_dirichlet_A, update_dirichlet_B, expected_B

kl_history = []
for t in range(100):
    action = agent.step(obs)
    pA = update_dirichlet_A(pA, obs, agent.q_s, learning_rate=1.0)
    agent.model.A = expected_A(pA)
    obs = env.step(action)
    # TODO: update pB, compute KL, append to kl_history
```

**応答**: {fill:textarea}

## 第3部：学習進捗の可視化

**目標**: 学習曲線と初期値と学習された行列の比較をプロットします。

1. `plot_learning_progress()` を使用して、時間の経過に伴う KL 分散をプロットします。
2. `plot_dirichlet_concentration()` を使用して、初期値と最終的な pA をプロットします。
3. `plot_A_matrix()` を使用して、最終的な期待される A 行列をプロットします。

```python
from active_inference.visualization import (
    plot_learning_progress, plot_dirichlet_concentration, plot_A_matrix
)

plot_learning_progress(kl_history, save_path="output/lab06_learning.png")
```

**応答**: {fill:textarea}

## 第4部：複数エピソードのトレーニング

**目標**: 50ステップの5エピソードを実行し、エピソード間で pA を累積します。

1. 各エピソードの後に、環境とエージェントの信念をリセットしますが、pA は保持します。
2. 各エピソード中の平均 KL 分散を記録します。
3. 平均 KL 分散をエピソードごとに示す棒グラフを作成します。

**応答**: {fill:textarea}

## 第5部：ベイズモデル削減

**目標**: BMRを使用して、学習されたモデルを削減されたモデルと比較します。

1. 100ステップの学習後に、`bayesian_model_reduction(pA_learned, pA_reduced)` を計算します。
2. `pA_reduced` に対して、小さな対角成分の濃度を 0.1 に設定します (疎なモデル)。
3. 削減されたモデルの好みを報告し、解釈します。

```python
from active_inference.math import bayesian_model_reduction

pA_reduced = pA.copy()
pA_reduced[0, 1] = 0.1  # reduce off-diagonal
pA_reduced[1, 0] = 0.1

delta_F = bayesian_model_reduction(pA, pA_reduced)
print(f"ΔF = {delta_F:.4f} → {'Reduced preferred' if delta_F < 0 else 'Full preferred'}")
```

**応答**: {fill:textarea}

## 概要

| スキル | ライブラリコンポーネント | ステータス |
|---|---|---|
| ディリクレ濃度の事前分布の初期化 | `pA = np.ones(...)`, `expected_A()` | |
| 各ステップで pA/pB を更新 | `update_dirichlet_A()`, `update_dirichlet_B()` | |
| 学習収束の追跡 | KL 分散, `plot_learning_progress()` | |
| 複数エピソードのトレーニングの実行 | エピソードごとの pA の累積 | |
| BMR を使用したモデル評価 | `bayesian_model_reduction()` | |