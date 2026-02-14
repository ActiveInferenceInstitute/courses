# Course 4: Computational Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md) | [Resources](../resources/) | [Agent Guidelines](./AGENTS.md)

## Course Description

このコースでは、Pythonを用いてアクティブ・インファーレンスアルゴリズムを実装します。pymdpにインスパイアされたカスタム`active_inference`ライブラリを使用し、学生はゼロから、離散状態空間のActive Inferenceエージェントを構築、実行、分析します。含まれるトピックには、生成モデルの仕様（A-E行列）、変分推論による信念の更新、期待されるフリーエネルギーによるポリシー選択、Dirichlet更新によるパラメータ学習、多エージェントシミュレーション、深層時間的計画が含まれます。すべてのコードは実行可能で、よく文書化されており、モジュール間で段階的に構築されます。

---

## Prerequisites

- Course 1-3（哲学、認知科学、Active Inferenceの数学）
- Pythonプログラミング：NumPy、基本的なOOP（クラス、メソッド）、matplotlibに慣れていること
- このコースでは、カリキュラムにバンドルされたカスタム`active_inference`ライブラリを使用します（`src/active_inference/`を参照）
- 推奨：インタラクティブな開発のためのJupyterノートブック

> **注**: すべてのソースパス（例：`src/active_inference/`）は`04_computer_science/`ディレクトリ内の相対パスです。

---

## Course Schedule

| 週 | モジュール | トピック | 実装の焦点 | 主要なコンポーネント | 成果物 |
|---|---|---|---|---|---|
| 1 | [Module 1](./01_systems/) | **システム** | 環境設定、生成プロセス vs モデル | `DiscreteEnvironment`、観測生成 | Lab 1、クイズ 1 |
| 2 | [Module 2](./02_agents/) | **エージェント** | エージェントクラス、A-E行列の仕様 | `GenerativeModel`、`ActiveInferenceAgent`、T-maze | Lab 2、クイズ 2 |
| 3 | [Module 3](./03_perception/) | **知覚** | 信念の更新、A-行列の尤度 | `run_state_inference()`、事後分布の可視化 | Lab 3、クイズ 3 |
| 4 | [Module 4](./04_cognition/) | **認知** | 優先度（C）、事前分布（D）、習慣（E） | C、D、Eベクトルの構築、精度γ | Lab 4、クイズ 4 |
| 5 | [Module 5](./05_action/) | **行動** | ポリシー選択、G(π)の計算 | `compute_efe()`、ソフトマックスポリシー選択 | Lab 5、クイズ 5 |
| 6 | [Module 6](./06_learning/) | **学習** | パラメータ学習、Dirichlet更新 | `update_dirichlet_A()`、`update_dirichlet_B()` | Lab 6、クイズ 6 |
| 7 | [Module 7](./07_communication/) | **コミュニケーション** | 多エージェントシミュレーション、シグナリングゲーム | 多エージェントループ、相互情報量の追跡 | Lab 7、クイズ 7 |
| 8 | [Module 8](./08_planning/) | **計画** | 深層時間的モデル、グリッドワールド | 時間的深さT、高度な推論 | Lab 8、クイズ 8、最終プロジェクト |

---

## Learning Objectives

このコースの終了時までに、あなたは以下のことができるようになるはずです。

1.  A, B, C, D, E行列を使用して、`active_inference`ライブラリで完全なActive Inferenceエージェントを構築できること
2.  固定点反復（変分信念更新）を使用して状態推定を実装できること
3.  期待されるフリーエネルギー（G）を計算し、ソフトマックスを使用してポリシーを選択できること
4.  探索と利用のトレードオフを示す、標準的なT-mazeベンチマークをシミュレーションできること
5.  Dirichlet濃度更新（pA、pB）を通してオンラインパラメータ学習を実装できること
6.  Active Inferenceエージェントが互いに観測し影響し合う多エージェントシミュレーションを設計できること
7.  将来の時間の時間軸にわたる計画のための深層時間的モデルを構築できること
8.  信念、予測誤差、EFEコンポーネント、フリーエネルギー軌跡を可視化できること

---

## Assessment Components

| コンポーネント | 説明 | 頻度 |
|---|---|---|
| 練習クイズ | パートA：7つの選択肢＋パートB：各モジュールで3つの自由記述（コードの理解） | 毎週（合計8件） |
| コーディングラボ | コードの実行を含む実践的な実装 | 毎週（合計8件） |
| 調査問題 | 各モジュールあたり20個の計算問題 | 毎週（合計8件） |
| 最終プロジェクト | 拡張された実装プロジェクト | コースの終了時 |

### 最終プロジェクトのオプション

1.  **カスタム環境**: T-mazeまたはグリッドワールドではなく、特定の認知現象（例：採餌、社会的ジレンマ、知覚的競争）を示すActive Inferenceの新しい環境を設計および実装します。
2.  **多エージェントシステム**: Active Inferenceエージェント間の出現するコミュニケーション、協力、または競争を示す多エージェントシミュレーションを構築します。
3.  **ベンチマーク研究**: Q-learning、SARSAなどの強化学習のベースラインと比較して、標準的なタスクでActive Inferenceエージェントの効率性、探索行動、および漸近的なパフォーマンスを測定します。
4.  **可視化ツール**: Active Inferenceエージェントの内部ダイナミクスをリアルタイムでインタラクティブに可視化するダッシュボードを構築します（信念、EFEコンポーネント、ポリシー確率、学習曲線）。

---

## Technical Setup

```bash
# Active Inferenceコースのディレクトリに移動
cd active_inference/04_computer_science/

# カスタムactive_inferenceライブラリはsrc/にあります
# Pythonパスに追加:
import sys
sys.path.insert(0, 'src')

# インストールを確認
from active_inference.agent import GenerativeModel, ActiveInferenceAgent
from active_inference.math import compute_vfe, compute_efe
from active_inference.visualization import plot_beliefs, plot_free_energy
```

### Dependencies

```bash
pip install numpy matplotlib scipy jupyter
```

---

## Resources

| リソース | 目的 |
|---|---|
| [Notation Table](../resources/notation_table.md) | 数学記号とコード変数間のマッピング |
| [Glossary](../resources/glossary.md) | 実装ノート付きの定義 |
| [References](../resources/references.md) | キーとなる論文とチュートリアルリファレンス |
| [Cross-Course Map](../resources/cross_course_map.md) | 他のコースの概念的な対応物へのナビゲーション |
| `src/active_inference/` | カスタムライブラリ：agent/, math/, visualization/サブパッケージ |
| [pymdp GitHub](https://github.com/infer-actively/pymdp) | この実装にインスパイアされた基礎となるライブラリ |
| [pymdp JOSS Paper](https://joss.theoj.org/papers/10.21105/joss.04098) | Heins et al. (2022) — pymdp の出版 |
