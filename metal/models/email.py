from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Email")

@attr.s(auto_attribs=True)
class Email:
    """
    Attributes:
        address (Union[Unset, str]):
        default (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        verified (Union[Unset, bool]):
    """

    address: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    verified: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        default = self.default
        href = self.href
        id = self.id
        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if default is not UNSET:
            field_dict["default"] = default
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        default = d.pop("default", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        verified = d.pop("verified", UNSET)

        email = cls(
            address=address,
            default=default,
            href=href,
            id=id,
            verified=verified,
        )

        email.additional_properties = d
        return email

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
