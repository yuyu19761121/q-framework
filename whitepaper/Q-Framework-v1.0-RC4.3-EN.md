# Q-Framework × Temporal Möbius
## Heterogeneous AI Compute Continuity, Native Generation, and a Heterogeneous Supercomputer Neural Network

**HAVEFUN AI Studio — Engineering Whitepaper**  
**Q-Framework v1.0 RC4.3 | 25 October 2026 | English edition**  
**Source:** RC4.3 Chinese full-merged review, retaining the RC4.2 technical evidence and adding the single-GPU findings.

> **Evidence convention.** This paper distinguishes observed execution, independently controlled tests, owner-reported findings awaiting archival evidence, and long-term research objectives. Results from different jobs, resolutions, GPU counts, frame windows, sampler steps, seeds, or retry policies must not be treated as matched performance benchmarks. "One RTX 2080 Ti 22 GB" refers to a memory-expanded card (22,528 MiB), **not** the manufacturer's original 11 GB configuration.

## Executive summary — proof of feasibility before proof of speed

HAVEFUN's Q-Framework is not merely a four-GPU dispatcher. It combines a foundational embedded runtime agent, native H3 sampler and DiT/attention hooks, QmRNA's pressure-aware computation, GPU/CPU state transport, render-segment (RS) coordination, and Temporal Möbius route decisions. Its long-term objective is a **heterogeneous supercomputer neural network**: independently owned, differently capable devices collaborating through verifiable work, reusable state, and feedback-based decisions.

The evidence forms **two distinct execution stories**:

1. **Single-GPU feasibility.** On the A0/A1 RTX 2080 Ti 22 GB environment, MiniMax H3 executed native video workloads. Jobs **#370** and **#371** yielded playable short MP4s; a separate 48-frame/24-fps/14-step H3 run completed on A0. Job **#365** delivered a 15-second, 360-frame video using *one* A0 GPU for ten successive 36-frame RS jobs. Its total elapsed time was **3 h 12 min 08 s**; nine native CUDA OOM attempts were followed by successful full-segment retries. This is a completed single-card **multi-segment** production job, not a one-pass 360-frame native sampler and not an OOM-free run.
2. **Four-GPU production efficiency.** Job **#361** used four independent RTX 2080 Ti 22 GB GPU workers for ten RS jobs, followed by CPU editing across nine seams. Its validated output was **15.000 s, 360 frames, 24 fps, 480×832**, delivered in **14 min 37 s** end to end. The original H3 workflow carried native QmRNA gates; per-job evidence does not show that QFREEZE or a full QVRAM spill/resume cycle fired during #361.

One of the more informative **matched single-card tests** occurred on 4 October 2026: at 480×832, 36 frames, 24 fps, 10 steps, the same A1 GPU, static reference and seed, a baseline without QmRNA guard hit a **PRE-OOM** rescue condition in step 1 and failed to produce the expected single-worker MP4. With QmRNA pre-step guard, the run reclaimed cache, finished all ten steps, and produced an MP4. **PRE-OOM is a software intervention, not proof of a CUDA hard OOM.** This test demonstrates a *workload-feasibility difference* in its measured configuration.

The owner also reports a successful **single-card H3 1080p** result. RC4.3 preserves that report as a **reported result pending primary receipt verification**, not a future target and not yet an independently audited native-1080p benchmark. Verification requires the job/prompt IDs, actual sampler width/height (as distinct from upscaling), frames, timing, native history, and output hash.

### Representative demonstrated results

