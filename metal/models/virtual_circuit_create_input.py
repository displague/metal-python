from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualCircuitCreateInput")

@attr.s(auto_attribs=True)
class VirtualCircuitCreateInput:
    """
    Attributes:
        project_id (str):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        nni_vlan (Union[Unset, int]):
        speed (Union[Unset, int]): speed can be passed as integer number representing bps speed or string (e.g. '52m' or
            '100g' or '4 gbps')
        tags (Union[Unset, List[str]]):
        vnid (Union[Unset, str]): A Virtual Network record UUID or the VNID of a Metro Virtual Network in your project
            (sent as integer).
    """

    project_id: str
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nni_vlan: Union[Unset, int] = UNSET
    speed: Union[Unset, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    vnid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        description = self.description
        name = self.name
        nni_vlan = self.nni_vlan
        speed = self.speed
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        vnid = self.vnid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if nni_vlan is not UNSET:
            field_dict["nni_vlan"] = nni_vlan
        if speed is not UNSET:
            field_dict["speed"] = speed
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vnid is not UNSET:
            field_dict["vnid"] = vnid

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("project_id")

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        nni_vlan = d.pop("nni_vlan", UNSET)

        speed = d.pop("speed", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        vnid = d.pop("vnid", UNSET)

        virtual_circuit_create_input = cls(
            project_id=project_id,
            description=description,
            name=name,
            nni_vlan=nni_vlan,
            speed=speed,
            tags=tags,
            vnid=vnid,
        )

        virtual_circuit_create_input.additional_properties = d
        return virtual_circuit_create_input

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
