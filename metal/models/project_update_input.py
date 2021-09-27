from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.project_update_input_customdata import ProjectUpdateInputCustomdata




T = TypeVar("T", bound="ProjectUpdateInput")

@attr.s(auto_attribs=True)
class ProjectUpdateInput:
    """
    Attributes:
        backend_transfer_enabled (Union[Unset, bool]):
        customdata (Union[Unset, ProjectUpdateInputCustomdata]):
        name (Union[Unset, str]):
        payment_method_id (Union[Unset, str]):
    """

    backend_transfer_enabled: Union[Unset, bool] = UNSET
    customdata: Union[Unset, 'ProjectUpdateInputCustomdata'] = UNSET
    name: Union[Unset, str] = UNSET
    payment_method_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        backend_transfer_enabled = self.backend_transfer_enabled
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        name = self.name
        payment_method_id = self.payment_method_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if backend_transfer_enabled is not UNSET:
            field_dict["backend_transfer_enabled"] = backend_transfer_enabled
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if name is not UNSET:
            field_dict["name"] = name
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_update_input_customdata import ProjectUpdateInputCustomdata
        d = src_dict.copy()
        backend_transfer_enabled = d.pop("backend_transfer_enabled", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, ProjectUpdateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = ProjectUpdateInputCustomdata.from_dict(_customdata)




        name = d.pop("name", UNSET)

        payment_method_id = d.pop("payment_method_id", UNSET)

        project_update_input = cls(
            backend_transfer_enabled=backend_transfer_enabled,
            customdata=customdata,
            name=name,
            payment_method_id=payment_method_id,
        )

        project_update_input.additional_properties = d
        return project_update_input

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
