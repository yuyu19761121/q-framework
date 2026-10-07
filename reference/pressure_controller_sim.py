"""Simplified public pressure-controller simulation.

The production QmRNA controller is NOT published here.
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    gpu_util: float
    vram_util: float
    io_pressure: float = 0.0


@dataclass
class PublicController:
    gpu_target: float = 0.80
    vram_target: float = 0.85
    min_rate: float = 0.10
    max_rate: float = 1.00
    rate: float = 0.50

    def update(self, m: Metrics) -> float:
        gpu_error = self.gpu_target - m.gpu_util
        vram_error = self.vram_target - m.vram_util
        pressure_penalty = max(0.0, -vram_error) * 0.8 + max(0.0, m.io_pressure) * 0.2
        headroom_bonus = max(0.0, gpu_error) * 0.3 + max(0.0, vram_error) * 0.2
        self.rate += headroom_bonus - pressure_penalty
        self.rate = max(self.min_rate, min(self.max_rate, self.rate))
        return self.rate
