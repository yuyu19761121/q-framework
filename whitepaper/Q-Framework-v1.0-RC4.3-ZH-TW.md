# Q-Framework × Temporal Möbius
## 異構 AI 運算延續、原生生成與異質超級電腦神經網絡技術白皮書

**HAVEFUN AI Studio 技術研發**  
**Q-Framework v1.0 RC4.3｜2026 年 10 月 25 日｜繁體中文版**  
**編輯基準：**以 RC4.3 中文完整合併審閱版為基礎，保留 RC4.2 技術成果，增訂單卡運算實證。

> **證據分級原則：**本白皮書明確區分原生運算紀錄、同條件受控實驗、Owner 已回報但待原始收據歸檔的成果，以及仍在研發的長期目標。不同 Job、解析度、GPU 數、幀數、Steps、Seed、重試策略，不得混為相同條件效能對照。RTX 2080 Ti 22 GB 指**擴充記憶體後的 22,528 MiB 硬體**，非原廠 11 GB 版本。

## 摘要：先證明「單卡跑得動」，再研究「叢集跑得快」

HAVEFUN Q-Framework 不只是把四張 GPU 同時派工的調度器。它結合 Foundation-00 原生執行底版、MiniMax H3 的 Sampler／DiT／Attention Hook、QmRNA 運算及顯存壓力控制、CPU／GPU 狀態搬運、Render Segments（RS）分段執行，以及 Temporal Möbius 的數學化路線決策。最終研究目標是建立**異質超級電腦神經網絡**：讓不同能力、不同世代、不同作業系統的計算設備，透過可驗證任務、可復用狀態與決策回饋形成協作。

現有實驗應分成**兩條彼此獨立、同等重要的證據線**：

1. **單卡可完成性。**A0／A1 擴充 22GB RTX 2080 Ti 已實際執行 MiniMax H3 原生影片。Studio **#370／#371** 產出可解碼短片；另有 A0 **48 幀、24fps、14 Steps** 原生影片。**#365** 以**單張 A0** 串行完成十份 36 幀 RS，最終交付 **15 秒、360 幀** MP4，端到端耗時 **3 小時 12 分 08 秒**。原生 history 顯示期間有 **9 次 CUDA OOM**，後續重新提交整個 RS 才成功；因此這是**單卡多段完整成片**，不是單次原生 360 幀採樣，也不能說全程零 OOM。
2. **四卡完成時間與交付效率。**正式 Job **#361** 使用 A0／A1／B0／B1 四張獨立 RTX 2080 Ti 22GB，完成十個 H3 RS，交給 CPU 處理九處接縫，交付 **15.000 秒、360 幀、24fps、480×832** 影片，端到端 **14 分 37 秒**。原生 QmRNA Gate 有接入證據，但不能從最終成片推定本 Job 必然觸發 QFREEZE 或完整 QVRAM 卸載／還原。

**最有解釋力的同卡對照**之一發生在 2026 年 10 月 4 日：在同張 A1、同參考 Static／Seed、480×832、36 幀、24fps、10 Steps 的條件下，**未開 QmRNA Guard 的單卡基準路徑**在 Step 1 觸發 **PRE-OOM** 救援條件，未交出指定單 Worker MP4；**啟用 QmRNA Pre-step Guard** 後，系統回收可用 VRAM、走完十個 Steps 並成功產出 MP4。須明確指出：**PRE-OOM 是軟體保護條件，並不等於已發生 CUDA HARD_OOM**。此對照支持的是特定工作負載下「原本無法直接完成→調整運算路徑後完成」的可行性差異。

Owner 另已回報**單卡完成 H3 1080p** 的實績。本版將其記為**已回報成果／等待原生收據核驗**，不寫成尚未開始的未來目標；正式發布定量宣稱前，仍需對齊 Job、Prompt ID、Sampler 原生解析度（區別後製升頻）、幀數、耗時、OOM history、影片規格與 SHA。

### 代表性實測成果

