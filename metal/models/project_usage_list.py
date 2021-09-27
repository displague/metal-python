from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.project_usage import ProjectUsage




T = TypeVar("T", bound="ProjectUsageList")

@attr.s(auto_attribs=True)
class ProjectUsageList:
    """
    Attributes:
        usages (Union[Unset, List['ProjectUsage']]):
    """

    usages: Union[Unset, List['ProjectUsage']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        usages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.usages, Unset):
            usages = []
            for usages_item_data in self.usages:
                usages_item = usages_item_data.to_dict()

                usages.append(usages_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if usages is not UNSET:
            field_dict["usages"] = usages

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_usage import ProjectUsage
        d = src_dict.copy()
        usages = []
        _usages = d.pop("usages", UNSET)
        for usages_item_data in (_usages or []):
            usages_item = ProjectUsage.from_dict(usages_item_data)



            usages.append(usages_item)


        project_usage_list = cls(
            usages=usages,
        )

        project_usage_list.additional_properties = d
        return project_usage_list

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
