from enum import Enum


class InvitationInputRolesItem(str, Enum):
    ADMIN = "admin"
    BILLING = "billing"
    COLLABORATOR = "collaborator"
    LIMITED_COLLABORATOR = "limited_collaborator"

    def __str__(self) -> str:
        return str(self.value)
