from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAssignmentMetro")

@attr.s(auto_attribs=True)
class IPAssignmentMetro:
    """
    Attributes:
        code (Union[Unset, str]):
        country (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        country = self.country
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if country is not UNSET:
            field_dict["country"] = country
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        country = d.pop("country", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ip_assignment_metro = cls(
            code=code,
            country=country,
            id=id,
            name=name,
        )

        ip_assignment_metro.additional_properties = d
        return ip_assignment_metro

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
