from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metadata_network_network_bonding import MetadataNetworkNetworkBonding




T = TypeVar("T", bound="MetadataNetworkNetwork")

@attr.s(auto_attribs=True)
class MetadataNetworkNetwork:
    """
    Attributes:
        bonding (Union[Unset, MetadataNetworkNetworkBonding]):
    """

    bonding: Union[Unset, 'MetadataNetworkNetworkBonding'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bonding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bonding, Unset):
            bonding = self.bonding.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bonding is not UNSET:
            field_dict["bonding"] = bonding

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_network_network_bonding import MetadataNetworkNetworkBonding
        d = src_dict.copy()
        _bonding = d.pop("bonding", UNSET)
        bonding: Union[Unset, MetadataNetworkNetworkBonding]
        if isinstance(_bonding,  Unset):
            bonding = UNSET
        else:
            bonding = MetadataNetworkNetworkBonding.from_dict(_bonding)




        metadata_network_network = cls(
            bonding=bonding,
        )

        metadata_network_network.additional_properties = d
        return metadata_network_network

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
