from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortAssignInput")

@attr.s(auto_attribs=True)
class PortAssignInput:
    """
    Attributes:
        vnid (Union[Unset, str]): Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value
            itself.
             Example: 1001.
    """

    vnid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        vnid = self.vnid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vnid is not UNSET:
            field_dict["vnid"] = vnid

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vnid = d.pop("vnid", UNSET)

        port_assign_input = cls(
            vnid=vnid,
        )

        port_assign_input.additional_properties = d
        return port_assign_input

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
