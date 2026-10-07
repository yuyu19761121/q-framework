# Q-Framework

**Compute-State Virtualization and Adaptive Flow Control for Heterogeneous AI Infrastructure**

Q-Framework is an experimental AI compute architecture focused on making long-running generative workloads observable, controllable, pausable, resumable, and movable across heterogeneous compute resources.

> **This repository documents a running system. It does not publish the proprietary production engine.**

**Status:** Development & Validation Whitepaper v1.0 RC2  
**Snapshot date:** 2026-10-07

[繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

## Whitepaper PDFs

**[English PDF](whitepaper/Q-Framework-v1.0-RC2-EN.pdf)** · **[繁體中文 PDF](whitepaper/Q-Framework-v1.0-RC2-ZH-TW.pdf)** · **[日本語 PDF](whitepaper/Q-Framework-v1.0-RC2-JA.pdf)**

## Sponsor Q-Framework

**[Sponsorship Overview](SPONSORSHIP.md)** · **[繁體中文贊助說明](SPONSORSHIP.zh-TW.md)** · **[Full Sponsorship Prospectus PDF](sponsorship/Q-Framework-Sponsorship-Prospectus-v1.0-ZH-TW.pdf)**

Funding, hardware, cloud credits and research collaboration can directly expand Q-Framework's validation capacity while the production engine remains proprietary.

## What Q-Framework is exploring

Conventional generative AI pipelines often treat GPU memory exhaustion as a terminal boundary. Q-Framework explores a different systems model:

- memory pressure is treated as a control signal;
- compute state can be persisted instead of discarded;
- work can be resumed after resource pressure or node failure;
- CPU, RAM, disk and multiple GPUs can participate as distinct resource tiers;
- GPU execution can be fed adaptively instead of only by fixed-size jobs.

The architectural vocabulary currently includes:

- **QmRNA** — runtime telemetry and control plane
- **Qvram** — persistent compute-state / checkpoint and residency layer
- **Qsearch** — state and working-set retrieval layer
- **Qanswer** — heterogeneous CPU/GPU orchestration layer
- **QSTATIC** — precomputed/static visual-state source layer
- **QSTATE / QBLOCK / QLINEAGE / QREV** — state, block, lineage and revision primitives

## Evidence status

### Demonstrated / reproducible in the current development system

- deterministic cross-GPU sampler-state transport has been exercised with exact state/hash verification;
- GPU → CPU/RAM → shared-memory → GPU continuation has been exercised as a real rescue path;
- persistent lineage and checkpoint metadata are used to preserve continuation identity;
- QmRNA has executed inside a MiniMax H3 model-forward candidate path rather than only observing external telemetry;
- exact FFN token chunking has been exercised in a live H3 candidate path;
- a CPU-only streamed/global-attention reference implementation has matched full attention within normal floating-point tolerance in controlled verification.

### Partially demonstrated / still under validation

- full-length compute-state virtualization for a 15-second continuous H3 task on a single 22 GB GPU;
- streamed Q/K/V GPU data-plane integration across the complete H3 forward path;
- general-purpose working-set virtualization across arbitrary models;
- production-grade spill/prefetch policy across RAM and disk.

### Not claimed

Q-Framework does **not** currently claim:

- “unlimited VRAM”;
- zero OOM probability;
- universal acceleration for all models;
- equivalence to a specific datacenter GPU;
- that the complete production control algorithm is published here.

See [docs/claim-ledger.md](docs/claim-ledger.md) and [Validated Execution Paths](docs/validated-execution-paths.md).

## Public repository scope

**Open Specification · Open Evidence · Open Reference Interfaces · Closed Production Engine**

Published here:

- architecture and terminology;
- claim ledger;
- benchmark methodology;
- public schemas and interfaces;
- simplified control-loop examples;
- a sanitized proof-manifest implementation derived from the internal verifier;
- multilingual publication notes.

Not published:

- production QmRNA pressure scoring;
- residency/page-selection logic;
- eviction and prefetch heuristics;
- Qvram production serialization and restore sequencing;
- Qsearch ranking / cache heuristics;
- scheduler weights, lease/fencing policy and retry authority;
- production streamed-QKV implementation;
- infrastructure endpoints, credentials or private topology.

See [docs/disclosure-boundary.md](docs/disclosure-boundary.md).

## Repository layout

```text
q-framework/
├── README.md
├── README.zh-TW.md
├── README.ja.md
├── NOTICE.md
├── SECURITY.md
├── CITATION.cff
├── CHANGELOG.md
├── docs/
├── benchmarks/
├── reference/
└── whitepaper/
```

## Publication note

The public code is intentionally **reference code**, not the production execution engine. Some functions are derived from non-sensitive portions of the running system and then simplified or stripped of proprietary policy.

No license file has been applied yet. Unless explicitly stated otherwise, publication of source text in this repository does not grant rights to the unpublished production engine, trademarks, patents, or proprietary implementation details.

## Next validation target

A reproducible full-length benchmark recording:

- model/version hash;
- GPU and VRAM;
- width/height/fps/frame count;
- precision and steps;
- peak VRAM;
- runtime;
- checkpoint / freeze / resume counts;
- intervention receipts;
- output hash;
- baseline outcome versus Q-Framework outcome.

**Let evidence carry the claim.**
