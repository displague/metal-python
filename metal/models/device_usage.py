from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceUsage")

@attr.s(auto_attribs=True)
class DeviceUsage:
    """
    Attributes:
        quantity (Union[Unset, str]):
        total (Union[Unset, str]):
        unit (Union[Unset, str]):
    """

    quantity: Union[Unset, str] = UNSET
    total: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        total = self.total
        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if total is not UNSET:
            field_dict["total"] = total
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity", UNSET)

        total = d.pop("total", UNSET)

        unit = d.pop("unit", UNSET)

        device_usage = cls(
            quantity=quantity,
            total=total,
            unit=unit,
        )

        device_usage.additional_properties = d
        return device_usage

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
