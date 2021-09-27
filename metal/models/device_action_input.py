from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.device_action_input_type import DeviceActionInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceActionInput")

@attr.s(auto_attribs=True)
class DeviceActionInput:
    """
    Attributes:
        type (DeviceActionInputType): Action to perform. See Device.actions for possible actions.
        force_delete (Union[Unset, bool]): May be required to perform actions under certain conditions
        deprovision_fast (Union[Unset, bool]): When type is `reinstall`, enabling fast deprovisioning will bypass full
            disk wiping.
        preserve_data (Union[Unset, bool]): When type is `reinstall`, preserve the existing data on all disks except the
            operating-system disk.
        operating_system (Union[Unset, str]): When type is `reinstall`, use this `operating_system` (defaults to the
            current `operating system`) Example: ubuntu_22_04.
        ipxe_script_url (Union[Unset, str]): When type is `reinstall`, use this `ipxe_script_url` (`operating_system`
            must be `custom_ipxe`, defaults to the current `ipxe_script_url`)
    """

    type: DeviceActionInputType
    force_delete: Union[Unset, bool] = UNSET
    deprovision_fast: Union[Unset, bool] = UNSET
    preserve_data: Union[Unset, bool] = UNSET
    operating_system: Union[Unset, str] = UNSET
    ipxe_script_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        force_delete = self.force_delete
        deprovision_fast = self.deprovision_fast
        preserve_data = self.preserve_data
        operating_system = self.operating_system
        ipxe_script_url = self.ipxe_script_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type,
        })
        if force_delete is not UNSET:
            field_dict["force_delete"] = force_delete
        if deprovision_fast is not UNSET:
            field_dict["deprovision_fast"] = deprovision_fast
        if preserve_data is not UNSET:
            field_dict["preserve_data"] = preserve_data
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if ipxe_script_url is not UNSET:
            field_dict["ipxe_script_url"] = ipxe_script_url

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DeviceActionInputType(d.pop("type"))




        force_delete = d.pop("force_delete", UNSET)

        deprovision_fast = d.pop("deprovision_fast", UNSET)

        preserve_data = d.pop("preserve_data", UNSET)

        operating_system = d.pop("operating_system", UNSET)

        ipxe_script_url = d.pop("ipxe_script_url", UNSET)

        device_action_input = cls(
            type=type,
            force_delete=force_delete,
            deprovision_fast=deprovision_fast,
            preserve_data=preserve_data,
            operating_system=operating_system,
            ipxe_script_url=ipxe_script_url,
        )

        device_action_input.additional_properties = d
        return device_action_input

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
