from enum import Enum


class InterconnectionPortRole(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
