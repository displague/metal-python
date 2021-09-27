from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.port_vlan_assignment import PortVlanAssignment




T = TypeVar("T", bound="PortVlanAssignmentList")

@attr.s(auto_attribs=True)
class PortVlanAssignmentList:
    """
    Attributes:
        vlan_assignments (Union[Unset, List['PortVlanAssignment']]):
    """

    vlan_assignments: Union[Unset, List['PortVlanAssignment']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        vlan_assignments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vlan_assignments, Unset):
            vlan_assignments = []
            for vlan_assignments_item_data in self.vlan_assignments:
                vlan_assignments_item = vlan_assignments_item_data.to_dict()

                vlan_assignments.append(vlan_assignments_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vlan_assignments is not UNSET:
            field_dict["vlan_assignments"] = vlan_assignments

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.port_vlan_assignment import PortVlanAssignment
        d = src_dict.copy()
        vlan_assignments = []
        _vlan_assignments = d.pop("vlan_assignments", UNSET)
        for vlan_assignments_item_data in (_vlan_assignments or []):
            vlan_assignments_item = PortVlanAssignment.from_dict(vlan_assignments_item_data)



            vlan_assignments.append(vlan_assignments_item)


        port_vlan_assignment_list = cls(
            vlan_assignments=vlan_assignments,
        )

        port_vlan_assignment_list.additional_properties = d
        return port_vlan_assignment_list

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
