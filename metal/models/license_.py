from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="License")

@attr.s(auto_attribs=True)
class License:
    """
    Attributes:
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        license_key (Union[Unset, str]):
        licensee_product (Union[Unset, Href]):
        project (Union[Unset, Href]):
        size (Union[Unset, float]):
    """

    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    license_key: Union[Unset, str] = UNSET
    licensee_product: Union[Unset, 'Href'] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        id = self.id
        license_key = self.license_key
        licensee_product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.licensee_product, Unset):
            licensee_product = self.licensee_product.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if license_key is not UNSET:
            field_dict["license_key"] = license_key
        if licensee_product is not UNSET:
            field_dict["licensee_product"] = licensee_product
        if project is not UNSET:
            field_dict["project"] = project
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        license_key = d.pop("license_key", UNSET)

        _licensee_product = d.pop("licensee_product", UNSET)
        licensee_product: Union[Unset, Href]
        if isinstance(_licensee_product,  Unset):
            licensee_product = UNSET
        else:
            licensee_product = Href.from_dict(_licensee_product)




        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        size = d.pop("size", UNSET)

        license_ = cls(
            description=description,
            id=id,
            license_key=license_key,
            licensee_product=licensee_product,
            project=project,
            size=size,
        )

        license_.additional_properties = d
        return license_

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
