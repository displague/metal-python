from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plan_specs_drives_inner_category import PlanSpecsDrivesInnerCategory
from ..models.plan_specs_drives_inner_type import PlanSpecsDrivesInnerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanSpecsDrivesInner")

@attr.s(auto_attribs=True)
class PlanSpecsDrivesInner:
    """
    Attributes:
        count (Union[Unset, int]):
        type (Union[Unset, PlanSpecsDrivesInnerType]):
        size (Union[Unset, str]):  Example: 3.84TB.
        category (Union[Unset, PlanSpecsDrivesInnerCategory]):
    """

    count: Union[Unset, int] = UNSET
    type: Union[Unset, PlanSpecsDrivesInnerType] = UNSET
    size: Union[Unset, str] = UNSET
    category: Union[Unset, PlanSpecsDrivesInnerCategory] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        size = self.size
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if type is not UNSET:
            field_dict["type"] = type
        if size is not UNSET:
            field_dict["size"] = size
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PlanSpecsDrivesInnerType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = PlanSpecsDrivesInnerType(_type)




        size = d.pop("size", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PlanSpecsDrivesInnerCategory]
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = PlanSpecsDrivesInnerCategory(_category)




        plan_specs_drives_inner = cls(
            count=count,
            type=type,
            size=size,
            category=category,
        )

        plan_specs_drives_inner.additional_properties = d
        return plan_specs_drives_inner

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
