from enum import Enum


class DeviceState(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    DEPROVISIONING = "deprovisioning"
    FAILED = "failed"
    INACTIVE = "inactive"
    QUEUED = "queued"
    REINSTALLING = "reinstalling"
    POST_PROVISIONING = "post_provisioning"
    POWERING_ON = "powering_on"
    POWERING_OFF = "powering_off"
    PROVISIONING = "provisioning"

    def __str__(self) -> str:
        return str(self.value)
