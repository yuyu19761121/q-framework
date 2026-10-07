"""Sanitized proof-manifest code derived from a non-sensitive verifier.

This public version retains generic integrity mechanics only.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, Iterable, List


def canonical(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class PublicPageDescriptor:
    page_index: int
    logical_start: int
    logical_stop: int
    descriptor_sha256: str


def build_proof(*, lineage: str, seed: int, logical_units: int,
                pages: Iterable[PublicPageDescriptor],
                metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
    page_list: List[Dict[str, Any]] = [asdict(p) for p in pages]
    body = {
        "schema": "q-framework-public-proof-v1",
        "lineage": lineage,
        "seed": int(seed),
        "logical_units": int(logical_units),
        "pages": page_list,
        "metadata": dict(metadata or {}),
    }
    body["proof_sha256"] = sha256_bytes(canonical(body))
    return body


def verify_proof(proof: Dict[str, Any]) -> bool:
    expected = str(proof.get("proof_sha256", ""))
    body = dict(proof)
    body.pop("proof_sha256", None)
    return bool(expected) and sha256_bytes(canonical(body)) == expected
