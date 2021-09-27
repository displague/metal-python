from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VrfRouteCreateInput")

@attr.s(auto_attribs=True)
class VrfRouteCreateInput:
    """
    Attributes:
        prefix (str): The IPv4 prefix for the route, in CIDR-style notation. For a static default route, this will
            always be "0.0.0.0/0" Example: 0.0.0.0/0.
        next_hop (str): The IPv4 address within the VRF of the host that will handle this route Example: 192.168.1.254.
    """

    prefix: str
    next_hop: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        prefix = self.prefix
        next_hop = self.next_hop

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prefix": prefix,
            "next_hop": next_hop,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prefix = d.pop("prefix")

        next_hop = d.pop("next_hop")

        vrf_route_create_input = cls(
            prefix=prefix,
            next_hop=next_hop,
        )

        vrf_route_create_input.additional_properties = d
        return vrf_route_create_input

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
