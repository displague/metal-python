from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VrfVirtualCircuitUpdateInput")

@attr.s(auto_attribs=True)
class VrfVirtualCircuitUpdateInput:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        speed (Union[Unset, str]): Speed can be changed only if it is an interconnection on a Dedicated Port
        tags (Union[Unset, List[str]]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        speed = self.speed
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        speed = d.pop("speed", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        vrf_virtual_circuit_update_input = cls(
            description=description,
            name=name,
            speed=speed,
            tags=tags,
        )

        vrf_virtual_circuit_update_input.additional_properties = d
        return vrf_virtual_circuit_update_input

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
