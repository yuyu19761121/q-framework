# QSTATIC Four-GPU Identity-State Consistency

## Status

**Evidence level: VALIDATED under the recorded smoke-test configuration.**

This document describes a QSTATIC / continuity-state validation in which four independent GPU workers consumed one authoritative identity-state package before executing different shot/action branches.

## Test shape

Workers:

- A0
- A1
- B0
- B1

Architecture:

```text
Character Master / QSTATIC identity state
                  |
          lineage + SHA receipt
                  |
       +----------+----------+----------+
       |          |          |          |
      A0         A1         B0         B1
       |          |          |          |
   branch A   branch B   branch C   branch D
```

The production system already treats these workers as independent execution slots rather than a single aggregated GPU.

## What was verified

The retained smoke-test evidence records:

1. all participating workers consumed the same authoritative identity/continuity package;
2. the shared identity/state SHA matched across the four workers;
3. the node-side computation-state SHA matched before branch-specific action execution;
4. workers could then execute different shot/action branches while preserving the same source identity contract.

## Important hash interpretation

The claim is **not** that four different videos should have the same final file SHA.

The equality condition applies before branch divergence:

```text
same authoritative state
        -> same identity/state SHA
        -> same pre-branch computation-state SHA
        -> independent action branches
        -> different final media outputs are allowed
```

This distinction matters. A matching pre-branch state is evidence that workers began from the same authoritative identity/continuity contract. Different actions are expected to produce different final media hashes.

## Why it matters

This test demonstrates an additional Q-Framework capability beyond memory rescue:

- one shared character/identity state can be distributed to independent GPU workers;
- cryptographic state equality can be checked before parallel execution;
- the workers do not need to independently reinterpret the character from an unconstrained prompt;
- branch-specific motion or shot execution can happen after the shared state has been verified.

This creates a basis for parallel production where different workers can render different actions or timeline locations while remaining anchored to the same identity contract.

## What is not claimed

This smoke test does not prove:

- perfect perceptual face identity for every model or every shot;
- automatic continuity across arbitrary models and hardware;
- byte-identical outputs after different action branches;
- elimination of the need for Face/Visual QC;
- universal compatibility of every QSTATIC state representation.

Those require separate benchmarks and acceptance criteria.

## Relationship to other Q-Framework evidence

QSTATIC shared-state consistency complements the previously demonstrated compute-state work:

- deterministic cross-GPU sampler-state transport;
- exact SHA verification through CPU/RAM/shared-memory transport;
- controlled cross-GPU H3 continuation;
- multi-worker timeline execution with common Character Master / identity locks.

Together, these results support the broader architecture in which GPU workers are independent execution resources operating from externally managed, verifiable state and lineage.


## Node-to-GPU computation fingerprint

The retained CURRENT evidence records an additional result beyond shared input/state identity: the node-side and GPU-side computation fingerprints across the four parallel paths were highly consistent, with computation-state SHA values nearly matching across the participating node/GPU workers.

This is deliberately not worded as universal bitwise GPU determinism. Q-Framework keeps two classes of evidence separate:

- **Exact:** controlled sampler/state transport tests with bitwise equality or exact SHA-256 equality.
- **Near-consistent:** multi-worker generative execution where the node+GPU computation fingerprint remains highly aligned before workers execute different action branches.

The distinction protects the claim boundary while still recording the practical observation that heterogeneous workers can remain anchored to the same computational lineage.


## Parallel timeline execution

The four-worker test was not a fixed sequential 0-3s / 3-6s split. Q-Framework's global frame queue can dispatch different absolute timeline units to independent workers. A retained first-wave assignment was:

- B0 -> F265-F269
- B1 -> F235-F239
- A0 -> F355-F359
- A1 -> F155-F159

Every unit carried the same Character Master/reference and immutable identity, wardrobe and scene constraints. Its bounded Call Sheet contained only the action/camera/dialogue contract for that absolute timeline range. A worker finishing early could claim another pending unit through work stealing.

## Two computation-consistency evidence classes

The project deliberately separates two observations.

**Multi-worker generative smoke:** the independent node + GPU computation fingerprints / SHA values were highly aligned and near-matching before workers diverged into different action branches. This is evidence of practical computation-state alignment, not a universal bitwise-GPU-determinism claim.

**Controlled cross-environment solver:** a real production sampler state was recomputed independently by Utility01, H410, and the Node B PyTorch reference. All three produced the exact same recomputed-x SHA:

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

Relative to the original source state, reverse-to-forward float32 reconstruction had max absolute error `4.76837158203125e-07` and mean absolute error about `2.03e-08`. The exact equality therefore applies to the three recomputed results; it is not generalized to every arbitrary inference path.

A separate H3 reference-state test also produced a bit-identical visual-latent SHA on Node A and Node B for the same 512x512 face reference:

`1488ccf08323200643d5759046f2d47e1e16d44a70f278a79346aec53103d937`

Together, these results distinguish shared authoritative state, near-consistent parallel generative execution, and exact controlled solver/reference-state reproducibility.
