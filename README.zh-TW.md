# Q-Framework

**可驗證的異構 AI 運算延續架構**

Q-Framework 是一套正在實際運行與驗證的 AI 運算研究系統。

> **公開原則：一半真實，一半黑箱。**

> **重要：Q-Framework 不是監控面板。** Live Compute 只是公開證據介面；production engine 已實際介入 MiniMax H3 / ComfyUI 類 workload 的 VRAM pressure / PRE-OOM 執行流程，包含 checkpoint、state spill、GPU residency release、restore、same-GPU / mixed-GPU continuation 與 recovery。它的目的不是只「看到 OOM」，而是讓已完成的計算可以在記憶體壓力下被保存、釋放、恢復並繼續執行。

本專案也與 Unity QFramework、NVIDIA CUDA-Q 或其他同名框架無關。

「真實」是指：公開的測試結果、SHA、bitwise / numerical comparison、完成案例與硬體級別皆來自實際驗證紀錄。

「黑箱」是指：足以重建 production engine 的核心方法不公開。

**目前公開版本：** Evidence Whitepaper v1.0 RC3  
**快照日期：** 2026-10-07

[English](README.md)

## 🔴 即時運算直播

**[開啟 Q-Framework Live Compute Stream](https://yuyu19761121.github.io/q-framework/)**

可直接觀看系統實際運行中的狀態：目前執行 Job、四張 GPU 的 branch 狀態、GPU / VRAM 負載、QmRNA / QSTATE 進度、正式節點 heartbeat 與即時執行資訊。這不是靜態示意頁，而是持續更新的公開 live telemetry。


## 公開什麼

- 真正觀察到 exact equality 的 SHA / bitwise 證據；
- numerical tolerance 結果；
- 已完成輸出的 hash；
- 去敏感化後的 workload / hardware 級別；
- 明確的 claim boundary。

詳見 **[Public Proof Pack](docs/public-proof-pack.md)**。

## 黑箱什麼

以下維持 proprietary：

- production state 真實資料結構；
- checkpoint packing / restore sequencing；
- QmRNA 訊號格式、控制方程、係數與判斷邏輯；
- QSTATIC 內部 contract、索引與選擇方式；
- Qvram residency 真實實作；
- memory-pressure threshold；
- eviction / prefetch policy；
- scheduler、worker selection、lease / fencing / retry 邏輯；
- production model-forward 修改；
- 私有 topology、endpoint 與 source code。

詳見 **[Disclosure Boundary](docs/disclosure-boundary.md)**。

## 已公開驗證結果

- Deterministic continuation：bitwise-identical，max absolute difference = 0.0。
- 約 250 MiB state transport：exact SHA preserved。
- 真實 H3 continuation：跨 GPU continuation 後成功產出。
- 四 Worker production-class execution：15.000 秒 / 540 frames，由四張獨立 RTX 2080 Ti 22 GB worker 共同參與。
- 跨環境數值一致性：三個 execution environment 得到相同 recomputed-result SHA。
- QSTATIC + QmRNA controlled equivalence：22 / 22 decoded frame hash 一致。

## 不宣稱

Q-Framework 不宣稱無限 VRAM、零 OOM、universal bitwise determinism、任意模型通用，或多張 GPU 在物理上合併成一張大 GPU。

## 白皮書

- [RC3 Evidence Whitepaper - English](whitepaper/Q-Framework-v1.0-RC3-EN.md)
- [RC3 Evidence Whitepaper - 繁體中文](whitepaper/Q-Framework-v1.0-RC3-ZH-TW.md)

舊 RC2 保留作歷史快照，但不再代表目前的公開邊界。

**真實證據，核心黑箱。**
