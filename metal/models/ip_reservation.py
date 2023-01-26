import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.ip_reservation_type import IPReservationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.ip_assignment import IPAssignment
  from ..models.ip_reservation_customdata import IPReservationCustomdata
  from ..models.ip_reservation_facility import IPReservationFacility
  from ..models.ip_reservation_metro import IPReservationMetro
  from ..models.metal_gateway_lite import MetalGatewayLite
  from ..models.project import Project




T = TypeVar("T", bound="IPReservation")

@attr.s(auto_attribs=True)
class IPReservation:
    """
    Attributes:
        type (IPReservationType):
        addon (Union[Unset, bool]):
        address (Union[Unset, str]):
        address_family (Union[Unset, int]):
        assignments (Union[Unset, List['IPAssignment']]):
        available (Union[Unset, str]):
        bill (Union[Unset, bool]):
        cidr (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        customdata (Union[Unset, IPReservationCustomdata]):
        enabled (Union[Unset, bool]):
        details (Union[Unset, str]):
        facility (Union[Unset, IPReservationFacility]):
        gateway (Union[Unset, str]):
        global_ip (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        manageable (Union[Unset, bool]):
        management (Union[Unset, bool]):
        metal_gateway (Union[Unset, MetalGatewayLite]):
        metro (Union[Unset, IPReservationMetro]):
        netmask (Union[Unset, str]):
        network (Union[Unset, str]):
        project (Union[Unset, Project]):
        project_lite (Union[Unset, Href]):
        requested_by (Union[Unset, Href]):
        public (Union[Unset, bool]):
        state (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
    """

    type: IPReservationType
    addon: Union[Unset, bool] = UNSET
    address: Union[Unset, str] = UNSET
    address_family: Union[Unset, int] = UNSET
    assignments: Union[Unset, List['IPAssignment']] = UNSET
    available: Union[Unset, str] = UNSET
    bill: Union[Unset, bool] = UNSET
    cidr: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    customdata: Union[Unset, 'IPReservationCustomdata'] = UNSET
    enabled: Union[Unset, bool] = UNSET
    details: Union[Unset, str] = UNSET
    facility: Union[Unset, 'IPReservationFacility'] = UNSET
    gateway: Union[Unset, str] = UNSET
    global_ip: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    manageable: Union[Unset, bool] = UNSET
    management: Union[Unset, bool] = UNSET
    metal_gateway: Union[Unset, 'MetalGatewayLite'] = UNSET
    metro: Union[Unset, 'IPReservationMetro'] = UNSET
    netmask: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    project: Union[Unset, 'Project'] = UNSET
    project_lite: Union[Unset, 'Href'] = UNSET
    requested_by: Union[Unset, 'Href'] = UNSET
    public: Union[Unset, bool] = UNSET
    state: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET


    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        addon = self.addon
        address = self.address
        address_family = self.address_family
        assignments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignments, Unset):
            assignments = []
            for assignments_item_data in self.assignments:
                assignments_item = assignments_item_data.to_dict()

                assignments.append(assignments_item)




        available = self.available
        bill = self.bill
        cidr = self.cidr
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        enabled = self.enabled
        details = self.details
        facility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facility, Unset):
            facility = self.facility.to_dict()

        gateway = self.gateway
        global_ip = self.global_ip
        href = self.href
        id = self.id
        manageable = self.manageable
        management = self.management
        metal_gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metal_gateway, Unset):
            metal_gateway = self.metal_gateway.to_dict()

        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        netmask = self.netmask
        network = self.network
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        project_lite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_lite, Unset):
            project_lite = self.project_lite.to_dict()

        requested_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = self.requested_by.to_dict()

        public = self.public
        state = self.state
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "type": type,
        })
        if addon is not UNSET:
            field_dict["addon"] = addon
        if address is not UNSET:
            field_dict["address"] = address
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if available is not UNSET:
            field_dict["available"] = available
        if bill is not UNSET:
            field_dict["bill"] = bill
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if details is not UNSET:
            field_dict["details"] = details
        if facility is not UNSET:
            field_dict["facility"] = facility
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
        if metal_gateway is not UNSET:
            field_dict["metal_gateway"] = metal_gateway
        if metro is not UNSET:
            field_dict["metro"] = metro
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if network is not UNSET:
            field_dict["network"] = network
        if project is not UNSET:
            field_dict["project"] = project
        if project_lite is not UNSET:
            field_dict["project_lite"] = project_lite
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by
        if public is not UNSET:
            field_dict["public"] = public
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.ip_assignment import IPAssignment
        from ..models.ip_reservation_customdata import IPReservationCustomdata
        from ..models.ip_reservation_facility import IPReservationFacility
        from ..models.ip_reservation_metro import IPReservationMetro
        from ..models.metal_gateway_lite import MetalGatewayLite
        from ..models.project import Project
        d = src_dict.copy()
        type = IPReservationType(d.pop("type"))




        addon = d.pop("addon", UNSET)

        address = d.pop("address", UNSET)

        address_family = d.pop("address_family", UNSET)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in (_assignments or []):
            assignments_item = IPAssignment.from_dict(assignments_item_data)



            assignments.append(assignments_item)


        available = d.pop("available", UNSET)

        bill = d.pop("bill", UNSET)

        cidr = d.pop("cidr", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, IPReservationCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = IPReservationCustomdata.from_dict(_customdata)




        enabled = d.pop("enabled", UNSET)

        details = d.pop("details", UNSET)

        _facility = d.pop("facility", UNSET)
        facility: Union[Unset, IPReservationFacility]
        if isinstance(_facility,  Unset):
            facility = UNSET
        else:
            facility = IPReservationFacility.from_dict(_facility)




        gateway = d.pop("gateway", UNSET)

        global_ip = d.pop("global_ip", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        manageable = d.pop("manageable", UNSET)

        management = d.pop("management", UNSET)

        _metal_gateway = d.pop("metal_gateway", UNSET)
        metal_gateway: Union[Unset, MetalGatewayLite]
        if isinstance(_metal_gateway,  Unset):
            metal_gateway = UNSET
        else:
            metal_gateway = MetalGatewayLite.from_dict(_metal_gateway)




        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, IPReservationMetro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = IPReservationMetro.from_dict(_metro)




        netmask = d.pop("netmask", UNSET)

        network = d.pop("network", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        _project_lite = d.pop("project_lite", UNSET)
        project_lite: Union[Unset, Href]
        if isinstance(_project_lite,  Unset):
            project_lite = UNSET
        else:
            project_lite = Href.from_dict(_project_lite)




        _requested_by = d.pop("requested_by", UNSET)
        requested_by: Union[Unset, Href]
        if isinstance(_requested_by,  Unset):
            requested_by = UNSET
        else:
            requested_by = Href.from_dict(_requested_by)




        public = d.pop("public", UNSET)

        state = d.pop("state", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        ip_reservation = cls(
            type=type,
            addon=addon,
            address=address,
            address_family=address_family,
            assignments=assignments,
            available=available,
            bill=bill,
            cidr=cidr,
            created_at=created_at,
            customdata=customdata,
            enabled=enabled,
            details=details,
            facility=facility,
            gateway=gateway,
            global_ip=global_ip,
            href=href,
            id=id,
            manageable=manageable,
            management=management,
            metal_gateway=metal_gateway,
            metro=metro,
            netmask=netmask,
            network=network,
            project=project,
            project_lite=project_lite,
            requested_by=requested_by,
            public=public,
            state=state,
            tags=tags,
        )

        return ip_reservation

