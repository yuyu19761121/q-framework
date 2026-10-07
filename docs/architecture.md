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

## Multi-node execution
GPUs remain independent execution resources. Continuation identity is preserved outside any single GPU.
