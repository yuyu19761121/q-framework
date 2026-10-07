# Q-Framework 開發與驗證白皮書 v1.0 RC1

## 異構 AI 基礎設施中的運算狀態虛擬化與自適應流量控制

**2026 年 10 月**

> **本白皮書記錄的是一套正在實際運行的系統。**

Q-Framework 是一套實驗性的異構 AI 運算架構，研究的核心問題是：當長時序生成式 AI 工作的實際 working set 接近或超過消費級 GPU 舒適的實體顯存範圍時，能不能不要把 OOM 當作唯一終點，而是讓任務仍然保持可控制、可保存、可恢復與可移動。

目前系統包含 lineage、checkpoint/resume、CPU/RAM-backed state、runtime control signal、QSTATIC、多節點 continuation，以及 model-forward candidate working-set virtualization。

## 設計原則

1. Logical state 與 physical residency 是不同的事。
2. Memory pressure 應該可以被觀察並成為控制訊號。
3. 運算狀態應該能跨越暫時性的資源壓力。
4. GPU 是執行資源，不等於整台機器。
5. 所有公開主張都必須有證據等級。

## 目前證據

目前可公開的開發證據包含：跨 GPU state/hash 驗證、真實 GPU→CPU/RAM→GPU rescue lineage、QmRNA 進入 H3 model-forward candidate、exact FFN token chunking，以及 CPU-only global streamed-attention reference 與 full attention 的浮點誤差範圍驗證。

「單張 22GB GPU 透過最新 full-length working-set virtualization 完成最終 15 秒 production-quality H3 任務」目前仍在驗證，因此不寫成已完成。
