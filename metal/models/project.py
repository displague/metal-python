import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.project_customdata import ProjectCustomdata
  from ..models.project_max_devices import ProjectMaxDevices
  from ..models.project_network_status import ProjectNetworkStatus




T = TypeVar("T", bound="Project")

@attr.s(auto_attribs=True)
class Project:
    """
    Attributes:
        bgp_config (Union[Unset, Href]):
        created_at (Union[Unset, datetime.datetime]):
        customdata (Union[Unset, ProjectCustomdata]):
        devices (Union[Unset, List['Href']]):
        id (Union[Unset, str]):
        invitations (Union[Unset, List['Href']]):
        max_devices (Union[Unset, ProjectMaxDevices]):
        members (Union[Unset, List['Href']]):
        memberships (Union[Unset, List['Href']]):
        name (Union[Unset, str]):
        network_status (Union[Unset, ProjectNetworkStatus]):
        payment_method (Union[Unset, Href]):
        ssh_keys (Union[Unset, List['Href']]):
        updated_at (Union[Unset, datetime.datetime]):
        volumes (Union[Unset, List['Href']]):
    """

    bgp_config: Union[Unset, 'Href'] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    customdata: Union[Unset, 'ProjectCustomdata'] = UNSET
    devices: Union[Unset, List['Href']] = UNSET
    id: Union[Unset, str] = UNSET
    invitations: Union[Unset, List['Href']] = UNSET
    max_devices: Union[Unset, 'ProjectMaxDevices'] = UNSET
    members: Union[Unset, List['Href']] = UNSET
    memberships: Union[Unset, List['Href']] = UNSET
    name: Union[Unset, str] = UNSET
    network_status: Union[Unset, 'ProjectNetworkStatus'] = UNSET
    payment_method: Union[Unset, 'Href'] = UNSET
    ssh_keys: Union[Unset, List['Href']] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    volumes: Union[Unset, List['Href']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bgp_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bgp_config, Unset):
            bgp_config = self.bgp_config.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()

                devices.append(devices_item)




        id = self.id
        invitations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invitations, Unset):
            invitations = []
            for invitations_item_data in self.invitations:
                invitations_item = invitations_item_data.to_dict()

                invitations.append(invitations_item)




        max_devices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_devices, Unset):
            max_devices = self.max_devices.to_dict()

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)




        memberships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()

                memberships.append(memberships_item)




        name = self.name
        network_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network_status, Unset):
            network_status = self.network_status.to_dict()

        payment_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.to_dict()

        ssh_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = []
            for ssh_keys_item_data in self.ssh_keys:
                ssh_keys_item = ssh_keys_item_data.to_dict()

                ssh_keys.append(ssh_keys_item)




        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

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
        if bgp_config is not UNSET:
            field_dict["bgp_config"] = bgp_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if devices is not UNSET:
            field_dict["devices"] = devices
        if id is not UNSET:
            field_dict["id"] = id
        if invitations is not UNSET:
            field_dict["invitations"] = invitations
        if max_devices is not UNSET:
            field_dict["max_devices"] = max_devices
        if members is not UNSET:
            field_dict["members"] = members
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if name is not UNSET:
            field_dict["name"] = name
        if network_status is not UNSET:
            field_dict["network_status"] = network_status
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.project_customdata import ProjectCustomdata
        from ..models.project_max_devices import ProjectMaxDevices
        from ..models.project_network_status import ProjectNetworkStatus
        d = src_dict.copy()
        _bgp_config = d.pop("bgp_config", UNSET)
        bgp_config: Union[Unset, Href]
        if isinstance(_bgp_config,  Unset):
            bgp_config = UNSET
        else:
            bgp_config = Href.from_dict(_bgp_config)




        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, ProjectCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = ProjectCustomdata.from_dict(_customdata)




        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in (_devices or []):
            devices_item = Href.from_dict(devices_item_data)



            devices.append(devices_item)


        id = d.pop("id", UNSET)

        invitations = []
        _invitations = d.pop("invitations", UNSET)
        for invitations_item_data in (_invitations or []):
            invitations_item = Href.from_dict(invitations_item_data)



            invitations.append(invitations_item)


        _max_devices = d.pop("max_devices", UNSET)
        max_devices: Union[Unset, ProjectMaxDevices]
        if isinstance(_max_devices,  Unset):
            max_devices = UNSET
        else:
            max_devices = ProjectMaxDevices.from_dict(_max_devices)




        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in (_members or []):
            members_item = Href.from_dict(members_item_data)



            members.append(members_item)


        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in (_memberships or []):
            memberships_item = Href.from_dict(memberships_item_data)



            memberships.append(memberships_item)


        name = d.pop("name", UNSET)

        _network_status = d.pop("network_status", UNSET)
        network_status: Union[Unset, ProjectNetworkStatus]
        if isinstance(_network_status,  Unset):
            network_status = UNSET
        else:
            network_status = ProjectNetworkStatus.from_dict(_network_status)




        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, Href]
        if isinstance(_payment_method,  Unset):
            payment_method = UNSET
        else:
            payment_method = Href.from_dict(_payment_method)




        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in (_ssh_keys or []):
            ssh_keys_item = Href.from_dict(ssh_keys_item_data)



            ssh_keys.append(ssh_keys_item)


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in (_volumes or []):
            volumes_item = Href.from_dict(volumes_item_data)



            volumes.append(volumes_item)


        project = cls(
            bgp_config=bgp_config,
            created_at=created_at,
            customdata=customdata,
            devices=devices,
            id=id,
            invitations=invitations,
            max_devices=max_devices,
            members=members,
            memberships=memberships,
            name=name,
            network_status=network_status,
            payment_method=payment_method,
            ssh_keys=ssh_keys,
            updated_at=updated_at,
            volumes=volumes,
        )

        project.additional_properties = d
        return project

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
