from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.metal_gateway_lite import MetalGatewayLite




T = TypeVar("T", bound="VirtualNetwork")

@attr.s(auto_attribs=True)
class VirtualNetwork:
    """
    Attributes:
        assigned_to (Union[Unset, Href]):
        assigned_to_virtual_circuit (Union[Unset, bool]): True if the virtual network is attached to a virtual circuit.
            False if not.
        description (Union[Unset, str]):
        facility (Union[Unset, Href]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        instances (Union[Unset, List['Href']]): A list of instances with ports currently associated to this Virtual
            Network.
        metal_gateways (Union[Unset, List['MetalGatewayLite']]): A list of metal gateways currently associated to this
            Virtual Network.
        metro (Union[Unset, Href]):
        metro_code (Union[Unset, str]): The Metro code of the metro in which this Virtual Network is defined.
        vxlan (Union[Unset, int]):
    """

    assigned_to: Union[Unset, 'Href'] = UNSET
    assigned_to_virtual_circuit: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    facility: Union[Unset, 'Href'] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    instances: Union[Unset, List['Href']] = UNSET
    metal_gateways: Union[Unset, List['MetalGatewayLite']] = UNSET
    metro: Union[Unset, 'Href'] = UNSET
    metro_code: Union[Unset, str] = UNSET
    vxlan: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        assigned_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict()

        assigned_to_virtual_circuit = self.assigned_to_virtual_circuit
        description = self.description
        facility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facility, Unset):
            facility = self.facility.to_dict()

        href = self.href
        id = self.id
        instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()

                instances.append(instances_item)




        metal_gateways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metal_gateways, Unset):
            metal_gateways = []
            for metal_gateways_item_data in self.metal_gateways:
                metal_gateways_item = metal_gateways_item_data.to_dict()

                metal_gateways.append(metal_gateways_item)




        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        metro_code = self.metro_code
        vxlan = self.vxlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if assigned_to_virtual_circuit is not UNSET:
            field_dict["assigned_to_virtual_circuit"] = assigned_to_virtual_circuit
        if description is not UNSET:
            field_dict["description"] = description
        if facility is not UNSET:
            field_dict["facility"] = facility
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if instances is not UNSET:
            field_dict["instances"] = instances
        if metal_gateways is not UNSET:
            field_dict["metal_gateways"] = metal_gateways
        if metro is not UNSET:
            field_dict["metro"] = metro
        if metro_code is not UNSET:
            field_dict["metro_code"] = metro_code
        if vxlan is not UNSET:
            field_dict["vxlan"] = vxlan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.metal_gateway_lite import MetalGatewayLite
        d = src_dict.copy()
        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Union[Unset, Href]
        if isinstance(_assigned_to,  Unset):
            assigned_to = UNSET
        else:
            assigned_to = Href.from_dict(_assigned_to)




        assigned_to_virtual_circuit = d.pop("assigned_to_virtual_circuit", UNSET)

        description = d.pop("description", UNSET)

        _facility = d.pop("facility", UNSET)
        facility: Union[Unset, Href]
        if isinstance(_facility,  Unset):
            facility = UNSET
        else:
            facility = Href.from_dict(_facility)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in (_instances or []):
            instances_item = Href.from_dict(instances_item_data)



            instances.append(instances_item)


        metal_gateways = []
        _metal_gateways = d.pop("metal_gateways", UNSET)
        for metal_gateways_item_data in (_metal_gateways or []):
            metal_gateways_item = MetalGatewayLite.from_dict(metal_gateways_item_data)



            metal_gateways.append(metal_gateways_item)


        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, Href]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = Href.from_dict(_metro)




        metro_code = d.pop("metro_code", UNSET)

        vxlan = d.pop("vxlan", UNSET)

        virtual_network = cls(
            assigned_to=assigned_to,
            assigned_to_virtual_circuit=assigned_to_virtual_circuit,
            description=description,
            facility=facility,
            href=href,
            id=id,
            instances=instances,
            metal_gateways=metal_gateways,
            metro=metro,
            metro_code=metro_code,
            vxlan=vxlan,
        )

        virtual_network.additional_properties = d
        return virtual_network

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
