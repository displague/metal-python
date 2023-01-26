from enum import Enum


class BgpConfigStatus(str, Enum):
    REQUESTED = "requested"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
