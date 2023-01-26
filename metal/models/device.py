import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.device_state import DeviceState
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.device_actions_inner import DeviceActionsInner
  from ..models.device_created_by import DeviceCreatedBy
  from ..models.device_customdata import DeviceCustomdata
  from ..models.device_metro import DeviceMetro
  from ..models.device_project import DeviceProject
  from ..models.device_project_lite import DeviceProjectLite
  from ..models.event import Event
  from ..models.facility import Facility
  from ..models.href import Href
  from ..models.ip_assignment import IPAssignment
  from ..models.operating_system import OperatingSystem
  from ..models.plan import Plan
  from ..models.port import Port




T = TypeVar("T", bound="Device")

@attr.s(auto_attribs=True)
class Device:
    """
    Attributes:
        always_pxe (Union[Unset, bool]):
        billing_cycle (Union[Unset, str]):
        bonding_mode (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DeviceCreatedBy]):
        customdata (Union[Unset, DeviceCustomdata]):
        description (Union[Unset, str]):
        facility (Union[Unset, Facility]):
        hardware_reservation (Union[Unset, Href]):
        hostname (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        image_url (Union[Unset, str]):
        ip_addresses (Union[Unset, List['IPAssignment']]):
        ipxe_script_url (Union[Unset, str]):
        iqn (Union[Unset, str]):
        locked (Union[Unset, bool]):
        metro (Union[Unset, DeviceMetro]):
        network_ports (Union[Unset, List['Port']]): By default, servers at Equinix Metal are configured in a “bonded”
            mode using LACP (Link Aggregation Control Protocol). Each 2-NIC server is configured with a single bond (namely
            bond0) with both interfaces eth0 and eth1 as members of the bond in a default Layer 3 mode. Some device plans
            may have a different number of ports and bonds available.
        operating_system (Union[Unset, OperatingSystem]):
        actions (Union[Unset, List['DeviceActionsInner']]): Actions supported by the device instance.
        plan (Union[Unset, Plan]):
        project (Union[Unset, DeviceProject]):
        project_lite (Union[Unset, DeviceProjectLite]):
        provisioning_events (Union[Unset, List['Event']]):
        provisioning_percentage (Union[Unset, float]): Only visible while device provisioning
        root_password (Union[Unset, str]): Root password is automatically generated when server is provisioned and it is
            removed after 24 hours
        short_id (Union[Unset, str]):
        spot_instance (Union[Unset, bool]): Whether or not the device is a spot instance.
        spot_price_max (Union[Unset, float]): The maximum price per hour you are willing to pay to keep this spot
            instance.  If you are outbid, the termination will be set allowing two
            minutes before shutdown.
        ssh_keys (Union[Unset, List['Href']]):
        state (Union[Unset, DeviceState]):
        switch_uuid (Union[Unset, str]): Switch short id. This can be used to determine if two devices are
            connected to the same switch, for example.
        tags (Union[Unset, List[str]]):
        termination_time (Union[Unset, datetime.datetime]): When the device will be terminated. This is commonly set in
            advance for
            ephemeral spot market instances but this field may also be set with
            on-demand and reservation instances to automatically delete the resource
            at a given time. The termination time can also be used to release a
            hardware reservation instance at a given time, keeping the reservation
            open for other uses.  On a spot market device, the termination time will
            be set automatically when outbid.
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, str]):
        userdata (Union[Unset, str]):
        volumes (Union[Unset, List['Href']]):
    """

    always_pxe: Union[Unset, bool] = UNSET
    billing_cycle: Union[Unset, str] = UNSET
    bonding_mode: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, 'DeviceCreatedBy'] = UNSET
    customdata: Union[Unset, 'DeviceCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    facility: Union[Unset, 'Facility'] = UNSET
    hardware_reservation: Union[Unset, 'Href'] = UNSET
    hostname: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    ip_addresses: Union[Unset, List['IPAssignment']] = UNSET
    ipxe_script_url: Union[Unset, str] = UNSET
    iqn: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    metro: Union[Unset, 'DeviceMetro'] = UNSET
    network_ports: Union[Unset, List['Port']] = UNSET
    operating_system: Union[Unset, 'OperatingSystem'] = UNSET
    actions: Union[Unset, List['DeviceActionsInner']] = UNSET
    plan: Union[Unset, 'Plan'] = UNSET
    project: Union[Unset, 'DeviceProject'] = UNSET
    project_lite: Union[Unset, 'DeviceProjectLite'] = UNSET
    provisioning_events: Union[Unset, List['Event']] = UNSET
    provisioning_percentage: Union[Unset, float] = UNSET
    root_password: Union[Unset, str] = UNSET
    short_id: Union[Unset, str] = UNSET
    spot_instance: Union[Unset, bool] = UNSET
    spot_price_max: Union[Unset, float] = UNSET
    ssh_keys: Union[Unset, List['Href']] = UNSET
    state: Union[Unset, DeviceState] = UNSET
    switch_uuid: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    termination_time: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, str] = UNSET
    userdata: Union[Unset, str] = UNSET
    volumes: Union[Unset, List['Href']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        always_pxe = self.always_pxe
        billing_cycle = self.billing_cycle
        bonding_mode = self.bonding_mode
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        facility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facility, Unset):
            facility = self.facility.to_dict()

        hardware_reservation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hardware_reservation, Unset):
            hardware_reservation = self.hardware_reservation.to_dict()

        hostname = self.hostname
        href = self.href
        id = self.id
        image_url = self.image_url
        ip_addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = []
            for ip_addresses_item_data in self.ip_addresses:
                ip_addresses_item = ip_addresses_item_data.to_dict()

                ip_addresses.append(ip_addresses_item)




        ipxe_script_url = self.ipxe_script_url
        iqn = self.iqn
        locked = self.locked
        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        network_ports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.network_ports, Unset):
            network_ports = []
            for network_ports_item_data in self.network_ports:
                network_ports_item = network_ports_item_data.to_dict()

                network_ports.append(network_ports_item)




        operating_system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system.to_dict()

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)




        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        project_lite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_lite, Unset):
            project_lite = self.project_lite.to_dict()

        provisioning_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provisioning_events, Unset):
            provisioning_events = []
            for provisioning_events_item_data in self.provisioning_events:
                provisioning_events_item = provisioning_events_item_data.to_dict()

                provisioning_events.append(provisioning_events_item)




        provisioning_percentage = self.provisioning_percentage
        root_password = self.root_password
        short_id = self.short_id
        spot_instance = self.spot_instance
        spot_price_max = self.spot_price_max
        ssh_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = []
            for ssh_keys_item_data in self.ssh_keys:
                ssh_keys_item = ssh_keys_item_data.to_dict()

                ssh_keys.append(ssh_keys_item)




        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        switch_uuid = self.switch_uuid
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        termination_time: Union[Unset, str] = UNSET
        if not isinstance(self.termination_time, Unset):
            termination_time = self.termination_time.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user = self.user
        userdata = self.userdata
        volumes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()

                volumes.append(volumes_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if always_pxe is not UNSET:
            field_dict["always_pxe"] = always_pxe
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if bonding_mode is not UNSET:
            field_dict["bonding_mode"] = bonding_mode
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if facility is not UNSET:
            field_dict["facility"] = facility
        if hardware_reservation is not UNSET:
            field_dict["hardware_reservation"] = hardware_reservation
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if ipxe_script_url is not UNSET:
            field_dict["ipxe_script_url"] = ipxe_script_url
        if iqn is not UNSET:
            field_dict["iqn"] = iqn
        if locked is not UNSET:
            field_dict["locked"] = locked
        if metro is not UNSET:
            field_dict["metro"] = metro
        if network_ports is not UNSET:
            field_dict["network_ports"] = network_ports
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if actions is not UNSET:
            field_dict["actions"] = actions
        if plan is not UNSET:
            field_dict["plan"] = plan
        if project is not UNSET:
            field_dict["project"] = project
        if project_lite is not UNSET:
            field_dict["project_lite"] = project_lite
        if provisioning_events is not UNSET:
            field_dict["provisioning_events"] = provisioning_events
        if provisioning_percentage is not UNSET:
            field_dict["provisioning_percentage"] = provisioning_percentage
        if root_password is not UNSET:
            field_dict["root_password"] = root_password
        if short_id is not UNSET:
            field_dict["short_id"] = short_id
        if spot_instance is not UNSET:
            field_dict["spot_instance"] = spot_instance
        if spot_price_max is not UNSET:
            field_dict["spot_price_max"] = spot_price_max
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if state is not UNSET:
            field_dict["state"] = state
        if switch_uuid is not UNSET:
            field_dict["switch_uuid"] = switch_uuid
        if tags is not UNSET:
            field_dict["tags"] = tags
        if termination_time is not UNSET:
            field_dict["termination_time"] = termination_time
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user
        if userdata is not UNSET:
            field_dict["userdata"] = userdata
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_actions_inner import DeviceActionsInner
        from ..models.device_created_by import DeviceCreatedBy
        from ..models.device_customdata import DeviceCustomdata
        from ..models.device_metro import DeviceMetro
        from ..models.device_project import DeviceProject
        from ..models.device_project_lite import DeviceProjectLite
        from ..models.event import Event
        from ..models.facility import Facility
        from ..models.href import Href
        from ..models.ip_assignment import IPAssignment
        from ..models.operating_system import OperatingSystem
        from ..models.plan import Plan
        from ..models.port import Port
        d = src_dict.copy()
        always_pxe = d.pop("always_pxe", UNSET)

        billing_cycle = d.pop("billing_cycle", UNSET)

        bonding_mode = d.pop("bonding_mode", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, DeviceCreatedBy]
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = DeviceCreatedBy.from_dict(_created_by)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, DeviceCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = DeviceCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        _facility = d.pop("facility", UNSET)
        facility: Union[Unset, Facility]
        if isinstance(_facility,  Unset):
            facility = UNSET
        else:
            facility = Facility.from_dict(_facility)




        _hardware_reservation = d.pop("hardware_reservation", UNSET)
        hardware_reservation: Union[Unset, Href]
        if isinstance(_hardware_reservation,  Unset):
            hardware_reservation = UNSET
        else:
            hardware_reservation = Href.from_dict(_hardware_reservation)




        hostname = d.pop("hostname", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        image_url = d.pop("image_url", UNSET)

        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses", UNSET)
        for ip_addresses_item_data in (_ip_addresses or []):
            ip_addresses_item = IPAssignment.from_dict(ip_addresses_item_data)



            ip_addresses.append(ip_addresses_item)


        ipxe_script_url = d.pop("ipxe_script_url", UNSET)

        iqn = d.pop("iqn", UNSET)

        locked = d.pop("locked", UNSET)

        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, DeviceMetro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = DeviceMetro.from_dict(_metro)




        network_ports = []
        _network_ports = d.pop("network_ports", UNSET)
        for network_ports_item_data in (_network_ports or []):
            network_ports_item = Port.from_dict(network_ports_item_data)



            network_ports.append(network_ports_item)


        _operating_system = d.pop("operating_system", UNSET)
        operating_system: Union[Unset, OperatingSystem]
        if isinstance(_operating_system,  Unset):
            operating_system = UNSET
        else:
            operating_system = OperatingSystem.from_dict(_operating_system)




        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in (_actions or []):
            actions_item = DeviceActionsInner.from_dict(actions_item_data)



            actions.append(actions_item)


        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, Plan]
        if isinstance(_plan,  Unset):
            plan = UNSET
        else:
            plan = Plan.from_dict(_plan)




        _project = d.pop("project", UNSET)
        project: Union[Unset, DeviceProject]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = DeviceProject.from_dict(_project)




        _project_lite = d.pop("project_lite", UNSET)
        project_lite: Union[Unset, DeviceProjectLite]
        if isinstance(_project_lite,  Unset):
            project_lite = UNSET
        else:
            project_lite = DeviceProjectLite.from_dict(_project_lite)




        provisioning_events = []
        _provisioning_events = d.pop("provisioning_events", UNSET)
        for provisioning_events_item_data in (_provisioning_events or []):
            provisioning_events_item = Event.from_dict(provisioning_events_item_data)



            provisioning_events.append(provisioning_events_item)


        provisioning_percentage = d.pop("provisioning_percentage", UNSET)

        root_password = d.pop("root_password", UNSET)

        short_id = d.pop("short_id", UNSET)

        spot_instance = d.pop("spot_instance", UNSET)

        spot_price_max = d.pop("spot_price_max", UNSET)

        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in (_ssh_keys or []):
            ssh_keys_item = Href.from_dict(ssh_keys_item_data)



            ssh_keys.append(ssh_keys_item)


        _state = d.pop("state", UNSET)
        state: Union[Unset, DeviceState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = DeviceState(_state)




        switch_uuid = d.pop("switch_uuid", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        _termination_time = d.pop("termination_time", UNSET)
        termination_time: Union[Unset, datetime.datetime]
        if isinstance(_termination_time,  Unset):
            termination_time = UNSET
        else:
            termination_time = isoparse(_termination_time)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        user = d.pop("user", UNSET)

        userdata = d.pop("userdata", UNSET)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in (_volumes or []):
            volumes_item = Href.from_dict(volumes_item_data)



            volumes.append(volumes_item)


        device = cls(
            always_pxe=always_pxe,
            billing_cycle=billing_cycle,
            bonding_mode=bonding_mode,
            created_at=created_at,
            created_by=created_by,
            customdata=customdata,
            description=description,
            facility=facility,
            hardware_reservation=hardware_reservation,
            hostname=hostname,
            href=href,
            id=id,
            image_url=image_url,
            ip_addresses=ip_addresses,
            ipxe_script_url=ipxe_script_url,
            iqn=iqn,
            locked=locked,
            metro=metro,
            network_ports=network_ports,
            operating_system=operating_system,
            actions=actions,
            plan=plan,
            project=project,
            project_lite=project_lite,
            provisioning_events=provisioning_events,
            provisioning_percentage=provisioning_percentage,
            root_password=root_password,
            short_id=short_id,
            spot_instance=spot_instance,
            spot_price_max=spot_price_max,
            ssh_keys=ssh_keys,
            state=state,
            switch_uuid=switch_uuid,
            tags=tags,
            termination_time=termination_time,
            updated_at=updated_at,
            user=user,
            userdata=userdata,
            volumes=volumes,
        )

        device.additional_properties = d
        return device

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
