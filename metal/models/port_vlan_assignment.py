import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.port_vlan_assignment_state import PortVlanAssignmentState
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="PortVlanAssignment")

@attr.s(auto_attribs=True)
class PortVlanAssignment:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        native (Union[Unset, bool]):
        port (Union[Unset, Href]):
        state (Union[Unset, PortVlanAssignmentState]):
        updated_at (Union[Unset, datetime.datetime]):
        virtual_network (Union[Unset, Href]):
        vlan (Union[Unset, int]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    native: Union[Unset, bool] = UNSET
    port: Union[Unset, 'Href'] = UNSET
    state: Union[Unset, PortVlanAssignmentState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    virtual_network: Union[Unset, 'Href'] = UNSET
    vlan: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        native = self.native
        port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        virtual_network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.virtual_network, Unset):
            virtual_network = self.virtual_network.to_dict()

        vlan = self.vlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if native is not UNSET:
            field_dict["native"] = native
        if port is not UNSET:
            field_dict["port"] = port
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if virtual_network is not UNSET:
            field_dict["virtual_network"] = virtual_network
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        id = d.pop("id", UNSET)

        native = d.pop("native", UNSET)

        _port = d.pop("port", UNSET)
        port: Union[Unset, Href]
        if isinstance(_port,  Unset):
            port = UNSET
        else:
            port = Href.from_dict(_port)




        _state = d.pop("state", UNSET)
        state: Union[Unset, PortVlanAssignmentState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = PortVlanAssignmentState(_state)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        _virtual_network = d.pop("virtual_network", UNSET)
        virtual_network: Union[Unset, Href]
        if isinstance(_virtual_network,  Unset):
            virtual_network = UNSET
        else:
            virtual_network = Href.from_dict(_virtual_network)




        vlan = d.pop("vlan", UNSET)

        port_vlan_assignment = cls(
            created_at=created_at,
            id=id,
            native=native,
            port=port,
            state=state,
            updated_at=updated_at,
            virtual_network=virtual_network,
            vlan=vlan,
        )

        port_vlan_assignment.additional_properties = d
        return port_vlan_assignment

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
