# Q-Framework | Public Research Evidence Methodology — BlackBox

Release a **measured outcome**, not a recipe for a proprietary runtime.

Minimum fields for any public claim:
- hardware class and number of independently addressable devices;
- model/workload category, final media size, frame count and duration, where available;
- result status, elapsed time, recorded retry/OOM conditions and measurement boundary;
- whether the record is a controlled comparison, completed task, owner report or research objective;
- whether output resolution comes from native model sampling, segment assembly or postprocessing, when verified.

Never conflate a PRE-OOM policy event with a CUDA hard OOM; do not compare different FPS, sampling steps or resolutions as if identical; and do not treat a 22GB memory-expanded 2080 Ti as factory 11GB hardware.

Approved verification material may be shared through separate revocable owner-controlled review. Never publish original source, model integration details, raw prompts, owner media, complete device configuration or credential-bearing logs.

[Machine-readable claims](../evidence/claims-public-rc4.3.json) · [Full public BlackBox paper](../whitepaper/Q-Framework-v1.0-RC4.3-EN.md)
