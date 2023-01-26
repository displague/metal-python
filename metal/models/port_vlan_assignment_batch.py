import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.port_vlan_assignment_batch_state import PortVlanAssignmentBatchState
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.port import Port
  from ..models.port_vlan_assignment_batch_vlan_assignments_inner import PortVlanAssignmentBatchVlanAssignmentsInner




T = TypeVar("T", bound="PortVlanAssignmentBatch")

@attr.s(auto_attribs=True)
class PortVlanAssignmentBatch:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        error_messages (Union[Unset, List[str]]):
        id (Union[Unset, str]):
        port (Union[Unset, Port]): Port is a hardware port associated with a reserved or instantiated hardware device.
        quantity (Union[Unset, int]):
        state (Union[Unset, PortVlanAssignmentBatchState]):
        updated_at (Union[Unset, datetime.datetime]):
        vlan_assignments (Union[Unset, List['PortVlanAssignmentBatchVlanAssignmentsInner']]):
        project (Union[Unset, Href]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    error_messages: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    port: Union[Unset, 'Port'] = UNSET
    quantity: Union[Unset, int] = UNSET
    state: Union[Unset, PortVlanAssignmentBatchState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    vlan_assignments: Union[Unset, List['PortVlanAssignmentBatchVlanAssignmentsInner']] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        error_messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = self.error_messages




        id = self.id
        port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        quantity = self.quantity
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        vlan_assignments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vlan_assignments, Unset):
            vlan_assignments = []
            for vlan_assignments_item_data in self.vlan_assignments:
                vlan_assignments_item = vlan_assignments_item_data.to_dict()

                vlan_assignments.append(vlan_assignments_item)




        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error_messages is not UNSET:
            field_dict["error_messages"] = error_messages
        if id is not UNSET:
            field_dict["id"] = id
        if port is not UNSET:
            field_dict["port"] = port
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vlan_assignments is not UNSET:
            field_dict["vlan_assignments"] = vlan_assignments
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.port import Port
        from ..models.port_vlan_assignment_batch_vlan_assignments_inner import (
            PortVlanAssignmentBatchVlanAssignmentsInner,
        )
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        error_messages = cast(List[str], d.pop("error_messages", UNSET))


        id = d.pop("id", UNSET)

        _port = d.pop("port", UNSET)
        port: Union[Unset, Port]
        if isinstance(_port,  Unset):
            port = UNSET
        else:
            port = Port.from_dict(_port)




        quantity = d.pop("quantity", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PortVlanAssignmentBatchState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = PortVlanAssignmentBatchState(_state)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        vlan_assignments = []
        _vlan_assignments = d.pop("vlan_assignments", UNSET)
        for vlan_assignments_item_data in (_vlan_assignments or []):
            vlan_assignments_item = PortVlanAssignmentBatchVlanAssignmentsInner.from_dict(vlan_assignments_item_data)



            vlan_assignments.append(vlan_assignments_item)


        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        port_vlan_assignment_batch = cls(
            created_at=created_at,
            error_messages=error_messages,
            id=id,
            port=port,
            quantity=quantity,
            state=state,
            updated_at=updated_at,
            vlan_assignments=vlan_assignments,
            project=project,
        )

        port_vlan_assignment_batch.additional_properties = d
        return port_vlan_assignment_batch

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
