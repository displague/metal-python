from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.facility import Facility




T = TypeVar("T", bound="FacilityList")

@attr.s(auto_attribs=True)
class FacilityList:
    """
    Attributes:
        facilities (Union[Unset, List['Facility']]):
    """

    facilities: Union[Unset, List['Facility']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        facilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = []
            for facilities_item_data in self.facilities:
                facilities_item = facilities_item_data.to_dict()

                facilities.append(facilities_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if facilities is not UNSET:
            field_dict["facilities"] = facilities

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.facility import Facility
        d = src_dict.copy()
        facilities = []
        _facilities = d.pop("facilities", UNSET)
        for facilities_item_data in (_facilities or []):
            facilities_item = Facility.from_dict(facilities_item_data)



            facilities.append(facilities_item)


        facility_list = cls(
            facilities=facilities,
        )

        facility_list.additional_properties = d
        return facility_list

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
