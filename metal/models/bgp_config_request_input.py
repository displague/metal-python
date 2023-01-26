from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BgpConfigRequestInput")

@attr.s(auto_attribs=True)
class BgpConfigRequestInput:
    """
    Attributes:
        asn (int):
        deployment_type (str):
        md5 (Union[Unset, str]):
        use_case (Union[Unset, str]):
    """

    asn: int
    deployment_type: str
    md5: Union[Unset, str] = UNSET
    use_case: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        asn = self.asn
        deployment_type = self.deployment_type
        md5 = self.md5
        use_case = self.use_case

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "asn": asn,
            "deployment_type": deployment_type,
        })
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if use_case is not UNSET:
            field_dict["use_case"] = use_case

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asn = d.pop("asn")

        deployment_type = d.pop("deployment_type")

        md5 = d.pop("md5", UNSET)

        use_case = d.pop("use_case", UNSET)

        bgp_config_request_input = cls(
            asn=asn,
            deployment_type=deployment_type,
            md5=md5,
            use_case=use_case,
        )

        bgp_config_request_input.additional_properties = d
        return bgp_config_request_input

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