| 項目 | 實驗／收據 | 結果與解釋邊界 |
|---|---|---|
| 跨 GPU 計算延續 | 20-step Sampler：GPU0 第 1–10 步→GPU1 第 11–20 步 | 對照結果位元一致，最大絕對差異 0.0 |
| 計算狀態搬運 | 約 250 MiB GPU→CPU→SharedMemory／Bridge→GPU | 來源、Bridge、目標 SHA-256 一致 |
| H3 原生控制 | Static 載體、DiT、Sampler Hook | 真實改變 checkpoint 週期，原生 `QMRNA_DIT_ENTER/EXIT` |
| QmRNA 同 Seed 對照 | 22 幀、同參考與 Seed | 22／22 解碼影格一致，單次 Sampler 視窗 81→76 秒 |
| 單卡 H3 原生短片 | #370／#371、A0 | 約 39 幀、16fps、2.437 秒的原生 MP4 |
| 單卡完整影片產線 | #365、A0 | 十段 36 幀→15 秒；含九次原生 OOM 後重投；3:12:08 |
| 四卡正式成片 | #361、四 GPU | 十段 H3 + CPU 九處接縫，15 秒、360 幀；14:37 |
| 分層記憶與暫停 | Q7 真 CUDA／QFREEZE 受控測試 | 獨立驗證 32 MiB 真實卸載回載及暫停接續 |
| Windows／Mac 協作 | 四 Windows Ollama、Mac LAN Math | 實際多腦對話、Mac 24／24 批驗算 |
| 數學與語言模型學習 | Möbius MLP、DistilGPT2 局部更新 | 各自有真實權重更新收據 |

---

## 一、系統定位與原生底版

### 1.1 運算延續不等於單純增加 GPU 數

傳統生成式 AI 工作流常把單次前向運算、固定執行節點與單張 GPU 的即時 VRAM，視為主要執行邊界。Q-Framework 研究如何讓**計算狀態**在相容條件下被識別、封存、雜湊驗證、搬運、還原與繼續使用；Temporal Möbius 則結合工作依賴、硬體資源、耗時及歷史結果評估可能的執行路線。

四張 22GB 顯卡合計約 **88GB 分散式實體 VRAM 資源**，但它們是**四個獨立工作者**，並不是一張「統一可直接定址的 88GB 顯卡」。真正的研究題目是：藉由新的運算路徑、狀態管理與分段調度，能否讓有限硬體完成原先執行失敗的特定 AI 工作，並在可拆分工作中改善整體交付效率？

### 1.2 Foundation-00：Master 與 Runtime 內嵌 Agent

Foundation-00 是早於新一代四 GPU JSON／Studio 控制介面的底層設計。Master 負責任務、資源與指令；內嵌於 H3／ComfyUI 的 Runtime Agent，於原生 ModelPatcher、Sampler、Attention、DiT 執行位置接受控制訊號並回報可核對收據。具體位置涵蓋 `HFQmRNAGate`、`HFQmRNAStaticLoader`、`ModelPatcher.set_model_patch_replace`、`optimized_attention` 與 Sampler Hook。

#341 的原生工作流記錄包括 `gpu_model_gate_present=true`、`gpu_model_gate_match=true`、`gpu_workflow_receipt_verified=true`。不能僅依後來新增的前台開關或 Heartbeat 缺失，否認原本已存在的原生 Q 系列接入能力。

### 1.3 異質硬體的實際分工

| 技術層 | 設備／環境 | 已完成的角色 |
|---|---|---|
| Studio／Owner | HAVEFUN AI Studio | 授權任務、進度、交付合約與成品入口 |
| Master | Windows YUYU3D | 排程、RS 收據、CPU 後製與母帶驗證 |
| 影片 GPU | Node A A0/A1、Node B B0/B1 | 四張獨立 RTX 2080 Ti 22GB 原生 H3 Worker |
| CPU／Bridge | QWorker、Compute Bridge | 分工計算、狀態傳輸、SHA 驗證與前後製 |
| Windows 多腦 | YUYU3D、Node A/B、Utility03 | 獨立 Ollama 問答與跨節點對話 |
| Mac Möbius | iMac、Mac mini M2、MacBook、第四台 M1 | LAN 數學分片、獨立驗算、MLP／LLM 實驗 |

