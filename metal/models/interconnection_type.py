from enum import Enum


class InterconnectionType(str, Enum):
    SHARED = "shared"
    DEDICATED = "dedicated"

    def __str__(self) -> str:
        return str(self.value)
