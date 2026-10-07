# Q-Framework Development & Validation Whitepaper v1.0 RC2

## 異種混在型 AI 基盤における計算状態仮想化・適応型フロー制御・検証可能な継続計算

**2026年10月7日**

> **本ホワイトペーパーは、runtime evidence、SHA、state receipt を保持する実稼働システムを記録する。**

Q-Framework は、複数 GPU を一つの巨大 GPU と見なす方式ではない。compute state、identity state、continuity state、execution lineage を単一 GPU の寿命から分離し、Freeze、Hash、Move、Restore、Resume、Branch、再検証を可能にする異種混在型 AI compute architecture である。

RC2 では CURRENT の実測記録に基づき、RC1 で十分に説明されていなかった四つの実行経路を追加する。

## 1. 設計原則

1. Logical state と physical residency を分離する。
2. GPU は execution worker であり、workload state の唯一の owner ではない。
3. Transport integrity と compute progression を別々に検証する。
4. 同じ lineage は resume も branch も可能である。
5. 公開 claim は runtime / SHA / receipt / measurable outcome に結び付ける。

## 2. 四つの検証済み実行経路

### 2.1 Mixed-GPU Stateful Continuation

250 MiB F-Block XCOPY では GPU0 VRAM → CPU/SharedMemory → GPU1 VRAM を実行し、source / Bridge RAM / target read-back の SHA-256 が完全一致した。

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

`bitwise_sha_match=true`、round trip 約 3.6753 秒。

H3 rescue では seed `2609282350` が B0 checkpoint → CPU/RAM Bridge → B1 restore → sampler continuation → MP4 output まで完了し、output SHA は

`307828DE5D0D54F36004EF9C97B2E4DAE5178E59A9C8EF74775F07522B788AB3`

である。

Transport 中は SHA equality が integrity を示し、GPU が実際に compute を進めた後は新しい QREV / 新しい SHA が生成される。

### 2.2 Fixed-Owner Same-GPU Resume

`qmrna_vvram_same_gpu` は chain ごとに owner GPU を固定し、`same_gpu_resume=true` で continuation を行う。

共通 CHARACTER_ROOT seed、persistent Character Master、previous tail、checkpoint/result receipt、Dynamic Static を利用し、不要な migration を避ける。H3 ref0 は Character Master、ref1 は Static / previous tail / continuity context として扱われる。

Same-GPU Resume は locality を優先し、Mixed-GPU Resume は failover / shared-pool flexibility を優先する別モードである。

### 2.3 H3 Memory Static / QSTATIC Shared-State Compute

H3 state-block mapping では reproducible SHA を確認した。

- Audio reference latent: `[1,32,2,40]` / 10,240 bytes、同一 input repeat SHA 完全一致。
- Visual reference latent: 480×832、`[1,24,1,52,30]` / 149,760 bytes、repeat SHA 一致。
- Face reference visual block: Node A/A1 と Node B/B1 が同一 512×512 face reference から bit-identical SHA
  `1488ccf08323200643d5759046f2d47e1e16d44a70f278a79346aec53103d937`
  を生成。

Job268 では QRS0001 が 24 frames / 1s context を完了し、Face QC PASS（median 0.310109、minimum 0.245260、threshold 0.22）。その実出力から QW9 が `dynamic_static_QRS0002.json` を生成し、次の GPU segment がその後に dispatch された。

4-worker smoke では A0/A1/B0/B1 が branch 前に同一 authoritative identity/continuity state を SHA で確認し、その後別々の action/shot branch を実行できることも確認した。

### 2.4 Mixed-GPU Cross-File / Cross-Shot Stateful Compute

Shot XCOPY / Motion Bridge は、RGB final-frame のみを渡すのではなく Boundary Memory / QBlock を介して shot/file boundary を越える。

64 MiB cross-host test では B0 → Bridge → A1 GPU compute `x+7` → Bridge → B0 restore を実行し、state integrity を確認した。

Job #135 / X1 では二つの別 boundary artifact：

- RS01 tail SHA `D539AD5EAEA6B5BED4132A94CD24689AB4D4AD61142582894BF6DAD93290ED6B`
- RS02 head SHA `1E51DBAAF8D30BAEBDB98D8393E82221FF1EEADAB93E2D9A50A7C100CFC444F4`

を H3 が同時に conditioning として受け取り、B0 → PRE-OOM → A0 restore → output を完了した。Smoke output SHA：

`7A909C59636C1A18C6B1A1C7CD2037120F25DDC2C7F36CD2E62B4C70A43212E1`

R3 は B0/A0/B1 間で s01→s20 を同一 lineage のまま進め、final artifact SHA：

`C35FAECFE3C1BD0B5338CC4BE0EB8A854A10CE0FEEF86D39CA750DE6BB4A357C`

を生成した。

## 3. Node + GPU / cross-environment solver consistency

HF_QWORKER_LITE V0.1 では、真の production sampler state に対して同じ arithmetic を：

- Utility01（ComfyUI/PyTorch math path なし）
- H410（ComfyUI math path なし）
- Node B PyTorch reference

で再実行した。

三者の recomputed-x SHA は完全一致：

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

source state に対する reverse→forward float32 reconstruction の max abs error は `4.76837158203125e-07`、mean は約 `2.03e-08`。

これは universal bitwise GPU determinism の主張ではない。真の production state を元 runtime から分離し、別 node/runtime solver で同じ computed-result hash を再現できたという証拠である。

## 4. SHA の三つの意味

- **Exact Transport SHA**: state が変化していない場合 SOURCE = BRIDGE = TARGET。
- **Progressive QREV SHA**: 実際に compute が進めば SHA_n と SHA_n+1 は変化する。
- **Cross-Environment Computed SHA**: 別 node/runtime が同一 arithmetic を実行して同一 computed hash を得る。

## 5. まだ主張しないこと

Unlimited VRAM、zero OOM、全 model への universal applicability、任意 GPU inference の universal bitwise determinism、22GB RTX 2080 Ti での最新 full-length 311-aligned H3 production PASS はまだ主張しない。

## 6. Disclosure boundary

公開：architecture、state lifecycle、smoke/runtime result、hash、receipt、benchmark methodology、sanitized interfaces。

非公開：production QmRNA pressure scoring、adaptive feed equation、page/residency selection、eviction/prefetch、Qvram serializer/restore order、Qsearch ranking、scheduler weight/fencing/retry authority、production streamed-QKV data-plane。

**Open Specification · Open Evidence · Open Reference Interfaces · Closed Production Engine**
