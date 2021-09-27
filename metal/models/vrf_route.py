import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.vrf_route_status import VrfRouteStatus
from ..models.vrf_route_type import VrfRouteType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.metal_gateway import MetalGateway
  from ..models.virtual_network import VirtualNetwork
  from ..models.vrf import Vrf




T = TypeVar("T", bound="VrfRoute")

@attr.s(auto_attribs=True)
class VrfRoute:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier for the newly-created resource Example:
            e1ff9c2b-051a-4688-965f-153e274f77e0.
        status (Union[Unset, VrfRouteStatus]): The status of the route. Potential values are "pending", "active",
            "deleting", and "error", representing various lifecycle states of the route and whether or not it has been
            successfully configured on the network Example: active.
        prefix (Union[Unset, str]): The IPv4 prefix for the route, in CIDR-style notation Example: 0.0.0.0/0.
        next_hop (Union[Unset, str]): The next-hop IPv4 address for the route Example: 192.168.1.254.
        type (Union[Unset, VrfRouteType]): VRF route type, like 'bgp', 'connected', and 'static'. Currently, only static
            routes are supported Example: static.
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        metal_gateway (Union['Href', 'MetalGateway', Unset]): A link to the Metal Gateway to which this VRF Route is
            associated
        virtual_network (Union['Href', 'VirtualNetwork', Unset]): A link to the Virtual Network to which this VRF Route
            is associated, through the Metal Gateway
        vrf (Union['Href', 'Vrf', Unset]): A link to the VRF within which this route exists
        href (Union[Unset, str]):  Example: /routes/e1ff9c2b-051a-4688-965f-153e274f77e0.
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, VrfRouteStatus] = UNSET
    prefix: Union[Unset, str] = UNSET
    next_hop: Union[Unset, str] = UNSET
    type: Union[Unset, VrfRouteType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    metal_gateway: Union['Href', 'MetalGateway', Unset] = UNSET
    virtual_network: Union['Href', 'VirtualNetwork', Unset] = UNSET
    vrf: Union['Href', 'Vrf', Unset] = UNSET
    href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.href import Href
        id = self.id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        prefix = self.prefix
        next_hop = self.next_hop
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        metal_gateway: Union[Dict[str, Any], Unset]
        if isinstance(self.metal_gateway, Unset):
            metal_gateway = UNSET

        elif isinstance(self.metal_gateway, Href):
            metal_gateway = self.metal_gateway.to_dict()

        else:
            metal_gateway = self.metal_gateway.to_dict()



        virtual_network: Union[Dict[str, Any], Unset]
        if isinstance(self.virtual_network, Unset):
            virtual_network = UNSET

        elif isinstance(self.virtual_network, Href):
            virtual_network = self.virtual_network.to_dict()

        else:
            virtual_network = self.virtual_network.to_dict()



        vrf: Union[Dict[str, Any], Unset]
        if isinstance(self.vrf, Unset):
            vrf = UNSET

        elif isinstance(self.vrf, Href):
            vrf = self.vrf.to_dict()

        else:
            vrf = self.vrf.to_dict()



        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if next_hop is not UNSET:
            field_dict["next_hop"] = next_hop
        if type is not UNSET:
            field_dict["type"] = type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if metal_gateway is not UNSET:
            field_dict["metal_gateway"] = metal_gateway
        if virtual_network is not UNSET:
            field_dict["virtual_network"] = virtual_network
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.metal_gateway import MetalGateway
        from ..models.virtual_network import VirtualNetwork
        from ..models.vrf import Vrf
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, VrfRouteStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = VrfRouteStatus(_status)




        prefix = d.pop("prefix", UNSET)

        next_hop = d.pop("next_hop", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, VrfRouteType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = VrfRouteType(_type)




        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        def _parse_metal_gateway(data: object) -> Union['Href', 'MetalGateway', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vrf_route_metal_gateway_type_0 = Href.from_dict(data)



                return componentsschemas_vrf_route_metal_gateway_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_vrf_route_metal_gateway_type_1 = MetalGateway.from_dict(data)



            return componentsschemas_vrf_route_metal_gateway_type_1

        metal_gateway = _parse_metal_gateway(d.pop("metal_gateway", UNSET))


        def _parse_virtual_network(data: object) -> Union['Href', 'VirtualNetwork', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vrf_route_virtual_network_type_0 = Href.from_dict(data)



                return componentsschemas_vrf_route_virtual_network_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_vrf_route_virtual_network_type_1 = VirtualNetwork.from_dict(data)



            return componentsschemas_vrf_route_virtual_network_type_1

        virtual_network = _parse_virtual_network(d.pop("virtual_network", UNSET))


        def _parse_vrf(data: object) -> Union['Href', 'Vrf', Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_vrf_route_vrf_type_0 = Href.from_dict(data)



                return componentsschemas_vrf_route_vrf_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_vrf_route_vrf_type_1 = Vrf.from_dict(data)



            return componentsschemas_vrf_route_vrf_type_1

        vrf = _parse_vrf(d.pop("vrf", UNSET))


        href = d.pop("href", UNSET)

        vrf_route = cls(
            id=id,
            status=status,
            prefix=prefix,
            next_hop=next_hop,
            type=type,
            created_at=created_at,
            updated_at=updated_at,
            metal_gateway=metal_gateway,
            virtual_network=virtual_network,
            vrf=vrf,
            href=href,
        )

        vrf_route.additional_properties = d
        return vrf_route

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
