from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortData")

@attr.s(auto_attribs=True)
class PortData:
    """
    Attributes:
        mac (Union[Unset, str]): MAC address is set for NetworkPort ports
        bonded (Union[Unset, bool]): Bonded is true for NetworkPort ports in a bond and NetworkBondPort ports that are
            active
    """

    mac: Union[Unset, str] = UNSET
    bonded: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        mac = self.mac
        bonded = self.bonded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mac is not UNSET:
            field_dict["mac"] = mac
        if bonded is not UNSET:
            field_dict["bonded"] = bonded

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mac = d.pop("mac", UNSET)

        bonded = d.pop("bonded", UNSET)

        port_data = cls(
            mac=mac,
            bonded=bonded,
        )

        port_data.additional_properties = d
        return port_data

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
