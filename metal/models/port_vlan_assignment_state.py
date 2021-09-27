from enum import Enum


class PortVlanAssignmentState(str, Enum):
    ASSIGNED = "assigned"
    UNASSIGNING = "unassigning"

    def __str__(self) -> str:
        return str(self.value)
