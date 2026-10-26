# Q-Framework × Temporal Möbius

**Single-GPU H3 successes · Four-GPU production · Heterogeneous supercomputer neural network**

HAVEFUN's Q-Framework is **not only a multi-GPU system**. Actual native MiniMax H3 video tests have **succeeded on a single memory-expanded RTX 2080 Ti 22 GB GPU**. QmRNA's low-memory execution control, computation-state continuity, and Temporal Möbius scheduling address both *whether a task can finish* and *how a heterogeneous system should execute it*.

### Demonstrated results

- **Single GPU, QmRNA feasibility:** On A1 (RTX 2080 Ti 22,528 MiB), a matched 36-frame, 10-step H3 test completed and produced an MP4 with QmRNA Pre-step Guard. The unguarded baseline hit a **PRE-OOM** intervention at step 1 and did not produce its expected single-worker MP4. PRE-OOM is not a CUDA hard OOM.
- **Single GPU, real H3 media:** Jobs **#370/#371** produced native H3 short videos on A0. **#365** also finished a complete **15-second / 360-frame** assembled video using *one A0 GPU*, rendering ten sequential 36-frame segments. Total elapsed time was **3h 12m 08s**; nine native CUDA OOM attempts required resubmission of the corresponding segments. It was **not** a single 360-frame sampler or an OOM-free run.
- **Four GPUs, rapid production:** Job **#361** delivered a **15-second / 360-frame / 480×832 / 24fps** video in **14m 37s** end to end using four independent RTX 2080 Ti workers and CPU editing.
- **Native execution and state integrity:** H3 sampler/DiT hooks, 22/22 matching decoded frames in a QmRNA control, bitwise-identical controlled 20-step cross-GPU continuation and approximately 250 MiB of SHA-verified state transport.
- **Mixed Windows/Mac research:** separate verifiable math sharding, model-response, and bounded weight-training results.

**Native high-resolution H3 RS completion is now verified on a single card.** Separate owner-reported single-GPU 1080p results still require matching original run receipts.

**26 Oct 2026 — single-card high-resolution H3 has succeeded:** On one RTX 2080 Ti 22GB, the Q-assisted route produced **four verified native 1088×1920 H3 RS videos**, cropped without upscaling to 1080×1920. **Successful individual RS generation already establishes native high-resolution GPU task feasibility; a full five-second edit is a separate delivery objective.** The Owner also reports bare no-Q H3 OOM under the corresponding target workload; its original error record remains to be correlated. [Evidence](docs/claim-ledger.md).

### RC4.3 technical whitepapers (full-length)

| Language | Markdown | PDF |
|---|---|---|
| English | [Full whitepaper](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |
| 繁體中文 | [技術白皮書](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| 日本語 | [技術白書](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |

Earlier RC1–RC3 versions remain available in [whitepaper/](whitepaper/).

**Long-term research goal:** a heterogeneous supercomputer neural network with verifiable, adaptive compute nodes. Universal cross-generation GPU resumption and matched superiority over H100/H200 are **not yet demonstrated**.

[Public claim ledger](docs/claim-ledger.md) · [Validated execution paths](docs/validated-execution-paths.md) · [Architecture](docs/architecture.md)

### BlackBox disclosure and AI-readable evidence

Only **approved outcome summaries and measurement limitations** are public. Proprietary QmRNA/QVRAM/Temporal Möbius source, native runtime integration, state encodings, decision algorithms, private prompts, customer media and full raw execution logs are **not part of this repository**.

- [Machine-readable public evidence (JSON)](evidence/claims-public-rc4.3.json)
- [BlackBox disclosure policy](docs/blackbox-disclosure-policy.md)
- [Responsible security communication](SECURITY.md)

Independent AI evaluation should distinguish confirmed executions, controlled comparisons, owner reports awaiting primary receipt verification, and future research objectives. No private implementation access is required.

**Q-Framework — Connecting Compute. Extending Possibility.**
