import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="TransferRequest")

@attr.s(auto_attribs=True)
class TransferRequest:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        project (Union[Unset, Href]):
        target_organization (Union[Unset, Href]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    target_organization: Union[Unset, 'Href'] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        href = self.href
        id = self.id
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        target_organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target_organization, Unset):
            target_organization = self.target_organization.to_dict()

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
        if project is not UNSET:
            field_dict["project"] = project
        if target_organization is not UNSET:
            field_dict["target_organization"] = target_organization
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

        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        _target_organization = d.pop("target_organization", UNSET)
        target_organization: Union[Unset, Href]
        if isinstance(_target_organization,  Unset):
            target_organization = UNSET
        else:
            target_organization = Href.from_dict(_target_organization)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        transfer_request = cls(
            created_at=created_at,
            href=href,
            id=id,
            project=project,
            target_organization=target_organization,
            updated_at=updated_at,
        )

        transfer_request.additional_properties = d
        return transfer_request

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
