# 計算活性推論 — 試行ガイドライン

> **クイックナビゲーション**: [README](./README.md) | [シラバス](./syllabus.md) | [コース・エージェントガイドライン](../AGENTS.md) | [リソース](../resources/)

## 概要

このコース（計算機科学）に取り組むエージェントは、すべてのコンテンツを**計算**的な視点からアプローチしつつ、コース全体の表記、用語、形式基準を維持する必要があります。

---

## ディレクトリの内容

| パス | タイプ | 説明 |
|------|------|-------------|
| `README.md` | ファイル | コース概要とナビゲーション |
| `AGENTS.md` | ファイル | このコース固有のエージェントガイドライン |
| `syllabus.md` | ファイル | スケジュールと評価を含む完全なコースシラバス |
| `src/` | ディレクトリ | `active_inference` Python パッケージ (v0.4.0) — 3 つのサブパッケージ、56 個のエクスポート |
| `tests/` | ディレクトリ | pytest スイート — 253 個のテスト (エージェント、数学、可視化、設定、出力) |
| `output/` | ディレクトリ | 生成された可視化図 (テストスイートからの 30 個の PNG ファイル) |
| `01_systems/` | ディレクトリ | モジュール 1: システム — 生成的プロセス vs 生成的モデル (pymdp) |
| `02_agents/` | ディレクトリ | モジュール 2: エージェント — エージェントクラス: 状態、観測、A-E行列 |
| `03_perception/` | ディレクトリ | モジュール 3: 認識 — A-行列とB-行列を使用した状態推定 |
| `04_cognition/` | ディレクトリ | モジュール 4: 認知 — C-行列 (好み)、D-行列 (事前確率)、E-行列 (習慣) |
| `05_action/` | ディレクトリ | モジュール 5: 行動 — ポリシー選択と期待されるフリーエネルギーの計算 |
| `06_learning/` | ディレクトリ | モジュール 6: 学習 — パラメータ学習: ディリクレ濃度の更新 |
| `07_communication/` | ディレクトリ | モジュール 7: コミュニケーション — マルチエージェントシミュレーションとシグナリングゲーム |
| `08_planning/` | ディレクトリ | モジュール 8: 計画 — 深層時間モデル、グリッドワールド、長期計画 |

---

## ソースパッケージ: `active_inference` (v0.4.0)

### サブパッケージ

| サブパッケージ | モジュール | 主要なエクスポート |
|------------|--------|-------------|
| `agent` | `generative_model.py` | `GenerativeModel` (A, B, C, D, E行列) |
| `agent` | `agent.py` | `ActiveInferenceAgent` (知覚–行動ループ) |
| `agent` | `environment.py` | `DiscreteEnvironment` (生成的プロセス) |
| `math` | `free_energy.py` | `compute_vfe`, `compute_efe`, `softmax`, `entropy`, `kl_divergence` |
| `math` | `inference.py` | `run_state_inference` (変分固定点反復) |
| `math` | `learning.py` | `update_dirichlet_A/B`, `expected_A/B`, `bayesian_model_reduction` |
| `visualization` | `config.py` | `VizConfig`, `configure`, `get_config`, `reset_config` |
| `visualization` | `plotting.py` | 6 つの時間系列プロット関数 |
| `visualization` | `matrices.py` | 9 つの行列/モデル構造関数 |
| `visualization` | `diagnostics.py` | 8 つの推論診断関数 |
| `visualization` | `simulation.py` | 5 つのシミュレーション/環境関数 |

### 可視化構成

すべての 28 個の可視化関数は、中央の `VizConfig` データクラスから読み取られます。 実行時に構成します。

```python
from active_inference.visualization import configure
configure(output_dir="./output", dpi=150, font_size=18, cmap_probability="Blues")
```

キー構成可能なフィールド: `output_dir`, `dpi`, `font_size`, `title_size`, `label_size`, `tick_size`, `legend_size`, `annotation_size`, `fig_width`, `fig_height`, `cmap_probability`, `cmap_diverging`, `cmap_concentration`, `cmap_states`, `grid_alpha`, `save_format`, `style_overrides`.

---

## テストスイート

| ファイル | テスト | 目的 |
|------|-------|---------|
| `test_agent.py` | 18 | エージェントの作成、推論、行動、履歴 |
| `test_environment.py` | 17 | 環境ダイナミクス、エッジケース |
| `test_free_energy.py` | 27 | VFE/EFE 数学、KL、エントロピー、驚愕、MI |
| `test_generative_model.py` | 29 | モデルの構築、検証、予測 |
| `test_inference.py` | 14 | 状態/ポリシーの推論、MMP |
| `test_integration.py` | 7 | エージェント–環境のループの統合 |
| `test_learning.py` | 20 | ディリクレの更新、期待される行列、BMR |
| `test_visualization.py` | 87 | すべての 28 個の視覚化関数に対するスモークテスト |
| `test_visualization_output.py` | 27 | `output/` に図を生成 |
| `test_viz_config.py` | 7 | `VizConfig` のデフォルト値、`configure()`、出力パス |

すべての 253 個のテストを実行します: `python -m pytest tests/ -v`

---

## コース固有のコンベンション

- **視点**: すべてのコンテンツは、**計算**的な視点からフレーム化される必要があります。
- **ラボタイプ**: ラボは **コーディングラボ**形式を使用します—pymdpの実装、シミュレーション、Pythonを使用した可視化。
- **表記**: [リソース/notation_table.md](../resources/notation_table.md)を参照してください。
- **用語**: [リソース/glossary.md](../resources/glossary.md)を参照してください。
- **参照**: [リソース/references.md](../resources/references.md)を参照してください。

---

## コンテンツ生成基準

- すべてのコンテンツは**実用的な方法**を使用します—モック、スタブ、プレースホルダー実装はありません。
- モジュールコンテンツは**モジュール化され、関数型で、文書化**されている必要があります。
- 質問は各モジュールあたり**20個**で、単純な番号リストでフォーマットする必要があります。
- すべての 20 個の質問は**計算**的な視点から反映される必要があります。
- クイズには**パートA: 7個の選択肢** + **パートB: 3個の自由記述**が含まれます。
- ラボには**構造化された部分**があり、学習目標と `{fill:textarea}` などのフィールドがあります。
- ラボの要約テーブルには**完全でトリミングされていない**スキル記述が含まれます。
- ダッシュボードは**インタラクティブな HTML5** で動作する JavaScript を使用する必要があります。
- 関連するコースの他のモジュールへの参照は、相対パスを使用する必要があります。
- 可視化関数は中央の `VizConfig` を使用する必要があります—ハードコードされたスタイルは使用しません。
- すべての図は、アクセシビリティコンプライアンスのために ≥16pt のフォントサイズを使用する必要があります。

---

## 品質チェックリスト

このコースのモジュールを完了する前に：

- [ ] コンテンツは**計算**的な視点（一般的ではない）を反映している必要があります
- [ ] すべての 7 ファイルが存在し、内容が充実している必要があります
- [ ] プレースホルダーの角かっこ `[...]` は存在しません
- [ ]表記は `resources/notation_table.md` に一致します
- [ ]用語は `resources/glossary.md` に一致します
- [ ] ラボの要約テーブルは完全（トリミングされていない）です
- [ ] クイズの質問はモジュールの講義から答えられます
- [ ] 参照パスは正しい相対パスを使用します
- [ ] 可視化は `VizConfig` を使用します（ハードコードされたスタイルではありません）
- [ ] すべてのテストがパスします (`python -m pytest tests/ -v`)