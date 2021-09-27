from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.interconnection_create_input_mode import InterconnectionCreateInputMode
from ..models.interconnection_create_input_service_token_type import InterconnectionCreateInputServiceTokenType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterconnectionCreateInput")

@attr.s(auto_attribs=True)
class InterconnectionCreateInput:
    """
    Attributes:
        metro (str): A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the
            issued Dedicated Ports. When creating Fabric VCs (Metal Billed), this is where interconnection will be
            originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection
            using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination
            location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the
            destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of
            the interconnection can be a different metro set here.
        name (str):
        redundancy (str): Either 'primary' or 'redundant'.
        type (str): Either 'shared' or 'dedicated'. The 'shared' type represents shared interconnections, or also known
            as Fabric VCs. The 'dedicated' type represents dedicated interconnections, or also known as Dedicated Ports.
        contact_email (Union[Unset, str]):
        description (Union[Unset, str]):
        mode (Union[Unset, InterconnectionCreateInputMode]): The mode of the interconnection (only relevant to Dedicated
            Ports). Fabric VCs won't have this field. Can be either 'standard' or 'tunnel'.
              The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when
            there are no associated virtual circuits on the interconnection.
              In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server
            instances. Example: standard.
        project (Union[Unset, str]):
        service_token_type (Union[Unset, InterconnectionCreateInputServiceTokenType]): Either 'a_side' or 'z_side'.
            Setting this field to 'a_side' will create an interconnection with Fabric VCs (Metal Billed). Setting this field
            to 'z_side' will create an interconnection with Fabric VCs (Fabric Billed). This is required when the 'type' is
            'shared', but this is not applicable when the 'type' is 'dedicated'. This parameter is included in the
            specification as a developer preview and is generally unavailable. Please contact our Support team for more
            details. Example: a_side.
        speed (Union[Unset, int]): A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be
            10Gbps or 100Gbps.
            For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this
            can only be one of the following:
            ''50mbps'', ''200mbps'', ''500mbps'', ''1gbps'', ''2gbps'', ''5gbps'' or ''10gbps'', and is required for
            creation. For Fabric VCs (Fabric Billed), this field will always default to ''10gbps'' even if it is not
            provided.
            For example, ''500000000'', ''50m'', or' ''500mbps'' will all work as valid inputs. Example: 10000000000.
        tags (Union[Unset, List[str]]):
        vlans (Union[Unset, List[int]]): A list of one or two metro-based VLANs that will be set on the virtual circuits
            of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can
            also be set after the interconnection is created, but are required to fully activate the interconnection. This
            parameter is included in the specification as a developer preview and is generally unavailable. Please contact
            our Support team for more details. Example: [1000, 1001].
    """

    metro: str
    name: str
    redundancy: str
    type: str
    contact_email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, InterconnectionCreateInputMode] = UNSET
    project: Union[Unset, str] = UNSET
    service_token_type: Union[Unset, InterconnectionCreateInputServiceTokenType] = UNSET
    speed: Union[Unset, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    vlans: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        metro = self.metro
        name = self.name
        redundancy = self.redundancy
        type = self.type
        contact_email = self.contact_email
        description = self.description
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        project = self.project
        service_token_type: Union[Unset, str] = UNSET
        if not isinstance(self.service_token_type, Unset):
            service_token_type = self.service_token_type.value

        speed = self.speed
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        vlans: Union[Unset, List[int]] = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = self.vlans





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "metro": metro,
            "name": name,
            "redundancy": redundancy,
            "type": type,
        })
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if project is not UNSET:
            field_dict["project"] = project
        if service_token_type is not UNSET:
            field_dict["service_token_type"] = service_token_type
        if speed is not UNSET:
            field_dict["speed"] = speed
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vlans is not UNSET:
            field_dict["vlans"] = vlans

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metro = d.pop("metro")

        name = d.pop("name")

        redundancy = d.pop("redundancy")

        type = d.pop("type")

        contact_email = d.pop("contact_email", UNSET)

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, InterconnectionCreateInputMode]
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = InterconnectionCreateInputMode(_mode)




        project = d.pop("project", UNSET)

        _service_token_type = d.pop("service_token_type", UNSET)
        service_token_type: Union[Unset, InterconnectionCreateInputServiceTokenType]
        if isinstance(_service_token_type,  Unset):
            service_token_type = UNSET
        else:
            service_token_type = InterconnectionCreateInputServiceTokenType(_service_token_type)




        speed = d.pop("speed", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        vlans = cast(List[int], d.pop("vlans", UNSET))


        interconnection_create_input = cls(
            metro=metro,
            name=name,
            redundancy=redundancy,
            type=type,
            contact_email=contact_email,
            description=description,
            mode=mode,
            project=project,
            service_token_type=service_token_type,
            speed=speed,
            tags=tags,
            vlans=vlans,
        )

        interconnection_create_input.additional_properties = d
        return interconnection_create_input

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
