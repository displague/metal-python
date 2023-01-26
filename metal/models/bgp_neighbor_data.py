from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bgp_route import BgpRoute




T = TypeVar("T", bound="BgpNeighborData")

@attr.s(auto_attribs=True)
class BgpNeighborData:
    """
    Attributes:
        address_family (Union[Unset, float]): Address Family for IP Address. Accepted values are 4 or 6 Example: 4.
        customer_as (Union[Unset, float]): The customer's ASN. In a local BGP deployment, this will be an internal ASN
            used to route within the data center. For a global BGP deployment, this will be the your own ASN, configured
            when you set up BGP for your project. Example: 65000.
        customer_ip (Union[Unset, str]): The device's IP address. For an IPv4 BGP session, this is typically the private
            bond0 address for the device. Example: 10.32.16.1 (IPv4) or 2604:1380:4111:2700::1 (IPv6).
        md5_enabled (Union[Unset, bool]): True if an MD5 password is configured for the project.
        md5_password (Union[Unset, str]): The MD5 password configured for the project, if set.
        multihop (Union[Unset, bool]): True when the BGP session should be configured as multihop.
        peer_as (Union[Unset, float]): The Peer ASN to use when configuring BGP on your device. Example: 65530.
        peer_ips (Union[Unset, List[str]]): A list of one or more IP addresses to use for the Peer IP section of your
            BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device.
            For multihop sessions, it will be a list of IPs. Example: ['169.254.255.1', '169.254.255.2'].
        routes_in (Union[Unset, List['BgpRoute']]): A list of project subnets Example: [{'exact': True, 'route':
            '10.32.16.0/31'}].
        routes_out (Union[Unset, List['BgpRoute']]): A list of outgoing routes. Only populated if the BGP session has
            default route enabled. Example: [{'exact': True, 'route': '0.0.0.0/0'}].
    """

    address_family: Union[Unset, float] = UNSET
    customer_as: Union[Unset, float] = UNSET
    customer_ip: Union[Unset, str] = UNSET
    md5_enabled: Union[Unset, bool] = UNSET
    md5_password: Union[Unset, str] = UNSET
    multihop: Union[Unset, bool] = UNSET
    peer_as: Union[Unset, float] = UNSET
    peer_ips: Union[Unset, List[str]] = UNSET
    routes_in: Union[Unset, List['BgpRoute']] = UNSET
    routes_out: Union[Unset, List['BgpRoute']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family = self.address_family
        customer_as = self.customer_as
        customer_ip = self.customer_ip
        md5_enabled = self.md5_enabled
        md5_password = self.md5_password
        multihop = self.multihop
        peer_as = self.peer_as
        peer_ips: Union[Unset, List[str]] = UNSET
        if not isinstance(self.peer_ips, Unset):
            peer_ips = self.peer_ips




        routes_in: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.routes_in, Unset):
            routes_in = []
            for routes_in_item_data in self.routes_in:
                routes_in_item = routes_in_item_data.to_dict()

                routes_in.append(routes_in_item)




        routes_out: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.routes_out, Unset):
            routes_out = []
            for routes_out_item_data in self.routes_out:
                routes_out_item = routes_out_item_data.to_dict()

                routes_out.append(routes_out_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if customer_as is not UNSET:
            field_dict["customer_as"] = customer_as
        if customer_ip is not UNSET:
            field_dict["customer_ip"] = customer_ip
        if md5_enabled is not UNSET:
            field_dict["md5_enabled"] = md5_enabled
        if md5_password is not UNSET:
            field_dict["md5_password"] = md5_password
        if multihop is not UNSET:
            field_dict["multihop"] = multihop
        if peer_as is not UNSET:
            field_dict["peer_as"] = peer_as
        if peer_ips is not UNSET:
            field_dict["peer_ips"] = peer_ips
        if routes_in is not UNSET:
            field_dict["routes_in"] = routes_in
        if routes_out is not UNSET:
            field_dict["routes_out"] = routes_out

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bgp_route import BgpRoute
        d = src_dict.copy()
        address_family = d.pop("address_family", UNSET)

        customer_as = d.pop("customer_as", UNSET)

        customer_ip = d.pop("customer_ip", UNSET)

        md5_enabled = d.pop("md5_enabled", UNSET)

        md5_password = d.pop("md5_password", UNSET)

        multihop = d.pop("multihop", UNSET)

        peer_as = d.pop("peer_as", UNSET)

        peer_ips = cast(List[str], d.pop("peer_ips", UNSET))


        routes_in = []
        _routes_in = d.pop("routes_in", UNSET)
        for routes_in_item_data in (_routes_in or []):
            routes_in_item = BgpRoute.from_dict(routes_in_item_data)



            routes_in.append(routes_in_item)


        routes_out = []
        _routes_out = d.pop("routes_out", UNSET)
        for routes_out_item_data in (_routes_out or []):
            routes_out_item = BgpRoute.from_dict(routes_out_item_data)



            routes_out.append(routes_out_item)


        bgp_neighbor_data = cls(
            address_family=address_family,
            customer_as=customer_as,
            customer_ip=customer_ip,
            md5_enabled=md5_enabled,
            md5_password=md5_password,
            multihop=multihop,
            peer_as=peer_as,
            peer_ips=peer_ips,
            routes_in=routes_in,
            routes_out=routes_out,
        )

        bgp_neighbor_data.additional_properties = d
        return bgp_neighbor_data

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
