# モジュール 02: エージェント — エージェントクラスとA–E行列

## 学習目標

1. 正しい形状と正規化を指定して、A、B、C、D、E行列を使用して `GenerativeModel` を構築します。
2. 生成モデル、ポリシー、および精度パラメータ γ を指定して `ActiveInferenceAgent` を初期化します。
3. 基本的な知覚-行動ループを実行します: `agent.step(observation) → action`。

## 導入

Active Inference エージェントは、その**生成モデル**—エージェントがどのように観測が生成されるかについての信念をエンコードする行列のセットによって定義されます(A)、状態の進化(B)、好ましい結果(C)、初期状態(D)、および習慣的なポリシー(E)。このモジュールでは、各行列を詳しく調べ、それらを動作するエージェントに組み込む方法を示します。

## 主要な概念

### 1. A-行列: 尤度

A-行列は、$P(o \mid s)$—状態から観測がどのように生じるかについてのエージェントの信念をエンコードします：

```python
import numpy as np
from active_inference.agent import GenerativeModel

# 2つの観測、2つの状態
A = np.array([[0.9, 0.1],   # P(o=0 | s=0) = 0.9, P(o=0 | s=1) = 0.1
              [0.1, 0.9]])   # P(o=1 | s=0) = 0.1, P(o=1 | s=1) = 0.9
```

**検証ルール**: Aの各列は1.0に合計される必要があります(状態から観測までの条件付き分布)。

### 2. B-行列: 遷移

B-行列は、$P(s' \mid s, a)$—各アクションの下で隠れた状態がどのように進化するかをエンコードします：

```python
# 2つの状態、2つのアクション
B = np.zeros((2, 2, 2))
B[:, :, 0] = np.eye(2)                # アクション 0: 状態を保つ
B[:, :, 1] = np.array([[0, 1],
                         [1, 0]])       # アクション 1: 状態を交換する
```

**形状**: `(num_states, num_states, num_actions)`。B[:, :, a]のスライスは、アクションごとに一様分布です。2次元のB(形状` (N, N)`)は単アクションモデルとして扱われます。

### 3. Cベクトル: 偏好

Cベクトルは、エージェントの**対数偏好**をエンコードします。これは、「エージェントはどの観測を体験したいですか？」という質問に答えます：

```python
# 観測 0を観測 1よりも好む
C = np.array([2.0, -2.0])   # 対数スケール
```

Cは、期待されるフリーエネルギー(EFE)の「リスク」項としてExpected Free Energy (EFE)に入ります。ポリシーが好ましい観測を導く場合、G(π)は低くなります。Cがすべて0の場合、エージェントは偏りを持たず、情報探索的(情報探索的)になります。

### 4. Dベクトル: 初期状態の事前分布

Dベクトルは、$P(s_0)$—エージェントの開始状態に関する事前信念です：

```python
D = np.array([0.5, 0.5])   # 等しい事前分布
```

**検証ルール**: Dは1.0に合計される必要があります。

### 5. Eベクトル: 習慣の事前分布

オプションのEベクトルは、ポリシーの**習慣の事前分布**をエンコードします—EFEを考慮する前に$P(\pi)$です：

```python
E = np.array([0.7, 0.3])   # ポリシー 0を好む
```

Eが提供されている場合、ポリシーの事後分布は$q(\pi) = \sigma(-\gamma \cdot G(\pi) + \ln E(\pi))$になります。Eが`None`の場合、等しい事前分布が使用されます。

### 6. 生成モデルの組み立て

```python
model = GenerativeModel(A=A, B=B, C=C, D=D, E=E)
print(model)  # GenerativeModel(obs=2, states=2, actions=2)
```

コンストラクターは、次のことを検証します：

- Aは2次元で正規化された列を持つ
- Bは2次元または3次元で正規化された列を持つ
- Cは`num_obs`の長さを持つ
- Dは`num_states`の長さで1.0に合計される
- E（提供されている場合）は1.0に合計される

### 7. ActiveInferenceAgent

エージェントは、生成モデルをラップし、推論の機械を付加します：

```python
from active_inference.agent import ActiveInferenceAgent

agent = ActiveInferenceAgent(model, gamma=4.0)
print(agent)  # ActiveInferenceAgent(γ=4.0, policies=2)
```

主なパラメータ：

- `gamma` (γ): ポリシー選択の精度。高いγ → より探求的。
- `policies`: アクションシーケンスのリスト（デフォルトはアクションごとに単ステップポリシー）。

### 8. 知覚-行動ループ

```python
from active_inference.agent import DiscreteEnvironment

env = DiscreteEnvironment(A, B, initial_state=0)
agent = ActiveInferenceAgent(model, gamma=4.0)

obs = env.reset(initial_state=0)
for t in range(10):
    action = agent.step(obs)     # 状態を推論 → ポリシーを推論 → アクションを選択する
    obs = env.step(action)       # 環境が遷移し観測を生成する
```

`agent.step(obs)`メソッドは、`infer_states(obs)`、`infer_policies()`、`select_action()`を順番に呼び出す便利な方法です。

## 応用

- **T-迷路**: 4つの状態（中心、左アーム、右アーム、ヒントの位置）、3つの観測（中心、報酬、報酬なし）、3つのアクション（保持、左に進む、右に進む）を持つ古典的なベンチマーク。Cベクトルは、報酬観測を好むことをエンコードします。
- **最小の2状態モデル**: Active Inferenceエージェントを完全に手動で分析できる最も単純なActive Inferenceエージェント—教育目的のための導出に役立ちます。
- **精度調整**: 0.01（ランダムなポリシー選択）から100（無益なアクション選択）まで、γを変化させると、探索と利用のトレードオフが明らかになります。

## 結論

A–E行列は、Active Inferenceエージェントの生成モデルを完全に指定します。これらの行列が検証され、`ActiveInferenceAgent`がインスタンス化されると、エージェントは知覚し、決定し、行動することができます。モジュール03では、知覚ステップ—信念がA行列と変分推論を使用して更新される方法について説明します。