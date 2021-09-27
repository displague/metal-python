from enum import Enum


class FabricServiceTokenState(str, Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
