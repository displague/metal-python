from enum import Enum


class CreateSelfServiceReservationRequestPeriodUnit(str, Enum):
    MONTHLY = "monthly"

    def __str__(self) -> str:
        return str(self.value)
