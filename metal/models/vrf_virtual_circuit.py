import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.vrf import Vrf




T = TypeVar("T", bound="VrfVirtualCircuit")

@attr.s(auto_attribs=True)
class VrfVirtualCircuit:
    """
    Attributes:
        customer_ip (Union[Unset, str]): An IP address from the subnet that will be used on the Customer side. This
            parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP.
            By default, the last usable IP address in the subnet will be used. Example: 12.0.0.2.
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        md5 (Union[Unset, str]): The MD5 password for the BGP peering in plaintext (not a checksum).
        metal_ip (Union[Unset, str]): An IP address from the subnet that will be used on the Metal side. This parameter
            is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By
            default, the first usable IP address in the subnet will be used. Example: 12.0.0.1.
        name (Union[Unset, str]):
        port (Union[Unset, Href]):
        nni_vlan (Union[Unset, int]):
        peer_asn (Union[Unset, int]): The peer ASN that will be used with the VRF on the Virtual Circuit.
        project (Union[Unset, Href]):
        speed (Union[Unset, int]): integer representing bps speed
        status (Union[Unset, str]):
        subnet (Union[Unset, str]): The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for
            the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF
            IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For
            /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. Example: 12.0.0.0/30.
        tags (Union[Unset, List[str]]):
        vrf (Union[Unset, Vrf]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    customer_ip: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    md5: Union[Unset, str] = UNSET
    metal_ip: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, 'Href'] = UNSET
    nni_vlan: Union[Unset, int] = UNSET
    peer_asn: Union[Unset, int] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    speed: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    subnet: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    vrf: Union[Unset, 'Vrf'] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        customer_ip = self.customer_ip
        description = self.description
        id = self.id
        md5 = self.md5
        metal_ip = self.metal_ip
        name = self.name
        port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        nni_vlan = self.nni_vlan
        peer_asn = self.peer_asn
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        speed = self.speed
        status = self.status
        subnet = self.subnet
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        vrf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vrf, Unset):
            vrf = self.vrf.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if customer_ip is not UNSET:
            field_dict["customer_ip"] = customer_ip
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if metal_ip is not UNSET:
            field_dict["metal_ip"] = metal_ip
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if nni_vlan is not UNSET:
            field_dict["nni_vlan"] = nni_vlan
        if peer_asn is not UNSET:
            field_dict["peer_asn"] = peer_asn
        if project is not UNSET:
            field_dict["project"] = project
        if speed is not UNSET:
            field_dict["speed"] = speed
        if status is not UNSET:
            field_dict["status"] = status
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.vrf import Vrf
        d = src_dict.copy()
        customer_ip = d.pop("customer_ip", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        md5 = d.pop("md5", UNSET)

        metal_ip = d.pop("metal_ip", UNSET)

        name = d.pop("name", UNSET)

        _port = d.pop("port", UNSET)
        port: Union[Unset, Href]
        if isinstance(_port,  Unset):
            port = UNSET
        else:
            port = Href.from_dict(_port)




        nni_vlan = d.pop("nni_vlan", UNSET)

        peer_asn = d.pop("peer_asn", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        speed = d.pop("speed", UNSET)

        status = d.pop("status", UNSET)

        subnet = d.pop("subnet", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        _vrf = d.pop("vrf", UNSET)
        vrf: Union[Unset, Vrf]
        if isinstance(_vrf,  Unset):
            vrf = UNSET
        else:
            vrf = Vrf.from_dict(_vrf)




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




        vrf_virtual_circuit = cls(
            customer_ip=customer_ip,
            description=description,
            id=id,
            md5=md5,
            metal_ip=metal_ip,
            name=name,
            port=port,
            nni_vlan=nni_vlan,
            peer_asn=peer_asn,
            project=project,
            speed=speed,
            status=status,
            subnet=subnet,
            tags=tags,
            vrf=vrf,
            created_at=created_at,
            updated_at=updated_at,
        )

        vrf_virtual_circuit.additional_properties = d
        return vrf_virtual_circuit

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
