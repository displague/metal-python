from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.meta import Meta
  from ..models.project import Project




T = TypeVar("T", bound="ProjectList")

@attr.s(auto_attribs=True)
class ProjectList:
    """
    Attributes:
        meta (Union[Unset, Meta]):
        projects (Union[Unset, List['Project']]):
    """

    meta: Union[Unset, 'Meta'] = UNSET
    projects: Union[Unset, List['Project']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if meta is not UNSET:
            field_dict["meta"] = meta
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meta import Meta
        from ..models.project import Project
        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)




        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in (_projects or []):
            projects_item = Project.from_dict(projects_item_data)



            projects.append(projects_item)


        project_list = cls(
            meta=meta,
            projects=projects,
        )

        project_list.additional_properties = d
        return project_list

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
