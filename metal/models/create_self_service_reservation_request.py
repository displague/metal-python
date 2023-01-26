import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
  from ..models.self_service_reservation_item_request import SelfServiceReservationItemRequest




T = TypeVar("T", bound="CreateSelfServiceReservationRequest")

@attr.s(auto_attribs=True)
class CreateSelfServiceReservationRequest:
    """
    Attributes:
        item (Union[Unset, List['SelfServiceReservationItemRequest']]):
        notes (Union[Unset, str]):
        period (Union[Unset, CreateSelfServiceReservationRequestPeriod]):
        start_date (Union[Unset, datetime.datetime]):
    """

    item: Union[Unset, List['SelfServiceReservationItemRequest']] = UNSET
    notes: Union[Unset, str] = UNSET
    period: Union[Unset, 'CreateSelfServiceReservationRequestPeriod'] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item, Unset):
            item = []
            for item_item_data in self.item:
                item_item = item_item_data.to_dict()

                item.append(item_item)




        notes = self.notes
        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if item is not UNSET:
            field_dict["item"] = item
        if notes is not UNSET:
            field_dict["notes"] = notes
        if period is not UNSET:
            field_dict["period"] = period
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
        from ..models.self_service_reservation_item_request import SelfServiceReservationItemRequest
        d = src_dict.copy()
        item = []
        _item = d.pop("item", UNSET)
        for item_item_data in (_item or []):
            item_item = SelfServiceReservationItemRequest.from_dict(item_item_data)



            item.append(item_item)


        notes = d.pop("notes", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, CreateSelfServiceReservationRequestPeriod]
        if isinstance(_period,  Unset):
            period = UNSET
        else:
            period = CreateSelfServiceReservationRequestPeriod.from_dict(_period)




        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)




        create_self_service_reservation_request = cls(
            item=item,
            notes=notes,
            period=period,
            start_date=start_date,
        )

        create_self_service_reservation_request.additional_properties = d
        return create_self_service_reservation_request

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
