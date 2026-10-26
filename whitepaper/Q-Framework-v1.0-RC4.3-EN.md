# HAVEFUN Q-Framework × Temporal Möbius
## RC4.3 — BlackBox Public Research Edition (English)

**Research: single-GPU AI workload feasibility, heterogeneous GPU collaboration, and a heterogeneous supercomputer neural network**  
**October 2026 | Proprietary implementation and private validation assets are owner-controlled**

> **Public disclosure boundary:** This document presents observable outcomes and their limits. It does not disclose proprietary source code, native model integration points, computation-state representation, control strategies, complete inference graphs, internal configuration, private images, video, audio or prompts. Full original receipts remain in separately authorized environments. Reported success is not a general performance guarantee.

## 1. The research question

A GPU's physical VRAM capacity is not necessarily the upper limit of the AI tasks that software can complete with that device under a specific architecture. HAVEFUN investigates **task feasibility on constrained hardware**, followed by efficient coordination of independently addressable devices.

The Q-Framework research portfolio includes QmRNA, QVRAM and QSTATIC for memory-aware execution and computation continuity, and Temporal Möbius for experience-informed execution-route decisions. These descriptions identify research responsibilities, **not proprietary algorithms or implementation procedures**. Software does not physically increase a GPU's arithmetic capability, bandwidth or onboard memory.

## 2. Evidence track one — real H3 video execution on one RTX 2080 Ti

**Hardware:** a memory-expanded RTX 2080 Ti with approximately 22 GB VRAM per card, not the factory 11 GB version.

- **Studio #370 and #371:** completed native MiniMax H3 short-video generation on a single GPU and produced decodable MP4s. These were short clips, not one-pass native 15-second inference.
- **Job #365:** one GPU sequentially executed ten short native video segments. The segments were assembled into a **15-second, 360-frame** output. End-to-end execution took **3 hours 12 minutes 08 seconds**. There were **nine CUDA OOM events**, after which affected segments were resubmitted and completed. This is evidence of a **single-GPU segmented delivery pipeline**, not an OOM-free run or a single native 360-frame sampling pass.
- **26 Oct 2026, verified single-GPU 1080p-class final movie:** One memory-expanded RTX 2080 Ti 22GB completed **10/10 native 1088×1920 H3 RS segments**, cropped and trimmed without upscaling to a verified **1080×1920, 5-second, 120-frame, 24fps MP4**. **Zero recorded CUDA OOM events**, **1h 39m 16s** elapsed; final-media integrity confirmed, owner visual-quality review pending. This is segmented generation, not a one-pass 120-frame native sample.

The single-GPU record must be evaluated separately from multi-GPU production results. Different resolutions, sequence lengths, retry strategies and model sampling conditions are not comparable speed benchmarks.

## 3. Evidence track two — controlled same-GPU QmRNA comparison

A controlled test on the same memory-expanded 22 GB RTX 2080 Ti used the same reference, seed and scope: **480×832, 36 frames, 24fps and 10 sampler steps**.

| Route | Observed outcome |
|---|---|
| Baseline route | Entered a **PRE-OOM** safeguard at the first step; the expected single-worker MP4 was not delivered |
| QmRNA-protected route | Completed all ten steps and wrote a playable MP4, with no recorded CUDA HARD_OOM in that run |

This is a bounded feasibility result: **different execution controls changed whether the measured task finished**. PRE-OOM is a preventive software condition, **not** proof that a native CUDA out-of-memory exception occurred. The result does not establish universal OOM immunity for all H3 workflows.

Implementation details, runtime configuration, internal state and control mechanisms are restricted; the public research claim concerns observed inputs, outcomes, comparison design and its limitations.

## 4. Evidence track three — four independent GPU workers

Official Job **#361** coordinated **four independent RTX 2080 Ti 22 GB GPUs**, generated ten short video segments and used CPU editing to deliver a checked final result:

| Measure | Recorded output |
|---|---|
| Final video duration | 15.000 seconds |
| Frame count / rate | 360 frames / 24fps |
| Final canvas | 480×832 portrait |
| GPU class and count | Four independent memory-expanded RTX 2080 Ti cards |
| End-to-end elapsed time | **14 minutes 37 seconds** |
| Media validation | Decodable MP4 matching the requested duration and frames |

