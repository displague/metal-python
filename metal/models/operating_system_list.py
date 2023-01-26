from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operating_system import OperatingSystem




T = TypeVar("T", bound="OperatingSystemList")

@attr.s(auto_attribs=True)
class OperatingSystemList:
    """
    Attributes:
        operating_systems (Union[Unset, List['OperatingSystem']]):
    """

    operating_systems: Union[Unset, List['OperatingSystem']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        operating_systems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.operating_systems, Unset):
            operating_systems = []
            for operating_systems_item_data in self.operating_systems:
                operating_systems_item = operating_systems_item_data.to_dict()

                operating_systems.append(operating_systems_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operating_systems is not UNSET:
            field_dict["operating_systems"] = operating_systems

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operating_system import OperatingSystem
        d = src_dict.copy()
        operating_systems = []
        _operating_systems = d.pop("operating_systems", UNSET)
        for operating_systems_item_data in (_operating_systems or []):
            operating_systems_item = OperatingSystem.from_dict(operating_systems_item_data)



            operating_systems.append(operating_systems_item)


        operating_system_list = cls(
            operating_systems=operating_systems,
        )

        operating_system_list.additional_properties = d
        return operating_system_list

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
