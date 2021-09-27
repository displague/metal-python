from enum import Enum


class PortType(str, Enum):
    NETWORKPORT = "NetworkPort"
    NETWORKBONDPORT = "NetworkBondPort"

    def __str__(self) -> str:
        return str(self.value)
