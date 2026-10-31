# Q-Framework × Temporal Möbius

**語言版本：** [English](README.md) · **繁體中文** · [日本語](README.ja.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

**單張 RTX 2080 Ti 的 H3 成功實例 · 四卡高速交付 · 異質超級電腦神經網絡**

HAVEFUN 的 Q-Framework **不只是多卡 GPU 系統**。我們已經在**單張擴充至 22GB 的 RTX 2080 Ti** 上，實際成功執行 MiniMax H3 原生影片生成。QmRNA 的顯存壓力管理、狀態延續與 Temporal Möbius 決策，同時研究「原本無法完成的任務如何變成可完成」以及「異質節點如何協同提高整體效率」。

### 2026/10/31 最新成果｜防 OOM × 運算重生，原生 4K AI 影片成功產出

**我們不只成功推動原生 4K H3 運算，也已將防止 OOM 與跨設備運算恢復的技術成果帶到真正的影片交付。原生 4K 等級 MP4 已成功生成，並完成影片完整性驗證。** 這是 Q-Framework × Temporal Möbius 從突破硬體限制走向運算持續性的實際成果。[閱讀發明者白皮書 RC4.5](whitepaper/Q-Framework-v1.0-RC4.5-ZH-TW.md)。

### 系統意外斷電後，跨 GPU 原生運算重生完整性：PASS

**HAVEFUN Temporal Möbius 已完成原生 H3 運算狀態跨 GPU 恢復驗證：移轉前後 SHA-256 完全一致、異地副本 2/2 PASS，恢復後原生 H3 運算成功重新執行。** 這是系統實際經歷斷電後的運算延續成果，不只是重新啟動程式。[閱讀跨卡重生完整性驗證報告](whitepaper/Q-Framework-RC4.5-Cross-GPU-Rebirth-Integrity-ZH-TW.md)。

### 真實單卡與多卡技術成果

- **最新突破：單卡 1080p 完整成片：**10／10 原生高解析度 RS 成功，完成 1080×1920／5 秒／120 幀影片，不升頻、不記錄 CUDA OOM，GPU 只有一張 RTX 2080 Ti 22GB 擴充版。

- **單卡 QmRNA 可完成性：**同張 A1 RTX 2080 Ti（22,528 MiB），同條件 36 幀、10 Steps 的 H3 測試，使用 QmRNA Pre-step Guard **成功產出 MP4**；沒有 Guard 的基準路徑在第一步觸發 **PRE-OOM**，未直接完成指定影片。PRE-OOM 與 CUDA 硬 OOM 不同。
- **單卡 H3 真實成片：****#370、#371** 在 A0 單張顯卡上成功產生原生短片；**#365** 更由**單張 A0 GPU** 串行完成十段 36 幀的 RS，最終組成**完整 15 秒、360 幀**影片，總耗時 **3 小時 12 分 08 秒**。期間曾有 **9 次 CUDA OOM**，之後重新提交相應整段 RS 成功；這不是單次 360 幀 Sampler，也不是全程零 OOM。
- **四卡高效率交付：****#361** 透過四張獨立 RTX 2080 Ti 與 CPU 接縫後製，於 **14 分 37 秒**完成 **15 秒、360 幀、480×832、24fps** 影片。
- **受控研究驗證：**既有跨設備一致性實驗已有分項收據；內部程式接線、資料規模及驗證細節均不公開。
- **跨硬體研究：**Windows／Mac 的數學分片、獨立驗算、AI 問答與部分模型權重訓練皆有獨立實績。

**2026/10/26｜單卡 1080p 已正式成片！**單張**擴充 22GB 的 RTX 2080 Ti**，在 Q 系列輔助路徑下完成 **10／10 支原生 1088×1920 MiniMax H3 RS**，只裁切及截幀、**沒有升頻**，組成完整 **1080×1920、5 秒、120 幀、24fps MP4**。本輪 **0 次 CUDA OOM 紀錄**，完成耗時 **1 小時 39 分 16 秒**（5 秒是影片長度，不是生成延遲）。原生運算、成片規格及雜湊驗證均有回執，影片視覺品質待 Owner 驗收。Owner 回報的無 Q OOM 對照仍待配對失敗原始證據。[技術證據](docs/claim-ledger.md)。

### 多節點異質運算計劃

[公開架構網頁](site/multi-node.html) · [工程路線圖](docs/multi-node-roadmap.md) · [網頁實際截圖](assets/multi-node-plan.png)。**四張 GPU 完成影片產線已驗證；四台 Mac Brain＋四台 Windows Worker 為八裝置目標，非八機已同步完成。**

### 中英日圖片圖庫

[**查看九張正式公開圖片**](docs/visual-gallery.md)：中／英／日招募海報、Q-Framework 完整架構圖、單卡與多卡運算比較圖。公開圖為視覺示意，實測成果與尚未完成的研發計畫分開標示。

### 最新白皮書｜RC4.5 發明者版本（繁體中文）

[**閱讀 RC4.5：我們正在重新定義 AI 運算的未來**](whitepaper/Q-Framework-v1.0-RC4.5-ZH-TW.md)

**Beyond OOM. Beyond Hardware. Beyond Boundaries.** 從 AI 產業面臨的硬體成本、運算中斷與閒置算力出發，介紹我們已取得的原生高解析度生成、運算重生、跨設備協作成果，以及技術授權、運算服務與異質算力平台三項商業方向。公開版僅揭露成果與市場價值，不揭露 BlackBox 核心機制。

### RC4.4 繁體中文審閱稿｜2026-10-30

[**閱讀 RC4.4 審閱全文**](whitepaper/Q-Framework-v1.0-RC4.4-ZH-TW-REVIEW.md) · [**查看 RC4.4 審閱版 PDF**](whitepaper/Q-Framework-v1.0-RC4.4-ZH-TW-REVIEW.pdf)。本版以原生高解析度 H3 運算避免 CUDA HARD OOM 為研究目標，僅公開核准的結果與限制。**這是供 Owner 審閱的新版本，未取代既有五語 RC4.3 正式白皮書；影片成片另行驗收。**

### RC4.3 完整技術白皮書

| 語言 | 全文 Markdown | PDF |
|---|---|---|
| 繁體中文 | [閱讀](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [下載](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| English | [Read](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |
| 日本語 | [読む](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |
| Español | [閱讀](whitepaper/Q-Framework-v1.0-RC4.3-ES.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ES.pdf) |
| Português (Brasil) | [閱讀](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.pdf) |

原 RC1–RC3 歷史版本保留於 [whitepaper/](whitepaper/)。

**最終研究目標：**具有可驗證計算狀態、共同決策與經驗回饋能力的**異質超級電腦神經網絡**。任意異世代 GPU 原生續算與超越 H100／H200 的同條件效能，仍待完整驗證。

[公開實證清單](docs/claim-ledger.md) · [驗證路徑](docs/validated-execution-paths.md) · [架構](docs/architecture.md)

### BlackBox：對外可驗證、對內保護核心

公開資料僅包含**經核准的技術成果、測量條件與驗證限制**。QmRNA／QVRAM／Temporal Möbius 的專有原始碼、原生模型接入、運算狀態格式、決策演算法、私人提示詞、客戶素材與原始日誌**不對外開放**。

- [AI 可讀匿名化證據 JSON](evidence/claims-public-rc4.3.json)
- [BlackBox 公開披露政策](docs/blackbox-disclosure-policy.md)
- [安全通報](SECURITY.md)

外部 AI 必須區分已完成的原生收據、受控對照、Owner 回報待核驗與長期研發目標；不需取得核心原始碼才能評估公開成果。

**Q-Framework — Connecting Compute. Extending Possibility.**
