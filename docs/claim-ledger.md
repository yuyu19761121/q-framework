# Q-Framework | RC4.3 Public Engineering Evidence

**Evidence-only publication:** proprietary implementation and original media are not published. Each result has a bounded test scope and separate private receipts.

| Claim | Measured or reported result | Status / limits |
|---|---|---|
| Single 22GB RTX 2080 Ti completed native H3 short clips | Studio #370 / #371 produced MP4 outputs | Completed, short duration, not one-pass 15 seconds |
| Single GPU completed a 15-second segmented output | #365, ten sequential video segments, 360 frames, 3h12m08s | Completed with nine CUDA OOM events followed by retries; not OOM-free |
| QmRNA changes feasibility on the same card | Controlled 480×832 / 36-frame / 10-step comparison: baseline PRE-OOM and no expected output versus successful QmRNA-protected output | Controlled A/B; PRE-OOM is not CUDA HARD_OOM |
| Four 22GB GPU workers delivered video quickly | #361, 15s, 360f, 24fps, 480×832, 14m37s | End-to-end segmented GPU generation and CPU assembly |
| Exact controlled numerical continuation | Cross-GPU 20 steps matched comparison, max absolute error 0.0 | Bounded numerical test, not arbitrary-model universal continuity |
| Controlled cross-device consistency | Bounded experiment recorded; internal state and verification particulars withheld | Not evidence of unified VRAM |
| Matching visual output in a controlled comparison | QmRNA evaluation: 22 of 22 decoded frames identical | Bounded comparison; not all workflows |
| **Verified single-card native H3 1080p-class RS and complete 5s video** (2026-10-26) | One expanded 22GB RTX 2080 Ti: **10/10 native 1088×1920 H3 RS generated successfully**, crop/trim without upscale into **1080×1920 / 5.000s / 24fps / 120-frame MP4**. Run elapsed **1h39m16s**, **zero CUDA OOM recorded**. | **Completed native high-resolution computation and full 1080p film verified** with original execution, media-dimension and hash receipts; owner visual-quality review pending; segmented workload, not one-pass 120-frame native inference |
| **Owner-reported Q vs no-Q comparison** (2026-10-26) | Owner reports unassisted H3 OOM under related 1080p-class target; Q-assisted complete 1080p film is separately verified | Original no-Q error receipt still to be matched; independent physical QVRAM offload not inferred |
| Single-card H3 1080p result evidence grade | Matching native RS success records, complete five-second MP4, verified artifact digest and elapsed runtime | **Confirmed by private execution receipts**, no longer merely owner-reported. Original media/prompt and core algorithms withheld under BlackBox |
| Heterogeneous supercomputer neural network | End-state research objective | Full autonomous generalization not yet verified |

**BlackBox rule:** reviewers may access approved synthetic demonstrations and sanitized evidence summaries. Complete runtime configuration, source, model patching details, private media and credentials stay Owner-only.

[AI-readable JSON](../evidence/claims-public-rc4.3.json) · [BlackBox policy](blackbox-disclosure-policy.md) · [繁體中文白皮書](../whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md)
