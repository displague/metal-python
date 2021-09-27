import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.vrf_ip_reservation_type import VrfIpReservationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.metal_gateway_lite import MetalGatewayLite
  from ..models.metro import Metro
  from ..models.project import Project
  from ..models.vrf import Vrf
  from ..models.vrf_ip_reservation_customdata import VrfIpReservationCustomdata




T = TypeVar("T", bound="VrfIpReservation")

@attr.s(auto_attribs=True)
class VrfIpReservation:
    """
    Attributes:
        type (VrfIpReservationType):
        vrf (Vrf):
        address_family (Union[Unset, int]):
        cidr (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, Href]):
        details (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        metal_gateway (Union[Unset, MetalGatewayLite]):
        netmask (Union[Unset, str]):
        network (Union[Unset, str]):
        project (Union[Unset, Project]):
        state (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        public (Union[Unset, bool]):
        management (Union[Unset, bool]):
        manageable (Union[Unset, bool]):
        customdata (Union[Unset, VrfIpReservationCustomdata]):
        bill (Union[Unset, bool]):
        project_lite (Union[Unset, Project]):
        address (Union[Unset, str]):
        gateway (Union[Unset, str]):
        metro (Union[Unset, Metro]):
    """

    type: VrfIpReservationType
    vrf: 'Vrf'
    address_family: Union[Unset, int] = UNSET
    cidr: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, 'Href'] = UNSET
    details: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    metal_gateway: Union[Unset, 'MetalGatewayLite'] = UNSET
    netmask: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    project: Union[Unset, 'Project'] = UNSET
    state: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    public: Union[Unset, bool] = UNSET
    management: Union[Unset, bool] = UNSET
    manageable: Union[Unset, bool] = UNSET
    customdata: Union[Unset, 'VrfIpReservationCustomdata'] = UNSET
    bill: Union[Unset, bool] = UNSET
    project_lite: Union[Unset, 'Project'] = UNSET
    address: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    metro: Union[Unset, 'Metro'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        vrf = self.vrf.to_dict()

        address_family = self.address_family
        cidr = self.cidr
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        details = self.details
        href = self.href
        id = self.id
        metal_gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metal_gateway, Unset):
            metal_gateway = self.metal_gateway.to_dict()

        netmask = self.netmask
        network = self.network
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        state = self.state
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        public = self.public
        management = self.management
        manageable = self.manageable
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        bill = self.bill
        project_lite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_lite, Unset):
            project_lite = self.project_lite.to_dict()

        address = self.address
        gateway = self.gateway
        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
            "vrf": vrf,
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if details is not UNSET:
            field_dict["details"] = details
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if metal_gateway is not UNSET:
            field_dict["metal_gateway"] = metal_gateway
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if network is not UNSET:
            field_dict["network"] = network
        if project is not UNSET:
            field_dict["project"] = project
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if public is not UNSET:
            field_dict["public"] = public
        if management is not UNSET:
            field_dict["management"] = management
        if manageable is not UNSET:
            field_dict["manageable"] = manageable
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if bill is not UNSET:
            field_dict["bill"] = bill
        if project_lite is not UNSET:
            field_dict["project_lite"] = project_lite
        if address is not UNSET:
            field_dict["address"] = address
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if metro is not UNSET:
            field_dict["metro"] = metro

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.metal_gateway_lite import MetalGatewayLite
        from ..models.metro import Metro
        from ..models.project import Project
        from ..models.vrf import Vrf
        from ..models.vrf_ip_reservation_customdata import VrfIpReservationCustomdata
        d = src_dict.copy()
        type = VrfIpReservationType(d.pop("type"))




        vrf = Vrf.from_dict(d.pop("vrf"))




        address_family = d.pop("address_family", UNSET)

        cidr = d.pop("cidr", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, Href]
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = Href.from_dict(_created_by)




        details = d.pop("details", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _metal_gateway = d.pop("metal_gateway", UNSET)
        metal_gateway: Union[Unset, MetalGatewayLite]
        if isinstance(_metal_gateway,  Unset):
            metal_gateway = UNSET
        else:
            metal_gateway = MetalGatewayLite.from_dict(_metal_gateway)




        netmask = d.pop("netmask", UNSET)

        network = d.pop("network", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        state = d.pop("state", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        public = d.pop("public", UNSET)

        management = d.pop("management", UNSET)

        manageable = d.pop("manageable", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, VrfIpReservationCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = VrfIpReservationCustomdata.from_dict(_customdata)




        bill = d.pop("bill", UNSET)

        _project_lite = d.pop("project_lite", UNSET)
        project_lite: Union[Unset, Project]
        if isinstance(_project_lite,  Unset):
            project_lite = UNSET
        else:
            project_lite = Project.from_dict(_project_lite)




        address = d.pop("address", UNSET)

        gateway = d.pop("gateway", UNSET)

        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, Metro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = Metro.from_dict(_metro)




        vrf_ip_reservation = cls(
            type=type,
            vrf=vrf,
            address_family=address_family,
            cidr=cidr,
            created_at=created_at,
            created_by=created_by,
            details=details,
            href=href,
            id=id,
            metal_gateway=metal_gateway,
            netmask=netmask,
            network=network,
            project=project,
            state=state,
            tags=tags,
            public=public,
            management=management,
            manageable=manageable,
            customdata=customdata,
            bill=bill,
            project_lite=project_lite,
            address=address,
            gateway=gateway,
            metro=metro,
        )

        vrf_ip_reservation.additional_properties = d
        return vrf_ip_reservation

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
