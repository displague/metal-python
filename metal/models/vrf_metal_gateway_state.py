from enum import Enum


class VrfMetalGatewayState(str, Enum):
    READY = "ready"
    ACTIVE = "active"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)
