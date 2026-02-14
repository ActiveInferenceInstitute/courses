# Course 2: Cognitive Behavioral Science & Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md) | [Resources](../resources/) | [Agent Guidelines](./AGENTS.md)

## Course Description

このコースでは、Active Inference の実装方法と、その表現方法が行動にどのように現れるかを検討します。Course 1 の哲学的な基盤を基盤として、予測、精度、注意の神経基盤を調査します。また、知覚、運動制御、学習の神経科学、精神医学および神経学における臨床応用、そして幼少期から成人期への発達軌跡を探求します。各モジュールは、Active Inference 理論を認知神経科学、行動心理学、臨床科学の経験的調査と関連付けます。

---

## Prerequisites

- Course 1: The Philosophy of Active Inference (または、マルコフ・ブランケット、生成モデル、フリーエネルギー、知覚-行動ループに関する十分な知識)
- 神経科学の用語に関する基本的な知識（ニューロン、シナプス、皮質など）は役立つが必須ではない。必要な場合は、キー用語が導入される

---

## Course Schedule

| 週 | モジュール | トピック | キーコンセプト | 経験的焦点 | 成果物 |
|------|--------|-------|--------------|-----------------|-------------|
| 1 | [Module 1](./01_systems/) | **システム** | 神経集塊、皮質列、脳-体-環境ループ | fMRI resting-state ネットワーク; Friston (2005) | Lab 1, Quiz 1 |
| 2 | [Module 2](./02_agents/) | **エージェント** | 自己モデル、内臓感、島皮質、自我境界 | Seth (2013); Tsakiris (2010) | Lab 2, Quiz 2 |
| 3 | [Module 3](./03_perception/) | **知覚** | 予測符号化、感覚減衰、幻覚 | Rao & Ballard (1999); Powers et al. (2017) | Lab 3, Quiz 3 |
| 4 | [Module 4](./04_cognition/) | **認知** | 精度重み付け、神経調節、ADHD、自閉症スペクトラム | Feldman & Friston (2010); Lawson et al. (2014) | Lab 4, Quiz 4 |
| 5 | [Module 5](./05_action/) | **行動** | 運動推論、小脳、習慣、運動障害 | Adams et al. (2013); Friston et al. (2011) | Lab 5, Quiz 5 |
| 6 | [Module 6](./06_learning/) | **学習** | シナプス可塑性、ドーパミン、睡眠固持 | Friston et al. (2017); Hobson & Friston (2012) | Lab 6, Quiz 6 |
| 7 | [Module 7](./07_communication/) | **コミュニケーション** | ミラーニューロン、メンタルリング、TPJ、自閉スペクトラム | Friston & Frith (2015); Kilner et al. (2007) | Lab 7, Quiz 7 |
| 8 | [Module 8](./08_planning/) | **計画** | PFC, デフォルトモードネットワーク, 実行機能, プロスペクション | Pezzulo et al. (2018); Buckner et al. (2008) | Lab 8, Quiz 8, Final Project |

---

## Learning Objectives

このコースの終了時には、以下のことができるようになることが期待されます。

1. **特定する**: 予測、精度、モデル更新といったキー Active Inference プロセスに関連する神経基盤
2. **説明する**: 視覚皮質における予測符号化が変分推論をどのように実装しているかを
3. **分析する**: ADHD、自閉症、統合失調症、不安、うつ病といった臨床状態を、精度またはモデル更新の特定のアバーレーションとして
4. **記述する**: シナプス可塑性、神経調節、睡眠が Active Inference の学習ダイナミクスをどのように実装しているかを
5. **適用する**: fMRI、EEG、行動研究からの経験的調査を解釈するために Active Inference の枠組みを使用する
6. **評価する**: 脳機能または行動に関する Active Inference の統一理論としての強みと限界

---

## Assessment Components

| コンポーネント | 説明 | 頻度 |
|-----------|-------------|-----------|
| Practice Quizzes | Part A: 7 multiple choice + Part B: 3 free response per module | 毎週 (8 回) |
| Case Study Labs | 臨床症例分析、実験データ解釈、神経地図作成 | 毎週 (8 回) |
| Study Questions | 各モジュールあたり 20 の認知科学に焦点を当てた質問 | 毎週 (8 回) |
| Final Project | 経験的統合論文または臨床症例ポートフォリオ | コース終了時 |

### Final Project Options

1. **Clinical Case Portfolio**: Active Inference のレンズを通して 3 つの臨床状態を分析し、各状態に対する提案された精度またはモデルアバーレーションを特定する
2. **Empirical Review**: Active Inference の予測をテストする 5-7 篇の経験的論文をレビューし、証拠の強さを評価する
3. **Experimental Proposal**: Active Inference の特定の予測に関する脳機能または行動の実験を設計する

### Evaluation Focus

| 基準 | 説明 |
|-----------|-------------|
| Conceptual accuracy | 正しい神経科学および Active Inference の用語の使用 |
| Empirical integration | fMRI、EEG、行動、臨床データからの証拠の統合 |
| Critical evaluation | Active Inference の説明の強みと限界の評価 |
| Clarity of writing | 論理的な議論と明確なコミュニケーション |

---

## Course Policies

- **Participation**: 各モジュールのラボアクティビティ（臨床症例ディスカッションと実験データの解釈を含む）に積極的に参加する必要があります。
- **Academic Integrity**: すべての書面はオリジナルのものでなければなりません。[references.md](../resources/references.md) から参照番号を使用してすべてのソースを適切に引用してください。
- **Accessibility**: すべての資料は Markdown 形式で提供されています。インタラクティブなダッシュボードは補助的なものであり、必須ではありません。

---

## Recommended Supplementary Reading

- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press. — Chapters 3-6 (neural implementation)
- Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Faber & Faber. — Accessible treatment of predictive processing and interoception
- Clark, A. (2016). *Surfing Uncertainty: Prediction, Action, and the Embodied Mind*. Oxford University Press. — Chapters 3-7 (neural mechanisms)

---

## Resources

| Resource | Purpose |
|----------|---------|
| [Notation Table](../resources/notation_table.md) | 規範的な記号と形式的な記法 |
| [Glossary](../resources/glossary.md) | 技術用語の定義 |
| [References](../resources/references.md) | トピックごとに整理された 82 個の規範的な引用 |
| [Cross-Course Map](../resources/cross_course_map.md) | 他のコースの並行モジュールにナビゲートする |
