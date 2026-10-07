# Validated Execution Outcomes

This document summarizes **what was observed**, not how the production mechanism works.

## Deterministic continuation
Bitwise equality was observed in a controlled continuation test.

- max absolute difference: 0.0
- mean absolute difference: 0.0
- SHA-256: `ae04c23d4daed035632855260f85c360a857c28a8d46544f5c92f91baff823a3`

## Large-state transport integrity
A ~250 MiB computation object preserved exact SHA through the tested transport path.

SHA-256: `330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

## Real H3 continuation
A real H3 workload completed after continuation on another GPU worker.

Output SHA-256: `307828DE5D0D54F36004EF9C97B2E4DAE5178E59A9C8EF74775F07522B788AB3`

## Four-worker production-class execution
A 15.000-second / 540-frame workload completed with four independent RTX 2080 Ti 22 GB workers participating.

Final SHA-256: `23CDBA13DBFF7B8EC234DB1D7DE61625597E128BD6684849FCB6CD33650ADF57`

## Cross-environment numerical consistency
Three execution environments produced the same recomputed-result SHA:

`330271d14ee7086e27f875a4a56e720f169cdef1523e908ad94696bb70df15a4`

Max absolute reconstruction error versus source: `4.76837158203125e-07`

## Shared identity/reference-state consistency
A cross-node reference-state validation produced the same SHA-256:

`1488ccf08323200643d5759046f2d47e1e16d44a70f278a79346aec53103d937`

## QSTATIC + QmRNA controlled equivalence
In one controlled A/B test, 22 / 22 decoded frame hashes matched.

framemd5 manifest SHA-256:
`FF55120ADF80F99D74405C5DECA7A9B54116B01F987591A012BD1FF01467F5D7`

## Cross-boundary continuation
Recorded completed-output hashes include:

- `7A909C59636C1A18C6B1A1C7CD2037120F25DDC2C7F36CD2E62B4C70A43212E1`
- `C35FAECFE3C1BD0B5338CC4BE0EB8A854A10CE0FEEF86D39CA750DE6BB4A357C`

## Evidence boundary

This document intentionally omits internal state schemas, control equations, threshold values, serialization, restore sequence, scheduler policy, QmRNA representation, QSTATIC contracts, Qvram implementation and production source code.

**Real evidence. Black-box mechanism.**
