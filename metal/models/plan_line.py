from enum import Enum


class PlanLine(str, Enum):
    BAREMETAL = "baremetal"

    def __str__(self) -> str:
        return str(self.value)
