import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.event_modified_by import EventModifiedBy
  from ..models.href import Href




T = TypeVar("T", bound="Event")

@attr.s(auto_attribs=True)
class Event:
    """
    Attributes:
        body (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        interpolated (Union[Unset, str]):
        relationships (Union[Unset, List['Href']]):
        state (Union[Unset, str]):
        type (Union[Unset, str]):
        modified_by (Union[Unset, EventModifiedBy]):
        ip (Union[Unset, str]):
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interpolated: Union[Unset, str] = UNSET
    relationships: Union[Unset, List['Href']] = UNSET
    state: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    modified_by: Union[Unset, 'EventModifiedBy'] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        body = self.body
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        href = self.href
        id = self.id
        interpolated = self.interpolated
        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()

                relationships.append(relationships_item)




        state = self.state
        type = self.type
        modified_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if interpolated is not UNSET:
            field_dict["interpolated"] = interpolated
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if state is not UNSET:
            field_dict["state"] = state
        if type is not UNSET:
            field_dict["type"] = type
        if modified_by is not UNSET:
            field_dict["modified_by"] = modified_by
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_modified_by import EventModifiedBy
        from ..models.href import Href
        d = src_dict.copy()
        body = d.pop("body", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        interpolated = d.pop("interpolated", UNSET)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in (_relationships or []):
            relationships_item = Href.from_dict(relationships_item_data)



            relationships.append(relationships_item)


        state = d.pop("state", UNSET)

        type = d.pop("type", UNSET)

        _modified_by = d.pop("modified_by", UNSET)
        modified_by: Union[Unset, EventModifiedBy]
        if isinstance(_modified_by,  Unset):
            modified_by = UNSET
        else:
            modified_by = EventModifiedBy.from_dict(_modified_by)




        ip = d.pop("ip", UNSET)

        event = cls(
            body=body,
            created_at=created_at,
            href=href,
            id=id,
            interpolated=interpolated,
            relationships=relationships,
            state=state,
            type=type,
            modified_by=modified_by,
            ip=ip,
        )

        event.additional_properties = d
        return event

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
