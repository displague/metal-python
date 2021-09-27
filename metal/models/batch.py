import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="Batch")

@attr.s(auto_attribs=True)
class Batch:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        devices (Union[Unset, List['Href']]):
        error_messages (Union[Unset, List[str]]):
        id (Union[Unset, str]):
        project (Union[Unset, Href]):
        quantity (Union[Unset, int]):
        state (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    devices: Union[Unset, List['Href']] = UNSET
    error_messages: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    quantity: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()

                devices.append(devices_item)




        error_messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = self.error_messages




        id = self.id
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        quantity = self.quantity
        state = self.state
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if devices is not UNSET:
            field_dict["devices"] = devices
        if error_messages is not UNSET:
            field_dict["error_messages"] = error_messages
        if id is not UNSET:
            field_dict["id"] = id
        if project is not UNSET:
            field_dict["project"] = project
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if state is not UNSET:
            field_dict["state"] = state
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




        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in (_devices or []):
            devices_item = Href.from_dict(devices_item_data)



            devices.append(devices_item)


        error_messages = cast(List[str], d.pop("error_messages", UNSET))


        id = d.pop("id", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        quantity = d.pop("quantity", UNSET)

        state = d.pop("state", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        batch = cls(
            created_at=created_at,
            devices=devices,
            error_messages=error_messages,
            id=id,
            project=project,
            quantity=quantity,
            state=state,
            updated_at=updated_at,
        )

        batch.additional_properties = d
        return batch

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
