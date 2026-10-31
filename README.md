# Q-Framework × Temporal Möbius

**Languages:** **English** · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md)

**Single-GPU H3 successes · Four-GPU production · Heterogeneous supercomputer neural network**

HAVEFUN's Q-Framework is **not only a multi-GPU system**. Actual native MiniMax H3 video tests have **succeeded on a single memory-expanded RTX 2080 Ti 22 GB GPU**. QmRNA's low-memory execution control, computation-state continuity, and Temporal Möbius scheduling address both *whether a task can finish* and *how a heterogeneous system should execute it*.

### October 31, 2026: Native 4K AI video produced through OOM prevention and compute rebirth

**We have moved beyond native 4K computation experiments to a real native-resolution H3 MP4 output.** Our existing OOM-prevention and cross-device recovery capabilities have supported real high-resolution video delivery. This is a practical milestone for HAVEFUN Q-Framework × Temporal Möbius, not just a theoretical architecture. [Read the inventor-led RC4.5 whitepaper (Traditional Chinese)](whitepaper/Q-Framework-v1.0-RC4.5-ZH-TW.md).

### Demonstrated results

- **New: single-card 1080p final H3 video:** 10/10 native high-resolution segments and a verified complete five-second 1080×1920 film on one memory-expanded 22GB RTX 2080 Ti, no recorded OOM, no upscaling.

- **Single GPU, QmRNA feasibility:** On A1 (RTX 2080 Ti 22,528 MiB), a matched 36-frame, 10-step H3 test completed and produced an MP4 with QmRNA Pre-step Guard. The unguarded baseline hit a **PRE-OOM** intervention at step 1 and did not produce its expected single-worker MP4. PRE-OOM is not a CUDA hard OOM.
- **Single GPU, real H3 media:** Jobs **#370/#371** produced native H3 short videos on A0. **#365** also finished a complete **15-second / 360-frame** assembled video using *one A0 GPU*, rendering ten sequential 36-frame segments. Total elapsed time was **3h 12m 08s**; nine native CUDA OOM attempts required resubmission of the corresponding segments. It was **not** a single 360-frame sampler or an OOM-free run.
- **Four GPUs, rapid production:** Job **#361** delivered a **15-second / 360-frame / 480×832 / 24fps** video in **14m 37s** end to end using four independent RTX 2080 Ti workers and CPU editing.
- **Controlled reproducibility research:** separate bounded consistency tests were completed; internal runtime design and measurements are not disclosed.
- **Mixed Windows/Mac research:** separate verifiable math sharding, model-response, and bounded weight-training results.

**26 October 2026 — verified single-GPU H3 1080p-class breakthrough:** A single memory-expanded **RTX 2080 Ti 22GB** completed **10/10 native 1088×1920 H3 RS segments** and assembled the final **1080×1920, 5-second, 120-frame, 24fps MP4**, with **zero recorded CUDA OOM** and **no upscaling**. The complete run took **1h 39m 16s**; five seconds is playback duration, not generation latency. Native-RS and final-film receipts are verified; visual quality awaits owner review. The owner-reported unassisted H3 OOM comparison remains separately uncorrelated. [Evidence](docs/claim-ledger.md).

### New whitepaper: RC4.5 Inventor's Vision (Traditional Chinese)

[**Read RC4.5: We Are Redefining the Future of AI Computation**](whitepaper/Q-Framework-v1.0-RC4.5-ZH-TW.md)

**Beyond OOM. Beyond Hardware. Beyond Boundaries.** Our inventor-led story connects the industry's three economic challenges—hardware cost, interrupted computing, and stranded capacity—with our native high-resolution AI achievements, Compute Rebirth research, heterogeneous collaboration, and technology licensing / compute service / network business opportunities. The public version protects proprietary BlackBox implementation details.

### Multi-node compute roadmap

[Public architecture & staged eight-device roadmap](site/multi-node.html) · [Engineering plan](docs/multi-node-roadmap.md) · [Architecture screenshot](assets/multi-node-plan.png). **Four-GPU video delivery is verified; four macOS Brain + four Windows Worker hosts are a target, not a completed eight-host demonstration.**

### Public image gallery (ZH / EN / JA)

[**Open the 9-image gallery**](docs/visual-gallery.md) — recruitment posters, complete architecture diagrams, and single-GPU versus multi-GPU operation comparisons in three languages. The images are illustrative; validated results and planned features remain separately labeled.

### RC4.4 owner review draft (Traditional Chinese, 30 October 2026)

[Read the RC4.4 review draft](whitepaper/Q-Framework-v1.0-RC4.4-ZH-TW-REVIEW.md) · [RC4.4 review PDF](whitepaper/Q-Framework-v1.0-RC4.4-ZH-TW-REVIEW.pdf). **Review edition only, not a replacement for the approved RC4.3 five-language whitepapers.** Focus: measurable native 4K H3 operation without CUDA HARD OOM, plus bounded distributed compute, recovery and checkpoint evidence. Final video delivery is a separate criterion.

### RC4.3 technical whitepapers (full-length)

| Language | Markdown | PDF |
|---|---|---|
| English | [Full whitepaper](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |
| 繁體中文 | [技術白皮書](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| 日本語 | [技術白書](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |
| Español | [Documento completo](whitepaper/Q-Framework-v1.0-RC4.3-ES.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ES.pdf) |
| Português (Brasil) | [Documento completo](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.pdf) |

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
