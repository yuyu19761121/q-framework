# Q-Framework | RC4.3 Public Engineering Evidence

**Evidence-only publication:** proprietary implementation and original media are not published. Each result has a bounded test scope and separate private receipts.

| Claim | Measured or reported result | Status / limits |
|---|---|---|
| Single 22GB RTX 2080 Ti completed native H3 short clips | Studio #370 / #371 produced MP4 outputs | Completed, short duration, not one-pass 15 seconds |
| Single GPU completed a 15-second segmented output | #365, ten sequential video segments, 360 frames, 3h12m08s | Completed with nine CUDA OOM events followed by retries; not OOM-free |
| QmRNA changes feasibility on the same card | Controlled 480×832 / 36-frame / 10-step comparison: baseline PRE-OOM and no expected output versus successful QmRNA-protected output | Controlled A/B; PRE-OOM is not CUDA HARD_OOM |
| Four 22GB GPU workers delivered video quickly | #361, 15s, 360f, 24fps, 480×832, 14m37s | End-to-end segmented GPU generation and CPU assembly |
| Exact controlled numerical continuation | Cross-GPU 20 steps matched comparison, max absolute error 0.0 | Bounded numerical test, not arbitrary-model universal continuity |
| Validated state integrity | Approximately 250 MiB moved with consistent digests | Controlled transport, not unified 88GB VRAM |
| Matching visual output in a controlled comparison | QmRNA evaluation: 22 of 22 decoded frames identical | Bounded comparison; not all workflows |
| 2026-10-26 H3 1080p / 9:16 / 5s Q-versus-no-Q | Owner reports bare H3 OOM and video generated with Q assistance. Separately traced Q-path test 004: 4 of 10 native segments complete at 09:47; native 1088×1920 to delivery 1080×1920 via crop/trim, no upscaling | Owner-reported A/B, partial Q-path native receipts verified; complete 5s media, no-Q error and matched A/B evidence still pending. Prior 002 was not Q-free |
| Single-card H3 1080p completion | Research Owner reports successful run | Await native-sampling and artifact receipts for independent verification |
| Heterogeneous supercomputer neural network | End-state research objective | Full autonomous generalization not yet verified |

**BlackBox rule:** reviewers may access approved synthetic demonstrations and sanitized evidence summaries. Complete runtime configuration, source, model patching details, private media and credentials stay Owner-only.

[AI-readable JSON](../evidence/claims-public-rc4.3.json) · [BlackBox policy](blackbox-disclosure-policy.md) · [繁體中文白皮書](../whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md)
