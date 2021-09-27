from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VrfUpdateInput")

@attr.s(auto_attribs=True)
class VrfUpdateInput:
    """
    Attributes:
        description (Union[Unset, str]):
        ip_ranges (Union[Unset, List[str]]): A list of CIDR network addresses. Like ["10.0.0.0/16", "2001:d78::/56"].
            IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\'s IP ranges must
            be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual
            Circuits. Adding a new CIDR address to the list will result in the creation of a new IP Range for this VRF.
            Removal of an existing CIDR address from the list will result in the deletion of an existing IP Range for this
            VRF. Deleting an IP Range will result in the deletion of any VRF IP Reservations contained within the IP Range,
            as well as the VRF IP Reservation\'s associated Metal Gateways or Virtual Circuits. If you do not wish to add or
            remove IP Ranges, either include the full existing list of IP Ranges in the update request, or do not specify
            the `ip_ranges` field in the update request. Specifying a value of `[]` will remove all existing IP Ranges from
            the VRF.
        local_asn (Union[Unset, int]): The new `local_asn` value for the VRF. This field cannot be updated when there
            are active Interconnection Virtual Circuits associated to the VRF.
        name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    ip_ranges: Union[Unset, List[str]] = UNSET
    local_asn: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_ranges, Unset):
            ip_ranges = self.ip_ranges




        local_asn = self.local_asn
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if ip_ranges is not UNSET:
            field_dict["ip_ranges"] = ip_ranges
        if local_asn is not UNSET:
            field_dict["local_asn"] = local_asn
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        ip_ranges = cast(List[str], d.pop("ip_ranges", UNSET))


        local_asn = d.pop("local_asn", UNSET)

        name = d.pop("name", UNSET)

        vrf_update_input = cls(
            description=description,
            ip_ranges=ip_ranges,
            local_asn=local_asn,
            name=name,
        )

        vrf_update_input.additional_properties = d
        return vrf_update_input

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
