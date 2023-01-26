from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.virtual_network import VirtualNetwork




T = TypeVar("T", bound="VirtualNetworkList")

@attr.s(auto_attribs=True)
class VirtualNetworkList:
    """
    Attributes:
        virtual_networks (Union[Unset, List['VirtualNetwork']]):
    """

    virtual_networks: Union[Unset, List['VirtualNetwork']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        virtual_networks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.virtual_networks, Unset):
            virtual_networks = []
            for virtual_networks_item_data in self.virtual_networks:
                virtual_networks_item = virtual_networks_item_data.to_dict()

                virtual_networks.append(virtual_networks_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if virtual_networks is not UNSET:
            field_dict["virtual_networks"] = virtual_networks

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.virtual_network import VirtualNetwork
        d = src_dict.copy()
        virtual_networks = []
        _virtual_networks = d.pop("virtual_networks", UNSET)
        for virtual_networks_item_data in (_virtual_networks or []):
            virtual_networks_item = VirtualNetwork.from_dict(virtual_networks_item_data)



            virtual_networks.append(virtual_networks_item)


        virtual_network_list = cls(
            virtual_networks=virtual_networks,
        )

        virtual_network_list.additional_properties = d
        return virtual_network_list

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