此處的「異質」已涵蓋 CPU／GPU、作業系統與設備職責。**不同 GPU 世代間任意 H3 原生狀態恢復**仍是待完整驗證的研究目標。

## 二、Q-Framework 技術資產譜系

原始資產分為 Foundation-00 與 Q01–Q19。QMobius／Temporal Möbius、QMater／QMaster 等早期別名保留歷史脈絡，不把同名變體冒算為獨立第二套引擎。

| 索引 | 技術資產 | 功能與對應工程證據 |
|---|---|---|
| Foundation-00／Q13 | Runtime 內嵌代理 | Master→H3 原生 Gate／Sampler／DiT Hook→GPU 收據 |
| Q01 | QmRNA Gate | 將訊號送入 H3 模型；#341 Gate 存在、匹配及原生工作流驗證 |
| Q02 | QmRNA Flag Control | 依 Job／Seed／RS 設定 checkpoint、顯存門檻與 Pre-OOM；10/3 `checkpoint_every` 由 2 變 1 |
| Q03 | QVRAM | VRAM／CPU RAM／Bridge 分層；250 MiB 跨卡位元搬運與另次 32 MiB CUDA 卸載回載 |
| Q04 | QSTATIC／Motion Static | 參考影格、錨點、狀態描述；Static 載體與 22 幀對照 |
| Q05 | QFREEZE | 在可保存的運算邊界暫停與接續；B1 微型 Sampler Step 1→5 |
| Q06 | QAnswer／Finalizer | 以已算 checkpoint 建立答案包；受控 Finalizer 僅執行剩餘 Step |
| Q07 | QSearch | Worker、分支、結果與路線搜尋；四分支工作驗證 |
| Q08 | QRebuild | 將封存狀態還原為可計算 Tensor；PyTorch 精確往返 |
| Q09 | QSTATE | Step／Seed／Tensor 狀態封存、雙複本 ACK 與 SHA |
| Q10 | Temporal Möbius／QMobius | DAG 相依與預測式路線決策，利用原生結果持續評估 |
| Q11 | QMater／QMaster／RS | 將影片目標編為多個可追蹤時間段並派給 GPU |
| Q12 | FaceOff | 人物身份比較、臉部 QC 與局部 RS 重做 |
| Q14 | Drip Feed | 有界 QKV／FFN 分頁分塊，原生 H3 `ffn_chunk=512` |
| Q15 | Sampler Hook | 原生 Callback、Sampler／模型入口，不是另一套獨立加速器 |
| Q16 | Master Message Transport | Job／Prompt／Worker／Event／ACK／Receipt 對帳 |
| Q17 | CPU Frame Editor／PostEdit | CPU 接縫、幀數校正、FFmpeg 組裝，避免重新跑 GPU |
| Q18 | Mixed GPU／跨節點接力 | A0→B0 CUDA 接續、跨 GPU 位元一致與四卡 RS |
| Q19 | Studio Q-Framework Controls | Owner 前台控制、派工與監測；UI 開關不等於真 GPU 介入證據 |

周邊與延伸模組包括 HF Compute Bridge／Motion Bridge、QWorker Lite、Streamed-QKV／Page Attention、QBLOCK／QLINEAGE／QREV 研究原型、QBonus、Windows Möbius Brain、Mac Math Stream、Möbius Neural／LLM、Partner 節點身份中心及 Network Map。**已安裝、已載入、可觀測、實際參與 GPU 執行與可獨立驗證**是不同證據等級。

工作流可概括為：

