from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ip_assignment_input_customdata import IPAssignmentInputCustomdata




T = TypeVar("T", bound="IPAssignmentInput")

@attr.s(auto_attribs=True)
class IPAssignmentInput:
    """
    Attributes:
        address (str):
        customdata (Union[Unset, IPAssignmentInputCustomdata]):
        manageable (Union[Unset, bool]):
    """

    address: str
    customdata: Union[Unset, 'IPAssignmentInputCustomdata'] = UNSET
    manageable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        manageable = self.manageable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "address": address,
        })
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if manageable is not UNSET:
            field_dict["manageable"] = manageable

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_assignment_input_customdata import IPAssignmentInputCustomdata
        d = src_dict.copy()
        address = d.pop("address")

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, IPAssignmentInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = IPAssignmentInputCustomdata.from_dict(_customdata)




        manageable = d.pop("manageable", UNSET)

        ip_assignment_input = cls(
            address=address,
            customdata=customdata,
            manageable=manageable,
        )

        ip_assignment_input.additional_properties = d
        return ip_assignment_input

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
