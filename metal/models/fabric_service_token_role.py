from enum import Enum


class FabricServiceTokenRole(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
