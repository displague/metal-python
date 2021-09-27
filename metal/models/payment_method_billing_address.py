from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethodBillingAddress")

@attr.s(auto_attribs=True)
class PaymentMethodBillingAddress:
    """
    Attributes:
        country_code_alpha2 (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        street_address (Union[Unset, str]):
    """

    country_code_alpha2: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    street_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        country_code_alpha2 = self.country_code_alpha2
        postal_code = self.postal_code
        street_address = self.street_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if country_code_alpha2 is not UNSET:
            field_dict["country_code_alpha2"] = country_code_alpha2
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if street_address is not UNSET:
            field_dict["street_address"] = street_address

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_code_alpha2 = d.pop("country_code_alpha2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        street_address = d.pop("street_address", UNSET)

        payment_method_billing_address = cls(
            country_code_alpha2=country_code_alpha2,
            postal_code=postal_code,
            street_address=street_address,
        )

        payment_method_billing_address.additional_properties = d
        return payment_method_billing_address

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
