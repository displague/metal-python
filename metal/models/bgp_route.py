from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BgpRoute")

@attr.s(auto_attribs=True)
class BgpRoute:
    """
    Attributes:
        exact (Union[Unset, bool]):
        route (Union[Unset, str]):  Example: 10.32.16.0/31.
    """

    exact: Union[Unset, bool] = UNSET
    route: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        exact = self.exact
        route = self.route

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exact is not UNSET:
            field_dict["exact"] = exact
        if route is not UNSET:
            field_dict["route"] = route

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exact = d.pop("exact", UNSET)

        route = d.pop("route", UNSET)

        bgp_route = cls(
            exact=exact,
            route=route,
        )

        bgp_route.additional_properties = d
        return bgp_route

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
