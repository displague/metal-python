from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanSpecsFeatures")

@attr.s(auto_attribs=True)
class PlanSpecsFeatures:
    """
    Attributes:
        raid (Union[Unset, bool]):
        txt (Union[Unset, bool]):
        uefi (Union[Unset, bool]):
    """

    raid: Union[Unset, bool] = UNSET
    txt: Union[Unset, bool] = UNSET
    uefi: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        raid = self.raid
        txt = self.txt
        uefi = self.uefi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if raid is not UNSET:
            field_dict["raid"] = raid
        if txt is not UNSET:
            field_dict["txt"] = txt
        if uefi is not UNSET:
            field_dict["uefi"] = uefi

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raid = d.pop("raid", UNSET)

        txt = d.pop("txt", UNSET)

        uefi = d.pop("uefi", UNSET)

        plan_specs_features = cls(
            raid=raid,
            txt=txt,
            uefi=uefi,
        )

        plan_specs_features.additional_properties = d
        return plan_specs_features

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
