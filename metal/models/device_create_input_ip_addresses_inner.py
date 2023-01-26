from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.device_create_input_ip_addresses_inner_address_family import (
    DeviceCreateInputIpAddressesInnerAddressFamily,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceCreateInputIpAddressesInner")

@attr.s(auto_attribs=True)
class DeviceCreateInputIpAddressesInner:
    """
    Attributes:
        address_family (Union[Unset, DeviceCreateInputIpAddressesInnerAddressFamily]): Address Family for IP Address
            Example: 4.
        cidr (Union[Unset, float]): Cidr Size for the IP Block created. Valid values depends on the operating system
            being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses) Example: 28.
        ip_reservations (Union[Unset, List[str]]): UUIDs of any IP reservations to use when assigning IPs
        public (Union[Unset, bool]): Address Type for IP Address Default: True.
    """

    address_family: Union[Unset, DeviceCreateInputIpAddressesInnerAddressFamily] = UNSET
    cidr: Union[Unset, float] = UNSET
    ip_reservations: Union[Unset, List[str]] = UNSET
    public: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family: Union[Unset, int] = UNSET
        if not isinstance(self.address_family, Unset):
            address_family = self.address_family.value

        cidr = self.cidr
        ip_reservations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_reservations, Unset):
            ip_reservations = self.ip_reservations




        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if ip_reservations is not UNSET:
            field_dict["ip_reservations"] = ip_reservations
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _address_family = d.pop("address_family", UNSET)
        address_family: Union[Unset, DeviceCreateInputIpAddressesInnerAddressFamily]
        if isinstance(_address_family,  Unset):
            address_family = UNSET
        else:
            address_family = DeviceCreateInputIpAddressesInnerAddressFamily(_address_family)




        cidr = d.pop("cidr", UNSET)

        ip_reservations = cast(List[str], d.pop("ip_reservations", UNSET))


        public = d.pop("public", UNSET)

        device_create_input_ip_addresses_inner = cls(
            address_family=address_family,
            cidr=cidr,
            ip_reservations=ip_reservations,
            public=public,
        )

        device_create_input_ip_addresses_inner.additional_properties = d
        return device_create_input_ip_addresses_inner

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
