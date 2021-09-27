from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plan_specs_nics_inner_type import PlanSpecsNicsInnerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanSpecsNicsInner")

@attr.s(auto_attribs=True)
class PlanSpecsNicsInner:
    """
    Attributes:
        count (Union[Unset, int]):  Example: 2.
        type (Union[Unset, PlanSpecsNicsInnerType]):
    """

    count: Union[Unset, int] = UNSET
    type: Union[Unset, PlanSpecsNicsInnerType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PlanSpecsNicsInnerType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = PlanSpecsNicsInnerType(_type)




        plan_specs_nics_inner = cls(
            count=count,
            type=type,
        )

        plan_specs_nics_inner.additional_properties = d
        return plan_specs_nics_inner

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
