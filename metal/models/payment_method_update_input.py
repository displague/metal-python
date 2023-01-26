from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.payment_method_update_input_billing_address import PaymentMethodUpdateInputBillingAddress




T = TypeVar("T", bound="PaymentMethodUpdateInput")

@attr.s(auto_attribs=True)
class PaymentMethodUpdateInput:
    """
    Attributes:
        billing_address (Union[Unset, PaymentMethodUpdateInputBillingAddress]):
        cardholder_name (Union[Unset, str]):
        default (Union[Unset, bool]):
        expiration_month (Union[Unset, str]):
        expiration_year (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    billing_address: Union[Unset, 'PaymentMethodUpdateInputBillingAddress'] = UNSET
    cardholder_name: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    expiration_month: Union[Unset, str] = UNSET
    expiration_year: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        cardholder_name = self.cardholder_name
        default = self.default
        expiration_month = self.expiration_month
        expiration_year = self.expiration_year
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if cardholder_name is not UNSET:
            field_dict["cardholder_name"] = cardholder_name
        if default is not UNSET:
            field_dict["default"] = default
        if expiration_month is not UNSET:
            field_dict["expiration_month"] = expiration_month
        if expiration_year is not UNSET:
            field_dict["expiration_year"] = expiration_year
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method_update_input_billing_address import PaymentMethodUpdateInputBillingAddress
        d = src_dict.copy()
        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, PaymentMethodUpdateInputBillingAddress]
        if isinstance(_billing_address,  Unset):
            billing_address = UNSET
        else:
            billing_address = PaymentMethodUpdateInputBillingAddress.from_dict(_billing_address)




        cardholder_name = d.pop("cardholder_name", UNSET)

        default = d.pop("default", UNSET)

        expiration_month = d.pop("expiration_month", UNSET)

        expiration_year = d.pop("expiration_year", UNSET)

        name = d.pop("name", UNSET)

        payment_method_update_input = cls(
            billing_address=billing_address,
            cardholder_name=cardholder_name,
            default=default,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            name=name,
        )

        payment_method_update_input.additional_properties = d
        return payment_method_update_input

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
