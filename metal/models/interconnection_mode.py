from enum import Enum


class InterconnectionMode(str, Enum):
    STANDARD = "standard"
    TUNNEL = "tunnel"

    def __str__(self) -> str:
        return str(self.value)
