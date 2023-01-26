from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanAvailableInInnerPrice")

@attr.s(auto_attribs=True)
class PlanAvailableInInnerPrice:
    """
    Attributes:
        hour (Union[Unset, float]):  Example: 1.23.
    """

    hour: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        hour = self.hour

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hour is not UNSET:
            field_dict["hour"] = hour

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hour = d.pop("hour", UNSET)

        plan_available_in_inner_price = cls(
            hour=hour,
        )

        plan_available_in_inner_price.additional_properties = d
        return plan_available_in_inner_price

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