~~~text
Studio / Director → Foundation-00 Master → Temporal Möbius 路線決策
  → RS 編譯與 QSearch / 合法 Worker 選擇
  → QmRNA Gate / QSTATIC / H3 原生 GPU Worker
  → RS 與 QSTATE 原生收據
  → CPU Frame Editor / FFmpeg
  → 時長、幀數、FPS、SHA 與交付確認
~~~

## 三、計算狀態延續：從 Tensor 到真實 H3

### 3.1 跨 GPU 20-Step 決定性運算

受控 Sampler 在 GPU0 計算 Step 1–10，經 CPU／RAM 封存，再於 GPU1 從 Step 11 計算至 20。最終與直接計算的對照結果達到 **bitwise identical**、`max_abs_diff=0.0`。移轉的是可延續的數值狀態，不只是 Prompt 或 RGB 圖片。

### 3.2 約 250 MiB 記憶狀態搬運

2026/9/28 將 262,144,000 bytes（約 250 MiB）沿 GPU0 VRAM → CPU RAM → Windows Named SharedMemory → HF Compute Bridge → GPU1 VRAM 移動，來源、Bridge 與目標讀回的 SHA-256 相同：

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

來源 GPU 測試 Tensor 刪除後，CUDA allocation 降為零。這證明指定資料的搬運與完整性，**不是**通用透明 88GB VRAM 池已完成。

### 3.3 原生 H3／跨主機延續

X1／Motion Bridge 已留下 H3 的 `RESTORE`、`SAMPLER_RESUME` 原生訊息，另有 B0 checkpoint → B1 restore → H3 影片輸出的受控路徑。2026/10/17 Q7 實驗由 A0 產出 CUDA `HF_SAMPLER_STATE_V1`，經 Bridge 雙複本與 SHA 驗證後由 B0 回載，並完成下一個受控 CUDA Step。上述成果不應延伸宣稱任意模型、任意異卡皆可無縫恢復。

## 四、QmRNA：真正進入原生模型的運算控制

### 4.1 Static 載體與 Sampler 行為更動

10/3 Static PNG iTXt `HF_QMRNA` 載體跨機 SHA 一致，A1 原生 Runtime 記錄 `QMRNA_CARRIER_LOADED`，實際將 `checkpoint_every=2` 改為 1，留下對應 checkpoint 與 `QMRNA_COMPLETE`。這是「CPU 訊號→載體傳遞→原生 GPU 讀取→Sampler 行為改變」的閉環證據。

### 4.2 H3 DiT Hook 真實進出

10/6 記錄原生 `QMRNA_DIT_ENTER`／`QMRNA_DIT_EXIT`；隱向量寬度 5,376、序列長度 36,988、FFN Chunk 512。此為真實 H3 模型路徑的事件，不只是網站開關或外部 `nvidia-smi` 監控。

### 4.3 相同 Seed 的 A/B 結果

| 原生 Sampler 視窗 | 基準 | QmRNA | 單次觀測 |
|---|---:|---:|---|
| 8 幀、4 Steps、同 Static／Seed | 約 34 秒 | 約 30 秒 | 快約 11.8% |
| 22 幀、10 Steps、同 Static／Seed | 約 81 秒 | 約 76 秒 | 快約 6.2% |

22 幀的 MP4 封裝 SHA 不同，但 **22／22 個解碼影格 framemd5 相同**。僅代表指定工作負載的單次觀測，不是所有模型均可固定加速的保證。

### 4.4 Pre-step Guard 顯存回收

強制 Guard 測試中，進入重負載 Step 前可用 VRAM 約 **460–492MB**，執行清理後增加至 **2,668MB**，22 幀／10 Steps 正常完成且未記錄 HARD_OOM。要區分「GPU 快取回收」與「真 CUDA Tensor 完整卸載回載」，兩者不應混為一談。

### 4.5 分頁 Attention 的數學一致性