| Domain | Test / receipt | Outcome and boundary |
|---|---|---|
| Controlled cross-GPU computation | 20-step sampler: GPU0 steps 1–10 → GPU1 steps 11–20 | Bitwise-identical to control; max absolute difference 0.0 |
| State movement | Approximately 250 MiB via GPU→CPU→shared memory/bridge→GPU | Matching source, bridge and destination SHA-256 |
| Native H3 control | QmRNA Static carrier, DiT and sampler hook receipts | Actual checkpoint-cadence change and `QMRNA_DIT_ENTER/EXIT` |
| QmRNA A/B | 22 frames, same reference/seed | All 22 decoded frame hashes matched; 81 s baseline versus 76 s in one measured sampler window |
| Single GPU native video | #370 / #371; A0 | Native H3 short MP4s, about 39 frames at 16 fps (2.437 s) |
| Single GPU full assembly | #365; A0 | Ten serial 36-frame segments → 15 s, with 9 native CUDA OOM retries; 3:12:08 |
| Four GPU end-to-end video | #361; A0/A1/B0/B1 | Ten RS + nine CPU seams; 15 s / 360 frames; 14:37 |
| CPU/GPU state hierarchy | Q7 CUDA state and QFREEZE tests | 32 MiB physical CUDA unload/reload, and controlled pause/resume, in separate experiments |
| Windows & macOS research | Windows Ollama nodes, Mac LAN math | Cross-node chat; 24/24 Mac math-stream batches verified |
| Mathematical learning | Möbius MLP and partial DistilGPT2 | Actual weight updates in separately scoped experimental models |

---

## 1. System position and foundational architecture

### 1.1 Compute continuity rather than GPU count alone

Conventional workflows often assume one model-forward run, one fixed worker, and one card's instantaneous VRAM as the main execution boundary. Q-Framework treats **compute state** as something that can, under compatible conditions, be identified, sealed, hashed, moved, restored and used for continued work. Temporal Möbius evaluates task dependencies, resource availability, elapsed time and observed outcomes when selecting possible execution routes.

The four 22 GB cards have roughly **88 GB of aggregate physical VRAM across four independent devices**. They do **not** become a single unified 88 GB GPU memory space. The research question is whether a software-defined, state-aware execution architecture can make otherwise infeasible individual workloads executable while also improving aggregate delivery efficiency for divisible jobs.

### 1.2 Foundation-00 — Master and embedded runtime agent

Foundation-00 predates the newer four-card job JSON and Studio controls. A Master issues work and resource commands. A runtime agent embedded in H3/ComfyUI connects to native ModelPatcher, Sampler, attention and DiT execution points, then emits attributable receipts. Native locations include `HFQmRNAGate`, `HFQmRNAStaticLoader`, `ModelPatcher.set_model_patch_replace`, `optimized_attention` and Sampler hooks.

Job #341's GPU workflow receipts record `gpu_model_gate_present=true`, `gpu_model_gate_match=true`, and `gpu_workflow_receipt_verified=true`. A newly added UI toggle or absent telemetry must not be confused with the existence of the earlier embedded Q execution path.

### 1.3 Physical heterogeneity and responsibilities

| Layer | Systems | Demonstrated role |
|---|---|---|
| Studio / Owner | HAVEFUN Studio | Authorized job intent, status, output contract and artifact delivery |
| Production Master | YUYU3D (Windows) | Scheduling, job/RS receipts, CPU editing and MP4 assembly |
| Video GPU workers | Node A A0/A1 and Node B B0/B1 | Four independent RTX 2080 Ti 22 GB H3 workers |
| Supporting CPU/bridge | QWorker / Compute Bridge | Mathematical tasks, state transport, SHA verification, rendering preparation |
| Windows Möbius brains | YUYU3D, Node A, Node B, Utility03 | Separate Ollama responses and cross-node dialogue |
| Mac Möbius research | iMac, Mac mini M2, MacBook, fourth M1 | LAN matrix sharding, independent verification, MLP and partial language-model training |

The platform is heterogeneous **across CPU, GPU, operating systems and device roles**. General native H3 state resumption across *different GPU model generations* is a longer-term target, not a universally verified present feature.

## 2. Q-Framework: original technology assets and product roles

The original register consists of Foundation-00 and Q01–Q19. Historical aliases such as QMobius/Temporal Möbius and QMater/QMaster are retained without counting an alias as a separate engine.

