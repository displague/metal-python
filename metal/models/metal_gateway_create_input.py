from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetalGatewayCreateInput")

@attr.s(auto_attribs=True)
class MetalGatewayCreateInput:
    """
    Attributes:
        virtual_network_id (str): The UUID of a metro virtual network that belongs to the same project as where the
            metal gateway will be created in.
        ip_reservation_id (Union[Unset, str]): The UUID of an IP reservation that belongs to the same project as where
            the metal gateway will be created in. This field is required unless the private IPv4 subnet size is specified.
        private_ipv4_subnet_size (Union[Unset, int]): The subnet size (8, 16, 32, 64, or 128) of the private IPv4
            reservation that will be created for the metal gateway. This field is required unless a project IP reservation
            was specified.
                      Please keep in mind that the number of private metal gateway ranges are limited per project. If you
            would like to increase the limit per project, please contact support for assistance.
    """

    virtual_network_id: str
    ip_reservation_id: Union[Unset, str] = UNSET
    private_ipv4_subnet_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        virtual_network_id = self.virtual_network_id
        ip_reservation_id = self.ip_reservation_id
        private_ipv4_subnet_size = self.private_ipv4_subnet_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "virtual_network_id": virtual_network_id,
        })
        if ip_reservation_id is not UNSET:
            field_dict["ip_reservation_id"] = ip_reservation_id
        if private_ipv4_subnet_size is not UNSET:
            field_dict["private_ipv4_subnet_size"] = private_ipv4_subnet_size

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        virtual_network_id = d.pop("virtual_network_id")

        ip_reservation_id = d.pop("ip_reservation_id", UNSET)

        private_ipv4_subnet_size = d.pop("private_ipv4_subnet_size", UNSET)

        metal_gateway_create_input = cls(
            virtual_network_id=virtual_network_id,
            ip_reservation_id=ip_reservation_id,
            private_ipv4_subnet_size=private_ipv4_subnet_size,
        )

        metal_gateway_create_input.additional_properties = d
        return metal_gateway_create_input

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
