# 計算的能動的推論

> **快速導航**: [課程主頁](../README.md) | [大綱](./syllabus.md) | [代理人規範](./AGENTS.md) | [資源](../resources/)

## 概述

使用自定義 `active_inference` 庫 (靈感來自 pymdp) 在 Python 中實現能動的推論算法。涵蓋生成模型規範（A-E 矩陣）、信念更新、通過期望自由能量的策略選擇、參數學習、多代理人模擬和深度時間規劃。所有代碼都是可執行的並且經過充分的文檔說明。

---

## 模組

| # | 主題 | 標題 | 描述 |
|---|-------|----------|-------------|
| 1 | [系統](./01_systems/) | 生成過程與生成模型在 pymdp 中的關係 | 環境設置。生成過程與生成模型。pymdp 安裝和基本用法。 |
| 2 | [代理人](./02_agents/) | 代理人類：狀態、觀測和 A-E 矩陣 | 代理人類初始化。A-E 矩陣規範。pymdp API 走訪摸管。 |
| 3 | [感知](./03_perception/) | A-矩陣和 B-矩陣的狀態估算 | A-矩陣的似然性。B-矩陣的轉換。信念更新的實施。後驗視覺化。 |
| 4 | [認知](./04_cognition/) | C-矩陣（偏好）、D-矩陣（先驗）、E-矩陣（習慣） | 偏好規範。先驗信念。習慣形成。精確度調整。 |
| 5 | [行動](./05_action/) | 策略選擇和期望自由能量計算 | 計算 G(π)。策略選擇。T-迷宮的實施。探索與利用。 |
| 6 | [學習](./06_learning/) | 參數學習：更新狄利克雷濃度 | pA 和 pB 的更新。線上學習循環。多集數訓練。行為視覺化。 |
| 7 | [通信](./07_communication/) | 多代理人模擬和信號遊戲 | 多代理人 pymdp。觀察其他代理人。信號遊戲。通信的產生。 |
| 8 | [規劃](./08_planning/) | 深度時間模型、格網世界和長程規劃 | 多步驟規劃。格網世界實施。帶有延遲獎勵的 T-迷宮。時間深度。 |

---

## 模組內容

每個模組資料夾包含 7 個文件：

| 文件 | 描述 |
|------|-------------|
| `module.md` | 從計算角度的完整課程內容 |
| `questions.md` | 20 個學習問題（計算角度） |
| `practice_quiz.md` | 測驗：A 部分多項選擇題（7題） + B 部分自由回答題（3題） |
| `lab.md` | 編碼實驗室 lab：使用 Python 的 pymdp 實施、模擬和視覺化 |
| `dashboard.html` | 帶有概念卡和測驗的互動式 HTML5 儀錶板 |
| `README.md` | 模組概述，包含跨參考 |
| `AGENTS.md` | 代理人規範，用於內容生成 |

---

## 原始代碼：`active_inference` Python 包 (v0.4.0)

`src/active_inference/` 目錄是一個自包含的 Python 包，提供實際測試的能動推論算法的實現。使用 `pip install -e src/` 安裝。

### 包結構

```text
src/active_inference/
├── __init__.py              # 頂層重新導向 (56 個符號：4 個類，48 個函數，3 個配置，1 個常量)
├── agent/
│   ├── generative_model.py  # GenerativeModel 類 (A, B, C, D, E 矩陣)
│   ├── agent.py             # ActiveInferenceAgent (感知–行動循環)
│   └── environment.py       # DiscreteEnvironment (生成過程)
├── math/
│   ├── free_energy.py       # VFE, EFE, softmax, 熵, KL 散度
│   ├── inference.py         # 變分狀態推論 (固定點迭代)
│   └── learning.py          # 狄利克雷更新，期望的 A/B，BMR
└── visualization/
    ├── config.py            # VizConfig 數據類 (運行時可配置的樣式)
    ├── plotting.py          # 觀測，VFE，預測誤差，策略 (6 個函數)
    ├── matrices.py          # A/B/C/D/E 矩陣熱圖，模型摘要，圖形 (9 個函數)
    ├── diagnostics.py       # 收斂性，VFE/EFE 組分，BMR (8 個函數)
    └── simulation.py        # 儀錶盤，軌跡，T-迷宮，格網世界 (5 個函數)
```

