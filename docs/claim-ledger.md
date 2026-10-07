# Claim Ledger

| Claim | Status | Public wording |
|---|---|---|
| Cross-GPU compute-state transport can preserve deterministic state identity | Demonstrated | Verified in controlled development tests with state/hash checks |
| GPU -> CPU/RAM -> shared memory -> GPU continuation has executed in a real rescue lineage | Demonstrated | Runtime evidence exists |
| QSTATIC can distribute one authoritative identity/continuity state to four independent GPU workers with matching shared-state SHA before branch execution | Demonstrated | Four-worker smoke test recorded matching identity/state SHA across A0/A1/B0/B1 |
| Node-side computation-state SHA can remain consistent across the same four-worker QSTATIC smoke before action branches diverge | Demonstrated | Equality applies to the shared pre-branch state; final branch output hashes are not expected to match |
| Independent node+GPU paths in the QSTATIC multi-worker smoke produced near-consistent computation-state SHA fingerprints before divergent actions | Demonstrated smoke observation | Reported as near-consistent, not as universal bitwise determinism |
| QmRNA can operate inside an H3 model-forward candidate path | Demonstrated candidate behavior | It has entered model-forward; this alone is not a full-length PASS |
| Exact FFN token chunking can reduce instantaneous FFN working set without changing per-token FFN semantics | Demonstrated candidate behavior | Live candidate path executed exact chunking |
| CPU reference streamed/global attention can reproduce full attention within normal floating-point tolerance | Demonstrated in CPU reference test | Mathematical/reference validation only |
| A single 22GB GPU completed the full target 15s H3 workload through newest full-length virtualization | **Not yet claimed** | Requires final output + valid continuation receipts |
| Q-Framework eliminates OOM | **Not claimed** | Goal is controlled pressure handling and recoverability |
| Q-Framework provides unlimited VRAM | **Not claimed** | Physical memory remains finite |
