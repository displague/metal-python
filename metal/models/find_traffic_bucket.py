from enum import Enum


class FindTrafficBucket(str, Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
