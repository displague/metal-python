import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.invitation_roles_item import InvitationRolesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="Invitation")

@attr.s(auto_attribs=True)
class Invitation:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        invitation (Union[Unset, Href]):
        invited_by (Union[Unset, Href]):
        invitee (Union[Unset, str]):
        nonce (Union[Unset, str]):
        organization (Union[Unset, Href]):
        projects (Union[Unset, List['Href']]):
        roles (Union[Unset, List[InvitationRolesItem]]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invitation: Union[Unset, 'Href'] = UNSET
    invited_by: Union[Unset, 'Href'] = UNSET
    invitee: Union[Unset, str] = UNSET
    nonce: Union[Unset, str] = UNSET
    organization: Union[Unset, 'Href'] = UNSET
    projects: Union[Unset, List['Href']] = UNSET
    roles: Union[Unset, List[InvitationRolesItem]] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        href = self.href
        id = self.id
        invitation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invitation, Unset):
            invitation = self.invitation.to_dict()

        invited_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invited_by, Unset):
            invited_by = self.invited_by.to_dict()

        invitee = self.invitee
        nonce = self.nonce
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)




        roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value

                roles.append(roles_item)




        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if invited_by is not UNSET:
            field_dict["invited_by"] = invited_by
        if invitee is not UNSET:
            field_dict["invitee"] = invitee
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if organization is not UNSET:
            field_dict["organization"] = organization
        if projects is not UNSET:
            field_dict["projects"] = projects
        if roles is not UNSET:
            field_dict["roles"] = roles
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _invitation = d.pop("invitation", UNSET)
        invitation: Union[Unset, Href]
        if isinstance(_invitation,  Unset):
            invitation = UNSET
        else:
            invitation = Href.from_dict(_invitation)




        _invited_by = d.pop("invited_by", UNSET)
        invited_by: Union[Unset, Href]
        if isinstance(_invited_by,  Unset):
            invited_by = UNSET
        else:
            invited_by = Href.from_dict(_invited_by)




        invitee = d.pop("invitee", UNSET)

        nonce = d.pop("nonce", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Href]
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = Href.from_dict(_organization)




        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in (_projects or []):
            projects_item = Href.from_dict(projects_item_data)



            projects.append(projects_item)


        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in (_roles or []):
            roles_item = InvitationRolesItem(roles_item_data)



            roles.append(roles_item)


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        invitation = cls(
            created_at=created_at,
            href=href,
            id=id,
            invitation=invitation,
            invited_by=invited_by,
            invitee=invitee,
            nonce=nonce,
            organization=organization,
            projects=projects,
            roles=roles,
            updated_at=updated_at,
        )

        invitation.additional_properties = d
        return invitation

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
