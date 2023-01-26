from enum import Enum


class FindIPReservationsTypesItem(str, Enum):
    GLOBAL_IPV4 = "global_ipv4"
    PRIVATE_IPV4 = "private_ipv4"
    PUBLIC_IPV4 = "public_ipv4"
    PUBLIC_IPV6 = "public_ipv6"
    VRF = "vrf"

    def __str__(self) -> str:
        return str(self.value)
