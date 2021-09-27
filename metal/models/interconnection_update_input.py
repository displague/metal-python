from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.interconnection_update_input_mode import InterconnectionUpdateInputMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterconnectionUpdateInput")

@attr.s(auto_attribs=True)
class InterconnectionUpdateInput:
    """
    Attributes:
        contact_email (Union[Unset, str]):
        description (Union[Unset, str]):
        mode (Union[Unset, InterconnectionUpdateInputMode]): The mode of the interconnection (only relevant to Dedicated
            Ports). Shared connections won't have this field. Can be either 'standard' or 'tunnel'.
              The default mode of an interconnection on a Dedicated Port is 'standard'. The mode can only be changed when
            there are no associated virtual circuits on the interconnection.
              In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server
            instances. Example: standard.
        name (Union[Unset, str]):
        redundancy (Union[Unset, str]): Updating from 'redundant' to 'primary' will remove a secondary port, while
            updating from 'primary' to 'redundant' will add one.
        tags (Union[Unset, List[str]]):
    """

    contact_email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, InterconnectionUpdateInputMode] = UNSET
    name: Union[Unset, str] = UNSET
    redundancy: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        contact_email = self.contact_email
        description = self.description
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        name = self.name
        redundancy = self.redundancy
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if redundancy is not UNSET:
            field_dict["redundancy"] = redundancy
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_email = d.pop("contact_email", UNSET)

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, InterconnectionUpdateInputMode]
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = InterconnectionUpdateInputMode(_mode)




        name = d.pop("name", UNSET)

        redundancy = d.pop("redundancy", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        interconnection_update_input = cls(
            contact_email=contact_email,
            description=description,
            mode=mode,
            name=name,
            redundancy=redundancy,
            tags=tags,
        )

        interconnection_update_input.additional_properties = d
        return interconnection_update_input

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
