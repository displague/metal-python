from enum import IntEnum


class CreateSelfServiceReservationRequestPeriodCount(IntEnum):
    VALUE_12 = 12
    VALUE_36 = 36

    def __str__(self) -> str:
        return str(self.value)