Streamed-QKV 使用 Online Softmax，CPU 對照在 257 tokens × 4 heads × 32 head_dim 測試，最大絕對誤差約 **2.09×10⁻⁷～2.98×10⁻⁷**，各分塊組合通過 `allclose`。這支持受控數學算式一致性，非所有 H3 影片設定的通用保證。

## 五、QFREEZE／QVRAM／QSTATE／QAnswer 的數值閉環

2026/10/17 Q7 等獨立受控測試記錄：

- **同卡暫停與恢復：**B1 CUDA 微型 Sampler 於 Step 1 產生 `HF_QFREEZE_PAUSED`，恢復至 Step 5。
- **真 CUDA 卸載與回載：**8,388,608 個 float32 元素，合計 **33,554,432 bytes（32 MiB）**，沿 GPU→CPU／Bridge→GPU 移動，CUDA allocation 呈 **33,554,432→0→33,554,432**，SHA 一致且可繼續計算。
- **QSTATE 歸檔：**真 Sampler 狀態、兩份 Replica ACK、Bridge 歸檔、Master 遠端 SHA 讀回。
- **CPU QAnswer／QRebuild：**PyTorch 計算及 `torch.save/load` 精確 Roundtrip。
- **跨主機接續：**A0 原生 CUDA 狀態經 Bridge 交給 B0，完成下一個 CUDA 計算步驟。

這些是**不同實驗**；不能因整套系統具有 QFREEZE 等功能，就斷言 #361／#365 一定觸發過這些細節。

## 六、MiniMax H3：四卡影片產線

Node A／B 各有兩張獨立擴充 22GB RTX 2080 Ti，YUYU3D 處理 Master、CPU 後製及交付。

| 任務／日期 | 工作路徑 | 可驗證結果 |
|---|---|---|
| #135／9/29 | 四 GPU H3／Bridge／Rescue | 最終 15.000 秒、36fps、540 幀、母帶 SHA |
| #243／10/4 | 四 GPU 平行 QRS | 17 個 QRS 完成並發布 |
| #327／10/13 | 四 GPU 原生 H3、7／7 RS | 設定 10 秒、1080×1920；MP4 可存取；約 1:55:44 完成 |
| #341／10/16 | 舊原生 QmRNA Gate、10／10 RS | 原生 RS 約 11 分 18 秒；整體 Studio 約 34 分 18 秒，過程曾有 OOM 重試 |
| #344／10/17 | Temporal Möbius 雙島 RS 路線 | 10 RS 與最終 15 秒、360 幀 MP4 驗證 |
| #360／10/19 | 四 GPU 10 RS＋CPU 9／9 接縫 | 15 秒、360 幀，端到端 **15 分 01 秒** |
| **#361／10/19** | **四 GPU 10 RS＋CPU 9／9 接縫** | **15 秒、360 幀，端到端 14 分 37 秒** |
| T195／10/21 | 十份真正不同的 RS Prompt SHA | 10 RS、完整 15 秒、360 幀原生輸出 |

### #361 Golden Baseline

正式 Job 自 2026/10/19 **23:07:24 至 23:22:01（台灣時間）**，共 **877 秒**。GPU 階段於 23:21:07 收齊 RS；CPU 階段完成九處接縫、42.609 秒，收據標示 `gpu_invoked=false`。最終 H.264、**480×832、24fps、360 幀、15.000 秒**、解碼 PASS，SHA-256：

`a219bb7e78c0e4b0d74823c45d6b0458515583e351c785a686f5c56c424254d8`

相鄰 #360 總耗時 901 秒，#361 少 24 秒（2.66%）。這是正式端到端成績，不能當成單張 GPU 核心算力測試。

2026/10/23 RS PostEdit V2 另利用 #365 已存在的十份 RS 重編 360／360 幀、24fps，與原片 SSIM **0.984182**，且強制靜音輸出驗證。CPU 重剪不必重新執行所有 H3 GPU RS。

## 七、Studio 五模式與高階模型原生實測

2026/10/20 Studio #368～#372 均取得 Comfy 原生 history 與正式媒體結果：