| Index | Asset | Actual function and available evidence |
|---|---|---|
| Foundation-00 / Q13 | Embedded runtime agent | Master → H3/ComfyUI native gate and sampler/DiT hooks → execution receipt |
| Q01 | QmRNA Gate | Carries controls into native H3 work; #341 gate and workflow match |
| Q02 | QmRNA Flag Control | Per-job/seed/RS checkpoint cadence, memory warning and pre-OOM policies; Oct 3 carrier changed `checkpoint_every` from 2 to 1 |
| Q03 | QVRAM | Hierarchical VRAM/CPU RAM/bridge state transport; 250 MiB cross-GPU bytes test and separate 32 MiB CUDA unload/reload |
| Q04 | QSTATIC / Motion Static | Reference frames, reusable anchors and state descriptors; static carrier and decoded-frame A/B evidence |
| Q05 | QFREEZE | Reversible pause at a saveable computation boundary; controlled B1 CUDA sampler step 1 → step 5 |
| Q06 | QAnswer / Finalizer | Produces answer packets from prior checkpoints; controlled finalizer executes only its remaining step |
| Q07 | QSearch | Resource, branch and result discovery; four-branch controlled completion |
| Q08 | QRebuild | Reconstructs usable numerical tensors from saved state; PyTorch round-trip test |
| Q09 | QSTATE | Indexed, hashed step/seed/tensor state with bridge replicas and acknowledgements |
| Q10 | Temporal Möbius / QMobius | Mathematical candidate-route and dependency/DAG decisions informed by actual outcomes |
| Q11 | QMater / QMaster / RS | Divides video time into attributable render segments and coordinates native workers |
| Q12 | FaceOff | Identity/face quality assessment and targeted segment retries |
| Q14 | Drip Feed | Bounded QKV/FFN work units; native DiT `ffn_chunk=512` observation |
| Q15 | Sampler Hook | In-runtime callback and model-entry control, not a standalone second accelerator |
| Q16 | Master Message Transport | Job, prompt, worker, event, receipt and ACK correlation |
| Q17 | CPU Frame Editor / PostEdit | Video seam repair, frame-accurate assembly and validation without GPU re-rendering |
| Q18 | Mixed GPU / cross-node handoff | Verified cross-GPU bytes/state tests, A0→B0 controlled CUDA continuation and multi-worker RS production |
| Q19 | Studio Controls | Owner-facing configuration and traceability; UI configuration is not evidence that a native intervention fired |

Additional implementations include HF Compute Bridge/Motion Bridge, QWorker Lite, Streamed-QKV/Page Attention, QBLOCK/QLINEAGE/QREV isolation prototypes, QBonus participation bookkeeping, Windows Möbius Brain, Mac Math Stream, Möbius Neural/LLM experiments, Partner identity enrollment and Network Map. Installation, a running process, a control flag and verified native execution are **different proof levels**.

The production concept is:

```text
Studio / Director -> Foundation-00 Master -> Temporal Mobius route model
  -> RS compiler and QSearch / eligible worker selection
  -> QmRNA Gate / QSTATIC / H3 native GPU workers
  -> attributable RS + QSTATE receipts
  -> CPU Frame Editor / FFmpeg
  -> decoded-frame, length, FPS, hash and delivery checks
```

## 3. Compute-state continuation — from tensors to H3

### 3.1 Deterministic 20-step continuation

A controlled sampler executed steps 1–10 on GPU0, saved the numerical state through CPU/RAM, and executed steps 11–20 on GPU1. The resulting state matched the direct 20-step control **bit for bit** (`max_abs_diff=0.0`). The moved state was numerical work, not merely a copied prompt or picture.

### 3.2 Approximately 250 MiB across memory tiers

The September 28 test moved 262,144,000 bytes (approximately 250 MiB) through GPU0 VRAM → CPU RAM → Windows named shared memory → HF Compute Bridge → GPU1 VRAM. Read-back checks yielded matching SHA-256 values:

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

After the source tensor was deleted, its CUDA memory allocation dropped to zero. The test establishes transport and byte integrity in its scope, **not** a general transparent pooled VRAM implementation.

### 3.3 Native H3 and cross-host state continuation

X1/Motion Bridge receipts include H3 `RESTORE` and `SAMPLER_RESUME` events across compatible workers. Another H3 rescue path reached B0 checkpoint → B1 restore → output. The October 17 Q7 test stored an A0 CUDA `HF_SAMPLER_STATE_V1`, transported it through authenticated bridge replicas with matching hashes, restored it on B0 and executed the controlled next CUDA step. These outcomes must be distinguished from generic arbitrary-model, arbitrary-device seamless resume.

## 4. QmRNA — demonstrable control inside native computation

### 4.1 Static carriers and real sampler control

