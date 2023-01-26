from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_self_service_reservation_request_period_count import CreateSelfServiceReservationRequestPeriodCount
from ..models.create_self_service_reservation_request_period_unit import CreateSelfServiceReservationRequestPeriodUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSelfServiceReservationRequestPeriod")

@attr.s(auto_attribs=True)
class CreateSelfServiceReservationRequestPeriod:
    """
    Attributes:
        count (Union[Unset, CreateSelfServiceReservationRequestPeriodCount]):
        unit (Union[Unset, CreateSelfServiceReservationRequestPeriodUnit]):
    """

    count: Union[Unset, CreateSelfServiceReservationRequestPeriodCount] = UNSET
    unit: Union[Unset, CreateSelfServiceReservationRequestPeriodUnit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        count: Union[Unset, int] = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.value

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _count = d.pop("count", UNSET)
        count: Union[Unset, CreateSelfServiceReservationRequestPeriodCount]
        if isinstance(_count,  Unset):
            count = UNSET
        else:
            count = CreateSelfServiceReservationRequestPeriodCount(_count)




        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, CreateSelfServiceReservationRequestPeriodUnit]
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = CreateSelfServiceReservationRequestPeriodUnit(_unit)




        create_self_service_reservation_request_period = cls(
            count=count,
            unit=unit,
        )

        create_self_service_reservation_request_period.additional_properties = d
        return create_self_service_reservation_request_period

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
