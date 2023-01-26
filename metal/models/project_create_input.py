from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.project_create_input_customdata import ProjectCreateInputCustomdata




T = TypeVar("T", bound="ProjectCreateInput")

@attr.s(auto_attribs=True)
class ProjectCreateInput:
    """
    Attributes:
        name (str):
        customdata (Union[Unset, ProjectCreateInputCustomdata]):
        payment_method_id (Union[Unset, str]):
    """

    name: str
    customdata: Union[Unset, 'ProjectCreateInputCustomdata'] = UNSET
    payment_method_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        payment_method_id = self.payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_create_input_customdata import ProjectCreateInputCustomdata
        d = src_dict.copy()
        name = d.pop("name")

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, ProjectCreateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = ProjectCreateInputCustomdata.from_dict(_customdata)




        payment_method_id = d.pop("payment_method_id", UNSET)

        project_create_input = cls(
            name=name,
            customdata=customdata,
            payment_method_id=payment_method_id,
        )

        project_create_input.additional_properties = d
        return project_create_input

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
