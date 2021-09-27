from enum import Enum


class PlanSpecsDrivesInnerCategory(str, Enum):
    BOOT = "boot"
    CACHE = "cache"
    STORAGE = "storage"

    def __str__(self) -> str:
        return str(self.value)
