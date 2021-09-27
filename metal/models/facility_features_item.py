from enum import Enum


class FacilityFeaturesItem(str, Enum):
    BAREMETAL = "baremetal"
    BACKEND_TRANSFER = "backend_transfer"
    LAYER_2 = "layer_2"
    GLOBAL_IPV4 = "global_ipv4"
    IBX = "ibx"

    def __str__(self) -> str:
        return str(self.value)
