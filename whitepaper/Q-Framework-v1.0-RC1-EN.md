# Q-Framework Development & Validation Whitepaper v1.0 RC1

## Compute-State Virtualization and Adaptive Flow Control for Heterogeneous AI Infrastructure

**October 2026**

> **This paper documents a running system.**

Q-Framework is an experimental heterogeneous AI compute architecture developed to investigate whether long-context generative workloads can remain recoverable and controllable when their practical working set approaches or exceeds the comfortable physical-memory envelope of a consumer GPU.

The current implementation includes explicit state lineage, checkpoint/resume behavior, CPU/RAM-backed state handling, runtime control signals, static-state sources, multi-node continuation, and candidate working-set virtualization inside model-forward execution.

The public paper reports observable architecture, development milestones, validation methods and current results. Proprietary scheduling, state-selection, adaptive-control and production data-plane algorithms are intentionally excluded.

## Design principles

1. Logical state and physical residency are different concepts.
2. Memory pressure should be observable and actionable.
3. Compute state should survive temporary resource pressure.
4. A GPU is an execution resource, not the entire machine.
5. Claims must be tied to runtime evidence.

## Current evidence

Demonstrated evidence includes deterministic state/hash verification across GPU continuation paths, real GPU→CPU/RAM→GPU rescue lineages, candidate QmRNA execution inside H3 model-forward blocks, exact FFN token chunking, and CPU-only global streamed-attention reference tests matching full attention within floating-point tolerance.

### QSTATIC four-GPU identity-state consistency

QSTATIC is not only a media-indexing layer. In the production design it can act as a shared continuity/identity-state source for parallel GPU workers. A four-worker smoke test exercised the independent A0/A1/B0/B1 execution slots with a common Character Master / identity-state package while branch-specific shot/action work was assigned independently.

The retained validation record reports that the shared identity/state SHA was consistent across the participating workers and that the node-side computation-state SHA was also consistent before branch-specific action execution. This matters because the invariant being preserved is the authoritative shared state, not byte-identical final videos. Once different action or shot branches execute, their final output hashes are expected to diverge.

This result is classified as **VALIDATED shared-state consistency under the tested smoke configuration**. It does not claim that every model, every identity representation, or every heterogeneous GPU combination will preserve perceptual identity without additional QC. It does demonstrate that Q-Framework can distribute a common identity/continuity state to independent workers and verify state equality cryptographically before allowing the workers to diverge into different execution branches.

### Node-to-GPU computation consistency

The same development record also contains a second, distinct observation: once the shared state was resolved by the node and handed into GPU execution, node-side and GPU-side computation fingerprints remained highly consistent across the parallel workers. In the QSTATIC multi-worker smoke, these computation-state SHA values were near-identical across the participating node/GPU paths even though the workers were independent devices.

This observation is intentionally separated from Q-Framework's exact-transfer proofs. In controlled state-transport experiments, Q-Framework has already produced exact results: a 20-step sampler handoff finished with bitwise equality and max absolute difference 0.0, and a 250 MiB GPU→CPU→shared-memory→GPU round trip preserved the exact SHA-256 value end to end. By contrast, the multi-worker QSTATIC execution result is reported as **near-consistent computation fingerprints**, not as a universal bitwise-determinism claim for arbitrary GPU inference.

The combined evidence supports a three-layer interpretation:

1. **Exact state transport can be proven** when the transported object and computation are controlled.
2. **Shared identity/continuity state can be proven equal** before parallel branch execution.
3. **Independent node+GPU execution can remain numerically/structurally highly consistent** while still allowing branch-specific actions and non-identical final media.

This is one reason Q-Framework treats the GPU as an execution worker rather than the owner of identity, lineage or the full workload state.

## Four validated execution paths

The CURRENT evidence now supports four distinct execution paths. These are not four marketing labels for the same mechanism; they exercise different placement and continuation contracts.

| Execution path | Status | Demonstrated behavior |
|---|---|---|
| **Mixed-GPU compute / continuation** | VALIDATED | State can freeze on one GPU, move through CPU/RAM or Bridge storage, restore on another GPU, and continue the same lineage. A 20-step deterministic POC finished bitwise equal with max diff 0.0; a 250 MiB transport preserved exact source/Bridge/target SHA; controlled H3 rescue completed B0 checkpoint -> B1 restore -> MP4 output. |
| **Same-GPU resume** | VALIDATED SMOKE | A story chain can remain pinned to one owner slot with `same_gpu_resume=true`, preserving lineage/state across segment boundaries and continuing from the retained chain state. |
| **H3 Memory Static / Reference-State compute** | VALIDATED | H3 audio, visual and face reference states were measured as explicit tensor blocks with shape/bytes/SHA. Identical input reproduced identical state SHA, and the same face reference on Node A and Node B produced the same visual-latent SHA. |
| **Mixed-GPU cross-file / cross-shot compute** | VALIDATED SMOKE | SHOT XCOPY / Motion Bridge used boundary state across separate shot artifacts; Job #135 accepted dual boundary references and crossed B0 PRE-OOM -> A0 restore before producing H3 output. |

These paths share one systems principle: **GPU residency is temporary; lineage and verifiable compute state remain authoritative outside any single execution slot.**

### SHA semantics: transport, compute revision and cross-environment arithmetic

Q-Framework deliberately distinguishes three kinds of SHA evidence.

1. **Exact transport SHA** — the same frozen state must remain bitwise identical while moving through GPU -> CPU/RAM/Bridge -> GPU. The 250 MiB XCOPY test met this condition.
2. **Progressive revision SHA** — after a restored state is actually computed further, the next freeze is expected to create a new revision and therefore a new SHA. When no step advances, the SHA remains unchanged. This separates real continuation from simple file movement.
3. **Cross-environment computed-result SHA** — real production sampler arithmetic was independently evaluated by Utility01, H410 and a Node B PyTorch reference. All three produced the same recomputed-x SHA. Relative to the original production source, reverse/forward float32 reconstruction differed only within rounding tolerance (max abs 4.768e-7; mean abs about 2.03e-8).

Therefore the public claim is **reproducible numerical behavior across the tested node/runtime paths**, not universal bitwise determinism for every intermediate tensor or every future model.

### QSTATIC four-GPU shared identity state

In the four-worker QSTATIC smoke, A0/A1/B0/B1 resolved the same authoritative identity/continuity state before action branching. The shared identity/state SHA matched across the workers, and the recorded node+GPU computation fingerprints were highly consistent before branch-specific execution.

After the branch point, workers were free to render different actions or shots. Their final media hashes are therefore not expected to match. The invariant is the common identity/state root and lineage before divergence.


The complete target of a final production-quality 15-second full-length H3 task on a single 22GB GPU through the newest full-length working-set virtualization path is still under validation and is not presented as completed fact.

## Disclosure boundary

This publication intentionally omits production state-selection policy, checkpoint packing, restore sequencing, pressure scoring, Qsearch ranking, scheduler weights, lease/fencing rules and the production streamed-QKV data-plane.
