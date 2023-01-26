from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.port_vlan_assignment_batch_vlan_assignments_inner_state import (
    PortVlanAssignmentBatchVlanAssignmentsInnerState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PortVlanAssignmentBatchVlanAssignmentsInner")

@attr.s(auto_attribs=True)
class PortVlanAssignmentBatchVlanAssignmentsInner:
    """
    Attributes:
        id (Union[Unset, str]):
        native (Union[Unset, bool]):
        state (Union[Unset, PortVlanAssignmentBatchVlanAssignmentsInnerState]):
        vlan (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    native: Union[Unset, bool] = UNSET
    state: Union[Unset, PortVlanAssignmentBatchVlanAssignmentsInnerState] = UNSET
    vlan: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        native = self.native
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        vlan = self.vlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if native is not UNSET:
            field_dict["native"] = native
        if state is not UNSET:
            field_dict["state"] = state
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        native = d.pop("native", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PortVlanAssignmentBatchVlanAssignmentsInnerState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = PortVlanAssignmentBatchVlanAssignmentsInnerState(_state)




        vlan = d.pop("vlan", UNSET)

        port_vlan_assignment_batch_vlan_assignments_inner = cls(
            id=id,
            native=native,
            state=state,
            vlan=vlan,
        )

        port_vlan_assignment_batch_vlan_assignments_inner.additional_properties = d
        return port_vlan_assignment_batch_vlan_assignments_inner

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
