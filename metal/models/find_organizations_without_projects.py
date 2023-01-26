from enum import Enum


class FindOrganizationsWithoutProjects(str, Enum):
    INCLUDE = "include"
    EXCLUDE = "exclude"
    ONLY = "only"

    def __str__(self) -> str:
        return str(self.value)
