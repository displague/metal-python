from enum import Enum


class FindOrganizationsPersonal(str, Enum):
    INCLUDE = "include"
    EXCLUDE = "exclude"
    ONLY = "only"

    def __str__(self) -> str:
        return str(self.value)