This is an **end-to-end video production** measurement, not a per-card native sampler benchmark. It must not be compared directly to unrelated 1080p tests. The four separate 22 GB VRAM devices are **not a single directly addressable 88 GB GPU**.

## 5. Independent numerical and consistency outcomes

Separate controlled experiments recorded:

- A 20-step numerical workload continuing across GPUs with a bitwise-identical result and measured maximum absolute difference **0.0**.
- Approximately **250 MiB** of computation-state movement with matching verification digests at the relevant endpoints.
- **22 of 22** matching decoded video frames in a bounded QmRNA comparison.
- Heterogeneous Windows/macOS mathematical tasks, independent recomputation and limited model-weight training trials.

These observations were not all produced within the same H3 video job. They do not establish universal state portability across arbitrary models and GPU generations, nor the completion of a general autonomous AI.

## 26 October 2026 — verified single-GPU 1080p-class native H3 RS **and complete five-second film**

**A completed, receipt-backed result:** A single **memory-expanded RTX 2080 Ti 22GB GPU** ran a Q-assisted MiniMax H3 workflow, producing **ten out of ten native high-resolution video segments and an assembled 1080×1920 five-second MP4**. Native per-segment GPU results and final-media integrity are separately documented.

| Measure | Confirmed single-GPU result |
|---|---|
| Hardware | **One RTX 2080 Ti expanded to ~22GB VRAM** (not factory 11GB) |
| Native MiniMax H3 segments | **10/10 succeeded**, natively generated at **1088×1920 / 22 frames each** |
| Delivered output | **1080×1920, 9:16, 5.000 seconds, 24fps, 120 frames, MP4** |
| Output transform | Crop and temporal trim (12 delivered frames per RS), **no upscaling** |
| Recorded CUDA OOM | **Zero in this run** |
| Total elapsed time | **1 hour 39 minutes 16 seconds** |
| Verification | Native execution and RS receipts; final dimensions and media-integrity digest; **owner visual-quality review pending** |

The result establishes **both native 1080p-class H3 RS feasibility on one card and verified completion of a five-second 1080p final movie**. Each segment was natively generated at 1088×1920, then cropped and trimmed to the delivery canvas. This was **not** low-resolution-to-1080p upscaling and **not** one uninterrupted native 120-frame sampling pass.

**Evidence limits:** Five seconds is the final video's **playback duration, not generation latency** (the run took 1h 39m 16s). A zero-OOM result for one bounded task does not establish universal OOM immunity. Q assistance was active, but isolated causal proof of a particular QVRAM physical spill/resume operation is not claimed. The owner's separate no-Q H3 OOM report still awaits matching primary error evidence.

**BlackBox:** Proprietary runtime internals, model integration, private prompts/media, customer data and complete control strategies are not published.

## 6. Long-term objective — heterogeneous supercomputer neural network

HAVEFUN seeks a network of independent GPU, CPU, workstation and other authorized compute resources that can collaborate through verifiable tasks, protected computation state, historical outcomes and progressively improved decision policies.

**Demonstrated foundations:** real single-card H3 outputs, a measured QmRNA same-GPU feasibility comparison, a four-worker video pipeline, controlled numerical continuity and scoped multi-device learning experiments.

**Still requiring generalization:** continuous autonomous learning across the whole network, native model-state restoration across arbitrary device generations, broadly validated automatic decision quality and strictly matched H100/H200 performance comparisons.

## 6A. Multi-node heterogeneous compute plan (public roadmap)

**Objective:** Under Owner authorization, coordinate distinct macOS/Windows, CPU/GPU and reasoning/production nodes for divisible math, inference, video-RS generation, verification and feedback tasks. **This is an engineering roadmap, not a claim that an eight-device native video inference network has already shipped.**

| Role | Intended work | Evidence status |
|---|---|---|
| Master / orchestration | Authorized task admission, verifiable work partitioning, route selection, receipts and Owner stop/rollback rights | Validated bounded multi-GPU video workflow; unified cross-host orchestration remains under integration |
| Brain / reasoning and evaluation | Bounded mathematical work, candidate route assessment, quality scoring and learning feedback across a target of four macOS devices | Limited distributed-math and training experiments exist; continuous autonomous closed loop not yet fully verified |
| Windows GPU/CPU Workers | Execute compatible RS or numerical tasks, report performance, completion and errors; target four Windows worker hosts | Four discrete GPUs completed one bounded production workload; generalized cross-host Worker protocol still being validated |

