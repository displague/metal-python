from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.payment_method import PaymentMethod




T = TypeVar("T", bound="PaymentMethodList")

@attr.s(auto_attribs=True)
class PaymentMethodList:
    """
    Attributes:
        payment_methods (Union[Unset, List['PaymentMethod']]):
    """

    payment_methods: Union[Unset, List['PaymentMethod']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        payment_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = []
            for payment_methods_item_data in self.payment_methods:
                payment_methods_item = payment_methods_item_data.to_dict()

                payment_methods.append(payment_methods_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if payment_methods is not UNSET:
            field_dict["payment_methods"] = payment_methods

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_method import PaymentMethod
        d = src_dict.copy()
        payment_methods = []
        _payment_methods = d.pop("payment_methods", UNSET)
        for payment_methods_item_data in (_payment_methods or []):
            payment_methods_item = PaymentMethod.from_dict(payment_methods_item_data)



            payment_methods.append(payment_methods_item)


        payment_method_list = cls(
            payment_methods=payment_methods,
        )

        payment_method_list.additional_properties = d
        return payment_method_list

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
