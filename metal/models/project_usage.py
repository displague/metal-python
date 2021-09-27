from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectUsage")

@attr.s(auto_attribs=True)
class ProjectUsage:
    """
    Attributes:
        facility (Union[Unset, str]):
        name (Union[Unset, str]):
        plan (Union[Unset, str]):
        plan_version (Union[Unset, str]):
        price (Union[Unset, str]):
        quantity (Union[Unset, str]):
        total (Union[Unset, str]):
        type (Union[Unset, str]):
        unit (Union[Unset, str]):
    """

    facility: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    plan_version: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    quantity: Union[Unset, str] = UNSET
    total: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        facility = self.facility
        name = self.name
        plan = self.plan
        plan_version = self.plan_version
        price = self.price
        quantity = self.quantity
        total = self.total
        type = self.type
        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if facility is not UNSET:
            field_dict["facility"] = facility
        if name is not UNSET:
            field_dict["name"] = name
        if plan is not UNSET:
            field_dict["plan"] = plan
        if plan_version is not UNSET:
            field_dict["plan_version"] = plan_version
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if total is not UNSET:
            field_dict["total"] = total
        if type is not UNSET:
            field_dict["type"] = type
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        facility = d.pop("facility", UNSET)

        name = d.pop("name", UNSET)

        plan = d.pop("plan", UNSET)

        plan_version = d.pop("plan_version", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        total = d.pop("total", UNSET)

        type = d.pop("type", UNSET)

        unit = d.pop("unit", UNSET)

        project_usage = cls(
            facility=facility,
            name=name,
            plan=plan,
            plan_version=plan_version,
            price=price,
            quantity=quantity,
            total=total,
            type=type,
            unit=unit,
        )

        project_usage.additional_properties = d
        return project_usage

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
