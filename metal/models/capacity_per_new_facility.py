from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.capacity_level_per_baremetal import CapacityLevelPerBaremetal




T = TypeVar("T", bound="CapacityPerNewFacility")

@attr.s(auto_attribs=True)
class CapacityPerNewFacility:
    """
    Attributes:
        baremetal_1e (Union[Unset, CapacityLevelPerBaremetal]):
    """

    baremetal_1e: Union[Unset, 'CapacityLevelPerBaremetal'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        baremetal_1e: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_1e, Unset):
            baremetal_1e = self.baremetal_1e.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if baremetal_1e is not UNSET:
            field_dict["baremetal_1e"] = baremetal_1e

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capacity_level_per_baremetal import CapacityLevelPerBaremetal
        d = src_dict.copy()
        _baremetal_1e = d.pop("baremetal_1e", UNSET)
        baremetal_1e: Union[Unset, CapacityLevelPerBaremetal]
        if isinstance(_baremetal_1e,  Unset):
            baremetal_1e = UNSET
        else:
            baremetal_1e = CapacityLevelPerBaremetal.from_dict(_baremetal_1e)




        capacity_per_new_facility = cls(
            baremetal_1e=baremetal_1e,
        )

        capacity_per_new_facility.additional_properties = d
        return capacity_per_new_facility

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
