# Q-Framework | Validated Execution Paths — RC4.3

| Workload | Proven route | Native output and boundary |
|---|---|---|
| QmRNA controlled A/B (2026-10-04) | A1 single 22GB GPU, 36f/10 Steps | Unprotected baseline PRE-OOM, no single-worker MP4; QmRNA Guard completed and wrote MP4 |
| Studio H3 short clips #370 / #371 | A0 single 22GB GPU | H3 native text-to-video/image-to-video MP4s, ~39 frames/16fps/~2.437s |
| H3 native 48-frame sample | A0 single 22GB GPU, 480×832, 24fps, 14 Steps | Completed 2 seconds of native video |
| Job #365 15-second single-GPU production | A0 performs 10 × 36-frame native RS serially | 15s/360f assembled MP4, 3h12m08s; 9 native CUDA OOMs followed by fresh RS submissions |
| Job #361 four-GPU golden delivery | A0/A1/B0/B1, 10 RS + CPU 9/9 | 15s/360f/24fps/480×832 completed in 14m37s |
| Job #135 four-GPU production | Separate 36fps line | 15s/540 frames and final hash |
| Controlled numerical continuation | 20 Steps GPU0→GPU1 | Bitwise identical, max absolute difference 0.0 |
| CUDA memory movement | ~250 MiB cross-GPU, separate Q7 32MiB CUDA | SHA checked, physical allocation release and restore |
| QmRNA decoded output A/B | Same-seed 22-frame run | 22/22 frames match |
| Mac heterogeneous mathematics | 24/24 Math-Stream batches | Actual LAN work, independent recomputation and SHA validation |

**Owner-reported 1080p:** a completed single-GPU H3 result is reported but remains pending original native receipt and resolution verification.

Different workloads must not be used for unqualified per-card speed comparisons. [RC4.3 full paper](../whitepaper/Q-Framework-v1.0-RC4.3-EN.md).
