from enum import Enum


class BgpConfigDeploymentType(str, Enum):
    GLOBAL = "global"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
