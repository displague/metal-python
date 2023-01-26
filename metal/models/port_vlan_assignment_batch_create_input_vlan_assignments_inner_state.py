from enum import Enum


class PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState(str, Enum):
    ASSIGNED = "assigned"
    UNASSIGNED = "unassigned"

    def __str__(self) -> str:
        return str(self.value)
