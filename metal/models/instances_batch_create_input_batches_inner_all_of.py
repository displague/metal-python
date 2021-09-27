from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstancesBatchCreateInputBatchesInnerAllOf")

@attr.s(auto_attribs=True)
class InstancesBatchCreateInputBatchesInnerAllOf:
    """
    Attributes:
        hostnames (Union[Unset, List[str]]):
        quantity (Union[Unset, int]): The number of devices to create in this batch. The hostname may contain an
            `{{index}}` placeholder, which will be replaced with the index of the device in the batch. For example, if the
            hostname is `device-{{index}}`, the first device in the batch will have the hostname `device-01`, the second
            device will have the hostname `device-02`, and so on.
    """

    hostnames: Union[Unset, List[str]] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        hostnames: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames




        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hostnames = cast(List[str], d.pop("hostnames", UNSET))


        quantity = d.pop("quantity", UNSET)

        instances_batch_create_input_batches_inner_all_of = cls(
            hostnames=hostnames,
            quantity=quantity,
        )

        instances_batch_create_input_batches_inner_all_of.additional_properties = d
        return instances_batch_create_input_batches_inner_all_of

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
