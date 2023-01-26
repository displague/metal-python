from enum import Enum


class PortNetworkType(str, Enum):
    LAYER2_BONDED = "layer2-bonded"
    LAYER2_INDIVIDUAL = "layer2-individual"
    LAYER3 = "layer3"
    HYBRID = "hybrid"
    HYBRID_BONDED = "hybrid-bonded"

    def __str__(self) -> str:
        return str(self.value)
