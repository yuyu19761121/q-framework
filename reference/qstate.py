"""Public QSTATE reference types.

This documents state semantics only. It is not the production state manager.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class QState(str, Enum):
    QUEUED = "QUEUED"
    ACTIVE = "ACTIVE"
    PRESSURE = "PRESSURE"
    FREEZING = "FREEZING"
    PERSISTED = "PERSISTED"
    RESTORING = "RESTORING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class StateReceipt:
    job_id: str
    lineage: str
    state: QState
    seed: Optional[int] = None
    checkpoint_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
