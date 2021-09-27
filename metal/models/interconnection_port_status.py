from enum import Enum


class InterconnectionPortStatus(str, Enum):
    REQUESTED = "requested"
    ACTIVE = "active"
    DELETING = "deleting"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
