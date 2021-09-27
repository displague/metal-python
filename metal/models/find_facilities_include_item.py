from enum import Enum


class FindFacilitiesIncludeItem(str, Enum):
    ADDRESS = "address"
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
