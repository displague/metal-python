from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VrfCreateInput")

@attr.s(auto_attribs=True)
class VrfCreateInput:
    """
    Attributes:
        metro (str): The UUID (or metro code) for the Metro in which to create this VRF.
        name (str):
        description (Union[Unset, str]):
        ip_ranges (Union[Unset, List[str]]): A list of CIDR network addresses. Like ["10.0.0.0/16", "2001:d78::/56"].
            IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\'s IP ranges must
            be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual
            Circuits.
        local_asn (Union[Unset, int]):
    """

    metro: str
    name: str
    description: Union[Unset, str] = UNSET
    ip_ranges: Union[Unset, List[str]] = UNSET
    local_asn: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        metro = self.metro
        name = self.name
        description = self.description
        ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_ranges, Unset):
            ip_ranges = self.ip_ranges




        local_asn = self.local_asn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "metro": metro,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if ip_ranges is not UNSET:
            field_dict["ip_ranges"] = ip_ranges
        if local_asn is not UNSET:
            field_dict["local_asn"] = local_asn

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metro = d.pop("metro")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        ip_ranges = cast(List[str], d.pop("ip_ranges", UNSET))


        local_asn = d.pop("local_asn", UNSET)

        vrf_create_input = cls(
            metro=metro,
            name=name,
            description=description,
            ip_ranges=ip_ranges,
            local_asn=local_asn,
        )

        vrf_create_input.additional_properties = d
        return vrf_create_input

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
