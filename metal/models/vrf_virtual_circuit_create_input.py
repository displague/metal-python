from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VrfVirtualCircuitCreateInput")

@attr.s(auto_attribs=True)
class VrfVirtualCircuitCreateInput:
    """
    Attributes:
        nni_vlan (int):
        peer_asn (int): The peer ASN that will be used with the VRF on the Virtual Circuit.
        project_id (str):
        subnet (str): The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual
            Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP
            reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30
            subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. The subnet specified must be
            contained within an already-defined IP Range for the VRF. Example: 12.0.0.0/30.
        vrf (str): The UUID of the VRF that will be associated with the Virtual Circuit.
        customer_ip (Union[Unset, str]): An IP address from the subnet that will be used on the Customer side. This
            parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP.
            By default, the last usable IP address in the subnet will be used. Example: 12.0.0.2.
        description (Union[Unset, str]):
        md5 (Union[Unset, None, str]): The MD5 password for the BGP peering in plaintext (not a checksum).
        metal_ip (Union[Unset, str]): An IP address from the subnet that will be used on the Metal side. This parameter
            is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By
            default, the first usable IP address in the subnet will be used. Example: 12.0.0.1.
        name (Union[Unset, str]):
        speed (Union[Unset, int]): speed can be passed as integer number representing bps speed or string (e.g. '52m' or
            '100g' or '4 gbps')
        tags (Union[Unset, List[str]]):
    """

    nni_vlan: int
    peer_asn: int
    project_id: str
    subnet: str
    vrf: str
    customer_ip: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    md5: Union[Unset, None, str] = UNSET
    metal_ip: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    speed: Union[Unset, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        nni_vlan = self.nni_vlan
        peer_asn = self.peer_asn
        project_id = self.project_id
        subnet = self.subnet
        vrf = self.vrf
        customer_ip = self.customer_ip
        description = self.description
        md5 = self.md5
        metal_ip = self.metal_ip
        name = self.name
        speed = self.speed
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nni_vlan": nni_vlan,
            "peer_asn": peer_asn,
            "project_id": project_id,
            "subnet": subnet,
            "vrf": vrf,
        })
        if customer_ip is not UNSET:
            field_dict["customer_ip"] = customer_ip
        if description is not UNSET:
            field_dict["description"] = description
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if metal_ip is not UNSET:
            field_dict["metal_ip"] = metal_ip
        if name is not UNSET:
            field_dict["name"] = name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nni_vlan = d.pop("nni_vlan")

        peer_asn = d.pop("peer_asn")

        project_id = d.pop("project_id")

        subnet = d.pop("subnet")

        vrf = d.pop("vrf")

        customer_ip = d.pop("customer_ip", UNSET)

        description = d.pop("description", UNSET)

        md5 = d.pop("md5", UNSET)

        metal_ip = d.pop("metal_ip", UNSET)

        name = d.pop("name", UNSET)

        speed = d.pop("speed", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        vrf_virtual_circuit_create_input = cls(
            nni_vlan=nni_vlan,
            peer_asn=peer_asn,
            project_id=project_id,
            subnet=subnet,
            vrf=vrf,
            customer_ip=customer_ip,
            description=description,
            md5=md5,
            metal_ip=metal_ip,
            name=name,
            speed=speed,
            tags=tags,
        )

        vrf_virtual_circuit_create_input.additional_properties = d
        return vrf_virtual_circuit_create_input

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
