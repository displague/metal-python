from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataNetworkNetworkBonding")

@attr.s(auto_attribs=True)
class MetadataNetworkNetworkBonding:
    """
    Attributes:
        link_aggregation (Union[Unset, str]):
        mac (Union[Unset, str]):
        mode (Union[Unset, int]):
    """

    link_aggregation: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        link_aggregation = self.link_aggregation
        mac = self.mac
        mode = self.mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if link_aggregation is not UNSET:
            field_dict["link_aggregation"] = link_aggregation
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_aggregation = d.pop("link_aggregation", UNSET)

        mac = d.pop("mac", UNSET)

        mode = d.pop("mode", UNSET)

        metadata_network_network_bonding = cls(
            link_aggregation=link_aggregation,
            mac=mac,
            mode=mode,
        )

        metadata_network_network_bonding.additional_properties = d
        return metadata_network_network_bonding

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