On October 3, a Static PNG iTXt `HF_QMRNA` carrier reached A1 without changing its SHA. The native runtime emitted `QMRNA_CARRIER_LOADED` and changed sampler `checkpoint_every=2` to `checkpoint_every=1`, with follow-on checkpoints and a `QMRNA_COMPLETE` receipt.

### 4.2 Native DiT hook

On October 6, `QMRNA_DIT_ENTER` and `QMRNA_DIT_EXIT` appeared inside actual MiniMax H3 model work. The logged hidden width was 5,376, sequence length 36,988, and bounded FFN chunk 512. This is model-execution instrumentation, not simply WordPress telemetry.

### 4.3 Same-seed A/B observations

| Measured native window | Baseline | QmRNA | Interpretation |
|---|---:|---:|---|
| 8 frames / 4 steps / same seed and Static | ~34 s | ~30 s | One observed 11.8% reduction |
| 22 frames / 10 steps / same seed and Static | ~81 s | ~76 s | One observed 6.2% reduction |

In the 22-frame case, MP4 container checksums differed, while **22/22 decoded frame MD5 measurements matched**. These are bounded observations, not an all-model speedup guarantee.

### 4.4 Pre-step VRAM reclamation

A forced-guard test logged free VRAM around **460–492 MB**, reclaimed to **2,668 MB** before the next heavy step, and completed 22 frames / 10 steps without a logged hard OOM. It is not proof that every real CUDA tensor was offloaded; cache cleanup and QVRAM tensor transport are distinct mechanisms.

### 4.5 Streamed-QKV numerical semantics

A CPU reference implementation of chunked Q/K/V with online softmax compared to full attention for 257 tokens × 4 heads × 32 head dimensions. The measured maximum absolute errors across tested chunks were approximately **2.09×10⁻⁷–2.98×10⁻⁷**, within the `allclose` checks. This verifies the referenced numerical experiment, not every H3 sampling configuration.

## 5. QFREEZE, QVRAM, QSTATE, QAnswer and QRebuild

October 17 Q7 controlled demonstrations established distinct capabilities:

- **Same-GPU pause/resume:** B1 CUDA micro-sampler recorded `HF_QFREEZE_PAUSED` at step 1, then resumed to step 5.
- **Physical CUDA tensor removal and reload:** 8,388,608 float32 entries (**33,554,432 bytes / 32 MiB**) moved GPU→CPU/bridge→GPU; observed allocation 33,554,432 → 0 → 33,554,432, with consistent SHA and subsequent CUDA computation.
- **State/archive checks:** real sampler QSTATE, two replicas, bridge archive, Master readback and SHA verification.
- **CPU answer/rebuild:** PyTorch numerical summaries and exact `torch.save/load` round-trip of captured tensors.
- **Cross-host continuation:** A0-originated CUDA state restored on B0 and followed by an additional controlled CUDA step.

These receipts belong to **separate experiments**; do not infer that all operations automatically fired in jobs #361 or #365.

## 6. MiniMax H3 — four-card video production

Two Windows video nodes host four independent memory-expanded RTX 2080 Ti cards (A0/A1/B0/B1); YUYU3D handles Master work and CPU delivery.

| Job / date | Workload or route | Recorded outcome |
|---|---|---|
| #135 / Sep 29 | Four-card H3 / bridge / rescue | Final 15.000 s, 36 fps, 540 frames; master hash |
| #243 / Oct 4 | Four GPU parallel QRS | 17 segments completed and video published |
| #327 / Oct 13 | Four-card native H3; 7/7 RS | Configured 10 s, 1080×1920; final MP4 available; approx. 1 h 55 m 44 s end to end |
| #341 / Oct 16 | Original QmRNA gate; 10/10 RS | Native segment phase ~11 m 18 s; complete Studio job ~34 m 18 s; native OOM retries occurred |
| #344 / Oct 17 | Two-island Möbius RS route | 10/10 RS and 15-second, 360-frame assembled MP4 verified |
| #360 / Oct 19 | Four GPUs, ten RS + CPU 9/9 seams | 15 s, 360 frames; **15 m 01 s** end to end |
| **#361 / Oct 19** | **Four GPUs, ten RS + CPU 9/9 seams** | **15 s, 360 frames; 14 m 37 s** end to end |
| T195 / Oct 21 | Ten distinct original RS prompt hashes | Ten native RS outputs, full 15 s / 360 frames |

