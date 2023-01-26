from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.support_request_input_priority import SupportRequestInputPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportRequestInput")

@attr.s(auto_attribs=True)
class SupportRequestInput:
    """
    Attributes:
        message (str):
        subject (str):
        device_id (Union[Unset, str]):
        priority (Union[Unset, SupportRequestInputPriority]):
        project_id (Union[Unset, str]):
    """

    message: str
    subject: str
    device_id: Union[Unset, str] = UNSET
    priority: Union[Unset, SupportRequestInputPriority] = UNSET
    project_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        subject = self.subject
        device_id = self.device_id
        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "subject": subject,
        })
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        subject = d.pop("subject")

        device_id = d.pop("device_id", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, SupportRequestInputPriority]
        if isinstance(_priority,  Unset):
            priority = UNSET
        else:
            priority = SupportRequestInputPriority(_priority)




        project_id = d.pop("project_id", UNSET)

        support_request_input = cls(
            message=message,
            subject=subject,
            device_id=device_id,
            priority=priority,
            project_id=project_id,
        )

        support_request_input.additional_properties = d
        return support_request_input

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
