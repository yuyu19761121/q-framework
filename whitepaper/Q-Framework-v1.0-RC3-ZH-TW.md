# Q-Framework Evidence Whitepaper v1.0 RC3

## 可驗證的異構 AI 運算延續架構

**2026 年 10 月 7 日**

Q-Framework 是一套 proprietary 的異構 AI 運算架構。本公開白皮書採用「一半真實、一半黑箱」原則：公開真實驗證結果，但不公開足以重建 production engine 的核心機制。

## 公開原則

**真實證據，核心黑箱。**

公開：
- 真實量測結果；
- SHA；
- bitwise / numerical comparison；
- 去敏感化硬體與 workload 級別；
- 已完成輸出證據。

黑箱：
- internal state representation；
- QmRNA 控制格式、方程與係數；
- QSTATIC internal contracts；
- Qvram residency 實作；
- checkpoint packing / restore sequencing；
- thresholds、scheduler、eviction / prefetch policy；
- production source code 與 private topology。

## 已公開驗證結果

### Deterministic continuation
bitwise-identical，max absolute difference = 0.0。

SHA-256：
`ae04c23d4daed035632855260f85c360a857c28a8d46544f5c92f91baff823a3`

### 約 250 MiB transport integrity
Exact SHA preserved：

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

### 真實 H3 continuation
跨 GPU continuation 後成功產出：

`307828DE5D0D54F36004EF9C97B2E4DAE5178E59A9C8EF74775F07522B788AB3`

### 四 Worker production-class execution
15.000 秒 / 540 frames，由四張獨立 RTX 2080 Ti 22 GB worker 共同參與。

Final SHA-256：
`23CDBA13DBFF7B8EC234DB1D7DE61625597E128BD6684849FCB6CD33650ADF57`

### 跨環境數值一致性
三個 environment 得到相同 recomputed-result SHA：

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

### Shared identity/reference-state consistency
Cross-node reference-state SHA：

`1488ccf08323200643d5759046f2d47e1e16d44a70f278a79346aec53103d937`

### QSTATIC + QmRNA controlled equivalence
22 / 22 decoded frame hash 一致。

framemd5 manifest SHA-256：
`FF55120ADF80F99D74405C5DECA7A9B54116B01F987591A012BD1FF01467F5D7`

### Cross-boundary continuation
已記錄 output hash：

`7A909C59636C1A18C6B1A1C7CD2037120F25DDC2C7F36CD2E62B4C70A43212E1`

`C35FAECFE3C1BD0B5338CC4BE0EB8A854A10CE0FEEF86D39CA750DE6BB4A357C`

## 不宣稱

Q-Framework 不宣稱無限 VRAM、零 OOM、universal bitwise determinism、任意模型通用，或多張 GPU 在物理上合併成一張更大的 GPU。

## 結論

公開文件用來證明「確實做得到」；真正讓它做到的 production mechanism 維持黑箱。
