from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.event import Event
  from ..models.meta import Meta




T = TypeVar("T", bound="EventList")

@attr.s(auto_attribs=True)
class EventList:
    """
    Attributes:
        events (Union[Unset, List['Event']]):
        meta (Union[Unset, Meta]):
    """

    events: Union[Unset, List['Event']] = UNSET
    meta: Union[Unset, 'Meta'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)




        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if events is not UNSET:
            field_dict["events"] = events
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event import Event
        from ..models.meta import Meta
        d = src_dict.copy()
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in (_events or []):
            events_item = Event.from_dict(events_item_data)



            events.append(events_item)


        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)




        event_list = cls(
            events=events,
            meta=meta,
        )

        event_list.additional_properties = d
        return event_list

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
