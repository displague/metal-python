import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.interconnection_mode import InterconnectionMode
from ..models.interconnection_redundancy import InterconnectionRedundancy
from ..models.interconnection_type import InterconnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.fabric_service_token import FabricServiceToken
  from ..models.href import Href
  from ..models.interconnection_port import InterconnectionPort
  from ..models.metro import Metro




T = TypeVar("T", bound="Interconnection")

@attr.s(auto_attribs=True)
class Interconnection:
    """
    Attributes:
        contact_email (Union[Unset, str]):
        description (Union[Unset, str]):
        facility (Union[Unset, Href]):
        id (Union[Unset, str]):
        metro (Union[Unset, Metro]):
        mode (Union[Unset, InterconnectionMode]): The mode of the interconnection (only relevant to Dedicated Ports).
            Shared connections won't have this field. Can be either 'standard' or 'tunnel'.
              The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when
            there are no associated virtual circuits on the interconnection.
              In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server
            instances. Example: standard.
        name (Union[Unset, str]):
        organization (Union[Unset, Href]):
        ports (Union[Unset, List['InterconnectionPort']]): For Fabric VCs, these represent Virtual Port(s) created for
            the interconnection. For dedicated interconnections, these represent the Dedicated Port(s).
        redundancy (Union[Unset, InterconnectionRedundancy]): Either 'primary', meaning a single interconnection, or
            'redundant', meaning a redundant interconnection.
        service_tokens (Union[Unset, List['FabricServiceToken']]): For Fabric VCs (Metal Billed), this will show details
            of the A-Side service tokens issued for the interconnection. For Fabric VCs (Fabric Billed), this will show the
            details of the Z-Side service tokens issued for the interconnection. Dedicated interconnections will not have
            any service tokens issued. There will be one per interconnection, so for redundant interconnections, there
            should be two service tokens issued.
        speed (Union[Unset, int]): For interconnections on Dedicated Ports and shared connections, this represents the
            interconnection's speed in bps. For Fabric VCs, this field refers to the maximum speed of the interconnection in
            bps. This value will default to 10Gbps for Fabric VCs (Fabric Billed). Example: 10000000000.
        status (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        token (Union[Unset, str]): This token is used for shared interconnections to be used as the Fabric Token. This
            field is entirely deprecated.
        type (Union[Unset, InterconnectionType]): The 'shared' type of interconnection refers to shared connections, or
            later also known as Fabric Virtual Connections (or Fabric VCs). The 'dedicated' type of interconnection refers
            to interconnections created with Dedicated Ports.
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        requested_by (Union[Unset, Href]):
    """

    contact_email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    facility: Union[Unset, 'Href'] = UNSET
    id: Union[Unset, str] = UNSET
    metro: Union[Unset, 'Metro'] = UNSET
    mode: Union[Unset, InterconnectionMode] = UNSET
    name: Union[Unset, str] = UNSET
    organization: Union[Unset, 'Href'] = UNSET
    ports: Union[Unset, List['InterconnectionPort']] = UNSET
    redundancy: Union[Unset, InterconnectionRedundancy] = UNSET
    service_tokens: Union[Unset, List['FabricServiceToken']] = UNSET
    speed: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    token: Union[Unset, str] = UNSET
    type: Union[Unset, InterconnectionType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    requested_by: Union[Unset, 'Href'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        contact_email = self.contact_email
        description = self.description
        facility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facility, Unset):
            facility = self.facility.to_dict()

        id = self.id
        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        ports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()

                ports.append(ports_item)




        redundancy: Union[Unset, str] = UNSET
        if not isinstance(self.redundancy, Unset):
            redundancy = self.redundancy.value

        service_tokens: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_tokens, Unset):
            service_tokens = []
            for service_tokens_item_data in self.service_tokens:
                service_tokens_item = service_tokens_item_data.to_dict()

                service_tokens.append(service_tokens_item)




        speed = self.speed
        status = self.status
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        token = self.token
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        requested_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = self.requested_by.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if description is not UNSET:
            field_dict["description"] = description
        if facility is not UNSET:
            field_dict["facility"] = facility
        if id is not UNSET:
            field_dict["id"] = id
        if metro is not UNSET:
            field_dict["metro"] = metro
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if ports is not UNSET:
            field_dict["ports"] = ports
        if redundancy is not UNSET:
            field_dict["redundancy"] = redundancy
        if service_tokens is not UNSET:
            field_dict["service_tokens"] = service_tokens
        if speed is not UNSET:
            field_dict["speed"] = speed
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if token is not UNSET:
            field_dict["token"] = token
        if type is not UNSET:
            field_dict["type"] = type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fabric_service_token import FabricServiceToken
        from ..models.href import Href
        from ..models.interconnection_port import InterconnectionPort
        from ..models.metro import Metro
        d = src_dict.copy()
        contact_email = d.pop("contact_email", UNSET)

        description = d.pop("description", UNSET)

        _facility = d.pop("facility", UNSET)
        facility: Union[Unset, Href]
        if isinstance(_facility,  Unset):
            facility = UNSET
        else:
            facility = Href.from_dict(_facility)




        id = d.pop("id", UNSET)

        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, Metro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = Metro.from_dict(_metro)




        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, InterconnectionMode]
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = InterconnectionMode(_mode)




        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Href]
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = Href.from_dict(_organization)




        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in (_ports or []):
            ports_item = InterconnectionPort.from_dict(ports_item_data)



            ports.append(ports_item)


        _redundancy = d.pop("redundancy", UNSET)
        redundancy: Union[Unset, InterconnectionRedundancy]
        if isinstance(_redundancy,  Unset):
            redundancy = UNSET
        else:
            redundancy = InterconnectionRedundancy(_redundancy)




        service_tokens = []
        _service_tokens = d.pop("service_tokens", UNSET)
        for service_tokens_item_data in (_service_tokens or []):
            service_tokens_item = FabricServiceToken.from_dict(service_tokens_item_data)



            service_tokens.append(service_tokens_item)


        speed = d.pop("speed", UNSET)

        status = d.pop("status", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        token = d.pop("token", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InterconnectionType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = InterconnectionType(_type)




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




        _requested_by = d.pop("requested_by", UNSET)
        requested_by: Union[Unset, Href]
        if isinstance(_requested_by,  Unset):
            requested_by = UNSET
        else:
            requested_by = Href.from_dict(_requested_by)




        interconnection = cls(
            contact_email=contact_email,
            description=description,
            facility=facility,
            id=id,
            metro=metro,
            mode=mode,
            name=name,
            organization=organization,
            ports=ports,
            redundancy=redundancy,
            service_tokens=service_tokens,
            speed=speed,
            status=status,
            tags=tags,
            token=token,
            type=type,
            created_at=created_at,
            updated_at=updated_at,
            requested_by=requested_by,
        )

        interconnection.additional_properties = d
        return interconnection

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
