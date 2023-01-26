from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelfServiceReservationItemResponse")

@attr.s(auto_attribs=True)
class SelfServiceReservationItemResponse:
    """
    Attributes:
        amount (Union[Unset, float]):
        id (Union[Unset, str]):
        metro_code (Union[Unset, str]):
        metro_id (Union[Unset, str]):
        metro_name (Union[Unset, str]):
        plan_id (Union[Unset, str]):
        plan_name (Union[Unset, str]):
        plan_slug (Union[Unset, str]):
        quantity (Union[Unset, int]):
        term (Union[Unset, str]):
    """

    amount: Union[Unset, float] = UNSET
    id: Union[Unset, str] = UNSET
    metro_code: Union[Unset, str] = UNSET
    metro_id: Union[Unset, str] = UNSET
    metro_name: Union[Unset, str] = UNSET
    plan_id: Union[Unset, str] = UNSET
    plan_name: Union[Unset, str] = UNSET
    plan_slug: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    term: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        id = self.id
        metro_code = self.metro_code
        metro_id = self.metro_id
        metro_name = self.metro_name
        plan_id = self.plan_id
        plan_name = self.plan_name
        plan_slug = self.plan_slug
        quantity = self.quantity
        term = self.term

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if id is not UNSET:
            field_dict["id"] = id
        if metro_code is not UNSET:
            field_dict["metro_code"] = metro_code
        if metro_id is not UNSET:
            field_dict["metro_id"] = metro_id
        if metro_name is not UNSET:
            field_dict["metro_name"] = metro_name
        if plan_id is not UNSET:
            field_dict["plan_id"] = plan_id
        if plan_name is not UNSET:
            field_dict["plan_name"] = plan_name
        if plan_slug is not UNSET:
            field_dict["plan_slug"] = plan_slug
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        id = d.pop("id", UNSET)

        metro_code = d.pop("metro_code", UNSET)

        metro_id = d.pop("metro_id", UNSET)

        metro_name = d.pop("metro_name", UNSET)

        plan_id = d.pop("plan_id", UNSET)

        plan_name = d.pop("plan_name", UNSET)

        plan_slug = d.pop("plan_slug", UNSET)

        quantity = d.pop("quantity", UNSET)

        term = d.pop("term", UNSET)

        self_service_reservation_item_response = cls(
            amount=amount,
            id=id,
            metro_code=metro_code,
            metro_id=metro_id,
            metro_name=metro_name,
            plan_id=plan_id,
            plan_name=plan_name,
            plan_slug=plan_slug,
            quantity=quantity,
            term=term,
        )

        self_service_reservation_item_response.additional_properties = d
        return self_service_reservation_item_response

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
