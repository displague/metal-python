from enum import Enum


class VirtualCircuitStatus(str, Enum):
    PENDING = "pending"
    WAITING_ON_CUSTOMER_VLAN = "waiting_on_customer_vlan"
    ACTIVATING = "activating"
    CHANGING_VLAN = "changing_vlan"
    DEACTIVATING = "deactivating"
    DELETING = "deleting"
    ACTIVE = "active"
    EXPIRED = "expired"
    ACTIVATION_FAILED = "activation_failed"
    CHANGING_VLAN_FAILED = "changing_vlan_failed"
    DEACTIVATION_FAILED = "deactivation_failed"
    DELETE_FAILED = "delete_failed"

    def __str__(self) -> str:
        return str(self.value)
