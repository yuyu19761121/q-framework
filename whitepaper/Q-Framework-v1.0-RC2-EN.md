# Q-Framework Development & Validation Whitepaper v1.0 RC2

## Compute-State Virtualization, Adaptive Flow Control, and Verifiable Continuation Across Heterogeneous AI Infrastructure

**October 7, 2026**

> **This paper documents a running system backed by runtime evidence, hashes, and state receipts.**

Q-Framework is an experimental heterogeneous AI compute architecture. Its objective is not to pretend that several GPUs form one physically unified accelerator. Instead, it separates compute state, identity state, continuity state, and execution lineage from the lifetime of any single GPU so that work can be frozen, hashed, moved, restored, resumed, branched, and verified.

RC2 adds four execution paths that were under-described in RC1 but are supported by retained CURRENT development records and smoke/runtime evidence.

## 1. Core design principles

1. Logical state and physical residency are separate concepts.
2. A GPU is an execution worker, not the sole owner of workload state.
3. Transport integrity and compute progression must be validated separately.
4. One lineage may be resumed or branched from a shared authoritative root.
5. Public claims must map to runtime evidence, hashes, receipts, or measurable outcomes.

## 2. Four validated execution paths

### 2.1 Mixed-GPU Stateful Continuation

Mixed-GPU execution does not aggregate VRAM. It allows one compute lineage to hand off between independent workers.

A controlled F-Block XCOPY moved a 262,144,000-byte (~250 MiB) state from GPU0 VRAM through CPU/shared memory to GPU1. Source, Bridge RAM, and target read-back SHA-256 were all:

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

with `bitwise_sha_match=true`, `sentinel_match=true`, and a measured round trip of approximately 3.6753 seconds.

A higher-level H3 rescue path also completed: seed `2609282350`, B0 checkpoint → CPU/RAM Bridge → B1 restore → sampler continuation → MP4 output, output SHA-256:

`307828DE5D0D54F36004EF9C97B2E4DAE5178E59A9C8EF74775F07522B788AB3`

Progressive State Block logs further show that when a target GPU performs real work, a new QREV and new SHA are expected. Exact SHA equality proves transport integrity; SHA evolution after compute proves state progression.

### 2.2 Fixed-Owner Same-GPU Resume

Q-Framework also supports `qmrna_vvram_same_gpu`, where each story chain is pinned to an owner slot and `same_gpu_resume=true`.

The path preserves stable lineage/seed state, previous-tail continuity, checkpoint/result receipts, and Dynamic Static context. Four chains may execute in parallel, while each chain preferentially resumes on its owner GPU.

A deterministic shared CHARACTER_ROOT seed and a persistent Character Master reference prevent the four chains from starting from four unrelated identities. H3 ref0 remains Character Master; ref1 carries selected Static, previous tail, or continuity/QmRNA context. Character embeddings are cached by SHA-256 and reused across cards and segments.

Same-GPU Resume and Mixed-GPU Resume are therefore separate control modes: the former avoids unnecessary migration; the latter provides flexible failover and resource sharing.

### 2.3 H3 Memory Static / QSTATIC Shared-State Compute

QSTATIC is not only an asset index. It can carry motion, pose, scene, composition, and lighting state while Character Master remains the identity authority.

H3 state-block signature mapping demonstrated reproducible state fingerprints:

- Audio reference latent: shape `[1,32,2,40]`, 10,240 bytes; repeated identical input produced identical SHA.
- Visual reference latent at 480×832: shape `[1,24,1,52,30]`, 149,760 bytes; repeat SHA matched, while a changed input produced a different SHA with unchanged shape.
- Face reference visual block at 512×512: Node A/A1 and Node B/B1 produced bit-identical visual-latent SHA:
  `1488ccf08323200643d5759046f2d47e1e16d44a70f278a79346aec53103d937`

This is direct evidence of environment-decoupled state for the tested H3 reference-encoding block.

The Dynamic Static loop also entered production flow. In Job268, QRS0001 completed a 24-frame / 1-second context, reached QMRNA_COMPLETE, passed Face QC (median similarity 0.310109; minimum 0.245260; threshold 0.22), emitted a real tail, and then a CPU QWorker generated `dynamic_static_QRS0002.json` with `computed_by=QW9`, `image_authority=PREVIOUS_GPU_TAIL`, and `identity_authority=USER_UPLOAD`. Only then was QRS0002 dispatched.

A four-worker QSTATIC/Character-Master smoke also validated equal authoritative shared identity/continuity state across A0/A1/B0/B1 before the workers branched into different shot/action work. Final video hashes are not expected to match after divergent actions; the invariant is the shared pre-branch state.

