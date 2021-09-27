from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParentBlock")

@attr.s(auto_attribs=True)
class ParentBlock:
    """
    Attributes:
        cidr (Union[Unset, int]):
        href (Union[Unset, str]):
        netmask (Union[Unset, str]):
        network (Union[Unset, str]):
    """

    cidr: Union[Unset, int] = UNSET
    href: Union[Unset, str] = UNSET
    netmask: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        cidr = self.cidr
        href = self.href
        netmask = self.netmask
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if href is not UNSET:
            field_dict["href"] = href
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cidr = d.pop("cidr", UNSET)

        href = d.pop("href", UNSET)

        netmask = d.pop("netmask", UNSET)

        network = d.pop("network", UNSET)

        parent_block = cls(
            cidr=cidr,
            href=href,
            netmask=netmask,
            network=network,
        )

        parent_block.additional_properties = d
        return parent_block

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