**Target fleet: four macOS Brain devices plus four Windows Worker hosts = eight heterogeneous devices.** The number **eight is a deployment target, not eight verified simultaneous compute nodes or eight GPUs**. The completed #361 four-GPU video pipeline and the planned eight-host topology are different evidence claims. Four separate 22GB GPUs do not form one directly addressable 88GB GPU.

**Planned closed loop:**

`Owner-approved request → Master task/RS partition → Brain reasoning + Worker execution → per-task receipts and independent checks → delivery / QC → experience feedback → next-route evaluation`

Each step must yield a task identifier, state, node-independent success or failure receipt, latency and verifiable output. Planned engineering gates include worker identity compatibility, heartbeat, timeout, idempotent claim/submit, offline recovery, recovery after failure, quality checks and Owner-authorized cancellation. **These are acceptance criteria, not blanket claims of current functionality.** QmRNA, QVRAM, QSTATIC, QAnswer and Temporal Möbius are named functional modules; proprietary orchestration, internal state representation and model integration remain BlackBox.

| Phase | Acceptance gate | Status |
|---|---|---|
| **P0 measured foundations** | Single-GPU 1080p/5s film, #361 four-GPU 480p/15s film, bounded numerical/integrity tests | Verified within stated scopes |
| **P1 one remote Worker loop** | Identity, claim, compute, submit, receipt, heartbeat, failure and independent re-check | Integration in progress |
| **P2 eight-device rollout** | Four Brain + four Windows Worker devices with observable availability, scheduling, isolation and failover | Planned, not fully verified |
| **P3 learning-to-smoke loop** | Learning output triggers isolated smoke, Master/Möbius evaluation of quality, consistency and throughput | Research stage |
| **P4 public benchmark** | Per-workload completion rate, runtime, node contributions, OOM/failure counts and output consistency | Awaiting verified dataset |

The principal metrics are **task feasibility first, then speed, correctness, reliability and resource use**. Do not infer universal cross-generation GPU model-state continuation or fully autonomous heterogeneous neural computation from a bounded four-GPU video production case.

Public diagram and stage details: [multi-node architecture page](../site/multi-node.html) · [public roadmap](../docs/multi-node-roadmap.md). Internal node names, IPs, authentication, native runtime and owner media are not published.

## 7. Guidance for independent AI evaluation

External AI researchers and tools should grade claims by evidence type, not by marketing language.

| Evidence status | Meaning | Example |
|---|---|---|
| Executed with identifiable receipts | Traceable native computation, final movie and integrity receipts | **26 Oct 2026 single-GPU 1080p / 5s / 120f / 10 RS completed**; #365 single-GPU segmented film; #361 four-GPU delivery |
| Controlled comparative result | Same device and matched input under alternative execution policy | QmRNA PRE-OOM comparison |
| Owner-reported, awaiting primary verification | Comparison-side original error not yet matched | **Separate bare-H3 no-Q OOM report**, not the verified Q-assisted 1080p movie |
| Research objective | Plausible future architecture, not an accomplished general result | Fully adaptive heterogeneous neural supercomputer |

Review may use sanitized measurements, approved synthetic workloads and owner-authorized audit reports. Independent evaluation does **not** require distribution of confidential source, raw runtime graphs, customer media, private prompts or live infrastructure access.

## 8. IP BlackBox and Owner-only data

- **Approved PUBLIC:** technology names, research questions, measured outcome summaries, job classes, bounded workload descriptions, validation status, limitations and forward-looking goals.
- **RESTRICTED BY AGREEMENT:** minimum-necessary, de-identified verification materials and revocable audit access.
- **OWNER-ONLY:** source code, proprietary procedures, runtime bindings and parameters, algorithmic state representations, private checkpoints, infrastructure secrets, private customer images, raw prompts, audio, video and credentials.

Public GitHub whitepapers are **not** deployment manuals for proprietary compute infrastructure. Every new disclosure must pass owner approval and publication screening. Historical versions can remain retrievable after changes; editing a document does **not** erase prior public disclosure.

**Q-Framework — Connecting Compute. Extending Possibility.**

[BlackBox disclosure policy](../docs/blackbox-disclosure-policy.md) · [Public evidence ledger](../docs/claim-ledger.md)
