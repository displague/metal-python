from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metadata_network_interfaces_item import MetadataNetworkInterfacesItem
  from ..models.metadata_network_network import MetadataNetworkNetwork




T = TypeVar("T", bound="MetadataNetwork")

@attr.s(auto_attribs=True)
class MetadataNetwork:
    """
    Attributes:
        addresses (Union[Unset, List[str]]):
        interfaces (Union[Unset, List['MetadataNetworkInterfacesItem']]):
        network (Union[Unset, MetadataNetworkNetwork]):
    """

    addresses: Union[Unset, List[str]] = UNSET
    interfaces: Union[Unset, List['MetadataNetworkInterfacesItem']] = UNSET
    network: Union[Unset, 'MetadataNetworkNetwork'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses




        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()

                interfaces.append(interfaces_item)




        network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_network_interfaces_item import MetadataNetworkInterfacesItem
        from ..models.metadata_network_network import MetadataNetworkNetwork
        d = src_dict.copy()
        addresses = cast(List[str], d.pop("addresses", UNSET))


        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in (_interfaces or []):
            interfaces_item = MetadataNetworkInterfacesItem.from_dict(interfaces_item_data)



            interfaces.append(interfaces_item)


        _network = d.pop("network", UNSET)
        network: Union[Unset, MetadataNetworkNetwork]
        if isinstance(_network,  Unset):
            network = UNSET
        else:
            network = MetadataNetworkNetwork.from_dict(_network)




        metadata_network = cls(
            addresses=addresses,
            interfaces=interfaces,
            network=network,
        )

        metadata_network.additional_properties = d
        return metadata_network

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
