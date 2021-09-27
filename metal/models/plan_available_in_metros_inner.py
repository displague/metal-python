from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plan_available_in_inner_price import PlanAvailableInInnerPrice




T = TypeVar("T", bound="PlanAvailableInMetrosInner")

@attr.s(auto_attribs=True)
class PlanAvailableInMetrosInner:
    """
    Attributes:
        href (Union[Unset, str]): href to the Metro
        price (Union[Unset, PlanAvailableInInnerPrice]):
    """

    href: Union[Unset, str] = UNSET
    price: Union[Unset, 'PlanAvailableInInnerPrice'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        href = self.href
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if href is not UNSET:
            field_dict["href"] = href
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_available_in_inner_price import PlanAvailableInInnerPrice
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, PlanAvailableInInnerPrice]
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = PlanAvailableInInnerPrice.from_dict(_price)




        plan_available_in_metros_inner = cls(
            href=href,
            price=price,
        )

        plan_available_in_metros_inner.additional_properties = d
        return plan_available_in_metros_inner

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
