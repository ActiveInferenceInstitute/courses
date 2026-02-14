# Lab 07: 複数エージェントシグナリングゲーム

## 目的

2エージェントのシグナリングゲームを構築し、学習を用いて実行し、相互情報による emergent コミュニケーションを測定する。

## 前提条件

- Lab 01～06 を完了する
- 相互情報と多エージェントダイナミクスに関する理解

## Part 1: エージェントの設定

**目標**: 2状態のシグナリングゲームのための送信者と受信者エージェントを作成する。

1. 送信者のモデルを定義する: A = 識別 (真のステートを観察), B = 識別, C = [報酬の好みを], D = 一様分布。
2. 受信者のモデルを定義する: A = 識別 (信号を観察にマッピング), B は送信者の行動によって影響を受ける, C = 同じ報酬の好み。
3. γ = 4.0 で `ActiveInferenceAgent` インスタンスの両方をインスタンス化する。

```python
import numpy as np
from active_inference.agent import GenerativeModel, ActiveInferenceAgent

# TODO: 送信者と受信者のモデルを定義する
# TODO: エージェントを作成する
```

## Part 2: シグナリングループの実行

**目標**: シグナリングゲームを100ラウンド実行する。

1. 各ラウンドで: ランダムにワールドステート (0 または 1) をサンプリングする。
2. 送信者はステートを観察し、シグナルを選択する。
3. 受信者はシグナルを観察し、方向を選択する。
4. 成功 (受信者が正しい方向を選択した) と (シグナル, ステート) ペアを記録する。

```python
signals = []
states = []
successes = []

for t in range(100):
    world_state = np.random.choice(2)
    signal = agent_sender.step(world_state)
    direction = agent_receiver.step(signal)
    success = (direction == world_state)

    signals.append(signal)
    states.append(world_state)
    successes.append(success)
```

## Part 3: 学習の追加

**目標**: エージェントがコミュニケーションプロトコルを開発できるように、Dirichlet 学習を追加する。

1. 各ラウンドの後に、両方のエージェントに対して `update_dirichlet_A()` を追加する。
2. 後の推論のための期待される A 行列を更新する。
3. 学習を有効にした状態で200ラウンド実行する。
4. ラウンド 1～50 とラウンド 151～200 での成功率を比較する。

## Part 4: 相互情報量の測定

**目標**: 時間経過に伴い、シグナルとワールドステート間の相互情報量を追跡する。

1. スライディングウィンドウ (20ラウンド) を使用して相互情報量を計算する。
2. ウィンドウ化された (シグナル, ステート) ペアから共分散分布を構築する。
3. 相互情報量を時間とともにプロットする。 コミュニケーションがemergeした場合、増加するはず。

```python
from active_inference.math import mutual_information

mi_history = []
window = 20
for t in range(window, len(signals)):
    joint = np.zeros((2, 2))
    for s, sig in zip(states[t-window:t], signals[t-window:t]):
        joint[sig, s] += 1
    joint /= joint.sum()
    mi_history.append(mutual_information(joint))
```

## Part 5: 分析質問

1. 相互情報量は時間とともに増加しましたか？ 最終的なMIは最大値 ($\ln 2 \approx 0.693$) と比較してどの程度でしたか？
2. 送信者はワールドステートとシグナル間の一貫したマッピングを開発しましたか？ マッピングは何でしたか？
3. 受信者の精度が80%を超えたまでに何ラウンド必要でしたか？

## 要約

| スキル | ライブラリコンポーネント | ステータス |
|-------|------------------|--------|
| 複数エージェントの Active Inference システムを構築する | 複数の `ActiveInferenceAgent` インスタンス | |
| シグナリングゲームループを実装する | 送信者-受信者アーキテクチャ | |
| 多エージェント設定で Dirichlet 学習を追加する | `update_dirichlet_A()` per エージェント | |
| Emergent コミュニケーションを測定する | `mutual_information()` on 共分散分布 | |
| コミュニケーション開発を時間経過とともに追跡する | スライディングウィンドウによる MI 追跡 | |
