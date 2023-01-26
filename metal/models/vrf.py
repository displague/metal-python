import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metro import Metro
  from ..models.project import Project
  from ..models.user import User




T = TypeVar("T", bound="Vrf")

@attr.s(auto_attribs=True)
class Vrf:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]): Optional field that can be set to describe the VRF
        local_asn (Union[Unset, int]): A 4-byte ASN associated with the VRF.
        ip_ranges (Union[Unset, List[str]]): A list of CIDR network addresses. Like ["10.0.0.0/16", "2001:d78::/56"].
        project (Union[Unset, Project]):
        metro (Union[Unset, Metro]):
        created_by (Union[Unset, User]):
        href (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    local_asn: Union[Unset, int] = UNSET
    ip_ranges: Union[Unset, List[str]] = UNSET
    project: Union[Unset, 'Project'] = UNSET
    metro: Union[Unset, 'Metro'] = UNSET
    created_by: Union[Unset, 'User'] = UNSET
    href: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        local_asn = self.local_asn
        ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_ranges, Unset):
            ip_ranges = self.ip_ranges




        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        href = self.href
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if local_asn is not UNSET:
            field_dict["local_asn"] = local_asn
        if ip_ranges is not UNSET:
            field_dict["ip_ranges"] = ip_ranges
        if project is not UNSET:
            field_dict["project"] = project
        if metro is not UNSET:
            field_dict["metro"] = metro
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if href is not UNSET:
            field_dict["href"] = href
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metro import Metro
        from ..models.project import Project
        from ..models.user import User
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        local_asn = d.pop("local_asn", UNSET)

        ip_ranges = cast(List[str], d.pop("ip_ranges", UNSET))


        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, Metro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = Metro.from_dict(_metro)




        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, User]
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = User.from_dict(_created_by)




        href = d.pop("href", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        vrf = cls(
            id=id,
            name=name,
            description=description,
            local_asn=local_asn,
            ip_ranges=ip_ranges,
            project=project,
            metro=metro,
            created_by=created_by,
            href=href,
            created_at=created_at,
            updated_at=updated_at,
        )

        vrf.additional_properties = d
        return vrf

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
