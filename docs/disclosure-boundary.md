# Disclosure Boundary

## Public
- architectural roles;
- state-machine concepts;
- benchmark methodology;
- sanitized hardware/workload metadata;
- result hashes and receipts;
- public interfaces;
- simplified controller examples;
- non-sensitive proof-manifest logic.

## Abstract only
- memory-pressure controller;
- page/residency manager;
- checkpoint lifecycle;
- worker selection/recovery;
- Qsearch active working-set policy;
- Qanswer operator/task split;
- QSTATIC selection/continuity contracts.

## Confidential / not published
- production pressure-scoring formula and coefficients;
- adaptive feed-rate policy;
- state-hotness / eviction scoring;
- prefetch timing and dependency heuristics;
- checkpoint packing/serialization;
- restore sequencing;
- Qsearch ranking/cache heuristics;
- scheduler weights/failover scoring;
- lease/fencing internals and retry authority;
- production streamed-QKV data-plane;
- credentials, private URLs, LAN addresses and internal storage paths.
