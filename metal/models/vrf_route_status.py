from enum import Enum


class VrfRouteStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    DELETING = "deleting"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
