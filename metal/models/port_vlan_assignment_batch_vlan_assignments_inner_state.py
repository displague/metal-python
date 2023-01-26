from enum import Enum


class PortVlanAssignmentBatchVlanAssignmentsInnerState(str, Enum):
    ASSIGNED = "assigned"
    UNASSIGNED = "unassigned"

    def __str__(self) -> str:
        return str(self.value)
