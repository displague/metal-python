from enum import Enum


class MetalGatewayLiteState(str, Enum):
    READY = "ready"
    ACTIVE = "active"
    DELETING = "deleting"

    def __str__(self) -> str:
        return str(self.value)
