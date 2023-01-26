from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.user_update_input_customdata import UserUpdateInputCustomdata




T = TypeVar("T", bound="UserUpdateInput")

@attr.s(auto_attribs=True)
class UserUpdateInput:
    """
    Attributes:
        customdata (Union[Unset, UserUpdateInputCustomdata]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        password (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        timezone (Union[Unset, str]):
    """

    customdata: Union[Unset, 'UserUpdateInputCustomdata'] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        first_name = self.first_name
        last_name = self.last_name
        password = self.password
        phone_number = self.phone_number
        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if password is not UNSET:
            field_dict["password"] = password
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_update_input_customdata import UserUpdateInputCustomdata
        d = src_dict.copy()
        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, UserUpdateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = UserUpdateInputCustomdata.from_dict(_customdata)




        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        password = d.pop("password", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        timezone = d.pop("timezone", UNSET)

        user_update_input = cls(
            customdata=customdata,
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone_number=phone_number,
            timezone=timezone,
        )

        user_update_input.additional_properties = d
        return user_update_input

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
