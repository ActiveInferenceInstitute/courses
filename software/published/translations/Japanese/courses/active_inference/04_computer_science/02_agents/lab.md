Okay, here's the translation of the provided text into Japanese, maintaining all markdown formatting, links, and code blocks exactly as they are.

# Lab 02: Active Inference Agent を構築する

## 目的

`GenerativeModel` (A-E行列) を完成させ、`ActiveInferenceAgent` を作成し、`DiscreteEnvironment` に対して知覚-行動ループを実行する。

## 前提条件

- Lab 01 (Systems) を完了する。
- 確率分布、行列正規化の理解
- `active_inference` ライブラリへのアクセス

## Part 1: A-E 行列の定義

**目標**: 4つの状態、3つの観察、3つの行動を持つT-maze 生成モデルを構築する。

状態: 中心 (0), 左腕 (1), 右腕 (2), 刺激場所 (3)
観察: 中立 (0), 報酬 (1), 報酬なし (2)
行動: 待機 (0), 左に進む (1), 右に進む (2)

1. A行列 (3×4) を定義する (エンコード): 中心と刺激場所は中立の観察を、左腕は報酬を、右腕は報酬なし (ある程度のノイズ付き) を与える。
2. Bテンソル (4×4×3) を定義する (遷移ダイナミクスをエンコード)。
3. C = [0, 3, -3] を定義する (報酬を好む、報酬なしを避ける)。
4. D = [1, 0, 0, 0] を定義する (中心から開始)。

```python
import numpy as np
from active_inference.agent import GenerativeModel

# TODO: A, B, C, D 行列を定義する
# TODO: モデル = GenerativeModel(A=A, B=B, C=C, D=D) を作成する
# TODO: モデルを出力する
```

**Response**: {fill:textarea}

## Part 2: モデルの可視化

**目標**: モデルを検査するために、可視化関数を使用する。

1. `plot_model_summary(モデル)` を呼び出して、すべての行列を一気に表示する。
2. `plot_A_matrix(モデル)` を呼び出して、カスタム観察と状態ラベル付きでA行列を表示する。
3. `plot_B_transition_graph(モデル)` を呼び出して、状態遷移グラフを表示する。

```python
from active_inference.visualization import (
    plot_model_summary, plot_A_matrix, plot_B_transition_graph
)

obs_labels = ["neutral", "reward", "no-reward"]
state_labels = ["center", "left", "right", "cue"]

# TODO: 可視化を生成する
```

**Response**: {fill:textarea}

## Part 3: エージェントの作成とループの実行

**目標**: 知覚-行動ループを10ステップ実行する。

1. 同じAとB行列で開始し、状態0で `DiscreteEnvironment` を作成する。
2. γ=4.0 の `ActiveInferenceAgent` を作成する。
3. 10ステップを実行し、各ステップでの観察、信念、選択された行動を出力する。

```python
from active_inference.agent import DiscreteEnvironment, ActiveInferenceAgent

# TODO: 環境とエージェントを作成する
# TODO: 知覚-行動ループを10ステップ実行する
```

**Response**: {fill:textarea}

## Part 4: 精度スキャン

**目標**: γが行動選択にどのように影響するかを調査する。

1. γ = 0.1, 1.0, 4.0, 16.0 で同じシナリオを実行する。
2. 各γについて、エージェントが10ステップで選択する行動を記録する。
3. 結果をプロットまたは表形式で記述し、トレンドを説明する。

**Response**: {fill:textarea}

## Part 5: 分析問題

1. エージェントが報酬腕 (状態1) を訪問しましたか？ もしそうでない場合、モデルをどのように変更すれば、報酬腕を訪問するように促せますか？

2. γを大きくすると、エージェントの行動はどのように変化しましたか？ エージェントがほぼ決定論的になったγの値はどれですか？

3. C = [0, 0, 0] を設定するとどうなりますか？ ループを実行し、元の結果と比較します。

**Response**: {fill:textarea}

## Summary

| スキル | ライブラリコンポーネント | ステータス |
|-------|------------------|--------|
| A, B, C, D, E 行列を適切な形状で定義する | `GenerativeModel(A, B, C, D, E)` | |
| モデル構造を可視化する | `plot_model_summary()`, `plot_A_matrix()` | |
| Active Inference エージェントを作成して実行する | `ActiveInferenceAgent(モデル, gamma)` | |
| 精度-行動トレードオフを調査する | γの変動 (`ActiveInferenceAgent`) | |
| T-maze ベンチマークを理解する | 4つの状態、3つの観察、3つの行動、報酬の好みを理解する | |
