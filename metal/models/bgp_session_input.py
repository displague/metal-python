from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bgp_session_input_address_family import BGPSessionInputAddressFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="BGPSessionInput")

@attr.s(auto_attribs=True)
class BGPSessionInput:
    """
    Attributes:
        address_family (Union[Unset, BGPSessionInputAddressFamily]): Address family for BGP session. Example: ipv4.
        default_route (Union[Unset, bool]): Set the default route policy.
    """

    address_family: Union[Unset, BGPSessionInputAddressFamily] = UNSET
    default_route: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family: Union[Unset, str] = UNSET
        if not isinstance(self.address_family, Unset):
            address_family = self.address_family.value

        default_route = self.default_route

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if default_route is not UNSET:
            field_dict["default_route"] = default_route

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _address_family = d.pop("address_family", UNSET)
        address_family: Union[Unset, BGPSessionInputAddressFamily]
        if isinstance(_address_family,  Unset):
            address_family = UNSET
        else:
            address_family = BGPSessionInputAddressFamily(_address_family)




        default_route = d.pop("default_route", UNSET)

        bgp_session_input = cls(
            address_family=address_family,
            default_route=default_route,
        )

        bgp_session_input.additional_properties = d
        return bgp_session_input

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
