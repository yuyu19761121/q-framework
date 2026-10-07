# Validated Execution Paths

This document separates Q-Framework's validated execution paths from still-experimental full-length residency-virtualization work.

## 1. Mixed-GPU stateful continuation

A compute lineage can freeze on one GPU, move through CPU/RAM-backed transport, restore on another GPU, and continue.

Evidence includes:

- **20-step deterministic handoff:** GPU0 steps 1-10 -> CPU/RAM -> GPU1 steps 11-20; final result was bitwise equal with max absolute difference 0.0.
- **250 MiB state XCOPY:** source GPU SHA, Bridge/RAM SHA, and target GPU read-back SHA matched exactly; `bitwise_sha_match=true`.
- **Controlled H3 rescue:** B0 checkpoint -> B1 restore -> sampler continuation -> MP4 output.

This validates state migration and continuation. It does not mean multiple GPUs become one physically aggregated GPU.

## 2. Fixed-owner same-GPU resume

Q-Framework also supports a fixed-owner execution chain.

With `same_gpu_resume=true`:

- a story chain remains pinned to its owner slot;
- lineage/state is preserved across segment boundaries;
- continuation can stay local instead of migrating when migration is unnecessary.

This path is useful when locality is preferable and the owner GPU remains available.

## 3. H3 Memory Static / Reference-State compute

H3 reference information has been measured as explicit state blocks rather than treated only as source media.

Validated observations include:

- repeated visual-reference input reproduced the same raw-state SHA;
- changed input at the same tensor shape produced a different state SHA;
- audio, visual, and face reference states were recorded with explicit shape, byte size, and SHA;
- the same 512x512 face reference, encoded on Node A and Node B with the same H3 Video VAE path, produced the same visual-latent SHA.

This demonstrates reproducible reference-state computation on the tested paths. A reference latent is not the entire H3 model or the full inference working set.

## 4. Mixed-GPU cross-file / cross-shot stateful compute

SHOT XCOPY / Motion Bridge allows state from one shot/artifact boundary to participate in another shot's computation instead of reducing continuity to an RGB-only handoff.

Job #135 smoke:

- RS01 tail reference SHA and RS02 head reference SHA were recorded separately;
- H3 accepted the two boundary references;
- the path entered B0, hit PRE-OOM, restored on A0, and continued to H3 output;
- smoke output SHA256: `7A909C59636C1A18C6B1A1C7CD2037120F25DDC2C7F36CD2E62B4C70A43212E1`.

This demonstrates that a lineage can cross both **artifact/shot boundaries** and **GPU-worker boundaries**.

## 5. QSTATIC four-worker shared identity state

QSTATIC can serve as a shared identity/continuity authority for independent GPU workers.

In the four-worker smoke:

- A0, A1, B0, and B1 resolved the same authoritative identity/continuity state before action branching;
- the shared identity/state SHA matched across participating workers;
- node + GPU computation fingerprints were highly consistent / near-matching before branch-specific execution;
- after validation of the common root, the workers could execute different action/shot branches.

Final media hashes are not expected to remain identical after different branches execute. The invariant is the common pre-branch identity/state authority and lineage.

## 6. SHA interpretation

Q-Framework uses SHA evidence in three distinct ways.

### Exact transport SHA

When the same frozen object is moved through:

```text
GPU -> CPU/RAM -> Bridge/SharedMemory -> GPU
```

its hash should remain exactly identical.

The ~250 MiB XCOPY test met this requirement end-to-end.

### Progressive revision SHA

When a restored state is actually computed further, the next freeze should produce a **new state revision** and therefore a new SHA.

Development logs show:

- real step progression -> new QREV / new SHA;
- no step progression -> state SHA remains unchanged.

This distinguishes real continuation from simply copying the same file.

### Cross-environment computed-result SHA

A real production sampler-state arithmetic test was independently executed on:

- Utility01 without the ComfyUI/PyTorch math path;
- H410 without the ComfyUI math path;
- Node B using the PyTorch reference path.

All three produced the same recomputed-x SHA:

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

Compared with the original production source reconstructed through reverse/forward float32 arithmetic:

- max absolute error: `4.76837158203125e-07`
- mean absolute error: approximately `2.03e-08`

This is evidence of **reproducible numerical consistency across the tested environments**.

It is not a claim that arbitrary GPU inference, every intermediate tensor, or every future model is universally bitwise deterministic.

## 7. Evidence boundary

The validated paths above should not be confused with the newest full-length residency-virtualization target.

Q-Framework does **not** yet claim that a single 22 GB GPU has completed the final 15-second / 311-aligned-frame H3 target through the newest full-length working-set virtualization path.

That remains a separate acceptance milestone.
