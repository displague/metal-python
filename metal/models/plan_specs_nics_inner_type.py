from enum import Enum


class PlanSpecsNicsInnerType(str, Enum):
    VALUE_0 = "1Gbps"
    VALUE_1 = "10Gbps"
    VALUE_2 = "25Gbps"

    def __str__(self) -> str:
        return str(self.value)