### Job #361 — golden end-to-end baseline

The official window was **23:07:24–23:22:01 (Taiwan time, October 19)**, 877 seconds. GPU segment production finished at 23:21:07; the CPU worker documented nine completed seams, **42.609 s** editing, and `gpu_invoked=false`. The output contract was H.264, **480×832, 24 fps, 360 frames, 15.000 s**, full decode PASS.

Final MP4 SHA-256:

`a219bb7e78c0e4b0d74823c45d6b0458515583e351c785a686f5c56c424254d8`

Relative to adjacent job #360's 901 s, #361 finished 24 s (2.66%) sooner. It is an **end-to-end** result, not an isolated GPU kernel speed comparison.

PostEdit V2 later reused job #365's original ten RS outputs to assemble 360/360 frames at 24 fps, with reported SSIM **0.984182** to its source and a verified audio-free output. Re-editing does not require regenerating all H3 segments.

## 7. Studio's five creation modes and advanced model work

October 20 Studio jobs **#368–#372** each reached native ComfyUI history success and stored outputs:

| Mode | Job / model / worker |
|---|---|
| Text-to-image | #368, SDXL, B1 |
| Image-to-image | #369, SDXL, B1 |
| Text-to-video | #370, MiniMax H3, A0 |
| Image-to-video | #371, MiniMax H3, A0 |
| Video-to-video | #372, Wan VACE 1.3B, A0 |

Jobs #370/#371 are approximately **2.437-second** native 39-frame/16-fps clips, not 15-second single-pass samples. Additional tests include Qwen-Image-2512 FP8 image generation, Qwen-Image-Edit-2511 FP8 image editing and an A0 MiniMax H3 **480×832, 48-frame, 24-fps, 14-step** text-to-video sample. The 48-frame sample took approximately **549.31 s GPU wall time**. Owner review of #377 showed progress on controlled image editing; a successful model execution is not automatically a final commercial-quality or identity-consistency approval.

## 8. Windows Möbius: actual multi-brain work

YUYU3D, Node A, Node B and Utility03 each operated a separate Ollama responder through identified Studio channels. Cross-node conversation receipts include actual questions, independent replies and follow-up discussion.

A measured Studio arithmetic response originally used a 14B model with **66.186 s** model latency. An isolated CPU-only Qwen2.5 3B service later recorded model calls of **1.094 s** and **1.265 s**, with roughly **4 s** end-to-end Studio completion on that narrow arithmetic task. These are different model/service configurations and not a universal 16× reasoning improvement.

## 9. Mac Möbius: LAN mathematics, four devices and verification

- **iMac:** teacher, source data, row shard A.
- **Mac mini M2:** coordinator and row shard B.
- **MacBook Pro:** independently computes the reference answer and checks hashes.
- **Mac mini M1:** fourth owner device, demonstrated an additional 32×256 row-shard calculation.

**MOBIUS-MATH-001:** controlled 256×256 integer matrix recomputation produced identical final SHA-256 values between M2 and MacBook.

**MOBIUS-MATH-002:** actual LAN dispatch allocated the first 128 rows to iMac and remaining 128 to M2; MacBook independently recomputed the whole matrix. Measured local timings were approximately **895.542 ms**, **578.363 ms** and **2,646.046 ms**, respectively, for their different roles.

**MOBIUS-MATH-STREAM-001:** 24/24 distinct seed/job batches completed and independently verified. Latest merged SHA:

`c8219ed9d202697cb93d771e8124d89d02e593fe8a297d89e80cda668cb88f57`

The fourth Mac successfully calculated its assigned rows in a subsequent controlled experiment. This shows a practical heterogeneous participation path; it does not mean all four Macs already operate as one universal training supercomputer.

## 10. Temporal Möbius: decisions and real model-weight learning

### 10.1 Route model trained on observed outcomes

A Windows World Model replay evaluated **41** native workload outcomes (**24 success, 15 OOM, 2 other failure**). Time-held-out Brier score was **0.338335**, versus comparator **0.375438**. This is a measured improvement in that experimental prediction setup, not a validated autonomous globally optimal scheduler.

### 10.2 Möbius Neural — trained mathematical strategy MLP

