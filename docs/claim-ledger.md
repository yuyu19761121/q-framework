# Claim Ledger

| Claim | Status | Public wording |
|---|---|---|
| A controlled ~250 MiB GPU→CPU/SharedMemory→GPU state transfer can preserve exact state identity | Demonstrated | Source / Bridge / target SHA-256 matched exactly; bitwise_sha_match=true |
| A live H3 lineage can checkpoint on one GPU and resume on another GPU | Demonstrated | Controlled B0→B1 continuation completed to MP4 output |
| Progressive state blocks create new QREV/SHA after real compute progression | Demonstrated | Exact SHA is expected during transport; a new revision hash after compute is evidence of progress |
| Q-Framework supports a fixed-owner same-GPU resume mode | Demonstrated implementation path | qmrna_vvram_same_gpu pins story chains to owner slots with same_gpu_resume=true and stable lineage |
| H3 reference-state blocks can produce reproducible SHA signatures | Demonstrated | Repeated audio/visual reference encoding produced identical state SHA for identical input |
| The same H3 face-reference block can be bit-identical across Node A and Node B | Demonstrated | Same 512×512 face input and H3 VAE produced identical visual-latent SHA on both nodes |
| QSTATIC / Character Master can distribute one authoritative identity/continuity root to four independent GPU workers before divergent actions | Demonstrated smoke | Shared pre-branch state is the invariant; final media hashes may diverge after different actions |
| Dynamic Static can evolve from a real GPU output through CPU/QWorker analysis into the next GPU segment | Demonstrated production flow | Job268 QRS0001→tail→QW9 dynamic_static_QRS0002→next dispatch ran end-to-end |
| Cross-shot / cross-file boundary memory can be used by H3 while the active lineage also crosses GPUs | Demonstrated smoke + runtime lineage | Motion Bridge used RS01 tail + RS02 head and completed a multi-GPU s01→s20 lineage |
| Real production sampler state can be recomputed in different node/runtime environments to the same computed-result SHA | Demonstrated | Utility01, H410, and Node B PyTorch reference produced identical recomputed-x SHA |
| Independent node+GPU execution paths can retain near-matching computation-state fingerprints under the same shared state / lineage | Demonstrated smoke observation | Reported as near-match / highly consistent, not universal bitwise determinism |
| Cross-environment reconstruction is universally bitwise-identical to the original source state | **Not claimed** | Float32 reverse→forward reconstruction showed max abs error ~4.77e-7 versus source |
| Q-Framework integrates with ComfyUI without requiring a private core fork on the validated Windows + H3 path | Demonstrated integration path | Node-local integration is provided through the custom-node/runtime-extension layer plus external Master/Bridge orchestration; the validated Node A ComfyUI source tree remains unmodified |
| QmRNA can operate inside an H3 model-forward candidate path | Demonstrated candidate behavior | It entered H3 model-forward and executed exact FFN token chunking |
| CPU reference streamed/global attention can reproduce full attention within floating-point tolerance | Demonstrated reference test | Mathematical/reference validation only |
| A single 22GB GPU completed the full target 15s / 311-aligned-frame H3 workload through newest residency virtualization | **Not yet claimed** | Requires final output + valid continuation receipts |
| Q-Framework eliminates OOM | **Not claimed** | Goal is controlled pressure handling and recoverability |
| Q-Framework provides unlimited VRAM | **Not claimed** | Physical memory remains finite |
| Q-Framework universally outperforms datacenter GPUs | **Not claimed** | No such benchmark claim is made |

Additional validated A/B evidence: under the same QSTATIC reference and seed, the QmRNA-enabled run and baseline produced identical decoded frame hashes for all 22 frames. Container file hashes differed, as expected.
