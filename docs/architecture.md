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

They do not disclose internal state primitives, lifecycle rules, freeze/restore sequencing, QmRNA control logic, QSTATIC contracts, Qvram residency mechanisms, scheduler decisions, pressure thresholds, prefetch/eviction policy, or production model-forward modifications.

See [Public Proof Pack](public-proof-pack.md).

**Real evidence. Black-box mechanism.**
