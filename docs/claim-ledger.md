# Q-Framework | Public Claim Ledger — RC4.3

**Scope:** each claim below refers to its measured native workload. Single-card feasibility and multi-card throughput are separate results.

| Technical claim | Evidence | Correct interpretation |
|---|---|---|
| Single-GPU successful H3 execution | A0 jobs #370 and #371; subsequent 48-frame native H3 on a 22GB RTX 2080 Ti | Successful native short video clips; not automatically 15-second one-pass output |
| QmRNA changed single-GPU feasibility | 2026-10-04 A1, same Static/Seed, 480×832, 36 frames, 10 steps | Baseline PRE-OOM/no single-worker MP4; QmRNA Pre-step Guard completed MP4. PRE-OOM is not CUDA hard OOM |
| Full 15-second video on only one GPU | #365, A0 10 sequential RS of 36 frames | 15s/360 frames, 3h12m08s, with 9 CUDA OOM events followed by new-prompt full-segment retries |
| Four-GPU fast production | #361, A0/A1/B0/B1, 10 RS, CPU 9/9 seams | 15s 480×832 24fps / 360f, 14m37s end to end |
| Native model execution hook | QmRNA DiT ENTER/EXIT; H3 Gate receipt #341 | Verified connection to model execution, not proof that all Q modules always fire |
| Control/output equivalence | 22f QmRNA same-Seed comparison | 22/22 decoded frames identical; 76s versus 81s observed once |
| Cross-GPU numerical continuation | Controlled 20 Steps GPU0→GPU1 | Bitwise-identical, max absolute difference 0.0 |
| Physical state transport | ~250 MiB GPU→CPU/Bridge→GPU | Three SHA-256 values match; four 22GB GPUs are not unified 88GB memory |
| Real CUDA offload/restore | Separate Q7 32 MiB test | Allocation 33,554,432→0→33,554,432; not necessarily triggered in job #361 |
| Native single-GPU H3 1080p | Owner-reported successful task | Await primary history, sampler resolution, frames, output and hash before independent publication |
| Heterogeneous supercomputer neural network | Research objective plus bounded Mac/Windows/GPU mathematical experiments | No universal autonomous AI or matched H100/H200 superiority claim |

The public documentation intentionally excludes owner-only imagery, full private prompts, node keys and credentials.

[Complete RC4.3 English whitepaper](../whitepaper/Q-Framework-v1.0-RC4.3-EN.md) · [繁體中文](../whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) · [日本語](../whitepaper/Q-Framework-v1.0-RC4.3-JA.md)
