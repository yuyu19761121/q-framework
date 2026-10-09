# Q-Framework Public Architecture

This public architecture is intentionally black-box.

```text
AI Workload
    |
    v
+---------------------------+
|     Q-Framework Core      |
|     PROPRIETARY BLACK BOX |
+-------------+-------------+
              |
              v
Heterogeneous Execution Resources
GPU / CPU / RAM / storage
              |
              v
Verified Result / Continuation Receipt
```

Public documents describe observable capabilities and validation outcomes only.


## ComfyUI integration boundary

For the validated Windows + H3 path, Q-Framework is an **extension/integration architecture**, not a ComfyUI core fork.

- node-local integration is placed in the ComfyUI custom-node / runtime-extension layer;
- Master / Bridge / state-lineage orchestration remain external to the ComfyUI process;
- validated model-memory candidates are scoped to controlled execution paths rather than a permanent global-backend replacement;
- the validated path does not require replacing ComfyUI core source files such as `execution.py` or the full official source tree.

Therefore, descriptions such as "modified ComfyUI fork" or "core-source mod" are not canonical Q-Framework terminology.


They do not disclose internal state primitives, lifecycle rules, freeze/restore sequencing, QmRNA control logic, QSTATIC contracts, QVRAM residency mechanisms, scheduler decisions, pressure thresholds, prefetch/eviction policy, or production model-forward modifications.

See [Public Proof Pack](public-proof-pack.md).

**Real evidence. Black-box mechanism.**
