# Q-Framework | Public BlackBox Disclosure Policy

**Purpose:** enable independent AI research assistants and human reviewers to understand and evaluate HAVEFUN results without access to proprietary implementation or private content.

## Three release levels

**PUBLIC (approved):** plain-language technology goals; outcome-level benchmarks; GPU class; workload dimensions; duration, success/failure and retry counts; narrowly scoped comparison results; independent-review limitations. Only synthetic and separately approved example media may be released.

**RESTRICTED (approved NDA / owner-reviewed):** reproducibility protocols and limited verification receipts needed by a specific evaluator. The default is aggregate measurements rather than native logs. Access must be revocable and auditable.

**OWNER-ONLY (never published):** source code and patches for QmRNA, QVRAM, QSTATIC, QFREEZE and Temporal Mobius; native node graphs, runtime hooks, configuration values, decision weights and state encodings; private checkpoint tensors; server and worker access; raw client photos, prompts, audio, video and other identifiable content; credentials, tokens and internal service paths.

## Additional BlackBox boundaries for runtime research

Runtime paging parameters, historical or active execution limits, adaptive-control settings, memory budgets, checkpoint or recovery formats, durability and replica topology, state-transfer measurements, validation methods, and node handoff policies are **OWNER-ONLY**. This applies even when a measurement comes from a successful test, a prior whitepaper, or a review draft. Do not publish exact values, value ranges, configuration examples, formulas, receipt excerpts, or comparisons that allow those values to be inferred.

For public summaries, describe only approved outcome-level findings and their limitations. Keep exact engineering observations in access-controlled CURRENT and TEST CURRENT, not in GitHub, public PDF artifacts, READMEs, translations, or investor materials. Translating a confidential detail does not make it eligible for disclosure.

## BlackBox technical evidence

Public results must distinguish:
- a completed single-card job from a multi-card result;
- native sampling from stitched segments or upscaled delivery;
- PRE-OOM intervention from CUDA hard OOM;
- an owner-reported achievement from a result confirmed by a primary receipt;
- controlled test performance from end-to-end production time.

Each public record should specify the claim, test scope, result, evidence class and limitations, but it must not expose the confidential method used to obtain it.

## Publication controls

1. **Default deny:** new public release content requires an explicit owner approval.
2. Prepare a sanitized publication from approved measurements; do **not** publish then redact private source material.
3. Scan for credentials, internal paths, node-graph instructions, full execution logs and restricted media references before publication.
4. Require a passing publication check on a protected GitHub branch before any merge or public deployment.
5. Keep source, complete receipts and owner media in private infrastructure with separate access controls and revocable authorization.
6. A public AI or reviewer is not entitled to private runtime access to verify a published claim.
7. Any potential incident requires source-access review and credential rotation where appropriate.

**Important:** editing a public GitHub file does not retract its Git history, external forks, cached copies or prior downloads. A historical disclosure requires a separate incident review; if secrets were exposed, rotate them rather than relying on deletion.

[Public results](../docs/claim-ledger.md) | [Whitepaper](../whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [Security](../SECURITY.md)