An experimental **5×12×3** Tanh/Softmax MLP learned to select between synthetic mathematical kernels. Fifty-four training cases were produced by the iMac; M2 executed **95 epochs**. Loss improved **1.083127 → 0.098988**. Independent MacBook evaluation on **24 unseen tasks** recorded **91.7%** selection accuracy and a measured **2.1161×** comparison to the naive option for those synthetic tasks. Training weights changed and evaluation receipts were retained.

### 10.3 Möbius LLM — partial pretrained-model update

On M2 MPS, a DistilGPT2 experiment used **81,912,576 total parameters**, with **7,089,408 trainable**. Forty-two synthetic training and 12 validation examples, 16 steps and **18.71 s** measured time yielded validation loss **5.720391 → 5.176930**. A 28,362,810-byte trained-weight artifact had a recorded SHA. This is true partial weight updating; it is **not** evidence that a general-purpose autonomous AI has already been completed.

## 11. Why mixed Windows/macOS collaboration matters

The architecture assigns distinct functions to different devices, preserves identity and provenance, and checks results at each boundary. Windows production has native H3 rendering, GPU execution hooks, CPU editing and output verification; Windows research has independent Ollama nodes; macOS research has sharded LAN mathematics and bounded learning experiments.

The broader aim is not to replace an H100 or H200's physical bandwidth with software. It is to **increase the set of executable tasks**, coordinate heterogeneous resources, and choose paths that jointly consider successful completion, time, quality and cost.

## 12. Evidence and verification ledger

| Evidence method | Representative receipt |
|---|---|
| Numerical exactness | Cross-GPU 20-step `max_abs_diff=0.0`; Streamed-QKV error ~2–3×10⁻⁷ |
| Hash integrity | ~250 MiB transported with matching source/bridge/destination SHA-256 |
| Model execution | `QMRNA_DIT_ENTER/EXIT`, #341 native H3 QmRNA gate |
| Callback continuity | QAnswer finalizer callback for remaining step |
| True CUDA residency | 32 MiB allocation 33,554,432→0→33,554,432 |
| Decode equivalence | 22/22 decoded H3 frames' MD5 equal |
| Media contract | #361 15.000 s / 360 frames / 24 fps / 480×832 / valid H.264 |
| CPU editing | Nine seams without GPU regeneration; V2 re-edit 360/360 frames, SSIM 0.984182 |
| Distributed mathematics | Mac LAN 24/24 verified batches with independent recomputation |
| Weight updating | MLP 95 epochs; DistilGPT2 partial 16-step training |

Every numeric finding is scoped to the corresponding run. Raw owner photos, private prompts, credentials and customer media are outside this publication.

## 13. Conclusion — executable work is the milestone

Q-Framework's central engineering contribution is to investigate **what computation can be completed on constrained, existing hardware**, not just how many GPUs can be put in one queue. The documented path reaches from a single memory-expanded 2080 Ti executing H3, through the 36-frame same-card QmRNA PRE-OOM contrast, to successful four-worker RS production, numerical state continuation and mixed-platform math/learning.

Temporal Möbius extends this toward an adaptive control loop: **past receipts → candidate future routes → current resource decision → measured result → updated decision evidence**. This is a practical research direction toward a heterogeneous supercomputer neural network, with substantial generalization and full-scale autonomy still to validate.

**Q-Framework — Connecting Compute. Extending Possibility.**

---

## Appendix A — Public technical material

- [Prior public whitepaper RC3 (English)](Q-Framework-v1.0-RC3-EN.md)
- [Validated execution paths](../docs/validated-execution-paths.md)
- [Public claim ledger](../docs/claim-ledger.md)
- [Architecture overview](../docs/architecture.md)

## Appendix B — Internal experiment locator index

These IDs locate audit records; complete private workflows, prompts, personal source media, tokens and credentials are intentionally excluded.

- State transport: HF Compute Bridge F-Block XCOPY (2026-09-28); Q7 integration (2026-10-17).
- QmRNA/QSTATIC: Oct 3 PNG iTXt carrier; Oct 4 A1 A/B; DiT job #303; #341 gate receipt.
- H3 video: #135, #243, #327, #341, #344, #360, #361, #365, #370, #371; 2026-10-21 T195.
- Windows brains: October 15 Studio Möbius Brain Chat and independent node reply receipts.
- Mac: MOBIUS-MATH-001/002/STREAM-001, MOBIUS-EIGHT-001, MOBIUS-NEURAL-001, MOBIUS-LLM-001.
- CPU re-edit: HF_RS_POSTEDIT_V2_IMPLEMENTED (2026-10-23).

