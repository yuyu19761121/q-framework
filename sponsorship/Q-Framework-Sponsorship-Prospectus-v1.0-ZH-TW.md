# Q-Framework 技術贊助計畫 v1.0

## 讓運算狀態成為可管理的資源

**October 2026**

> **這不是從零開始的構想募資。**  
> Q-Framework 已有實際運行中的系統、公開 GitHub、白皮書、驗證紀錄與 reference code。贊助的目的，是把目前已經能運作的研究架構，推進到更完整的 benchmark、更多硬體、更多節點、更高解析度與更可重現的工程驗證。

## 1. Executive Overview

Q-Framework 正在研究一個很直接的問題：當 AI 工作的實際 working set 接近 GPU 實體顯存上限時，運算是否一定只能失敗、縮小、或整段重來？

我們選擇把 memory pressure 變成控制訊號，把 compute state 變成可保存、可恢復、可移動、可重新分配的系統資源。

目前系統已從多 GPU 影片生成工作流程，逐步演進到 lineage、checkpoint/resume、CPU/RAM-backed state、QmRNA runtime control、QSTATIC、跨節點 continuation，以及 model-forward candidate working-set virtualization。

### 目前公開且可合理陳述的進展

- 已執行跨 GPU compute-state / sampler-state transport 與 hash identity 驗證。
- 已執行 GPU → CPU/RAM → shared memory → GPU 的 continuation / rescue 路徑。
- QmRNA 已進入 MiniMax H3 model-forward candidate path，而不只是在外部看 GPU utilization。
- Exact FFN token chunking 已進入 live candidate path。
- CPU-only global streamed-attention reference 已完成與 full attention 的數值比對驗證。
- 公開 GitHub 已提供 architecture、claim ledger、benchmark methodology、reference interfaces 與 sanitized proof-manifest。

### 我們尚未宣稱

- 「無限 VRAM」或零 OOM。
- 對任何模型都通用的 working-set virtualization 已完成。
- 單張 22GB GPU 的完整 15 秒 H3 full-length production acceptance 已完成。
- Q-Framework 已等同或超越某一款 datacenter GPU。

## 2. 為什麼現在值得贊助

AI 算力的成本，不只來自 GPU 價格，也來自大量因 working set、排程、恢復與資源切分不理想，而被迫閒置或失敗的運算。

Q-Framework 的方向，是把更多系統層能力放到模型與硬體之間，讓不同等級的 GPU、CPU、RAM、Disk 與多節點可以形成更有彈性的 execution fabric。

| 研究價值 | Q-Framework 的方向 |
|---|---|
| 硬體利用率 | 讓 GPU 以受控 feed rate 工作，而不是永遠固定切塊 |
| 失敗成本 | 把「失敗重來」逐步轉成 freeze / persist / restore / resume |
| 異構資源 | 讓 CPU、RAM、Disk、不同 GPU 承擔各自適合的角色 |
| 驗證可信度 | 用 receipt、hash、runtime trace、benchmark manifest 限制過度宣稱 |

## 3. 12 個月技術贊助 Roadmap

以下是研究與工程目標，不是保證交付的投資報酬。

| 期間 | 重點 | 預期驗證輸出 |
|---|---|---|
| 0-3 個月 | Reproducible Baseline | 15s / 9:16 / 480p / 24fps benchmark manifest；baseline vs Q-Framework；pause/freeze/resume receipts |
| 3-6 個月 | Working-set Virtualization | model-forward candidate、streamed Q/K/V data-plane、RAM/Disk state lifecycle |
| 6-9 個月 | Heterogeneous Multi-node | worker handoff、lease/fencing、failover、priority scheduling |
| 9-12 個月 | Validation at Scale | 720p/1080p、長秒數、不同模型 adapter、sponsor hardware validation report |

## 4. 贊助資源將如何使用

| 比例 | 用途 | 內容 |
|---:|---|---|
| 35% | GPU / Compute | 新增或借調 GPU、不同 VRAM/architecture、burn-in、benchmark |
| 20% | Storage / Network / Power | NVMe、共享儲存、網路、UPS、供電、冷卻 |
| 20% | Engineering | instrumentation、state lifecycle、worker control、frontend observability |
| 10% | Benchmark / QA | manifest、failure injection、hash/receipt、regression |
| 10% | Documentation / Public Evidence | 白皮書、公開 benchmark、reference interfaces、多語文件 |
| 5% | IP / Security / Governance | IP 盤點、security review、公開邊界與合作條款 |

非金錢型贊助同樣有價值：GPU、記憶體、NVMe、網路設備、機櫃、冷卻、cloud credits、借測機、工程顧問與研究合作。

## 5. 建議贊助層級

| 層級 | 建議額度 | Sponsor Benefits |
|---|---:|---|
| Research Supporter | US$5,000+ | Sponsor 名錄（可匿名）、版本更新、季度技術摘要 |
| Development Sponsor | US$25,000+ | 上述權益 + sponsor briefing、roadmap review、非獨家 benchmark 摘要 |
| Infrastructure Sponsor | US$100,000+ | 上述權益 + 指定硬體 / workload 驗證優先排程、聯合技術案例 |
| Founding Strategic Sponsor | US$250,000+ | 上述權益 + 年度深度技術 review、共同定義 validation program、策略合作框架 |

> 贊助不自動取得 production source code、核心演算法、專利權、商標權、獨家授權或客戶資料。OEM、商業授權、客製開發、獨家權利或 IP 移轉需另簽正式合約與 SOW。

## 6. Sponsor 可以得到什麼

- 版本化技術進度與 changelog。
- Demonstrated / Partial / In Progress / Proposed 分級。
- 在可公開範圍內的 benchmark receipts。
- Sponsor briefing 與 roadmap review。
- 指定硬體 / workload validation（需另定範圍）。
- 經雙方同意後的公開合作案例。

## 7. 技術治理與 Due Diligence

Q-Framework 採用「公開證據、保留 enabling secret」的方式。

- Claim Ledger
- Disclosure Boundary
- Benchmark Manifest
- Rollback / Lineage / Receipts
- Security Hygiene

公開 repository：<https://github.com/yuyu19761121/q-framework>

## 8. 如何支持 Q-Framework

目前接受三類合作方向：

- 資金贊助
- 硬體 / 算力 / Cloud Credit 贊助
- 共同驗證研究

企業、研究機構、硬體廠商或雲端平台，可透過 repository owner 的 GitHub profile 可用聯絡方式提出合作。

公開詢問可建立 issue，標題以 **[Sponsorship]** 或 **[Research Collaboration]** 開頭。請勿在公開 issue 放置機密資訊。
