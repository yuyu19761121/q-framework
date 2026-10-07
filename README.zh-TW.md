# Q-Framework

**異構 AI 基礎設施的運算狀態虛擬化與自適應流量控制架構**

Q-Framework 是一套正在實際開發與運行的 AI 運算架構，核心研究方向是：讓長時間生成式 AI 工作不再把 GPU 顯存不足視為唯一終點，而是把運算狀態變成可觀察、可控制、可凍結、可保存、可恢復、可移動的資源。

> **這個 repository 記錄的是一套正在運行的系統，但不公開 proprietary production engine。**

**版本：** Development & Validation Whitepaper v1.0 RC2  
**進度快照：** 2026-10-07

[English](README.md) · [日本語](README.ja.md)

## 白皮書 PDF

**[English PDF](whitepaper/Q-Framework-v1.0-RC2-EN.pdf)** · **[繁體中文 PDF](whitepaper/Q-Framework-v1.0-RC2-ZH-TW.pdf)** · **[日本語 PDF](whitepaper/Q-Framework-v1.0-RC2-JA.pdf)**

## 贊助 Q-Framework

**[贊助說明](SPONSORSHIP.zh-TW.md)** · **[English Sponsorship Page](SPONSORSHIP.md)** · **[完整募資 Prospectus PDF](sponsorship/Q-Framework-Sponsorship-Prospectus-v1.0-ZH-TW.pdf)**

資金、GPU／硬體、Cloud Credit 與研究合作，都可以直接擴大 Q-Framework 的驗證能力；production engine 與核心演算法仍維持封閉。

## 目前公開的核心概念

- **QmRNA**：runtime telemetry 與控制平面
- **Qvram**：持久化運算狀態、checkpoint 與 residency 管理層
- **Qsearch**：狀態與 working-set 搜尋／取回層
- **Qanswer**：CPU/GPU 異構運算協調層
- **QSTATIC**：預先分析與保存的 Static / visual-state 來源層
- **QSTATE / QBLOCK / QLINEAGE / QREV**：狀態、區塊、血統與版本原語

## 我們怎麼寫成果

Q-Framework 不把推測寫成成果，而是把技術分成：

- **Demonstrated**：已有 runtime / hash / receipt / output 證據
- **Partial**：部分路徑已跑通，但完整 acceptance 還沒完成
- **In Progress**：已進入實作或 candidate 階段
- **Proposed**：架構方向與 roadmap

目前已能公開說明的結果包含：

- 跨 GPU sampler state transport 與 hash 驗證；
- GPU → CPU/RAM → shared memory → GPU 的 continuation/rescue；
- continuation lineage 與 checkpoint identity；
- QmRNA 已進入 MiniMax H3 model forward 的 candidate 路徑，而不只是外部監控；
- exact FFN token chunking 已在 live candidate 中執行；
- CPU-only streamed/global attention reference 與完整 attention 的數學驗證，在測試 shape 下落於一般浮點誤差範圍。

尚未宣稱完成的部分包括：

- 單張 22GB GPU 完整 15 秒 H3 full-length 的最終 production PASS；
- streamed Q/K/V 在完整 H3 forward 的 production data-plane；
- 任意模型都可通用的 working-set virtualization；
- RAM/Disk spill/prefetch 的完整 production policy。

## 公開原則

**公開架構 · 公開證據 · 公開介面 · 核心引擎保密**

本 repo 不會公開：

- QmRNA 真正 pressure score 與 adaptive policy；
- residency / page selection；
- eviction / prefetch；
- Qvram production serializer 與 restore sequencing；
- Qsearch ranking / cache heuristics；
- scheduler weights / lease / fencing / retry authority；
- production streamed-QKV data-plane；
- IP、token、憑證、LAN topology 與 private infrastructure。

詳見 [docs/disclosure-boundary.md](docs/disclosure-boundary.md)，以及 [四大已驗證運算路徑](docs/validated-execution-paths.md)。
