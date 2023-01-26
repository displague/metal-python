from enum import Enum


class FindFacilitiesExcludeItem(str, Enum):
    ADDRESS = "address"
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
