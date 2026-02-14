# モジュール 07: コミュニケーション — マルチエージェントシミュレーションとシグナリングゲーム

## 学習目標

1. 互いに観察し、影響を与えることができるマルチエージェントシミュレーションを構築する。
2. 送信者と受信者のアクティブインファーレンスエージェントを用いたシグナリングゲームを実装する。
3. 発生するコミュニケーションを測定するために、相互情報量を追跡する。

## 導入

アクティブインファーレンスエージェントは、孤立して存在しません。複数のエージェントが共有する環境において、各エージェントのアクションは他のエージェントの観察の一部となります。これにより、豊かなダイナミクスが生まれます。エージェントは、他者の行動を予測し、影響を与えることを学習することで、暗黙的なコミュニケーションを開発します。このモジュールでは、モジュール 01～06 で開発されたシングルエージェントのツールからマルチエージェントシミュレーションを構築します。

## 主要な概念

### 1. マルチエージェントアーキテクチャ

マルチエージェント設定では、各エージェントは独自の生成モデルを持ちますが、環境の状態はすべてのエージェントの状態とアクションを含みます。

```python
from active_inference.agent import GenerativeModel, ActiveInferenceAgent, DiscreteEnvironment

# エージェント1：送信者
model_sender = GenerativeModel(A=A_sender, B=B_sender, C=C_sender, D=D_sender)
agent_sender = ActiveInferenceAgent(model_sender, gamma=4.0)

# エージェント2：受信者
model_receiver = GenerativeModel(A=A_receiver, B=B_receiver, C=C_receiver, D=D_receiver)
agent_receiver = ActiveInferenceAgent(model_receiver, gamma=4.0)
```

### 2. シグナリングゲーム

発生するコミュニケーションの標準的なテストです。

- **2 つの世界の状態**: 食料の左側（0）、食料の右側（1）
- **送信者**: 真の状態を観察し、信号（アクション 0 または 1）を選択する。
- **受信者**: 送信者の信号を観察し、方向（左に進むか右に進むか）を選択する。
- **成功**: 受信者が食料に到達する。

送信者の A-行列を使用すると、その状態を観察できます。受信者の A-行列は、信号を観察にマッピングします。報酬は共有され、両方のエージェントが受信者が食料に到達することを好みます。

```python
# 送信者の A-行列: 真の状態を直接観察する
A_sender = np.eye(2)  # o = s (完全に観測可能)

# 受信者の A-行列: 送信者のアクションを観察する
A_receiver = np.eye(2)  # 初期状態: 信号 0 → 観察 0、信号 1 → 観察 1
```

### 3. マルチエージェントシミュレーションループ

```python
num_steps = 100
mi_history = []

for t in range(num_steps):
    # 送信者が世界の状態を観察し、信号を生成する
    obs_sender = env.get_observation(agent_id=0)
    signal = agent_sender.step(obs_sender)

    # 受信者が信号を観察し、アクションを選択する
    obs_receiver = signal  # 受信者は送信者のアクションを見る
    direction = agent_receiver.step(obs_receiver)

    # 環境が評価する: 受信者は食料を見つけたか？
    reward = env.evaluate(direction)

    # 相互情報量を追跡する
    mi = compute_mutual_information(signals, states)
    mi_history.append(mi)
```

### 4. 相互情報量によるコミュニケーションの測定

相互情報量 $I(X; Y)$ は、送信者の信号が世界の状態に関する不確実性をどれだけ減らすかを定量化します。

$$I(\text{signal} ; \text{state}) = H(\text{signal}) + H(\text{state}) - H(\text{signal}, \text{state})$$

$I = 0$ の場合、信号は状態と相関していません（コミュニケーションはありません）。$I = H(\text{state})$ の場合、信号は状態を完璧にエンコードします。

```python
from active_inference.math import mutual_information

# 観測された信号-状態のペアからの共役分布を構築する
joint = np.zeros((2, 2))
for s, sig in zip(world_states, signals):
    joint[sig, s] += 1
joint /= joint.sum()

mi = mutual_information(joint)
print(f"Mutual Information: {mi:.4f} bits")
```

### 5. コミュニケーション学習

どちらのエージェントも組み込みのコミュニケーションプロトコルを持っていません。コミュニケーションは学習を通じて**発生**します。

1. 送信者は、報酬につながる信号を学習します（pA/pB の更新）。
2. 受信者は、どの信号がどの世界状態と相関しているかを学習します。
3. 時間の経過とともに、エージェントが共有コードを開発するにつれて、相互情報量は増加します。

### 6. より多くのエージェントへの拡張

同じパターンは N エージェントに拡張できます。

- 各エージェントは独自の `GenerativeModel` と `ActiveInferenceAgent` を維持します。
- 環境はエージェントのアクションを他のエージェントの観察にマッピングします。
- 相互情報量はペアごとに追跡できます。

## 応用

- **言語進化**: 記述的なシステムが非言語エージェントからどのように発生するか？
- **協調ロボティクス**: 事前にプログラムされた信号なしで協調プロトコルを開発するエージェント。
- **社会的推論**: 他のエージェントの信念（理論の知性）を生成モデルの一部としてモデル化するエージェント。

## 結論

マルチエージェントアクティブインファーレンスは、シングルエージェントのフレームワークを自然に拡張します。各エージェントのアクションは、他のエージェントの観察になります。コミュニケーションは、エージェントが自分の信号が他者の行動にシステム的に影響を与えることを学習することで発生します。モジュール 08 は時間的次元を拡張します—複数の将来ステップに対する計画。
