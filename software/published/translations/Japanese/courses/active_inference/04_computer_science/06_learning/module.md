# モジュール 06: 学習 — ディリクレ濃縮の更新

## 学習の目的

1.  A と B の行列のディリクレ濃縮更新を使用してパラメータ学習を実装する。
2.  ディリクレ事後分布から期待されるパラメータ行列を計算し、真の値と比較する。
3.  ベイズモデル削減 (BMR) を使用してモデルの品質を評価する。

## 導入

モジュール 01〜05 では、エージェントの生成モデルは固定されていました—A、B、C、D、E の行列は一度設定され、決して変更されませんでした。しかし、真に適応的なエージェントは**学習**する必要があります—経験に基づいて環境の因果構造について信念を更新する必要があります。アクティブインファーレンスにおいて、学習とはディリクレ濃縮パラメータ (pA、pB) を更新することであり、これらのパラメータはエージェントが A と B についての信念をパラメータ化します。

## 重要な概念

### 1. なぜディリクレ分布を使うのか？

A行列の各列はカテゴリカル分布です。カテゴリカル分布のベイズ共役事前分布は**ディリクレ分布**です。Aの点推定値ではなく、エージェントは、次の式でパラメータ化された濃縮パラメータ $\mathbf{p}_A$ を維持します。

$$P(\mathbf{A}[:, s]) = \text{Dir}(\mathbf{p}_A[:, s])$$

期待される (平均) A行列は次のとおりです。

$$\mathbb{E}[\mathbf{A}[:, s]] = \frac{\mathbf{p}_A[:, s]}{\sum_o \mathbf{p}_A[o, s]}$$

```python
from active_inference.math import expected_A

pA = np.array([[10.0, 1.0],
                [1.0, 10.0]])

A_expected = expected_A(pA)
# A_expected ≈ [[0.909, 0.091], [0.091, 0.909]]
```

### 2. pA の更新：尤度の学習

各観測-状態ペア $(o_t, q_s)$ ごとに、エージェントは pA を更新します。

$$\mathbf{p}_A[o_t, :] \mathrel{+}= q(s) \cdot \eta$$

ここで、η は学習率です。これは、事後信念に基づいて外積更新されます。

```python
from active_inference.math import update_dirichlet_A

pA_new = update_dirichlet_A(
    pA=pA.copy(),
    observation=0,
    q_s=np.array([0.9, 0.1]),
    learning_rate=1.0,
)
# pA_new[0, 0] は 0.9 で増加 (観測-状態ペアに一致)
# pA_new[0, 1] は 0.1 で増加 (二次的な信念)
```

### 3. pB の更新：遷移の学習

同様に、各 (状態、行動、次の状態) 三重項ごとの、遷移濃度は次のとおりに更新されます。

$$\mathbf{p}_B[:, s, a] \mathrel{+}= q(s') \cdot q(s) \cdot \eta$$

```python
from active_inference.math import update_dirichlet_B

pB_new = update_dirichlet_B(
    pB=pB.copy(),
    q_s=np.array([0.9, 0.1]),
    q_s_next=np.array([0.1, 0.9]),
    action=1,
    learning_rate=1.0,
)
```

### 4. オンライン学習ループ

各タイムステップでの完全な知覚-行動-学習ループ：

```python
for t in range(100):
    # 1. 知覚
    action = agent.step(obs)

    # 2. A の学習
    pA = update_dirichlet_A(pA, obs, agent.q_s, learning_rate=1.0)
    agent.model.A = expected_A(pA)

    # 3. 行動と観察
    obs = env.step(action)

    # 4. B の学習
    pB = update_dirichlet_B(pB, q_s_prev, agent.q_s, action, learning_rate=1.0)
    agent.model.B = expected_B(pB)
```

### 5. 学習の進捗状況の追跡

KL 分散を使用して、学習されたモデルが真の値にどれだけ近いかを測定します。

```python
from active_inference.math import kl_divergence

# 各列の学習された A と真の A を比較
for s in range(num_states):
    kl = kl_divergence(expected_A(pA)[:, s], true_A[:, s])
    print(f"KL[学習済み || 真実] for state {s}: {kl:.6f}")
```

`plot_learning_progress()` を使用して可視化します。

```python
from active_inference.visualization import plot_learning_progress
plot_learning_progress(kl_history)
```

### 6. ディリクレエントロピー

ディリクレ分布のエントロピーは、エージェントがパラメータ列についてどれだけ不確実であるかを測定します。

$$H[\text{Dir}(\boldsymbol{\alpha})] = \ln B(\boldsymbol{\alpha}) + (\alpha_0 - K) \psi(\alpha_0) - \sum_k (\alpha_k - 1) \psi(\alpha_k)$$

```python
from active_inference.math import dirichlet_entropy

# pA 列 0 のエントロピー
H = dirichlet_entropy(pA[:, 0])
print(f"pA 列 0 のエントロピー: {H:.4f}")
```

### 7. ベイズモデル削減 (BMR)

BMR は、完全なモデルと簡略化された (より単純) モデルの間のフリーエネルギーの変化を計算することにより、モデルを比較します。

$$\Delta F = F_{\text{簡略化}} - F_{\text{完全}}$$

ΔF が負である場合、簡略化されたモデルが優れていることを意味します (より単純で、同じ性能)。

```python
from active_inference.math import bayesian_model_reduction

delta_F = bayesian_model_reduction(pA_full, pA_reduced)
print(f"ΔF = {delta_F:.4f}")  # 負 = 簡略化されたモデルが好まれる
```

## 応用

- **マルチエピソードのトレーニング**: 多くのエピソードを実行し、エピソードごとに pA と pB を蓄積します。エージェントは、より正確なモデルを開発します。
- **カタルシスフォゲッティング**: 一つのコンテキストで学習がパフォーマンスに影響を与えるかどうかを監視します。
- **モデルの比較**: BMR を使用してモデルから不要なパラメータを削除します。

## 結論

学習は、エージェントが感知し、行動するだけでなく、時間とともに生成モデルを改善することによって、ループを閉じます。ディリクレ更新は、この改善のための、原理的なベイズメカニズムを提供します。モジュール 07 は、エージェントが互いについて学習するマルチエージェント設定でこれらのアイデアを拡張します。