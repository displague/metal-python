from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.interconnection import Interconnection




T = TypeVar("T", bound="InterconnectionList")

@attr.s(auto_attribs=True)
class InterconnectionList:
    """
    Attributes:
        interconnections (Union[Unset, List['Interconnection']]):
    """

    interconnections: Union[Unset, List['Interconnection']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        interconnections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interconnections, Unset):
            interconnections = []
            for interconnections_item_data in self.interconnections:
                interconnections_item = interconnections_item_data.to_dict()

                interconnections.append(interconnections_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if interconnections is not UNSET:
            field_dict["interconnections"] = interconnections

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interconnection import Interconnection
        d = src_dict.copy()
        interconnections = []
        _interconnections = d.pop("interconnections", UNSET)
        for interconnections_item_data in (_interconnections or []):
            interconnections_item = Interconnection.from_dict(interconnections_item_data)



            interconnections.append(interconnections_item)


        interconnection_list = cls(
            interconnections=interconnections,
        )

        interconnection_list.additional_properties = d
        return interconnection_list

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
