from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.capacity_report import CapacityReport




T = TypeVar("T", bound="CapacityList")

@attr.s(auto_attribs=True)
class CapacityList:
    """
    Attributes:
        capacity (Union[Unset, CapacityReport]):
    """

    capacity: Union[Unset, 'CapacityReport'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        capacity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capacity_report import CapacityReport
        d = src_dict.copy()
        _capacity = d.pop("capacity", UNSET)
        capacity: Union[Unset, CapacityReport]
        if isinstance(_capacity,  Unset):
            capacity = UNSET
        else:
            capacity = CapacityReport.from_dict(_capacity)




        capacity_list = cls(
            capacity=capacity,
        )

        capacity_list.additional_properties = d
        return capacity_list

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
