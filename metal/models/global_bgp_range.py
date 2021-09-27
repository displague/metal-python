from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="GlobalBgpRange")

@attr.s(auto_attribs=True)
class GlobalBgpRange:
    """
    Attributes:
        address_family (Union[Unset, int]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        project (Union[Unset, Href]):
        range_ (Union[Unset, str]):
    """

    address_family: Union[Unset, int] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    range_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family = self.address_family
        href = self.href
        id = self.id
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        range_ = self.range_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if project is not UNSET:
            field_dict["project"] = project
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        address_family = d.pop("address_family", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        range_ = d.pop("range", UNSET)

        global_bgp_range = cls(
            address_family=address_family,
            href=href,
            id=id,
            project=project,
            range_=range_,
        )

        global_bgp_range.additional_properties = d
        return global_bgp_range

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
