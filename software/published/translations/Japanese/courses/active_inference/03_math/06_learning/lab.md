# Lab: Derivation Exercise — Parameter Learning and Model Reduction

## Objective

パラメータ学習の方程式とベイズモデル削減の公式を導出し、具体的な例を適用します。

## Part 1: Dirichlet-Categorical Conjugacy

**Goal**: conjugate update を第一原理から導出する。

**Setup**: Prior: p(θ) = Dir(θ; α₁, α₂, α₃) with α = [2, 3, 1]. Likelihood: p(x|θ) = Cat(x; θ). Data: 10 observations: {1, 1, 2, 1, 3, 2, 1, 1, 2, 1} (category counts: n₁=6, n₂=3, n₃=1).

**Task**:

1.  ベイズの法則を書きなさい: p(θ|x₁:N) ∝ p(x₁:N|θ) · p(θ)
2.  尤度を ∏ₖ θₖ^nₖ と事前分布を ∏ₖ θₖ^(αₖ-1) で展開する
3.  事後分布が Dir(θ; α₁+n₁, α₂+n₂, α₃+n₃) = Dir(θ; 8, 6, 2) であることを示す
4.  データに対する事後平均 E[θ|data] を計算し、MLEと比較する

{fill:textarea}

## Part 2: A-Matrix Learning in a POMDP

**Goal**: 経験を通して A行列がどのように変化するかを追跡する。

**Setup**: 2状態、2観測のPOMDP。初期A行列の濃度:

a = [[10, 1], [1, 10]]  (状態1 → 観測1; 状態2 → 観測2)

エージェントが状態1が観測1 (18回) と観測2 (2回) を経験する20回の試行を行う。

**Task**:

1.  ディレクトリ更新ルールを適用する: a_ij ← a_ij + n_ij
2.  更新された濃度パラメータを計算する
3.  更新された期待値A行列（事後平均）を計算する
4.  A行列はどのように変化したか？エージェントはどれだけ自信を持っているか？

{fill:textarea}

## Part 3: Bayesian Model Reduction

**Goal**: BMR を適用してパラメータを削減するかどうかを決定する。

**Setup**: 学習後、3状態のPOMDPの事後A行列の濃度:

a_full = [[50, 2, 1], [2, 48, 1], [1, 1, 45]]

状態2と3を統合することで状態数を2に削減（3から2）、削減された事前濃度:

ã₀ = [[50, 3], [2, 49]]

元の事前分布: a₀ = [[10, 1, 1], [1, 10, 1], [1, 1, 10]]

**Task**:

1.  BMRの証拠比を計算する: ΔF ≈ ln B(ã₀) - ln B(a₀) - ln B(ã) + ln B(a)
2.  ここで、ã = a + ã₀ - a₀
3.  削減されたモデルが好ましいかどうかを決定する（ΔF < 0）
4.  これは何を意味するのか説明する：第3の状態は「作業」をしているのか、それとも削減できるのか？

{fill:textarea}

## Part 4: Bayesian Model Reduction

**Goal**: パラメータ学習（ディレクトリ更新）と構造学習（BMR）が組み合わさることで、エージェントが生成モデルを同時に洗練させ、簡略化する方法と、それが目覚め学習と睡眠固持の神経科学にどのように対応するかを分析する。

**Task**:

1.  ディレクトリ更新 a ← a + η · n を分析し、η < 1（遅い学習）と η > 1（速い学習）の効果を評価する。
2.  忘却メカニズムを検討する: a ← λ · a + η · n、ここで λ < 1 は減衰因子である。これにより指数忘却が実装されることを示す。
3.  有効な「メモリウィンドウ」を λ の関数として計算する。
4.  議論する：忘却は適応的か、あるいは maladaptive なのか？

{fill:textarea}

## Part 5: Synthesis

200語で、パラメータ学習（ディレクトリ更新）と構造学習（BMR）が組み合わさることで、エージェントが生成モデルを同時に洗練させ、簡略化する方法と、それが目覚め学習と睡眠固持の神経科学にどのように対応するかを説明してください。

{fill:textarea}

## Lab Summary

| Part | Skill Developed | Mathematical Result |
|------|----------------|-------------------|
| 1 | Bayesian updating | Dirichlet-Categorical conjugate derivation |
| 2 | Matrix learning | A-matrix concentration update tracking |
| 3 | Model comparison | Bayesian Model Reduction evidence ratio |
| 4 | Dynamical analysis | Learning rate and forgetting trade-offs |
| 5 | Conceptual integration | Connecting learning math to neuroscience |
