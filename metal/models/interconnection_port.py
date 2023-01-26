from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.interconnection_port_role import InterconnectionPortRole
from ..models.interconnection_port_status import InterconnectionPortStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.virtual_circuit_list import VirtualCircuitList




T = TypeVar("T", bound="InterconnectionPort")

@attr.s(auto_attribs=True)
class InterconnectionPort:
    """
    Attributes:
        id (Union[Unset, str]):
        organization (Union[Unset, Href]):
        role (Union[Unset, InterconnectionPortRole]): Either 'primary' or 'secondary'.
        status (Union[Unset, InterconnectionPortStatus]): For both Fabric VCs and Dedicated Ports, this will be
            'requested' on creation and 'deleting' on deletion. Once the Fabric VC has found its corresponding Fabric
            connection, this will turn to 'active'. For Dedicated Ports, once the dedicated port is associated, this will
            also turn to 'active'. For Fabric VCs, this can turn into an 'expired' state if the service token associated is
            expired.
        switch_id (Union[Unset, str]): A switch 'short ID'
        virtual_circuits (Union[Unset, VirtualCircuitList]):
        name (Union[Unset, str]):
        speed (Union[Unset, int]):
        link_status (Union[Unset, str]):
        href (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    organization: Union[Unset, 'Href'] = UNSET
    role: Union[Unset, InterconnectionPortRole] = UNSET
    status: Union[Unset, InterconnectionPortStatus] = UNSET
    switch_id: Union[Unset, str] = UNSET
    virtual_circuits: Union[Unset, 'VirtualCircuitList'] = UNSET
    name: Union[Unset, str] = UNSET
    speed: Union[Unset, int] = UNSET
    link_status: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        switch_id = self.switch_id
        virtual_circuits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.virtual_circuits, Unset):
            virtual_circuits = self.virtual_circuits.to_dict()

        name = self.name
        speed = self.speed
        link_status = self.link_status
        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if switch_id is not UNSET:
            field_dict["switch_id"] = switch_id
        if virtual_circuits is not UNSET:
            field_dict["virtual_circuits"] = virtual_circuits
        if name is not UNSET:
            field_dict["name"] = name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if link_status is not UNSET:
            field_dict["link_status"] = link_status
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.virtual_circuit_list import VirtualCircuitList
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Href]
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = Href.from_dict(_organization)




        _role = d.pop("role", UNSET)
        role: Union[Unset, InterconnectionPortRole]
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = InterconnectionPortRole(_role)




        _status = d.pop("status", UNSET)
        status: Union[Unset, InterconnectionPortStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = InterconnectionPortStatus(_status)




        switch_id = d.pop("switch_id", UNSET)

        _virtual_circuits = d.pop("virtual_circuits", UNSET)
        virtual_circuits: Union[Unset, VirtualCircuitList]
        if isinstance(_virtual_circuits,  Unset):
            virtual_circuits = UNSET
        else:
            virtual_circuits = VirtualCircuitList.from_dict(_virtual_circuits)




        name = d.pop("name", UNSET)

        speed = d.pop("speed", UNSET)

        link_status = d.pop("link_status", UNSET)

        href = d.pop("href", UNSET)

        interconnection_port = cls(
            id=id,
            organization=organization,
            role=role,
            status=status,
            switch_id=switch_id,
            virtual_circuits=virtual_circuits,
            name=name,
            speed=speed,
            link_status=link_status,
            href=href,
        )

        interconnection_port.additional_properties = d
        return interconnection_port

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
