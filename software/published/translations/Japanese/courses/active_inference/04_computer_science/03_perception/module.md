# モジュール 03: 認識 – バリアンス推論による状態推定

## 学習目標

1. A行列の尤度と固定点反復を用いて、信念更新を実装する。
2. `run_state_inference()` を使用して、観測から隠れた状態を推論する。
3. 事後信念と収束診断を可視化する。

## 導入

アクティブインファレンスの認識とは、新しい観測に基づいてエージェントが隠れた状態に関する信念を更新するプロセスです。これはパッシブなパターンマッチングではありません。これは、ベアリングフリーエネルギー (VFE) を最小化することにより、事後分布 $q(s)$ を見つけるアクティブな _推論_ プロセスです。この分布は、観測とエージェントの先験的な信念を最もよく一致させます。

## 主要な概念

### 1. 推論問題

与えられた：

- 先験的な信念：$q(s)$ (初期値は $D$、または前の事後分布)
- 新しい観測：$o_t$ (整数インデックス)
- 尤度モデル：$\mathbf{A}$、ここで $A[o, s] = P(o \mid s)$

事後 $q(s \mid o_t)$ を最小化する：

$$F = D_{KL}[q(s) \| p(s)] - \mathbb{E}_{q(s)}[\ln P(o_t \mid s)]$$

### 2. 固定点反復

`run_state_inference()` 関数は、この問題を反復メッセージパッシングによって解決します：

$$q(s) \propto P(o_t \mid s) \cdot q_{\text{prior}}(s)$$

各反復において：

1. 対対事後ロガーを計算する：$\ln q(s) = \ln A[o_t, :] + \ln q_{\text{prior}}(s)$
2. ソフトマックスで正規化する：$q(s) = \sigma(\ln q(s))$
3. 収束を確認する：$\delta = \| q^{(k)} - q^{(k-1)} \|$

```python
from active_inference.math import run_state_inference

result = run_state_inference(
    prior=np.array([0.5, 0.5]),   # uniform prior
    observation=0,                 # observed o=0
    A=model.A,                     # likelihood matrix
    num_iterations=16,             # max iterations
    convergence_threshold=1e-8,    # stop when delta < threshold
)

print(result["q_s"])           # posterior beliefs
print(result["converged"])     # True/False
print(result["num_iters"])     # iterations used
print(result["delta_history"]) # convergence trace
```

### 3. A行列が認識をどのように形作るか

A行列は、各観測がどれだけ情報を持っているかを示す：

| A-matrix structure | Perceptual effect |
|---|---|
| Identity (A = I) | Fully observable — each observation uniquely identifies a state |
| Uniform columns | Observations carry no information — beliefs don't update |
| High diagonal | Clear signal — beliefs shift strongly toward the matching state |
| Ambiguous (similar columns) | Weak evidence — beliefs change slowly, need more observations |

```python
# High-information A: observation 0 strongly implies state 0
A_clear = np.array([[0.95, 0.05],
                     [0.05, 0.95]])

# Low-information A: observations are nearly uninformative
A_noisy = np.array([[0.55, 0.45],
                     [0.45, 0.55]])
```

### 4. エージェントレベルの推論

`ActiveInferenceAgent.infer_states(obs)` メソッドは、`run_state_inference()` をラップします：

```python
from active_inference.agent import ActiveInferenceAgent

agent = ActiveInferenceAgent(model, gamma=4.0)
agent.infer_states(0)         # observe o=0, update beliefs
print(agent.q_s)              # posterior
print(agent.history["vfe"])   # VFE logged after each inference
```

推論後、`agent.q_s` は更新された事後分布と VFE を保持します。VFE は履歴に追加されます。

### 5. 対対尤度ベクトルの

`model.log_likelihood(obs)` は、$\ln A[o, :]$ を返す対対尤度ベクトル — 各状態が観測を生成する可能性の対対証拠です：

```python
ll = model.log_likelihood(0)   # shape: (num_states,)
# For A = [[0.9, 0.1], [0.1, 0.9]]:
# ll ≈ [-0.105, -2.303]  (state 0 is much more likely to produce obs 0)
```

### 6. 予測誤差

信念が更新された後、エージェントは予測誤差を計算できます：

$$\varepsilon = \mathbf{e}_o - \mathbf{A} \cdot q(s)$$

ここで、$\mathbf{e}_o$ は実際の観測に対応する1hotベクトルです：

```python
agent.infer_states(0)
pe = agent.prediction_error(0)    # shape: (num_obs,)
print(pe.sum())                    # ≈ 0 (prediction errors sum to zero)
```

### 7. 収束診断

`plot_convergence()` を使用して、推論がどれだけ早く収束するかを可視化します：

```python
from active_inference.visualization import plot_convergence

result = run_state_inference(prior=model.D, observation=0, A=model.A)
plot_convergence(result["delta_history"], threshold=1e-8)
```

## 応用

- **曖昧な刺激**: ノイズのある A 行列の場合、単一の観測が状態を解決できない—エージェントは、確信を得るために複数の観測を必要とします（ぼやけた画像を見るのと同様）。
- **ベイズの驚き**: 推論後に信念がどれだけシフトするかは、観測がどれだけ驚くかを表します。
- **先験的-観測の対立**: 先験的な信念が 1 つの状態を強く好むが、観測が別の状態を好む場合、事後分布は、相対的な強さに重み付けされた妥協です。

## 結論

認識は、バリアンス推論に還元されます。A行列、先験的な信念、観測は、反復メッセージパッシングによって事後分布を決定します。モジュール 04 は、優先順位 (C)、先験的な信念 (D)、習慣 (E) を内部モデルの制約として導入することで、この枠組みを拡張します。
