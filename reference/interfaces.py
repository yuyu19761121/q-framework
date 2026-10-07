"""Public architectural interfaces. They express roles, not production policy."""

from typing import Mapping, Protocol, Any


class TelemetrySource(Protocol):
    def snapshot(self) -> Mapping[str, float]: ...


class ControlPlane(Protocol):
    def update(self, metrics: Mapping[str, float]) -> Mapping[str, Any]: ...


class StateStore(Protocol):
    def freeze(self, job_id: str) -> str: ...
    def restore(self, checkpoint_id: str) -> Mapping[str, Any]: ...


class Worker(Protocol):
    def submit(self, payload: Mapping[str, Any]) -> str: ...


class Validator(Protocol):
    def validate(self, artifact: Mapping[str, Any]) -> bool: ...
