# モジュール 05: 行動 — 期待される自由エネルギーによるポリシー選択

## 学習目標

1. 期待される自由エネルギー $G(\pi)$ を計算し、リスクと曖昧さのコンポーネントに分解する。
2. ソフトマックス関数を用いてポリシー選択を実装する（負のEFE値を使用）。
3. T-mazeベンチマークを実行し、探索–利用行動を分析する。

## 導入

Active Inferenceにおける行動選択は、報酬最大化ではない—それは未来に投影された自由エネルギー最小化である。エージェントは、各候補ポリシーを評価し、期待される自由エネルギー (EFE) $G(\pi)$ を計算することで、そのポリシーがどれだけ驚きと不確実性をもたらすかをスコアリングする。好ましい、情報的なアウトカムをもたらすポリシーは、より低い $G$ 値と高い事後確率を持つ。

## 主要な概念

### 1. 期待される自由エネルギー：アクション選択基準

単一ステップポリシー $\pi = [a]$ の場合、EFEは以下の通りである：

$$G(\pi) = \underbrace{D_{KL}[q(o \mid \pi) \| \tilde{P}(o)}_{\text{リスク（実践的）}} + \underbrace{\mathbb{E}_{q(s' \mid \pi)}[H[P(o \mid s')]]}_{\text{曖昧さ（認識的）}}$$

- **リスク**: 予測された観察が好み $\tilde{P}(o) = \sigma(C)$ から逸脱する場合にペナルティを科す。
- **曖昧さ**: 状態が予測しにくい（A行列の条件付きエントロピーが高い）場合にペナルティを科す。

```python
from active_inference.math import compute_efe, compute_efe_components

q_s = np.array([0.5, 0.5])
G = compute_efe(q_s, model.A, model.B, model.C, action=0)
print(f"G(action=0) = {G:.4f}")

comps = compute_efe_components(q_s, model.A, model.B, model.C, action=0)
print(f"リスク = {comps['risk']:.4f}, 曖昧さ = {comps['ambiguity']:.4f}")
print(f"G = リスク + 曖昧さ = {comps['G']:.4f}")
```

### 2. ソフトマックスによるポリシー事後分布

EFEの値がすべてのポリシーに対して与えられた場合、ポリシーに対する事後分布は以下の通りである：

$$q(\pi) = \sigma(-\gamma \cdot G(\pi) + \ln E(\pi))$$

ここで $\sigma$ はソフトマックス関数、 $\gamma$ は精度、 $E(\pi)$ は習慣事前分布である。

```python
from active_inference.math import run_policy_inference

result = run_policy_inference(
    q_s=agent.q_s,
    A=model.A, B=model.B, C=model.C,
    policies=[[0], [1]],   # 単一ステップポリシー
    gamma=4.0,
    E=model.E,
)

print(result["q_pi"])             # ポリシー事後分布
print(result["G_values"])         # EFE 各ポリシーに対して
print(result["selected_action"])  # argmax of q(π)
```

### 3. リスクが目標指向行動を駆動する方法

リスクは、ポリシーが観察を予測するかどうかと、ポリシーが好む観察との間でKL散度を測定する：

$$\text{リスク}(\pi) = D_{KL}[q(o \mid \pi) \| \sigma(C)]$$

ポリシーが好ましい観察を生み出す状態に導く場合、リスクは低い。T-mazeはこれを明確に示している：

- ポリシー“左に進む”は報酬腕につながる → 予測される $q(o \mid \pi)$ が $\sigma(C)$ と一致する → リスクが低い
- ポリシー“右に進む”は報酬なしの腕につながる → 予測される観察が好みから逸脱する → リスクが高い

### 4. 曖昧さが情報探索を駆動する方法

曖昧さは、尤度に関する期待される条件付きエントロピーである：

$$\text{曖昧さ}(\pi) = \sum_{s'} q(s' \mid \pi) \cdot H[P(o \mid s')]$$

ポリシーが、観察が非常に情報量が多い（A行列の列のエントロピーが低い）状態に導く場合、曖昧さは低い。これはエージェントが不確実性を削減する傾向を駆動する—好奇心の計算的な基礎である。

### 5. T-mazeベンチマーク

T-mazeはActive Inferenceの標準的なベンチマークである：

```
         [左/報酬]
              |
[開始] --- [中央]
              |
         [右/報酬なし]
              |
          [ヒューロ位置]
```

- 4の状態、3の観察、3の行動
- ヒューロ位置が報酬の場所を明らかにする
- 理想的なエージェントはまずヒューロ位置を訪問する（認識的駆動）、次に報酬腕に行く（実践的駆動）

```python
from active_inference.visualization import plot_tmaze
plot_tmaze(current_state=0, reward_location="left")
```

### 6. EFE分解の可視化

```python
from active_inference.visualization import plot_efe_decomposition

risk_values = [comps["risk"] for comps in efe_history]
ambiguity_values = [comps["ambiguity"] for comps in efe_history]
plot_efe_decomposition(risk_values, ambiguity_values)
```

## アプリケーション

- **探索前に利用**: T-mazeでは、曖昧さ項がエージェントがヒューロ位置を訪問する前に、エージェントを誘導する。曖昧さ項がない場合、エージェントはランダムに推測する。
- **リスク感応計画**: CベクトルMagnitudeを調整することで、エージェントをよりまたはより少ない感応させるようにすることができる。
- **ポリシー比較**: すべてのポリシーに対して $G(\pi)$ をプロットすることで、エージェントの決定の地形を明らかにする。

## 結論

Active Inferenceにおける行動選択は、目標達成（リスク最小化）と情報収集（曖昧さ削減）の原理的な組み合わせである。`compute_efe()`関数と`run_policy_inference()`は、このメカニズムを実装する。モジュール06は、経験に基づいてモデルのパラメータを学習するために、この枠組みを拡張する。