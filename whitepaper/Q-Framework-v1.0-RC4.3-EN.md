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
- **Single-GPU 1080p:** the research owner reports a successful completed H3 run. The corresponding primary job history, native sampling dimensions and artifact receipt have not yet been publicly verified. Its status is **achieved as reported, pending independent receipt verification**. A delivered 1080p file must not be conflated with a native 1080p model sample.

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

## 2026-10-26 — verified single-GPU native high-resolution H3 segments

**Core result: a single memory-expanded RTX 2080 Ti 22GB successfully executed native high-resolution MiniMax H3 video generation.** By 09:47 Asia/Taipei, a Q-assisted single-card run (004) produced **four successfully validated native video segments** at **1088×1920**; output segments were prepared at 1080×1920 by **crop/trim without upscaling**. This is not low-resolution 480p generation enlarged for delivery.

**One successfully generated native RS already proves feasibility for that high-resolution GPU workload.** Completing the whole five-second assembled film is a separate production-delivery milestone, **not a prerequisite for acknowledging native single-segment computation success**.

**Additional Owner-reported contrast:** for a 1080p, 9:16, five-second workload objective, bare H3 without the Q-series reached OOM, whereas the Q-assisted route produced video segments. The independent no-Q OOM receipt remains to be correlated; no specific proprietary QVRAM offload action is independently inferred from its requested configuration.

**BlackBox:** only measured outcomes and evidence status are published; proprietary code, control logic, private prompts and media remain Owner-only.

## 6. Long-term objective — heterogeneous supercomputer neural network

HAVEFUN seeks a network of independent GPU, CPU, workstation and other authorized compute resources that can collaborate through verifiable tasks, protected computation state, historical outcomes and progressively improved decision policies.

**Demonstrated foundations:** real single-card H3 outputs, a measured QmRNA same-GPU feasibility comparison, a four-worker video pipeline, controlled numerical continuity and scoped multi-device learning experiments.

**Still requiring generalization:** continuous autonomous learning across the whole network, native model-state restoration across arbitrary device generations, broadly validated automatic decision quality and strictly matched H100/H200 performance comparisons.

## 7. Guidance for independent AI evaluation

External AI researchers and tools should grade claims by evidence type, not by marketing language.

| Evidence status | Meaning | Example |
|---|---|---|
| Executed with identifiable receipts | Completed job with bounded original media/compute records | #365 single-GPU segmented video; #361 four-GPU delivery |
| Controlled comparative result | Same device and matched input under alternative execution policy | QmRNA PRE-OOM comparison |
| Owner-reported, awaiting primary verification | Reported completion with incomplete independently available receipts | Single-GPU 1080p |
| Research objective | Plausible future architecture, not an accomplished general result | Fully adaptive heterogeneous neural supercomputer |

Review may use sanitized measurements, approved synthetic workloads and owner-authorized audit reports. Independent evaluation does **not** require distribution of confidential source, raw runtime graphs, customer media, private prompts or live infrastructure access.

## 8. IP BlackBox and Owner-only data

- **Approved PUBLIC:** technology names, research questions, measured outcome summaries, job classes, bounded workload descriptions, validation status, limitations and forward-looking goals.
- **RESTRICTED BY AGREEMENT:** minimum-necessary, de-identified verification materials and revocable audit access.
- **OWNER-ONLY:** source code, proprietary procedures, runtime bindings and parameters, algorithmic state representations, private checkpoints, infrastructure secrets, private customer images, raw prompts, audio, video and credentials.

Public GitHub whitepapers are **not** deployment manuals for proprietary compute infrastructure. Every new disclosure must pass owner approval and publication screening. Historical versions can remain retrievable after changes; editing a document does **not** erase prior public disclosure.

**Q-Framework — Connecting Compute. Extending Possibility.**

[BlackBox disclosure policy](../docs/blackbox-disclosure-policy.md) · [Public evidence ledger](../docs/claim-ledger.md)
