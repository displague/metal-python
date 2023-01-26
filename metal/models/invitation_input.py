from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.invitation_input_roles_item import InvitationInputRolesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationInput")

@attr.s(auto_attribs=True)
class InvitationInput:
    """
    Attributes:
        invitee (str):
        message (Union[Unset, str]):
        organization_id (Union[Unset, str]):
        projects_ids (Union[Unset, List[str]]):
        roles (Union[Unset, List[InvitationInputRolesItem]]):
    """

    invitee: str
    message: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    projects_ids: Union[Unset, List[str]] = UNSET
    roles: Union[Unset, List[InvitationInputRolesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        invitee = self.invitee
        message = self.message
        organization_id = self.organization_id
        projects_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.projects_ids, Unset):
            projects_ids = self.projects_ids




        roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value

                roles.append(roles_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invitee": invitee,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if projects_ids is not UNSET:
            field_dict["projects_ids"] = projects_ids
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invitee = d.pop("invitee")

        message = d.pop("message", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        projects_ids = cast(List[str], d.pop("projects_ids", UNSET))


        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in (_roles or []):
            roles_item = InvitationInputRolesItem(roles_item_data)



            roles.append(roles_item)


        invitation_input = cls(
            invitee=invitee,
            message=message,
            organization_id=organization_id,
            projects_ids=projects_ids,
            roles=roles,
        )

        invitation_input.additional_properties = d
        return invitation_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
