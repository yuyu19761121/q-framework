# Benchmark Methodology

A Q-Framework benchmark should identify the workload, baseline, Q-Framework configuration, observed resource behavior and terminal result.

## Required metadata
- benchmark_id
- timestamp
- model/version/hash
- runtime/framework version
- GPU / physical VRAM
- CPU / RAM / storage
- driver/CUDA/runtime
- width / height / duration / FPS
- requested frames and model-aligned frames
- precision / steps / seed
- baseline outcome
- Q-Framework outcome
- wall-clock runtime
- peak VRAM
- checkpoint/freeze count
- restore/resume count
- QmRNA intervention count
- failure/retry count
- final output hash
- evidence/receipt hash

## Evidence levels
- **L0 Proposed**
- **L1 Static verified**
- **L2 Runtime partial**
- **L3 Completed workload**
- **L4 Reproduced**
