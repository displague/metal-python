from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapacityCheckPerFacilityInfo")

@attr.s(auto_attribs=True)
class CapacityCheckPerFacilityInfo:
    """
    Attributes:
        available (Union[Unset, bool]):
        facility (Union[Unset, str]):
        plan (Union[Unset, str]):
        quantity (Union[Unset, str]):
    """

    available: Union[Unset, bool] = UNSET
    facility: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        available = self.available
        facility = self.facility
        plan = self.plan
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if facility is not UNSET:
            field_dict["facility"] = facility
        if plan is not UNSET:
            field_dict["plan"] = plan
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available = d.pop("available", UNSET)

        facility = d.pop("facility", UNSET)

        plan = d.pop("plan", UNSET)

        quantity = d.pop("quantity", UNSET)

        capacity_check_per_facility_info = cls(
            available=available,
            facility=facility,
            plan=plan,
            quantity=quantity,
        )

        capacity_check_per_facility_info.additional_properties = d
        return capacity_check_per_facility_info

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
