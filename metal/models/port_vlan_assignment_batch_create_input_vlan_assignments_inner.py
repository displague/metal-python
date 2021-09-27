from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.port_vlan_assignment_batch_create_input_vlan_assignments_inner_state import (
    PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PortVlanAssignmentBatchCreateInputVlanAssignmentsInner")

@attr.s(auto_attribs=True)
class PortVlanAssignmentBatchCreateInputVlanAssignmentsInner:
    """
    Attributes:
        native (Union[Unset, bool]):
        state (Union[Unset, PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState]):
        vlan (Union[Unset, str]):
    """

    native: Union[Unset, bool] = UNSET
    state: Union[Unset, PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState] = UNSET
    vlan: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        native = self.native
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        vlan = self.vlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        native = d.pop("native", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = PortVlanAssignmentBatchCreateInputVlanAssignmentsInnerState(_state)




        vlan = d.pop("vlan", UNSET)

        port_vlan_assignment_batch_create_input_vlan_assignments_inner = cls(
            native=native,
            state=state,
            vlan=vlan,
        )

        port_vlan_assignment_batch_create_input_vlan_assignments_inner.additional_properties = d
        return port_vlan_assignment_batch_create_input_vlan_assignments_inner

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