### 2.4 Mixed-GPU Cross-File / Cross-Shot Stateful Compute

Shot XCOPY and Motion Bridge extend the model across file and shot boundaries.

Instead of:

`Shot A → decode RGB → final frame → Shot B re-encode`

Q-Framework can preserve boundary/state information:

`Shot A state → Boundary Memory / QBlock → Bridge → Shot B / Solver`

A 64 MiB cross-host round trip moved state B0 → Bridge → A1, performed real GPU compute (`x+7`), then returned the state to B0 with raw-state SHA/sentinel verification.

Job #135 / X1 used two distinct boundary artifacts:

- RS01 tail SHA: `D539AD5EAEA6B5BED4132A94CD24689AB4D4AD61142582894BF6DAD93290ED6B`
- RS02 head SHA: `1E51DBAAF8D30BAEBDB98D8393E82221FF1EEADAB93E2D9A50A7C100CFC444F4`

MiniMax H3 consumed both references. The smoke path ran B0 → PRE-OOM → A0 restore → H3 output, producing SHA:

`7A909C59636C1A18C6B1A1C7CD2037120F25DDC2C7F36CD2E62B4C70A43212E1`

The later R3 lineage advanced:

`B0 s01 → A0 s02 → B1 s04 → A0 s06 → B1 s08 → A0 s10 → A0 s12 → B1 s14 → A0 s16 → B1 s18 → A0 s20 → B1 final`

and produced final artifact SHA:

`C35FAECFE3C1BD0B5338CC4BE0EB8A854A10CE0FEEF86D39CA750DE6BB4A357C`

This is an executed example of cross-shot boundary memory combined with cross-GPU continuation.

## 3. Node + GPU / cross-environment solver consistency

HF_QWORKER_LITE V0.1 used a real production sampler state and re-executed the same sampler arithmetic in three environments:

- Utility01: no ComfyUI / no PyTorch math path
- H410: no ComfyUI math path
- Node B: PyTorch reference

All three produced the same recomputed-x SHA:

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

Relative to the source state, reverse→forward float32 reconstruction produced:

- max absolute error: `4.76837158203125e-07`
- mean absolute error: approximately `2.03e-08`
- exact elements: 523,127 / 740,352
- exact ratio: approximately 0.706592

The correct claim is not universal bitwise determinism. The evidence shows that real production state can leave the original ComfyUI process and be solved in another node/runtime while reproducing the same computed-result hash.

### Node + GPU computation-fingerprint near-match

In addition to the exact recomputed-x SHA across the three solver environments above, the four-worker QSTATIC smoke retained a different class of evidence: under the same shared state, lineage, and compatible execution contract, independent node+GPU paths produced **near-matching / highly consistent computation-state fingerprints**.

This must not be confused with Exact Transport SHA. It describes consistency after state has entered independent node+GPU execution paths. Because GPU kernels, drivers, precision, execution order, and later action branches can introduce legitimate differences, RC2 does not convert this observation into a universal bitwise-determinism claim.

RC2 therefore labels this evidence separately as **Node + GPU Computation Fingerprint Near-Match**. Together with exact transport, progressive QREV, and cross-environment recomputed SHA, it forms a fourth SHA/fingerprint evidence class.

## 4. Interpreting SHA evidence

Q-Framework uses three distinct SHA meanings:

**Exact Transport SHA** — unchanged state: SOURCE = BRIDGE = TARGET.

**Progressive QREV SHA** — after real compute, SHA_n is expected to differ from SHA_n+1.

**Cross-Environment Computed SHA** — different node/runtime solvers executing the same arithmetic can produce the same computed result hash.

Together these form a traceable state lineage.

## 5. Claims still not made

RC2 does not claim unlimited VRAM, zero OOM, universal model compatibility, universal bitwise GPU determinism, or a completed production-quality full-length 311-aligned-frame H3 run on a single 22 GB RTX 2080 Ti using the newest residency path.

## 6. Disclosure boundary

Published: architecture roles, state lifecycles, smoke/runtime outcomes, hashes, receipts, benchmark methods, sanitized reference interfaces.

Not published: production QmRNA pressure scoring, adaptive-feed equations, page/residency selection, eviction/prefetch policy, Qvram production serialization/restore ordering, Qsearch ranking, scheduler weights/fencing/retry authority, and the production streamed-QKV data plane.

**Open Specification · Open Evidence · Open Reference Interfaces · Closed Production Engine**
