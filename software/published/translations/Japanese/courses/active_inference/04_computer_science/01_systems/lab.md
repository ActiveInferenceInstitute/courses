# Lab 01: 離散環境の構築と探索

## 目的

`DiscreteEnvironment` をゼロから構築し、その中をステップごとに進み、軌跡を記録し、生成過程を視覚化する。

## 前提条件

- NumPy と matplotlib がインストールされた Python
- 確率分布と行列表記に関する知識
- `active_inference` ライブラリへのアクセス (`src/active_inference/`)

## Part 1: 環境の構築

**目標**: 3状態、2観察状態の環境を2つの行動で作成する。

1. 形状 `(2, 3)` の `true_A` 行列を定義する。ここで：
   - 状態 0 は観察 0 を確率 0.8 で生成する
   - 状態 1 は各観察を等しい確率で生成する
   - 状態 2 は観察 1 を確率 0.9 で生成する

2. 形状 `(3, 3, 2)` の `true_B` テンソルを定義する。ここで：
   - 行動 0 はアイデンティティ（現在の状態を維持）
   - 行動 1 は回転：状態 0 → 1、状態 1 → 2、状態 2 → 0

3. 状態 0 から開始する `DiscreteEnvironment` を作成する。

```python
import numpy as np
from active_inference.agent import DiscreteEnvironment

# TODO: true_A と true_B を定義
# TODO: 環境を作成
```

**Response**: {}

## Part 2: 軌跡の実行

**目標**: 固定された行動シーケンスで環境を 20 回ステップする。

1. 環境を状態 0 にリセットする。
2. 20 回ステップごとに行動 0 (維持) と行動 1 (回転) を交互に行う。
3. 各ステップで状態、観察、行動を記録する。
4. 軌跡全体を出力する。

```python
env.reset(initial_state=0)
for t in range(20):
    action = t % 2  # alternate stay/rotate
    obs = env.step(action)
    print(f"t={t}: action={action}, state={env.state}, obs={obs}")
```

**Response**: {}

## Part 3: 軌跡の視覚化

**目標**: `plot_environment_trajectory` を使用して、状態-観察-行動シーケンスを視覚化する。

1. Part 2 を実行した後、`env.history` から状態、観察を抽出する。
2. `plot_environment_trajectory` を呼び出して、図を作成する。
3. 図を `output/lab01_trajectory.png` に保存する。

```python
from active_inference.visualization import plot_environment_trajectory

plot_environment_trajectory(
    states=env.history["states"],
    observations=env.history["observations"],
    save_path="output/lab01_trajectory.png",
)
```

**Response**: {}

## Part 4: 経験的尤度推定

**目標**: `true_A` 行列を収集した観察で検証する。

1. 環境をリセットする。行動 0 (アイデンティティ) を使用して既知の開始状態から状態を固定する。
2. 各状態から 1000 個の観察を収集する (各状態にリセットし、アイデンティティの行動で 1000 回ステップする)。
3. 各状態あたりの観察の経験的頻度を計算する。
4. 元の `true_A` 行列と比較する。

**Response**: {}

## Part 5: 分析問題

1. 20 回ステップで交互に行動を行った場合、軌跡が訪問したユニークな状態はいくつでしたか？これは `true_B` 行列から予測可能でしたか？

2. Part 4 で計算された経験的尤度推定値は、真の値に収束しましたか？ 2 桁の精度を得るために必要なサンプル数はいくつでしたか？

3. `true_A = np.eye(3, 2).T` (非正方形のアイデンティティのような行列) を使用した場合、何が変わりますか？環境は依然として有効ですか？

**Response**: {}

## Summary

| スキル | ライブラリコンポーネント | ステータス |
|-------|------------------|--------|
| カスタム A および B 行列で環境を作成 | `DiscreteEnvironment(true_A, true_B)` | |
| 環境をステップし、軌跡を収集 | `env.step(action)`, `env.history` | |
| 状態-観察軌跡を視覚化 | `plot_environment_trajectory()` | |
| 経験的に尤度行列を検証 | 手動で頻度をカウント vs `true_A` | |
| 生成プロセス抽象を理解 | 生成的モデル ≠ 生成的プロセス | |