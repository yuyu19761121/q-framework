# Q-Framework

**Verifiable Heterogeneous AI Compute Continuation**

Q-Framework is a running AI-compute research system focused on resumable and verifiable execution across constrained, heterogeneous compute resources.

> **Publication policy: real evidence, black-box mechanism.**

> **Important: Q-Framework is not a monitoring dashboard.** Live Compute is only the public proof surface. The production engine has been exercised inside MiniMax H3 / ComfyUI-class VRAM-pressure and PRE-OOM execution paths, including checkpointing, state spill, GPU-residency release, restore, same-GPU / mixed-GPU continuation and recovery. The purpose is not merely to observe OOM; it is to preserve useful computation, release memory residency, restore state and continue execution.

This project is unrelated to Unity QFramework, NVIDIA CUDA-Q, or other similarly named frameworks.

**Naming concept:** `QmRNA` is the Q-Framework-defined runtime messenger / control-signal layer. Its name intentionally borrows the messenger principle of mRNA—carrying instructions toward the place where they are acted upon. In Q-Framework, it carries workload intent and control signals toward the QVRAM / VRAM-facing runtime. This is a computing metaphor, not biological RNA technology; **Q does not mean Quantum**. `H3` refers to the MiniMax H3 AI video-generation path, and `OOM` means Out of Memory in the CUDA / PyTorch / GPU-VRAM context.

**ComfyUI integration status:** the production H3 recovery path is integrated with a local Windows ComfyUI runtime, including a node-local custom runtime hook inside the ComfyUI process plus external Master / Bridge state-lineage orchestration. It is not merely cloud telemetry, and it is not currently packaged as a universal one-click ComfyUI Manager plugin. **It is also not a ComfyUI core fork or core-source modification distribution**; the validated path uses custom-node / runtime-extension integration plus external state/orchestration layers and does not require replacing the official ComfyUI source tree.

**Current public release:** Evidence Whitepaper v1.0 RC3  
**Snapshot:** 2026-10-07

[繁體中文](README.zh-TW.md)

## 🔴 Live Compute Stream

**[Open the Q-Framework Live Compute Stream](https://yuyu19761121.github.io/q-framework/)**

Watch the system while it is actually running: current Job, four-GPU branch activity, GPU / VRAM load, QmRNA / QSTATE progress, production-node heartbeat, and live execution status. The public telemetry view updates continuously and is designed to show that the compute path is active, not a static demo.


## Public proof

The repository publishes selected proof of feasibility:

- exact hash and bitwise validation where exact equality was observed;
- numerical-tolerance evidence where exact equality was not expected;
- completed-output hashes;
- sanitized workload and hardware classes;
- carefully bounded claims.

See **[Public Proof Pack](docs/public-proof-pack.md)**.

## Black-box boundary

Q-Framework does not publish enough information to reconstruct the production engine.

The following remain proprietary:

- production state representation;
- checkpoint packing and restore sequencing;
- QmRNA signal representation, control equations and coefficients;
- QSTATIC internal contracts and selection logic;
- QVRAM residency implementation;
- memory-pressure thresholds;
- eviction/prefetch policy;
- scheduler, worker-selection, lease/fencing and retry logic;
- production model-forward modifications;
- internal topology and source code.

See **[Disclosure Boundary](docs/disclosure-boundary.md)**.

## Selected validated outcomes

- Deterministic continuation: bitwise-identical result, max absolute difference 0.0.
- ~250 MiB state transport: exact SHA preserved end-to-end.
- Real H3 continuation: completed output after continuation on another GPU worker.
- Four-worker production-class execution: 15.000 s / 540 frames with four independent RTX 2080 Ti 22 GB workers participating.
- Cross-environment numerical consistency: identical recomputed-result SHA across three execution environments.
- QSTATIC + QmRNA controlled equivalence: 22 / 22 decoded frame hashes matched.

## Claim discipline

Q-Framework does **not** claim unlimited VRAM, zero OOM probability, universal bitwise determinism, universal model compatibility, or physical VRAM aggregation.

## Whitepaper

- [RC3 Evidence Whitepaper - English](whitepaper/Q-Framework-v1.0-RC3-EN.md)
- [RC3 Evidence Whitepaper - Traditional Chinese](whitepaper/Q-Framework-v1.0-RC3-ZH-TW.md)

Previous RC2 files remain historical snapshots and do not represent the current disclosure boundary.

**Real evidence. Black-box mechanism.**
