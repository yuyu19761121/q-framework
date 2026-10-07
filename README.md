# Q-Framework

**Verifiable Heterogeneous AI Compute Continuation**

Q-Framework is a running AI-compute research system focused on resumable and verifiable execution across constrained, heterogeneous compute resources.

> **Publication policy: real evidence, black-box mechanism.**

**Current public release:** Evidence Whitepaper v1.0 RC3  
**Snapshot:** 2026-10-07

[繁體中文](README.zh-TW.md)

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
- Qvram residency implementation;
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
