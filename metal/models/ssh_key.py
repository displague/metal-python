import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="SSHKey")

@attr.s(auto_attribs=True)
class SSHKey:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        entity (Union[Unset, Href]):
        fingerprint (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        key (Union[Unset, str]):
        label (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    entity: Union[Unset, 'Href'] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        fingerprint = self.fingerprint
        href = self.href
        id = self.id
        key = self.key
        label = self.label
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if entity is not UNSET:
            field_dict["entity"] = entity
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
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




        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, Href]
        if isinstance(_entity,  Unset):
            entity = UNSET
        else:
            entity = Href.from_dict(_entity)




        fingerprint = d.pop("fingerprint", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        ssh_key = cls(
            created_at=created_at,
            entity=entity,
            fingerprint=fingerprint,
            href=href,
            id=id,
            key=key,
            label=label,
            updated_at=updated_at,
        )

        ssh_key.additional_properties = d
        return ssh_key

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
