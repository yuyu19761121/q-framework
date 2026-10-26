# Q-Framework | Validated Execution Summaries — BlackBox Public

| Case | Publicly shareable outcome | Evidence boundary |
|---|---|---|
| Single GPU native H3 (#370, #371) | Native short MP4 outputs completed on one memory-expanded 22GB RTX 2080 Ti | Not a 15-second single-pass sampler |
| One GPU assembled video (#365) | 15s/360f final video from ten sequential short RS; elapsed 3h12m08s | Nine CUDA OOM events led to new segment submissions |
| Single GPU QmRNA A/B | Same-card 36f/10 steps: baseline PRE-OOM did not directly deliver; protected route completed | PRE-OOM != HARD_OOM; proprietary control internals withheld |
| Four GPU production (#361) | 15s/360f/24fps/480×832 produced in 14m37s | Different workload than single-card run; CPU assembly |
| Numerical continuation | 20-step cross-GPU controlled result matched bitwise | Does not prove arbitrary GPU-generation portability |
| State transport | Approximately 250 MiB with matching verification hashes | Does not pool VRAM |
| Visual comparison | 22/22 decoded frames matched | Specific controlled experiment |
| H3 single-GPU 1080p (2026-10-26) | One 22GB RTX 2080 Ti generated 10/10 native 1088×1920 RS; final 1080×1920, 5s, 120f MP4 verified, no upscaling; no CUDA OOM recorded in this run | Private native and final media receipts verified, Owner visual QC pending; not a single uninterrupted 120-frame native pass |

Sanitized outcome summaries are public. Native graph layouts, full raw logs, model settings, runtime source, original Owner media and private prompts are not public evidence artifacts.

[Machine-readable claims](../evidence/claims-public-rc4.3.json) · [Disclosure policy](blackbox-disclosure-policy.md)
