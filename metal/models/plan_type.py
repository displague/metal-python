from enum import Enum


class PlanType(str, Enum):
    STANDARD = "standard"
    WORKLOAD_OPTIMIZED = "workload_optimized"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
