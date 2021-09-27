from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetroServerInfo")

@attr.s(auto_attribs=True)
class MetroServerInfo:
    """
    Attributes:
        metro (Union[Unset, str]): The metro ID or code to check the capacity in.
        plan (Union[Unset, str]): The plan ID or slug to check the capacity of.
        quantity (Union[Unset, str]): The number of servers to check the capacity of.
    """

    metro: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        metro = self.metro
        plan = self.plan
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metro is not UNSET:
            field_dict["metro"] = metro
        if plan is not UNSET:
            field_dict["plan"] = plan
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metro = d.pop("metro", UNSET)

        plan = d.pop("plan", UNSET)

        quantity = d.pop("quantity", UNSET)

        metro_server_info = cls(
            metro=metro,
            plan=plan,
            quantity=quantity,
        )

        metro_server_info.additional_properties = d
        return metro_server_info

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
