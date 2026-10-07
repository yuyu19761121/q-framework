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

### QSTATIC 四 GPU 共享角色狀態一致性

QSTATIC 不只是媒體索引或素材庫；在 production architecture 中，它也可以作為平行 GPU Worker 共用的 continuity / identity-state source。四 GPU smoke test 以 A0／A1／B0／B1 四個獨立 execution slot 執行，在不同 shot／action branch 被分別派工之前，四個 Worker 取得同一份 Character Master／identity-state package。

保留的驗證紀錄顯示：參與 Worker 的 shared identity/state SHA 一致，節點端 computation-state SHA 也一致。這裡真正需要一致的是「共享的 authoritative state」，而不是不同動作分支完成後的最終影片檔案。不同 action／shot branch 開始執行後，最終 output SHA 本來就應該可以不同。

因此，本項成果在本白皮書中列為 **已驗證（VALIDATED）的 shared-state consistency smoke proof**。它不代表任意模型、任意角色表示法或任意異構 GPU 都必然不需要額外 QC；它證明的是：Q-Framework 可以把共同 identity／continuity state 分送到多個獨立 GPU Worker，先用 SHA 驗證狀態一致，再讓各 Worker 分別執行不同的動作分支。

### 節點到 GPU 的運算一致性

CURRENT 同一條開發證據鏈還記錄了第二個、需要獨立描述的現象：共享狀態在節點端完成解析並交給 GPU 執行後，各平行 Worker 的 **node-side / GPU-side computation fingerprint 仍呈現高度一致**。在 QSTATIC 多 Worker smoke 中，參與的節點＋GPU 路徑雖然是獨立裝置，但 computation-state SHA 幾乎一致。

這裡必須與 Q-Framework 已完成的「exact transfer proof」分開解讀。受控狀態搬運實驗中，我們已經有完全相等的證據：20-step sampler handoff 的最終結果 bitwise equal、max absolute difference = 0.0；另一個 250 MiB GPU→CPU→SharedMemory→GPU round trip 則從 source、Bridge RAM 到 target GPU read-back 都維持完全相同的 SHA-256。

相較之下，QSTATIC 四 Worker 的節點＋GPU 運算結果，白皮書採用 **高度一致／近一致的 computation fingerprint** 描述，而不是宣稱任意 GPU inference 都能保證 bitwise deterministic。

因此完整證據應分成三層：

1. **受控 Compute State 搬運可做到 exact SHA／bitwise match。**
2. **平行 Worker 分支前的 identity／continuity authoritative state 可用 SHA 證明一致。**
3. **獨立 node + GPU 執行路徑的 computation fingerprint 可維持高度一致，同時允許後續 action／shot branch 產生不同的最終影片。**

這也是 Q-Framework 把 GPU 定義為 execution worker、而不是 identity／lineage／完整 workload state owner 的重要依據。

「單張 22GB GPU 透過最新 full-length working-set virtualization 完成最終 15 秒 production-quality H3 任務」目前仍在驗證，因此不寫成已完成。
