from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VrfMetalGatewayCreateInput")

@attr.s(auto_attribs=True)
class VrfMetalGatewayCreateInput:
    """
    Attributes:
        ip_reservation_id (str): The UUID an a VRF IP Reservation that belongs to the same project as the one in which
            the Metal Gateway is to be created. Additionally, the VRF IP Reservation and the Virtual Network must reside in
            the same Metro.
        virtual_network_id (str): THe UUID of a Metro Virtual Network that belongs to the same project as the one in
            which the Metal Gateway is to be created. Additionally, the Virtual Network and the VRF IP Reservation must
            reside in the same metro.
    """

    ip_reservation_id: str
    virtual_network_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ip_reservation_id = self.ip_reservation_id
        virtual_network_id = self.virtual_network_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ip_reservation_id": ip_reservation_id,
            "virtual_network_id": virtual_network_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_reservation_id = d.pop("ip_reservation_id")

        virtual_network_id = d.pop("virtual_network_id")

        vrf_metal_gateway_create_input = cls(
            ip_reservation_id=ip_reservation_id,
            virtual_network_id=virtual_network_id,
        )

        vrf_metal_gateway_create_input.additional_properties = d
        return vrf_metal_gateway_create_input

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
