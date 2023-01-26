import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserLite")

@attr.s(auto_attribs=True)
class UserLite:
    """
    Attributes:
        id (str): ID of the User
        short_id (str): Short ID of the User
        avatar_thumb_url (Union[Unset, str]): Avatar thumbnail URL of the User
        created_at (Union[Unset, datetime.datetime]): When the user was created
        email (Union[Unset, str]): Primary email address of the User
        first_name (Union[Unset, str]): First name of the User
        full_name (Union[Unset, str]): Full name of the User
        href (Union[Unset, str]): API URL uniquely representing the User
        last_name (Union[Unset, str]): Last name of the User
        updated_at (Union[Unset, datetime.datetime]): When the user details were last updated
    """

    id: str
    short_id: str
    avatar_thumb_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        short_id = self.short_id
        avatar_thumb_url = self.avatar_thumb_url
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email = self.email
        first_name = self.first_name
        full_name = self.full_name
        href = self.href
        last_name = self.last_name
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "short_id": short_id,
        })
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if href is not UNSET:
            field_dict["href"] = href
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        short_id = d.pop("short_id")

        avatar_thumb_url = d.pop("avatar_thumb_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        full_name = d.pop("full_name", UNSET)

        href = d.pop("href", UNSET)

        last_name = d.pop("last_name", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        user_lite = cls(
            id=id,
            short_id=short_id,
            avatar_thumb_url=avatar_thumb_url,
            created_at=created_at,
            email=email,
            first_name=first_name,
            full_name=full_name,
            href=href,
            last_name=last_name,
            updated_at=updated_at,
        )

        user_lite.additional_properties = d
        return user_lite

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
