from enum import Enum


class FindProjectHardwareReservationsState(str, Enum):
    ACTIVE = "active"
    SPARE = "spare"
    NEED_OF_SERVICE = "need_of_service"

    def __str__(self) -> str:
        return str(self.value)
