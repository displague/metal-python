from enum import Enum


class FabricServiceTokenServiceTokenType(str, Enum):
    A_SIDE = "a_side"
    Z_SIDE = "z_side"

    def __str__(self) -> str:
        return str(self.value)
