from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.global_bgp_range import GlobalBgpRange




T = TypeVar("T", bound="GlobalBgpRangeList")

@attr.s(auto_attribs=True)
class GlobalBgpRangeList:
    """
    Attributes:
        global_bgp_ranges (Union[Unset, List['GlobalBgpRange']]):
    """

    global_bgp_ranges: Union[Unset, List['GlobalBgpRange']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        global_bgp_ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.global_bgp_ranges, Unset):
            global_bgp_ranges = []
            for global_bgp_ranges_item_data in self.global_bgp_ranges:
                global_bgp_ranges_item = global_bgp_ranges_item_data.to_dict()

                global_bgp_ranges.append(global_bgp_ranges_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if global_bgp_ranges is not UNSET:
            field_dict["global_bgp_ranges"] = global_bgp_ranges

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.global_bgp_range import GlobalBgpRange
        d = src_dict.copy()
        global_bgp_ranges = []
        _global_bgp_ranges = d.pop("global_bgp_ranges", UNSET)
        for global_bgp_ranges_item_data in (_global_bgp_ranges or []):
            global_bgp_ranges_item = GlobalBgpRange.from_dict(global_bgp_ranges_item_data)



            global_bgp_ranges.append(global_bgp_ranges_item)


        global_bgp_range_list = cls(
            global_bgp_ranges=global_bgp_ranges,
        )

        global_bgp_range_list.additional_properties = d
        return global_bgp_range_list

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
