from enum import Enum


class FindProjectHardwareReservationsProvisionable(str, Enum):
    ONLY = "only"

    def __str__(self) -> str:
        return str(self.value)