## Appendix C — The standalone 2080 Ti 22 GB matters

**Why this appendix exists.** RC4.2 emphasized multi-GPU production. RC4.3 independently establishes a single-card evidence chain. A job assigned entirely to A0 or A1 is not a four-worker collaboration, even if it uses sequential 1.5-second RS, CPU editing and normal storage services.

| Case | Native single-card evidence | Limit |
|---|---|---|
| #370 / #371 | H3 A0 short text-to-video/image-to-video native MP4s | 39 frames, 16 fps, ~2.437 s, not 15 s |
| Oct 21 H3 | A0 at 480×832, 48 frames, 24 fps, 14 steps, ~549.31 s | Two seconds of native video |
| #365 | A0 produced ten successive 36-frame RS and a final 15-second, 360-frame video | 3:12:08; 9 CUDA OOM attempts subsequently retried from new prompt IDs |
| #361 (separate) | Four RTX 2080 Ti workers | 14:37 for a different 8-step end-to-end configuration |

**1080p evidence status.** The owner states that a single memory-expanded 2080 Ti successfully completed H3 work at 1080p. This report is preserved as an achieved *owner-reported* result awaiting a matching native job receipt. The publication does not reclassify it as merely a future goal, and does not relabel a 480p/upscaled artifact as native 1080p.

## Appendix D — A bounded before/after feasibility demonstration

**Date:** 2026-10-04. **Hardware:** Node A A1, RTX 2080 Ti 22,528 MiB. **Comparable settings:** same reference Static, seed, 480×832, 24 fps, 36 frames, 10 steps.

- **Baseline, no QmRNA Guard:** at step 1 the runtime recorded **108 MB** free and `RESCUE_ARMED reason=PRE_OOM`. No final direct single-worker `cut_A1_BASE36*.mp4` was produced.
- **QmRNA Guard:** before steps 1–9, pressure fell to **76–140 MB** free. The guard reclaimed cache to roughly **3,212–3,244 MB**, proceeded through all 10 steps, and produced a **188,242-byte MP4** without a recorded HARD_OOM in that run.
- **Additional test:** a 22-frame/10-step forced guard raised free VRAM from **460–492 MB to 2,668 MB** and finished.
- **Control at model execution:** H3 DiT logging showed native enters/exits and `ffn_chunk=512`.

**Interpretation:** under these specific conditions, QmRNA made a difference between *baseline pre-OOM non-completion* and *single-card completion*. This directly supports feasibility-oriented research. It does **not** demonstrate that every baseline model on this GPU must fail, that every QmRNA run avoids OOM, or that a 32 MiB independent CUDA offload was necessarily triggered in this H3 job.

## Appendix E — Long-term objective: heterogeneous supercomputer neural network

The proposed system has four layers:

1. **Native execution:** Foundation-00 and QmRNA connect to sampler/DiT/attention control within a compatible host.
2. **State and memory:** QVRAM, QSTATIC, QSTATE and QFREEZE represent reproducible saved work and controlled memory transitions.
3. **Distributed collaboration:** QSearch, QWorker, RS and Compute Bridge route tasks and verifiable outputs among independent devices.
4. **Decision and learning:** Temporal Möbius learns from prior results, predicts bounded candidate routes, makes present decisions and feeds real outcomes back into its evaluation.

**Already demonstrated:** bounded QmRNA A/B, native single-card H3 outputs, #365 sequential single-card 15-second completion with retries, #361 four-worker production, cross-GPU state tests, Mac LAN mathematical verification, and small MLP training.

**Not yet generalized:** seamless native H3 state continuation across arbitrary GPU generations, a quantitatively validated globally autonomous scheduler, continuously learning global network intelligence, or matched single-GPU H100/H200 performance superiority.

A heterogeneous supercomputer neural network should be evaluated by **task feasibility, reproducible state integrity, validated decision quality, media quality, end-to-end delivery, and total resource cost** rather than by raw aggregate VRAM alone.
