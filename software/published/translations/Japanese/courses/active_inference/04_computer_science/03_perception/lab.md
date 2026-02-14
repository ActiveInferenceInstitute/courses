# Lab 03: State Estimationと信念更新

## 目的

A-行列の尤度を使用して信念更新を実装および可視化し、異なる観測ノイズレベルでの推論を比較し、収束挙動を分析します。

## 前提条件

- Lab 01–02 の完了
- ベイジアン推論と VFE の理解
- `active_inference` ライブラリへのアクセス

## 部門 1: 基本の状態推論

**目標**: 簡単な 2 状態システムで状態推論を実行し、事後分布を調べます。

1. 明確な A-行列 ($A = [[0.9, 0.1], [0.1, 0.9]]$) を持つ `GenerativeModel` を作成します。
2. 一様な事前分布と観測 $o = 0$ で `run_state_inference()` を実行します。
3. 事後分布、イテレーション数、および収束が達成されたかどうかを出力します。

```python
import numpy as np
from active_inference.agent import GenerativeModel
from active_inference.math import run_state_inference

# TODO: モデルを作成し、状態推論を実行する
# TODO: result["q_s"], result["converged"], result["num_iters"] を出力する
```

**応答**: {fill:textarea}

## 部門 2: 順序付き観測更新

**目標**: 複数の観測に対して信念を更新します。

1. 一様な事前分布 $q(s) = [0.5, 0.5]$ で開始します。
2. 観測シーケンス $[0, 0, 1, 0, 1, 1]$ を処理します。
3. 各観測の後に、事後分布を新しい事前分布として使用します。
4. `plot_beliefs()` を使用して信念軌跡を記録し、プロットします。

```python
from active_inference.visualization import plot_beliefs

beliefs_history = []
prior = model.D.copy()
for obs in [0, 0, 1, 0, 1, 1]:
    result = run_state_inference(prior=prior, observation=obs, A=model.A)
    prior = result["q_s"]
    beliefs_history.append(prior.copy())

plot_beliefs(beliefs_history, state_labels=["s0", "s1"],
             save_path="output/lab03_beliefs.png")
```

**応答**: {fill:textarea}

## 部門 3: ノイズ比較

**目標**: 異なる A-行列ノイズレベルでの推論を比較します。

1. 明瞭な ($0.95/0.05$）、中程度 ($0.75/0.25$）、ノイズ ($0.55/0.45$）の 3 つの A-行列を定義します。
2. 各行列に対して、同じ観測シーケンス $[0, 0, 0, 0, 0]$ で推論を実行します。
3. すべてのノイズレベルで、各観測後の事後分布 $q(s_0)$ を同じグラフにプロットします。

**応答**: {fill:textarea}

## 部門 4: 収束分析

**目標**: 推論の収束を視覚化および分析します。

1. 厳密な閾値 ($10^{-12}$) と最大 50 イテレーションで `run_state_inference()` を実行します。
2. `plot_convergence()` を使用して収束曲線を描画します。
3. ノイズのある A-行列を使用して繰り返すこと、および収束速度を比較します。

```python
from active_inference.visualization import plot_convergence

result = run_state_inference(
    prior=model.D.copy(), observation=0, A=model.A,
    num_iterations=50, convergence_threshold=1e-12,
)
plot_convergence(result["delta_history"], threshold=1e-12,
                 save_path="output/lab03_convergence.png")
```

**応答**: {fill:textarea}

## 部門 5: ライブエージェントでの予測誤差

**目標**: エージェントを実行し、予測誤差を調べます。

1. `ActiveInferenceAgent` と `DiscreteEnvironment` を作成します。
2. 20 ステップの知覚-行動ループを実行します。
3. 各ステップで、`agent.prediction_error(obs)` を計算し、保存します。
4. `plot_prediction_errors()` を使用して可視化します。

```python
from active_inference.visualization import plot_prediction_errors

# TODO: ループを実行し、観測と予測された観測を収集する
# TODO: plot_prediction_errors() を呼び出す
```

**応答**: {fill:textarea}

## 概要

| スキル | ライブラリコンポーネント | ステータス |
|-------|------------------|--------|
| 単独のステート推論を実行する | `run_state_inference()` | |
| 順序付き観測の信念を更新する | 事前チェーン | |
| 異なるノイズレベルでの推論を比較する | 変調された A-行列 | |
| 収束診断を視覚化する | `plot_convergence()` | |
| 予測誤差を計算し、プロットする | `agent.prediction_error()`、`plot_prediction_errors()` | |