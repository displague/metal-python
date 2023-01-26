from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethodCreateInput")

@attr.s(auto_attribs=True)
class PaymentMethodCreateInput:
    """
    Attributes:
        name (str):
        nonce (str):
        default (Union[Unset, bool]):
    """

    name: str
    nonce: str
    default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        nonce = self.nonce
        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "nonce": nonce,
        })
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        nonce = d.pop("nonce")

        default = d.pop("default", UNSET)

        payment_method_create_input = cls(
            name=name,
            nonce=nonce,
            default=default,
        )

        payment_method_create_input.additional_properties = d
        return payment_method_create_input

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