### 配置

所有視覺化樣式都通過 `VizConfig` 在運行時配置：

```python
from active_inference.visualization import configure, get_config

# 定制輸出
configure(
    output_dir="./output",
    dpi=150,
    font_size=18,
    cmap_probability="Blues",
    save_format="pdf",
)

# 讀取當前設置
cfg = get_config()
print(cfg.output_dir, cfg.dpi)
```

#### 可配置字段

| 字段 | 默認值 | 描述 |
|-------|---------|-------------|
| `output_dir` | `./output` | 默認保存圖形的目錄 |
| `dpi` | `100` | 圖形分辨率 |
| `font_size` | `16` | 基礎字體大小（≥16 以便可訪問） |
| `title_size` | `18` | 標題字體大小 |
| `label_size` | `16` | 軸標籤大小 |
| `tick_size` | `14` | 刻度標籤 |
| `legend_size` | `14` | 圖例文本 |
| `annotation_size` | `14` | 內核註釋 |
| `fig_width` | `10.0` | 默認圖形寬度（英寸） |
| `fig_height` | `6.0` | 默認圖形高度（英寸） |
| `cmap_probability` | `YlOrRd` | 概率矩陣的顏色映射 |
| `cmap_diverging` | `RdBu_r` | 偏移值顏色映射 |
| `cmap_concentration` | `viridis` | 狄利克雷濃度顏色映射 |
| `save_format` | `png` | 默認文件擴展名 |
| `style_overrides` | `{}` | 額外的 matplotlib rcParams |

### 視覺化函數 (28)

