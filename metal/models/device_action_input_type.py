from enum import Enum


class DeviceActionInputType(str, Enum):
    POWER_ON = "power_on"
    POWER_OFF = "power_off"
    REBOOT = "reboot"
    RESCUE = "rescue"
    REINSTALL = "reinstall"

    def __str__(self) -> str:
        return str(self.value)
