from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.vrf import Vrf




T = TypeVar("T", bound="VrfList")

@attr.s(auto_attribs=True)
class VrfList:
    """
    Attributes:
        vrfs (Union[Unset, List['Vrf']]):
    """

    vrfs: Union[Unset, List['Vrf']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        vrfs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vrfs, Unset):
            vrfs = []
            for vrfs_item_data in self.vrfs:
                vrfs_item = vrfs_item_data.to_dict()

                vrfs.append(vrfs_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vrfs is not UNSET:
            field_dict["vrfs"] = vrfs

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vrf import Vrf
        d = src_dict.copy()
        vrfs = []
        _vrfs = d.pop("vrfs", UNSET)
        for vrfs_item_data in (_vrfs or []):
            vrfs_item = Vrf.from_dict(vrfs_item_data)



            vrfs.append(vrfs_item)


        vrf_list = cls(
            vrfs=vrfs,
        )

        vrf_list.additional_properties = d
        return vrf_list

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
