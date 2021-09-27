from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ip_reservation import IPReservation
  from ..models.vrf_ip_reservation import VrfIpReservation




T = TypeVar("T", bound="IPReservationList")

@attr.s(auto_attribs=True)
class IPReservationList:
    """
    Attributes:
        ip_addresses (Union[Unset, List[Union['IPReservation', 'VrfIpReservation']]]):
    """

    ip_addresses: Union[Unset, List[Union['IPReservation', 'VrfIpReservation']]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.ip_reservation import IPReservation
        ip_addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = []
            for ip_addresses_item_data in self.ip_addresses:
                ip_addresses_item: Dict[str, Any]

                if isinstance(ip_addresses_item_data, IPReservation):
                    ip_addresses_item = ip_addresses_item_data.to_dict()

                else:
                    ip_addresses_item = ip_addresses_item_data.to_dict()



                ip_addresses.append(ip_addresses_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_reservation import IPReservation
        from ..models.vrf_ip_reservation import VrfIpReservation
        d = src_dict.copy()
        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses", UNSET)
        for ip_addresses_item_data in (_ip_addresses or []):
            def _parse_ip_addresses_item(data: object) -> Union['IPReservation', 'VrfIpReservation']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ip_reservation_list_ip_addresses_inner_type_0 = IPReservation.from_dict(data)



                    return componentsschemas_ip_reservation_list_ip_addresses_inner_type_0
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ip_reservation_list_ip_addresses_inner_type_1 = VrfIpReservation.from_dict(data)



                return componentsschemas_ip_reservation_list_ip_addresses_inner_type_1

            ip_addresses_item = _parse_ip_addresses_item(ip_addresses_item_data)

            ip_addresses.append(ip_addresses_item)


        ip_reservation_list = cls(
            ip_addresses=ip_addresses,
        )

        ip_reservation_list.additional_properties = d
        return ip_reservation_list

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
