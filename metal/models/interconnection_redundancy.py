from enum import Enum


class InterconnectionRedundancy(str, Enum):
    PRIMARY = "primary"
    REDUNDANT = "redundant"

    def __str__(self) -> str:
        return str(self.value)