| # | 函數 | 模塊 | 描述 |
|---|----------|--------|-------------|
| 1 | `plot_beliefs` | plotting | 觀測 q(s) 在時間上的演化 |
| 2 | `plot_free_energy` | plotting | VFE 軌跡 |
| 3 | `plot_prediction_errors` | plotting | 預測誤差條 |
| 4 | `plot_policy_values` | plotting | EFE 值 |
| 5 | `plot_efe_decomposition` | plotting |  ryzy + ambiguity 分解 |
| 6 | `plot_learning_progress` | plotting | KL 散度學習曲線 |
| 7 | `plot_matrix_heatmap` | matrices | 通用標記熱圖 |
| 8 | `plot_A_matrix` | matrices | 似然性 P(o\|s) 熱圖 |
| 9 | `plot_B_matrix` | matrices | 轉換 P(s'\|s,a) 熱圖 (s) |
| 10 | `plot_C_preferences` | matrices | 偏好 P(c) 條形圖 |
| 11 | `plot_D_prior` | matrices | 先驗信念 P(s₀) 條形圖 |
| 12 | `plot_E_habits` | matrices | 習慣先驗 P(π) 條形圖 |
| 13 | `plot_model_summary` | matrices | A/B/C/D 總結多面板 |
| 14 | `plot_B_transition_graph` | matrices | 從 B 矩陣的定向圖 |
| 15 | `plot_dirichlet_concentration` | matrices | pA 先驗 vs 學習到的 |
| 16 | `plot_convergence` | diagnostics | 推論收斂曲線 |
| 17 | `plot_vfe_components` | diagnostics | VFE 組分 (複雜度 − 精確度) |
| 18 | `plot_efe_components` | diagnostics | EFE 組分 (風險 + 歧義) |
| 19 | `plot_precision_sweep` | diagnostics | q(π) 在 γ 值上 |
| 20 | `plot_entropy_trajectory` | diagnostics | H[q(s)] 在時間上 |
| 21 | `plot_surprise_trajectory` | diagnostics | S(o) = −ln p(o) |
| 22 | `plot_dirichlet_learning` | diagnostics | pA 學習到真實的 A |
| 23 | `plot_bmr_results` | diagnostics | BMR ΔF 條形圖 |
| 24 | `plot_simulation_dashboard` | simulation | 5 面板模擬儀錶盤 |
| 25 | `plot_environment_trajectory` | simulation | 狀態/觀測/行動軌跡 |
| 26 | `plot_agent_vs_environment` | simulation | 觀測 vs 實際狀態 |
| 27 | `plot_tmaze` | simulation | T-迷宮佈局渲染器 |
| 28 | `plot_gridworld` | simulation | 使用障礙物和路徑的格網世界 |

---

## 輸出目錄

`output/` 接收所有生成的圖形，當運行測試時生成。每個圖形名為 `##_description.png`（例如 `01_beliefs.png`）。 運行輸出套件：

```bash
cd 04_computer_science
python -m pytest tests/test_visualization_output.py -v
```

這生成 30 個 PNG 文件，使用分析準確的合成數據。

---

## 測試

```bash
# 運行所有測試 (253 個測試)
python -m pytest tests/ -v

# 運行僅測試視覺化輸出
python -m pytest tests/test_visualization_output.py -v

# 運行僅單元測試
python -m pytest tests/ --ignore=tests/test_visualization_output.py -v
```

| 測試文件 | 測試 | 描述 |
|-----------|-------|-------------|
| `test_agent.py` | 18 | 代理人創建、狀態推論、行動選擇、預測誤差、歷史 |
| `test_environment.py` | 17 | 環境創建、動力學、歷史追蹤、邊界情況 |
| `test_free_energy.py` | 27 | VFE/EFE 數學準確性、KL 散度、熵、驚奇值、MI |
| `test_generative_model.py` | 29 | GenerativeModel 構建、驗證、對數似然性、預測 |
| `test_inference.py` | 14 | 狀態/策略推論收斂、邊界訊息傳遞 |
| `test_integration.py` | 7 | 代理人–環境端到端模擬循環 |
| `test_learning.py` | 20 | 狄利克雷 A/B/D 更新、期望矩陣、熵、BMR |
| `test_visualization.py` | 87 | 煙霧/內容測試，用於 28 個視覺化函數 |
| `test_visualization_output.py` | 27 | 輸出測試，生成到 `output/` 中的圖形 |
| `test_viz_config.py` | 7 | VizConfig 默認值、configure()、輸出路徑、樣式覆蓋 |

---

## 預備條件

哲學、認知科學、數學課程 1-3 個。 Python 編程經驗（NumPy、基本 OOP）。 安裝自定義庫：`pip install -e src/`。

---

## 關鍵參考

- Heins 等人 (2022) pymdp: A Python library for active inference (JOSS)
- Sajid 等人 (2021) 能動推論：被解密並比較
- Smith 等人 (2022) 能動推論的逐步教程
- Da Costa 等人 (2020) 在離散狀態空間上進行能動推論
- pymdp 文檔：github.com/infer-actively/pymdp

請參閱 [資源/references.md](../resources/references.md) 以獲取完整的參考文獻列表，包含 82 個標準引文。

---

## 交叉參考

這門課是 4 門課中的一門。 每行下方都從不同的角度涵蓋相同的內容：

| 課程 | 觀點 | 實驗類型 |
|--------|-------------|----------|
| [哲學](../01_philosophy/) | 哲學基礎 | 思維實驗 |
| [認知科學](../02_cognitive_science/) | 神經和行為相關性 | 用例分析 |
| [數學](../03_math/) | 形式推導和證明 | 推導練習 |
| [計算機科學](../04_computer_science/) | 使用 pymdp 的 Python 實現 | 編碼實驗室 |

請參閱 [資源/cross_course_map.md](../resources/cross_course_map.md) 以獲取完整的交叉課程導航地圖，其中包含指向所有 32 個模塊的鏈接。

---

## 共享資源

| 資源 | 描述 |
|----------|-------------|
| [符號表](../resources/notation_table.md) | 所有課程中使用的標準符號 |
| [詞彙表](../resources/glossary.md) | 50+ 個術語的定義，以及每個課程的使用 |
| [參考文獻](../resources/references.md) | 按照主題組織的 82 個標準引文 |
| [交叉課程地圖](../resources/cross_course_map.md) | 鏈接到其他課程中的所有 32 個模塊 |

---

## 文檔

| 文件 | 描述 |
|----------|-------------|
| [大綱](./syllabus.md) | 包含時間表、學習目標和評估的課程大綱 |
| [代理人規範](./AGENTS.md) | 針對這門課程的代理人規範 |
| [../README.md](../README.md) | 課程概述和學習途徑 |
| [../AGENTS.md](../AGENTS.md) | 課程範圍內的標準和規範 |