| 模式 | 實際模型與節點 |
|---|---|
| 文生圖 | #368 SDXL、B1 |
| 圖生圖 | #369 SDXL、B1 |
| 文生影片 | #370 MiniMax H3、A0 |
| 圖生影片 | #371 MiniMax H3、A0 |
| 影片生影片 | #372 Wan VACE 1.3B、A0 |

#370／#371 是原生約 **39 幀／16fps／2.437 秒**短片，非單次 15 秒 H3 Sampler。其他測試包含 Qwen-Image-2512 FP8 文生圖、Qwen-Image-Edit-2511 FP8 圖生圖，以及 A0 上 **480×832、48 幀、24fps、14 Steps** 的 H3 文生影片（原生 GPU wall 約 **549.31 秒**）。#377 也有 Owner 審核的有效圖片編輯成果，但模型完成不等於所有商業品質與人物身份保真項目都已通過。

## 八、Windows Möbius 多腦實證

YUYU3D、Node A、Node B 與 Utility03 各自以 Ollama 回應 Studio 工作，具有獨立 Job 與實際跨節點對話。指定算術題原本 14B 模型的 Studio 模型延遲曾達 **66.186 秒**；隔離 CPU-only Qwen2.5 3B 服務後，記錄模型端 **1.094／1.265 秒**、Studio 建立至完成約 **4 秒**。這是模型／服務配置不同的同類簡單問題觀測，不能宣稱所有 AI 推理都獲得固定倍率加速。

## 九、Mac Möbius：多機 LAN 數學驗算

- **iMac：**Teacher／資料來源、矩陣前 128 列分片。
- **Mac mini M2：**Coordinator、後 128 列及中央合併。
- **MacBook Pro：**Evaluator、用獨立演算法重算整題。
- **Mac mini M1：**第四台 Owner Mac，實測額外 32×256 矩陣分片。

**MOBIUS-MATH-001：**256×256 整數矩陣測試，M2 與 MacBook 最終 SHA-256 一致。

**MOBIUS-MATH-002：**真 LAN 領工、iMac／M2 分算、MacBook 重算；三機各自實算時間約 **895.542／578.363／2,646.046 ms**（職責不同，不可直接當效能排行）。

**MOBIUS-MATH-STREAM-001：**24／24 筆不同 Seed／Job 均 VERIFIED；最新中央合併與參考 SHA：

`c8219ed9d202697cb93d771e8124d89d02e593fe8a297d89e80cda668cb88f57`

第四台 M1 亦完成被指定的部分矩陣計算，但不能由此推論四台 Mac 已成為通用型大模型聯合訓練超級電腦。

## 十、Temporal Möbius：模型式決策與真正權重更新

### 10.1 使用原生結果評估路線

Windows World Model 歷史回放使用 **41** 筆原生結果（24 Success、15 OOM、2 其他 Failed）。留時序評估 Brier Score **0.338335**，相對基準 **0.375438** 有改善。此為特定資料與設定下的預測能力，不是自主全域最佳排程已證實。

### 10.2 Möbius Neural：數學策略 MLP

以 **5×12×3** Tanh／Softmax MLP 選擇合成數學 Kernel。iMac 產生 54 筆訓練案例，M2 真正訓練 **95 Epoch**，Loss **1.083127→0.098988**；MacBook 在 **24 筆未見題**獨立評估，記錄最佳演算法選擇正確率 **91.7%**，該批合成題相對 Naive 的時間比較 **2.1161 倍**，並有權重雜湊改變。

### 10.3 Möbius LLM：預訓練模型局部學習

M2 MPS 的 DistilGPT2：總參數 **81,912,576**、當次可訓練 **7,089,408**；42 筆合成訓練、12 筆驗證、16 Steps、耗時 **18.71 秒**；Validation Loss **5.720391→5.176930**。產生約 28,362,810 bytes 權重檔及 SHA。這確實屬於局部權重訓練，但不能據此宣布完整自主通用 AI 已完成。

