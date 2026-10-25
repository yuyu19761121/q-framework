# Q-Framework × Temporal Möbius | BlackBox Public Architecture

## Research capabilities, not a deployment blueprint

HAVEFUN studies three distinct engineering capabilities:

1. **Constrained-hardware task feasibility:** making selected high-load workloads finish on an individually limited GPU, with a measured same-card QmRNA control.
2. **Independent-worker collaboration:** coordinating segmented tasks across independent GPUs while keeping end-to-end output measurable.
3. **Evidence-informed decisions:** using bounded prior results and verification feedback to study the choice of candidate routes across heterogeneous equipment.

The product research portfolio includes **QmRNA, QVRAM, QSTATIC and Temporal Möbius**. Their implementation, native model control interfaces, algorithms, state representation, internal node topology, exact configuration and runtime source are **not publicly disclosed**.

## Observed results

- A single memory-expanded 22GB RTX 2080 Ti has successfully completed native H3 video clips (#370, #371). Job #365 also yielded a 15-second assembled video using one GPU for sequential short segments, with observed CUDA OOM retries.
- A measured single-card QmRNA comparison finished with the QmRNA-protected route where its unprotected comparison entered a preventive PRE-OOM condition.
- Four independent 22GB RTX 2080 Ti workers delivered a 15-second 480×832 video in 14m37s end-to-end (#361).
- Independent numeric tests verified bounded cross-device continuity and integrity.

These outcomes do not physically pool four GPUs into one VRAM address space. A fully autonomous heterogeneous supercomputer neural network remains the long-term goal.

[RC4.3 whitepaper](../whitepaper/Q-Framework-v1.0-RC4.3-EN.md) · [Machine-readable evidence](../evidence/claims-public-rc4.3.json) · [BlackBox rules](blackbox-disclosure-policy.md)
