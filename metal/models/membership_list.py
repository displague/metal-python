from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.membership import Membership




T = TypeVar("T", bound="MembershipList")

@attr.s(auto_attribs=True)
class MembershipList:
    """
    Attributes:
        memberships (Union[Unset, List['Membership']]):
    """

    memberships: Union[Unset, List['Membership']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        memberships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()

                memberships.append(memberships_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if memberships is not UNSET:
            field_dict["memberships"] = memberships

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.membership import Membership
        d = src_dict.copy()
        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in (_memberships or []):
            memberships_item = Membership.from_dict(memberships_item_data)



            memberships.append(memberships_item)


        membership_list = cls(
            memberships=memberships,
        )

        membership_list.additional_properties = d
        return membership_list

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