## 十一、Windows／Mac 混合協作的工程意義

HAVEFUN 不是把相同程式強制安裝到所有設備，而是以工作身份、數值狀態、原生運算收據與結果驗算，讓不同角色硬體在同一研究體系發揮作用。

重要主張不是「軟體讓 2080 Ti 在硬體頻寬上變成 H100／H200」，而是**改變可成功完成的任務集合**，進一步研究總交付時間、品質與成本的最佳路線。

## 十二、代表性證據與驗證方法

| 方法 | 原生收據或實驗 |
|---|---|
| 數學一致性 | 跨 GPU 20-Step `max_abs_diff=0.0`；Streamed-QKV 誤差約 2～3×10⁻⁷ |
| 位元完整性 | 250 MiB 狀態搬運三端 SHA 一致 |
| 原生模型事件 | `QMRNA_DIT_ENTER/EXIT`、#341 H3 Gate Receipt |
| 步驟接續 | QAnswer Finalizer 只計算剩餘 Step |
| CUDA 顯存 | 32 MiB allocation 33,554,432→0→33,554,432 |
| 解碼影格 | 22／22 幀 framemd5 相同 |
| MP4 合約 | #361：15.000 秒／360 幀／24fps／480×832 |
| CPU 剪輯 | GPU 不重算九處接縫；V2 重剪 360／360 幀、SSIM 0.984182 |
| Mac LAN 數學 | 24／24 批跨機獨立驗算 |
| 真實權重更新 | MLP 95 Epoch、DistilGPT2 16 Steps |

原始 Owner 素材、私人 Prompt、金鑰、授權資訊及客戶媒體不列入公開文件。

## 十三、結語：運算可完成性本身就是研發成果

Q-Framework 的核心價值，不只在 GPU 分配效率，更在於研究**如何讓已有硬體完成原本無法成功交付的高負載任務**。工程實證從單張擴充 22GB 2080 Ti 執行 H3、同張 A1 的 QmRNA PRE-OOM 對照，延伸至 #361 四 GPU 高效率產線、數值狀態接續、多機數學與局部權重學習。

Temporal Möbius 的決策方向是：**過去收據→預測候選未來路線→現在的硬體與運算選擇→實際結果→更新經驗**。這是朝向異質超級電腦神經網絡的工程路線，但不同代 GPU 全面相容、全網持續自主學習與對高階卡的嚴格超越比較仍須實測。

**Q-Framework — Connecting Compute. Extending Possibility.**

---

## 附錄 A｜公開技術索引

- [前版公開白皮書 RC3（繁體中文）](Q-Framework-v1.0-RC3-ZH-TW.md)
- [Validated Execution Paths](../docs/validated-execution-paths.md)
- [Public Claim Ledger](../docs/claim-ledger.md)
- [Architecture Overview](../docs/architecture.md)

## 附錄 B｜內部測試收據對照索引

只列任務識別，不對外揭露私人工作流、照片、原始 Prompt、節點金鑰與客戶資料。

- 狀態搬運：HF Compute Bridge F-Block XCOPY（2026/9/28）、Q7 Integration（2026/10/17）。
- QmRNA／QSTATIC：10/3 PNG iTXt、10/4 A1 A/B、DiT Job #303、#341 Gate。
- H3 影片：#135、#243、#327、#341、#344、#360、#361、#365、#370、#371、T195。
- Windows 多腦：10/15 Möbius Brain Chat／四節點 Ollama 收據。
- Mac：MATH-001／002／STREAM-001、MOBIUS-EIGHT-001、NEURAL-001、LLM-001。
- CPU：HF_RS_POSTEDIT_V2_IMPLEMENTED（2026/10/23）。

## 附錄 C｜單張 RTX 2080 Ti 22GB 的 H3 能力

