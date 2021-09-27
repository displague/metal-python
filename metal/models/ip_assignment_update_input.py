from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ip_assignment_update_input_customdata import IPAssignmentUpdateInputCustomdata




T = TypeVar("T", bound="IPAssignmentUpdateInput")

@attr.s(auto_attribs=True)
class IPAssignmentUpdateInput:
    """
    Attributes:
        details (Union[Unset, str]):
        customdata (Union[Unset, IPAssignmentUpdateInputCustomdata]):
        tags (Union[Unset, List[str]]):
    """

    details: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'IPAssignmentUpdateInputCustomdata'] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        details = self.details
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if details is not UNSET:
            field_dict["details"] = details
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_assignment_update_input_customdata import IPAssignmentUpdateInputCustomdata
        d = src_dict.copy()
        details = d.pop("details", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, IPAssignmentUpdateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = IPAssignmentUpdateInputCustomdata.from_dict(_customdata)




        tags = cast(List[str], d.pop("tags", UNSET))


        ip_assignment_update_input = cls(
            details=details,
            customdata=customdata,
            tags=tags,
        )

        ip_assignment_update_input.additional_properties = d
        return ip_assignment_update_input

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
