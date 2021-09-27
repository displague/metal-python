from enum import Enum


class DeviceCreateInputBillingCycle(str, Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
