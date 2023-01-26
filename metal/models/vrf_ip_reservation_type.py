from enum import Enum


class VrfIpReservationType(str, Enum):
    VRF = "vrf"

    def __str__(self) -> str:
        return str(self.value)
