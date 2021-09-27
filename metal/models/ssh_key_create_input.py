from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHKeyCreateInput")

@attr.s(auto_attribs=True)
class SSHKeyCreateInput:
    """
    Attributes:
        instances_ids (Union[Unset, List[str]]): List of instance UUIDs to associate SSH key with, when empty array is
            sent all instances belonging
                  to entity will be included
        key (Union[Unset, str]):
        label (Union[Unset, str]):
    """

    instances_ids: Union[Unset, List[str]] = UNSET
    key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        instances_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instances_ids, Unset):
            instances_ids = self.instances_ids




        key = self.key
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if instances_ids is not UNSET:
            field_dict["instances_ids"] = instances_ids
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instances_ids = cast(List[str], d.pop("instances_ids", UNSET))


        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        ssh_key_create_input = cls(
            instances_ids=instances_ids,
            key=key,
            label=label,
        )

        ssh_key_create_input.additional_properties = d
        return ssh_key_create_input

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
