from enum import Enum


class BgpSessionStatus(str, Enum):
    UNKNOWN = "unknown"
    UP = "up"
    DOWN = "down"

    def __str__(self) -> str:
        return str(self.value)
