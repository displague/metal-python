from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.license_ import License




T = TypeVar("T", bound="LicenseList")

@attr.s(auto_attribs=True)
class LicenseList:
    """
    Attributes:
        licenses (Union[Unset, List['License']]):
    """

    licenses: Union[Unset, List['License']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        licenses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()

                licenses.append(licenses_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if licenses is not UNSET:
            field_dict["licenses"] = licenses

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.license_ import License
        d = src_dict.copy()
        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in (_licenses or []):
            licenses_item = License.from_dict(licenses_item_data)



            licenses.append(licenses_item)


        license_list = cls(
            licenses=licenses,
        )

        license_list.additional_properties = d
        return license_list

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
