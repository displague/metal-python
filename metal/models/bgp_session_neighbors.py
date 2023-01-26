from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bgp_neighbor_data import BgpNeighborData




T = TypeVar("T", bound="BgpSessionNeighbors")

@attr.s(auto_attribs=True)
class BgpSessionNeighbors:
    """
    Attributes:
        bgp_neighbors (Union[Unset, List['BgpNeighborData']]): A list of BGP session neighbor data
    """

    bgp_neighbors: Union[Unset, List['BgpNeighborData']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bgp_neighbors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_neighbors, Unset):
            bgp_neighbors = []
            for bgp_neighbors_item_data in self.bgp_neighbors:
                bgp_neighbors_item = bgp_neighbors_item_data.to_dict()

                bgp_neighbors.append(bgp_neighbors_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bgp_neighbors is not UNSET:
            field_dict["bgp_neighbors"] = bgp_neighbors

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bgp_neighbor_data import BgpNeighborData
        d = src_dict.copy()
        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgp_neighbors", UNSET)
        for bgp_neighbors_item_data in (_bgp_neighbors or []):
            bgp_neighbors_item = BgpNeighborData.from_dict(bgp_neighbors_item_data)



            bgp_neighbors.append(bgp_neighbors_item)


        bgp_session_neighbors = cls(
            bgp_neighbors=bgp_neighbors,
        )

        bgp_session_neighbors.additional_properties = d
        return bgp_session_neighbors

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
