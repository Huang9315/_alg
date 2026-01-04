

# 📚 EDA 電路優化算法學習筆記

## 1. 核心目標：PPA 權衡

在 EDA 流程的每個階段，優化算法的目標幾乎都圍繞著 **PPA** 進行權衡 (Trade-off)：

* **Performance (性能/時序):** 確保電路運作頻率達到要求，關鍵路徑 (Critical Path) 延遲最小化。
* **Power (功耗):**
* **動態功耗:** 與開關活動因子  和頻率  成正比 ()。
* **靜態功耗:** 漏電流 (Leakage Current)。


* **Area (面積):** 晶片面積越小，成本越低，良率通常越高。

---

## 2. 邏輯綜合階段 (Logic Synthesis)

這一階段將 HDL (Verilog/VHDL) 代碼轉換為邏輯閘 (Gate-level Netlist)。

### A. 布林邏輯優化 (Two-Level Logic Minimization)

這是布林代數的直接應用，目標是減少邏輯閘的數量和層級。

* **精確算法:** **Quine-McCluskey 算法** (適用於變數較少的情況，保證最優解)。
* **啟發式算法:** **Espresso 算法** (工業界標準)。它不保證全域最優，但能在多項式時間內處理大量變數。它通過 `Expand` (擴展)、`Irredundant` (去冗餘)、`Reduce` (縮減) 循環來優化。

### B. 多層邏輯優化 (Multi-Level Logic Optimization)

* 使用 **BDD (Binary Decision Diagrams, 二元決策圖)** 或 **AIG (And-Inverter Graphs)** 來表示邏輯功能。
* **代數運算:** 對邏輯表達式進行提取公因式 (Factoring)、替換 (Substitution) 和分解 (Decomposition) 來共享邏輯節點，減少面積。

### C. 工藝映射 (Technology Mapping)

將通用的布林邏輯門 (如 AND, OR) 映射到特定工藝庫 (Standard Cell Library，如 NAND2, NOR3, MUX)。

* **動態規劃 (Dynamic Programming):** 常用於樹狀結構的覆蓋問題，以最小代價 (面積或延遲) 覆蓋邏輯樹。

---

## 3. 物理設計階段 (Physical Design)

這是算法最密集、最複雜的階段，屬於 NP-Hard 問題。

### A. 佈局規劃 (Floorplanning)

確定各個模塊 (Modules) 的形狀和位置。

* **數據結構:** **B*-Tree (B-star Tree)** 或 **Sequence Pair** 用來表示模塊的拓撲關係。
* **優化算法:** **模擬退火 (Simulated Annealing, SA)** 是主流。
* 通過隨機擾動 (旋轉模塊、交換位置) 並以一定機率接受較差解 (Metropolis 準則) 來跳出局部最優 (Local Optima)。



### B. 佈局 (Placement)

決定數百萬個標準單元 (Standard Cells) 的具體坐標。

* **解析法 (Analytical Placement):**
* 將離散的佈局問題轉化為連續的數學優化問題。
* **力導向算法 (Force-Directed):** 模擬彈簧系統，連線產生引力，單元重疊產生斥力，求解系統平衡態。
* 求解大型線性方程組或使用梯度下降法。


* **最小割 (Min-Cut / Partitioning):**
* 使用 **KL 算法 (Kernighan-Lin Algorithm)** 或 **FM 算法 (Fiduccia-Mattheyses)** 將電路遞歸分割，減少分區之間的連線數。



### C. 佈線 (Routing)

在金屬層上連接各個引腳，且不能短路或違反設計規則 (DRC)。

* **全局佈線 (Global Routing):** 規劃大致路徑，評估擁塞 (Congestion)。
* **Steiner Tree (史泰納樹):** 尋找連接多個點的最短路徑樹 (比最小生成樹 MST 更優，因為允許引入額外的史泰納點)。


* **詳細佈線 (Detailed Routing):** 確定具體的導線軌跡。
* **迷宮路由 (Maze Routing / Lee's Algorithm):** 基於 BFS (廣度優先搜索)，保證找到最短路徑，但內存消耗大。
* **A* Search:** 引入啟發函數 (Heuristic Function) 加速搜索。



---

## 4. 時序優化 (Timing Optimization)

* **Retiming (重定時):** 在組合邏輯中移動暫存器 (Registers) 的位置，以平衡各級流水線的延遲，提高時脈頻率，而不改變電路邏輯功能。
* **Buffer Insertion (緩衝器插入):** 在長連線上插入 Buffer 以增強信號驅動能力，減少延遲 (Elmore Delay 模型)。

---

## 5. 前沿趨勢：機器學習在 EDA 的應用 (ML-EDA)

傳統算法依賴人工設計的啟發式規則 (Heuristics)，現在趨勢是利用數據驅動。

* **擁塞預測:** 使用 CNN (卷積神經網絡) 分析佈局圖，提前預測哪些區域在佈線階段會擁塞。
* **強化學習佈局 (Reinforcement Learning for Placement):** 如 Google 的 **DREAMPlace** 或 **Graph Placement**，將佈局視為遊戲，讓 Agent 學習如何擺放單元以獲得最佳 PPA。

---

💡 總結表
| 設計階段 | 關鍵問題 | 常用核心算法 |
| :--- | :--- | :--- |
| **邏輯綜合** | 布林函數化簡 | Quine-McCluskey, Espresso, BDD |
| **佈局規劃** | 模塊擺放 (幾何封裝) | 模擬退火 (Simulated Annealing), B*-Tree |
| **佈局** | 數百萬單元定位 | 力導向 (Force-Directed), 最小割 (FM Algorithm) |
| **佈線** | 多點連線路徑 | Dijkstra, A*, Steiner Tree |
| **時序** | 關鍵路徑優化 | Retiming, Buffer Insertion |
---

