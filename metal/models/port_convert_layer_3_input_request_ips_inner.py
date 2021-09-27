from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortConvertLayer3InputRequestIpsInner")

@attr.s(auto_attribs=True)
class PortConvertLayer3InputRequestIpsInner:
    """
    Attributes:
        address_family (Union[Unset, int]):
        public (Union[Unset, bool]):
    """

    address_family: Union[Unset, int] = UNSET
    public: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family = self.address_family
        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_family is not UNSET:
            field_dict["address_family"] = address_family
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_family = d.pop("address_family", UNSET)

        public = d.pop("public", UNSET)

        port_convert_layer_3_input_request_ips_inner = cls(
            address_family=address_family,
            public=public,
        )

        port_convert_layer_3_input_request_ips_inner.additional_properties = d
        return port_convert_layer_3_input_request_ips_inner

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
