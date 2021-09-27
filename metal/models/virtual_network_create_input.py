from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualNetworkCreateInput")

@attr.s(auto_attribs=True)
class VirtualNetworkCreateInput:
    """
    Attributes:
        description (Union[Unset, str]):
        facility (Union[Unset, str]): The UUID (or facility code) for the Facility in which to create this Virtual
            network.
        metro (Union[Unset, str]): The UUID (or metro code) for the Metro in which to create this Virtual Network.
        vxlan (Union[Unset, int]): VLAN ID between 2-3999. Must be unique for the project within the Metro in which this
            Virtual Network is being created. If no value is specified, the next-available VLAN ID in the range 1000-1999
            will be automatically selected. Example: 1099.
    """

    description: Union[Unset, str] = UNSET
    facility: Union[Unset, str] = UNSET
    metro: Union[Unset, str] = UNSET
    vxlan: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        facility = self.facility
        metro = self.metro
        vxlan = self.vxlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if facility is not UNSET:
            field_dict["facility"] = facility
        if metro is not UNSET:
            field_dict["metro"] = metro
        if vxlan is not UNSET:
            field_dict["vxlan"] = vxlan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        facility = d.pop("facility", UNSET)

        metro = d.pop("metro", UNSET)

        vxlan = d.pop("vxlan", UNSET)

        virtual_network_create_input = cls(
            description=description,
            facility=facility,
            metro=metro,
            vxlan=vxlan,
        )

        virtual_network_create_input.additional_properties = d
        return virtual_network_create_input

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
