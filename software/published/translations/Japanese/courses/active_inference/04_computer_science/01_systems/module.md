# モジュール 01: システム - 生成的プロセスと生成的モデル

## 学習目標

1.  **生成的プロセス**（真の環境）と**生成的モデル**（エージェントの内部モデル）を区別する。
2.  真のAとB行列を持つ`DiscreteEnvironment`を実装し、プログラム的にステップを進める。
3.  観察が真の確率行列からサンプリングされ、状態が真のダイナミクスのもとでどのように遷移するかを説明する。

## 導入

Active Inferenceのエージェントは、直接アクセスできない世界の中に住んでいます。**生成的プロセス**は、その世界の真の因果構造—真の状態、遷移確率、観察確率—です。**生成的モデル**は、エージェントが更新できる行列にエンコードされた、その構造の _近似_ です。

この区別は、計算Active Inferenceのすべてにおいて出発点となります。生成的モデルが生成的プロセスと完全に一致する場合、フリーエネルギーはゼロになり、エージェントは学習する以上のことがなくなります。実際には、この二つの間の不一致こそが、認識、行動、学習を駆動するものです。

`active_inference`ライブラリでは、これらの二つのコインの側面は、以下のクラスでそれぞれ表されます。

| 概念 | クラス | 行列 |
|---|---|---|
| 生成的プロセス | `DiscreteEnvironment` | `true_A`, `true_B` (真の値) |
| 生成的モデル | `GenerativeModel` | `A`, `B`, `C`, `D`, `E` (エージェントの信念) |

## 主要な概念

### 1. 生成的プロセスが真の値であること

生成的プロセスは、環境の真の因果構造を定義します。離散的な場合、これには以下が含まれます。

-   **真の状態** $s \in \{0, 1, \ldots, N_s - 1\}$：世界の隠れた状態。
-   **真の確率** $\mathbf{A}_{\text{true}}$： $A[o, s] = P(o \mid s)$—状態$s$にあるとき観察$o$の確率—を示す行列。
-   **真の遷移** $\mathbf{B}_{\text{true}}$： $B[s', s, a] = P(s' \mid s, a)$—現在の状態$s$と行動$a$に対する状態$s'$の確率—を示すテンソル。

コードでは、これらの行列を提供することで`DiscreteEnvironment`を作成します。

```python
import numpy as np
from active_inference.agent import DiscreteEnvironment

# 真の確率：観察 0 は状態 0 の強力な証拠
true_A = np.array([[0.9, 0.1],
                    [0.1, 0.9]])

# 真の遷移：行動 0 = 待機、行動 1 = スワップ
true_B = np.zeros((2, 2, 2))
true_B[:, :, 0] = np.eye(2)           # 待機
true_B[:, :, 1] = np.array([[0, 1],
                              [1, 0]])  # スワップ

env = DiscreteEnvironment(true_A, true_B, initial_state=0)
```

### 2. 観察の生成

環境がクエリされると、現在の隠れた状態から真の確率列から観察をサンプリングします。

$$o_t \sim \text{Cat}(\mathbf{A}_{\text{true}}[\cdot, s_t])$$

これは、`env.step(action)`を通じて実装され、以下を実行します。

1.  隠れた状態の遷移：$s_{t+1} \sim \text{Cat}(\mathbf{B}_{\text{true}}[\cdot, s_t, a_t])$
2.  観察の生成：$o_{t+1} \sim \text{Cat}(\mathbf{A}_{\text{true}}[\cdot, s_{t+1}])$
3.  観察インデックスの返却

```python
obs = env.reset(initial_state=0)   # 最初の観察をサンプリング
obs = env.step(action=1)            # スワップアクションを実行し、新しい観察を取得
print(f"State: {env.state}, Obs: {obs}, Timestep: {env.timestep}")
```

### 3. スパース・スペースの次元

環境の次元は、行列から導出されます。

| プロパティ | 導出 | 例 |
|---|---|---|
| `num_obs` | Aの行数 | 2 |
| `num_states` | Aの列数 | 2 |
| `num_actions` | Bの3次元 (またはBが2次元の場合) | 2 |

2次元のB行列は、エージェントに選択肢がない（単一のアクション環境）と見なされます。

### 4. 履歴追跡

環境は、完全な軌跡を記録します。

```python
env = DiscreteEnvironment(true_A, true_B, initial_state=0)
env.reset(initial_state=0)
for a in [0, 1, 1, 0]:
    env.step(a)

print(env.history["states"])        # [0, 0, 1, 0, 0]  (初期 + 4 ステップ)
print(env.history["observations"])  # [obs0, obs1, obs2, obs3]
print(env.history["actions"])       # [0, 1, 1, 0]
```

この履歴は、`plot_environment_trajectory()`を使用して視覚化できます。

### 5. 生成的モデルがエージェントの仮説であること

環境は `true_A` と `true_B` を使用しますが、エージェントは `GenerativeModel`という独自の仮説を構築し、これは現実と一致するかどうかに関わらず、行列でエンコードされています。

```python
from active_inference.agent import GenerativeModel

# エージェントのモデル（真の値と異なる可能性がある）
model = GenerativeModel(
    A=true_A.copy(),       # エージェントの確率信念
    B=true_B.copy(),       # エージェントの遷移信念
    C=np.zeros(2),         # 偏り (対数スケール)
    D=np.array([0.5, 0.5]) # 初期状態に対する事前確率
)
```

`model.A` と `true_A` (および同様に `B`) の間のギャップこそが、Active Inferenceにおいてエージェントが閉じる必要があるものです。これはActive Inferenceの基本的な非対称性です。

## 応用

-   **感覚ノイズ:** `true_A` の対角成分外の確率>0は、ノイズのある観察をシミュレートします。`true_A = np.eye(N)`を設定すると、完全に観測可能な環境が作成されます。
-   **確率的なダイナミクス:** `true_B` が正方行列でない場合、行動の効果が不確実（たとえば、滑りやすいグリッドワールド）になる環境を作成します。
-   **ベンチマーク:** エージェントが学習した`A`と`true_A`を比較することで、エージェントが環境の因果構造をどれだけ正確に復元したかを測定できます。

## 結論

生成的プロセス/生成的モデルの区別は、Active Inferenceのすべての計算構造化されています。`DiscreteEnvironment`クラスは、エージェントが推論する必要がある真の値をエンコードします。モジュール 02 では、エージェントクラスを構築して、不一致を最小限に抑えるために`GenerativeModel`を維持および更新します。