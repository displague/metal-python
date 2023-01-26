from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.project_create_from_root_input_customdata import ProjectCreateFromRootInputCustomdata




T = TypeVar("T", bound="ProjectCreateFromRootInput")

@attr.s(auto_attribs=True)
class ProjectCreateFromRootInput:
    """
    Attributes:
        name (str):
        customdata (Union[Unset, ProjectCreateFromRootInputCustomdata]):
        organization_id (Union[Unset, str]):
        payment_method_id (Union[Unset, str]):
    """

    name: str
    customdata: Union[Unset, 'ProjectCreateFromRootInputCustomdata'] = UNSET
    organization_id: Union[Unset, str] = UNSET
    payment_method_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        organization_id = self.organization_id
        payment_method_id = self.payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_create_from_root_input_customdata import ProjectCreateFromRootInputCustomdata
        d = src_dict.copy()
        name = d.pop("name")

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, ProjectCreateFromRootInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = ProjectCreateFromRootInputCustomdata.from_dict(_customdata)




        organization_id = d.pop("organization_id", UNSET)

        payment_method_id = d.pop("payment_method_id", UNSET)

        project_create_from_root_input = cls(
            name=name,
            customdata=customdata,
            organization_id=organization_id,
            payment_method_id=payment_method_id,
        )

        project_create_from_root_input.additional_properties = d
        return project_create_from_root_input

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
