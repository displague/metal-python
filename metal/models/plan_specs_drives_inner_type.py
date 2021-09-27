from enum import Enum


class PlanSpecsDrivesInnerType(str, Enum):
    HDD = "HDD"
    SSD = "SSD"
    NVME = "NVME"

    def __str__(self) -> str:
        return str(self.value)
