# Q-Framework Architecture

Q-Framework sits between an AI workload and heterogeneous execution resources.

```text
AI workload / project
        |
        v
+---------------------+
|     Q-Framework     |
|                     |
|  QmRNA control      |
|   |       |         |
| Qsearch  Qanswer    |
|   \       /         |
|    Qvram / QSTATE   |
+---------+-----------+
          |
          v
GPU(s) / CPU / RAM / disk / media-state sources
```

## QmRNA
Runtime signalling/control context. Production scoring and adaptation policy are proprietary.

## Qvram
Persistent compute-state lifecycle and checkpoint/resume roles.

```text
ACTIVE -> PRESSURE -> FREEZE -> PERSIST -> RELEASE -> RESTORE -> ACTIVE
```

## Qsearch
Working-set/state retrieval. No asymptotic-complexity or fixed-percentage reduction claim is made without benchmark evidence.

## Qanswer
Separates CPU-suitable orchestration, deterministic preprocessing, scheduling and selected auxiliary work from GPU-critical tensor execution.

## QSTATIC
Stores precomputed or extracted visual/static state for later planning/rendering stages.

QSTATIC also participates in identity and continuity distribution. In the validated four-worker smoke path, independent GPU workers received the same authoritative Character Master / identity-state package. Shared-state SHA and node-side computation-state SHA were checked before branch-specific action execution.

The architectural rule is:

```text
ONE AUTHORITATIVE IDENTITY / CONTINUITY STATE
                 |
        SHA / lineage verify
                 |
       +---------+---------+---------+
       |         |         |         |
      A0        A1        B0        B1
       |         |         |         |
   action A  action B  action C  action D
```

State equality is required before branching. Final media hashes may differ because the workers intentionally execute different action/shot branches.

## Multi-node execution
GPUs remain independent execution resources. Continuation identity is preserved outside any single GPU.
