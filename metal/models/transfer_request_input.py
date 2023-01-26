from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferRequestInput")

@attr.s(auto_attribs=True)
class TransferRequestInput:
    """
    Attributes:
        target_organization_id (Union[Unset, str]):
    """

    target_organization_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        target_organization_id = self.target_organization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if target_organization_id is not UNSET:
            field_dict["target_organization_id"] = target_organization_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_organization_id = d.pop("target_organization_id", UNSET)

        transfer_request_input = cls(
            target_organization_id=target_organization_id,
        )

        transfer_request_input.additional_properties = d
        return transfer_request_input

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
