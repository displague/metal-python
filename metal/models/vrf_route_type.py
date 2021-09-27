from enum import Enum


class VrfRouteType(str, Enum):
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
