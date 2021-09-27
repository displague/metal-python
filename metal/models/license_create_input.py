from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseCreateInput")

@attr.s(auto_attribs=True)
class LicenseCreateInput:
    """
    Attributes:
        description (Union[Unset, str]):
        licensee_product_id (Union[Unset, str]):
        size (Union[Unset, float]):
    """

    description: Union[Unset, str] = UNSET
    licensee_product_id: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        licensee_product_id = self.licensee_product_id
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if licensee_product_id is not UNSET:
            field_dict["licensee_product_id"] = licensee_product_id
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        licensee_product_id = d.pop("licensee_product_id", UNSET)

        size = d.pop("size", UNSET)

        license_create_input = cls(
            description=description,
            licensee_product_id=licensee_product_id,
            size=size,
        )

        license_create_input.additional_properties = d
        return license_create_input

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
