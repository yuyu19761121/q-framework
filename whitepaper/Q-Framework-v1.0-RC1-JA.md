# Q-Framework Development & Validation Whitepaper v1.0 RC1

## 異種混在型AI基盤のための計算状態仮想化・適応型フロー制御

**2026年10月**

> **本ホワイトペーパーは、実際に稼働しているシステムを記録したものである。**

Q-Framework は、長時間の生成AIワークロードがコンシューマGPUの実用的なVRAM領域に近づいた場合でも、OOMを単純な終端とせず、計算状態を観測・制御・保存・復元・移動可能な資源として扱えるかを検証する異種混在型コンピューティング基盤です。

現在のシステムは lineage、checkpoint/resume、CPU/RAM-backed state、runtime control signal、QSTATIC、multi-node continuation、model-forward candidate working-set virtualization を持つ構成へ発展しています。

## 現在の証拠

公開可能な開発証拠には、cross-GPU state/hash verification、GPU→CPU/RAM→GPU rescue lineage、H3 model-forward 内の QmRNA candidate、exact FFN token chunking、CPU-only global streamed-attention reference と full attention の数値一致検証が含まれます。

### QSTATIC 4-GPU shared identity-state consistency

QSTATIC は単なる media index / asset library ではなく、parallel GPU Worker が共有する continuity / identity-state source としても機能する。4-GPU smoke test では A0／A1／B0／B1 の独立 execution slot に同一 Character Master / identity-state package を供給し、その後に各 Worker が別々の shot / action branch を実行する構成を検証した。

保持された validation record では、参加 Worker 間の shared identity/state SHA が一致し、node-side computation-state SHA も branch-specific action 実行前に一致した。重要なのは最終動画の byte-level hash が同一であることではなく、分岐前の authoritative shared state が同一であることである。異なる action / shot branch に分岐した後は final output SHA が異なることが正常である。

本結果は、テストした smoke configuration における **VALIDATED shared-state consistency** と位置付ける。すべての model / identity representation / heterogeneous GPU combination で perceptual identity が自動的に保証されるという主張ではないが、共通 identity / continuity state を複数の独立 GPU Worker に配布し、SHA で equality を検証した後に異なる execution branch へ分岐できることを示している。

### Node-to-GPU computation consistency

同じ CURRENT の development evidence には、共有 state が node 側で解決され GPU execution に渡された後も、parallel worker 間の node-side / GPU-side computation fingerprint が非常に近い状態を維持したことが記録されている。QSTATIC multi-worker smoke では独立した node/GPU path であるにもかかわらず、computation-state SHA はほぼ一致した。

この結果は exact transfer proof と区別して記述する。制御された state transport では、20-step sampler handoff が bitwise equal / max absolute difference 0.0 を達成し、250 MiB の GPU→CPU→SharedMemory→GPU round trip では source / Bridge RAM / target GPU read-back の SHA-256 が完全一致した。

一方、QSTATIC 4-worker execution は **near-consistent computation fingerprints** と表現し、任意の GPU inference に対する universal bitwise determinism は主張しない。

したがって evidence は三層に分けることができる。

1. Controlled compute-state transport では exact SHA / bitwise match を証明できる。
2. Parallel branch 前の authoritative identity / continuity state は SHA で equality を検証できる。
3. Independent node + GPU execution でも computation fingerprint を高い一致度に保ちながら、その後の action / shot branch は異なる final media を生成できる。

この点は、Q-Framework が GPU を identity / lineage / workload state の owner ではなく execution worker として扱う根拠の一つである。

## 4つの検証済み実行パス

CURRENT のエビデンスは、Q-Framework に少なくとも4つの異なる stateful execution path があることを示している。

| 実行パス | 状態 | 検証済み内容 |
|---|---|---|
| **Mixed-GPU compute / continuation** | VALIDATED | GPU A で freeze した state を CPU/RAM/Bridge 経由で GPU B に restore し、同じ lineage を継続できる。20-step POC は bitwise equal / max diff=0.0、250 MiB transport は source/Bridge/target SHA exact、controlled H3 rescue は B0 checkpoint -> B1 restore -> MP4 output まで到達した。 |
| **Same-GPU resume** | VALIDATED SMOKE | story chain を owner slot に固定し `same_gpu_resume=true` とすることで、同一 GPU 内で lineage/state を保持したまま segment continuation が可能である。 |
| **H3 Memory Static / Reference-State compute** | VALIDATED | H3 audio/visual/face reference を shape/bytes/SHA を持つ tensor block として測定した。同一入力は同一 state SHA を再現し、同一 face reference は Node A/Node B で同一 visual-latent SHA を生成した。 |
| **Mixed-GPU cross-file / cross-shot compute** | VALIDATED SMOKE | SHOT XCOPY / Motion Bridge は別 shot/artifact の boundary state を利用できる。Job #135 smoke は dual boundary reference を受け取り、B0 PRE-OOM -> A0 restore を経て H3 output を生成した。 |

共通原則は、**GPU residency は一時的な execution window であり、lineage と検証可能な compute state は GPU 外部で authoritative に維持される**ことである。

### SHA の3つの意味

1. **Exact transport SHA**：同じ frozen state は GPU -> CPU/RAM/Bridge -> GPU の transport 中に bitwise identical でなければならない。
2. **Progressive revision SHA**：restore 後に実計算が進めば、新しい freeze は新 revision / 新 SHA を生成する。step が進まなければ SHA は変化しない。
3. **Cross-environment computed-result SHA**：Utility01、H410、Node B PyTorch reference が同じ production sampler arithmetic を独立に計算し、同一 recomputed-x SHA を生成した。original source との差は float32 rounding tolerance の範囲で、max abs 4.768e-7、mean abs 約 2.03e-8 だった。

従って public claim は、tested node/runtime path における **reproducible numerical consistency** であり、任意の model/intermediate tensor の universal bitwise determinism ではない。

### QSTATIC 4-GPU shared identity state

A0/A1/B0/B1 は action branch 分岐前に同じ authoritative identity/continuity state を解決し、shared identity/state SHA は一致した。node+GPU computation fingerprint も branch 前に高い整合性を維持した。

分岐後は各 worker が異なる action/shot を生成するため、final media SHA は同一である必要がない。検証された invariant は branch 前の common identity root/state authority と lineage である。


単一22GB GPUで最新 full-length working-set virtualization を用いて最終15秒 H3 workload を production quality で完了した、という主張はまだ行いません。
