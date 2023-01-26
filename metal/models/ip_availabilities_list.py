from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAvailabilitiesList")

@attr.s(auto_attribs=True)
class IPAvailabilitiesList:
    """
    Attributes:
        available (Union[Unset, List[str]]):
    """

    available: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        available: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available, Unset):
            available = self.available





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available = cast(List[str], d.pop("available", UNSET))


        ip_availabilities_list = cls(
            available=available,
        )

        ip_availabilities_list.additional_properties = d
        return ip_availabilities_list

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
