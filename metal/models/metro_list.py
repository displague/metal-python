from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metro import Metro




T = TypeVar("T", bound="MetroList")

@attr.s(auto_attribs=True)
class MetroList:
    """
    Attributes:
        metros (Union[Unset, List['Metro']]):
    """

    metros: Union[Unset, List['Metro']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        metros: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metros, Unset):
            metros = []
            for metros_item_data in self.metros:
                metros_item = metros_item_data.to_dict()

                metros.append(metros_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metros is not UNSET:
            field_dict["metros"] = metros

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metro import Metro
        d = src_dict.copy()
        metros = []
        _metros = d.pop("metros", UNSET)
        for metros_item_data in (_metros or []):
            metros_item = Metro.from_dict(metros_item_data)



            metros.append(metros_item)


        metro_list = cls(
            metros=metros,
        )

        metro_list.additional_properties = d
        return metro_list

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
