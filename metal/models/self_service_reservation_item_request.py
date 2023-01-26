from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelfServiceReservationItemRequest")

@attr.s(auto_attribs=True)
class SelfServiceReservationItemRequest:
    """
    Attributes:
        amount (Union[Unset, float]):
        metro_id (Union[Unset, str]):
        plan_id (Union[Unset, str]):
        quantity (Union[Unset, int]):
        term (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    metro_id: Union[Unset, str] = UNSET
    plan_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    term: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        metro_id = self.metro_id
        plan_id = self.plan_id
        quantity = self.quantity
        term = self.term

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if metro_id is not UNSET:
            field_dict["metro_id"] = metro_id
        if plan_id is not UNSET:
            field_dict["plan_id"] = plan_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        metro_id = d.pop("metro_id", UNSET)

        plan_id = d.pop("plan_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        term = d.pop("term", UNSET)

        self_service_reservation_item_request = cls(
            amount=amount,
            metro_id=metro_id,
            plan_id=plan_id,
            quantity=quantity,
            term=term,
        )

        self_service_reservation_item_request.additional_properties = d
        return self_service_reservation_item_request

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
