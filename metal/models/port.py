from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.port_network_type import PortNetworkType
from ..models.port_type import PortType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bond_port_data import BondPortData
  from ..models.href import Href
  from ..models.port_data import PortData
  from ..models.virtual_network import VirtualNetwork




T = TypeVar("T", bound="Port")

@attr.s(auto_attribs=True)
class Port:
    """Port is a hardware port associated with a reserved or instantiated hardware device.

    Attributes:
        bond (Union[Unset, BondPortData]):
        data (Union[Unset, PortData]):
        disbond_operation_supported (Union[Unset, bool]): Indicates whether or not the bond can be broken on the port
            (when applicable).
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):  Example: bond0.
        type (Union[Unset, PortType]): Type is either "NetworkBondPort" for bond ports or "NetworkPort" for bondable
            ethernet ports
        network_type (Union[Unset, PortNetworkType]): Composite network type of the bond
        native_virtual_network (Union[Unset, VirtualNetwork]):
        virtual_networks (Union[Unset, List['Href']]):
    """

    bond: Union[Unset, 'BondPortData'] = UNSET
    data: Union[Unset, 'PortData'] = UNSET
    disbond_operation_supported: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, PortType] = UNSET
    network_type: Union[Unset, PortNetworkType] = UNSET
    native_virtual_network: Union[Unset, 'VirtualNetwork'] = UNSET
    virtual_networks: Union[Unset, List['Href']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bond: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bond, Unset):
            bond = self.bond.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        disbond_operation_supported = self.disbond_operation_supported
        href = self.href
        id = self.id
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        network_type: Union[Unset, str] = UNSET
        if not isinstance(self.network_type, Unset):
            network_type = self.network_type.value

        native_virtual_network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.native_virtual_network, Unset):
            native_virtual_network = self.native_virtual_network.to_dict()

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
        if bond is not UNSET:
            field_dict["bond"] = bond
        if data is not UNSET:
            field_dict["data"] = data
        if disbond_operation_supported is not UNSET:
            field_dict["disbond_operation_supported"] = disbond_operation_supported
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if network_type is not UNSET:
            field_dict["network_type"] = network_type
        if native_virtual_network is not UNSET:
            field_dict["native_virtual_network"] = native_virtual_network
        if virtual_networks is not UNSET:
            field_dict["virtual_networks"] = virtual_networks

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bond_port_data import BondPortData
        from ..models.href import Href
        from ..models.port_data import PortData
        from ..models.virtual_network import VirtualNetwork
        d = src_dict.copy()
        _bond = d.pop("bond", UNSET)
        bond: Union[Unset, BondPortData]
        if isinstance(_bond,  Unset):
            bond = UNSET
        else:
            bond = BondPortData.from_dict(_bond)




        _data = d.pop("data", UNSET)
        data: Union[Unset, PortData]
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = PortData.from_dict(_data)




        disbond_operation_supported = d.pop("disbond_operation_supported", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PortType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = PortType(_type)




        _network_type = d.pop("network_type", UNSET)
        network_type: Union[Unset, PortNetworkType]
        if isinstance(_network_type,  Unset):
            network_type = UNSET
        else:
            network_type = PortNetworkType(_network_type)




        _native_virtual_network = d.pop("native_virtual_network", UNSET)
        native_virtual_network: Union[Unset, VirtualNetwork]
        if isinstance(_native_virtual_network,  Unset):
            native_virtual_network = UNSET
        else:
            native_virtual_network = VirtualNetwork.from_dict(_native_virtual_network)




        virtual_networks = []
        _virtual_networks = d.pop("virtual_networks", UNSET)
        for virtual_networks_item_data in (_virtual_networks or []):
            virtual_networks_item = Href.from_dict(virtual_networks_item_data)



            virtual_networks.append(virtual_networks_item)


        port = cls(
            bond=bond,
            data=data,
            disbond_operation_supported=disbond_operation_supported,
            href=href,
            id=id,
            name=name,
            type=type,
            network_type=network_type,
            native_virtual_network=native_virtual_network,
            virtual_networks=virtual_networks,
        )

        port.additional_properties = d
        return port

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
