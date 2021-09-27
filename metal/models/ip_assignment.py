import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.ip_assignment_metro import IPAssignmentMetro
  from ..models.parent_block import ParentBlock




T = TypeVar("T", bound="IPAssignment")

@attr.s(auto_attribs=True)
class IPAssignment:
    """
    Attributes:
        address (Union[Unset, str]):
        address_family (Union[Unset, int]):
        assigned_to (Union[Unset, Href]):
        cidr (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, bool]):
        gateway (Union[Unset, str]):
        global_ip (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        manageable (Union[Unset, bool]):
        management (Union[Unset, bool]):
        metro (Union[Unset, IPAssignmentMetro]):
        netmask (Union[Unset, str]):
        network (Union[Unset, str]):
        parent_block (Union[Unset, ParentBlock]):
        public (Union[Unset, bool]):
    """

    address: Union[Unset, str] = UNSET
    address_family: Union[Unset, int] = UNSET
    assigned_to: Union[Unset, 'Href'] = UNSET
    cidr: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    enabled: Union[Unset, bool] = UNSET
    gateway: Union[Unset, str] = UNSET
    global_ip: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    manageable: Union[Unset, bool] = UNSET
    management: Union[Unset, bool] = UNSET
    metro: Union[Unset, 'IPAssignmentMetro'] = UNSET
    netmask: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    parent_block: Union[Unset, 'ParentBlock'] = UNSET
    public: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        address_family = self.address_family
        assigned_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to, Unset):
            assigned_to = self.assigned_to.to_dict()

        cidr = self.cidr
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        enabled = self.enabled
        gateway = self.gateway
        global_ip = self.global_ip
        href = self.href
        id = self.id
        manageable = self.manageable
        management = self.management
        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        netmask = self.netmask
        network = self.network
        parent_block: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_block, Unset):
            parent_block = self.parent_block.to_dict()

        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if assigned_to is not UNSET:
            field_dict["assigned_to"] = assigned_to
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if global_ip is not UNSET:
            field_dict["global_ip"] = global_ip
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if manageable is not UNSET:
            field_dict["manageable"] = manageable
        if management is not UNSET:
            field_dict["management"] = management
        if metro is not UNSET:
            field_dict["metro"] = metro
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if network is not UNSET:
            field_dict["network"] = network
        if parent_block is not UNSET:
            field_dict["parent_block"] = parent_block
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.ip_assignment_metro import IPAssignmentMetro
        from ..models.parent_block import ParentBlock
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        address_family = d.pop("address_family", UNSET)

        _assigned_to = d.pop("assigned_to", UNSET)
        assigned_to: Union[Unset, Href]
        if isinstance(_assigned_to,  Unset):
            assigned_to = UNSET
        else:
            assigned_to = Href.from_dict(_assigned_to)




        cidr = d.pop("cidr", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        enabled = d.pop("enabled", UNSET)

        gateway = d.pop("gateway", UNSET)

        global_ip = d.pop("global_ip", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        manageable = d.pop("manageable", UNSET)

        management = d.pop("management", UNSET)

        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, IPAssignmentMetro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = IPAssignmentMetro.from_dict(_metro)




        netmask = d.pop("netmask", UNSET)

        network = d.pop("network", UNSET)

        _parent_block = d.pop("parent_block", UNSET)
        parent_block: Union[Unset, ParentBlock]
        if isinstance(_parent_block,  Unset):
            parent_block = UNSET
        else:
            parent_block = ParentBlock.from_dict(_parent_block)




        public = d.pop("public", UNSET)

        ip_assignment = cls(
            address=address,
            address_family=address_family,
            assigned_to=assigned_to,
            cidr=cidr,
            created_at=created_at,
            enabled=enabled,
            gateway=gateway,
            global_ip=global_ip,
            href=href,
            id=id,
            manageable=manageable,
            management=management,
            metro=metro,
            netmask=netmask,
            network=network,
            parent_block=parent_block,
            public=public,
        )

        ip_assignment.additional_properties = d
        return ip_assignment

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