**增訂理由：**RC4.2 第六章以多卡生產為主，RC4.3 將單卡成果獨立列證據。A0／A1 的「單卡」指原生 H3 GPU 推論只在一張顯卡上執行；仍可有必要的 CPU 後製與一般檔案傳輸。

| 案例 | 單卡證據 | 範圍與限制 |
|---|---|---|
| #370／#371 | A0 原生 H3 文生／圖生影片 MP4 | 約 39 幀、16fps、2.437 秒，非 15 秒 |
| 10/21 48 幀 H3 | A0、480×832、24fps、14 Steps、約 549.31 秒 | 原生 2 秒影片 |
| #365 | A0 串行十份 36 幀 RS，最終 15 秒、360 幀影片 | 3:12:08，九次 CUDA OOM 後重送對應 RS |
| #361（另案） | 四張 RTX 2080 Ti | 不同 8-Step 工作條件，14:37 交付 |

**單卡 1080p 證據狀態：**Owner 回報已成功完成單卡 H3 1080p；此項保留為**已回報但待核對原生工作收據**。必要資料為 Job ID、原生 Sampler 寬高、是否升頻、幀數、耗時、OOM History、FFprobe、影片 SHA。不能把 480p 產物升頻後冒稱原生 1080p，也不能把尚未歸檔理解成 Owner 尚未達成。

## 附錄 D｜從 Pre-OOM 未完成，到同卡運算完成

**日期：**2026/10/4。**硬體：**A1 擴充 22,528 MiB RTX 2080 Ti。**對照條件：**同 Static、Seed、480×832、24fps、36 幀、10 Steps。

- **未開 QmRNA Guard 基準路徑：**Step 1 可用 VRAM 約 **108MB**，觸發 `RESCUE_ARMED reason=PRE_OOM`，沒有產出指定單 Worker MP4。
- **啟用 QmRNA Guard：**Step 1–9 前顯存壓力一度使可用量降至 **76–140MB**，Guard 回收快取後增至約 **3,212–3,244MB**，完成所有 10 Steps，產出 **188,242 bytes** MP4，該輪未記錄 HARD_OOM。
- **另一單卡 Guard：**22 幀／10 Steps，可用 VRAM **460–492MB→2,668MB**，正常完成。
- **原生控制：**DiT ENTER／EXIT 與 `ffn_chunk=512` 已有真 GPU 日誌。

**解讀：**這是特定工作負載下「基準 PRE-OOM 無法直接交付→QmRNA Guard 路徑可完成」的可行性證明；不等於所有未安裝 Q 系列的 2080 Ti 任何 H3 工作都會 HARD_OOM，也不代表所有啟用 Guard 的工作永不 OOM，更不能把獨立 32 MiB 真 CUDA 卸載測試直接歸因於本次 H3 運算。

## 附錄 E｜最終願景：異質超級電腦神經網絡

1. **原生執行層：**Foundation-00／QmRNA 對 Sampler、DiT、Attention 提供原生控制。
2. **狀態與記憶層：**QVRAM／QSTATIC／QSTATE／QFREEZE 形成可驗算的封存、搬運、回載與延續機制。
3. **跨節點協作層：**QSearch／QWorker／RS／Compute Bridge 協調單卡、四卡與跨 Windows／Mac 的不同工作。
4. **數學決策與學習層：**Temporal Möbius 依歷史結果預測可行路徑，評估風險、時間及資源，根據真實結果修正。

**已驗證：**QmRNA 受控單卡 A/B、原生單卡 H3 影片、#365 單卡多段 15 秒（含 OOM 重試）、#361 四卡、CUDA 狀態實驗、Mac LAN 數學與小型 MLP 學習。

**尚待通用化：**任意不同世代 GPU 的原生 H3 狀態接續、全網可信自主決策與持續學習、同條件 H100／H200 嚴格效能比較。

評估異質超級電腦神經網絡的指標，應包括**任務可完成性、數值狀態完整性、決策品質、影片品質、端到端時間，以及整體資源成本**，不能只看 GPU 顯存總和。
