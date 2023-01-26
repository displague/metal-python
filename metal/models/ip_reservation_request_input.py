from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ip_reservation_request_input_customdata import IPReservationRequestInputCustomdata




T = TypeVar("T", bound="IPReservationRequestInput")

@attr.s(auto_attribs=True)
class IPReservationRequestInput:
    """
    Attributes:
        quantity (int):
        type (str):
        comments (Union[Unset, str]):
        customdata (Union[Unset, IPReservationRequestInputCustomdata]):
        details (Union[Unset, str]):
        facility (Union[Unset, str]):
        fail_on_approval_required (Union[Unset, bool]):
        metro (Union[Unset, str]): The code of the metro you are requesting the IP reservation in. Example: SV.
        tags (Union[Unset, List[str]]):
    """

    quantity: int
    type: str
    comments: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'IPReservationRequestInputCustomdata'] = UNSET
    details: Union[Unset, str] = UNSET
    facility: Union[Unset, str] = UNSET
    fail_on_approval_required: Union[Unset, bool] = UNSET
    metro: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity
        type = self.type
        comments = self.comments
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        details = self.details
        facility = self.facility
        fail_on_approval_required = self.fail_on_approval_required
        metro = self.metro
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quantity": quantity,
            "type": type,
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if details is not UNSET:
            field_dict["details"] = details
        if facility is not UNSET:
            field_dict["facility"] = facility
        if fail_on_approval_required is not UNSET:
            field_dict["fail_on_approval_required"] = fail_on_approval_required
        if metro is not UNSET:
            field_dict["metro"] = metro
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_reservation_request_input_customdata import IPReservationRequestInputCustomdata
        d = src_dict.copy()
        quantity = d.pop("quantity")

        type = d.pop("type")

        comments = d.pop("comments", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, IPReservationRequestInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = IPReservationRequestInputCustomdata.from_dict(_customdata)




        details = d.pop("details", UNSET)

        facility = d.pop("facility", UNSET)

        fail_on_approval_required = d.pop("fail_on_approval_required", UNSET)

        metro = d.pop("metro", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        ip_reservation_request_input = cls(
            quantity=quantity,
            type=type,
            comments=comments,
            customdata=customdata,
            details=details,
            facility=facility,
            fail_on_approval_required=fail_on_approval_required,
            metro=metro,
            tags=tags,
        )

        ip_reservation_request_input.additional_properties = d
        return ip_reservation_request_input

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
