from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.meta import Meta
  from ..models.organization import Organization




T = TypeVar("T", bound="OrganizationList")

@attr.s(auto_attribs=True)
class OrganizationList:
    """
    Attributes:
        meta (Union[Unset, Meta]):
        organizations (Union[Unset, List['Organization']]):
    """

    meta: Union[Unset, 'Meta'] = UNSET
    organizations: Union[Unset, List['Organization']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()

                organizations.append(organizations_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if meta is not UNSET:
            field_dict["meta"] = meta
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meta import Meta
        from ..models.organization import Organization
        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)




        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in (_organizations or []):
            organizations_item = Organization.from_dict(organizations_item_data)



            organizations.append(organizations_item)


        organization_list = cls(
            meta=meta,
            organizations=organizations,
        )

        organization_list.additional_properties = d
        return organization_list

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
