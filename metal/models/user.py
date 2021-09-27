import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.user_customdata import UserCustomdata




T = TypeVar("T", bound="User")

@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        avatar_thumb_url (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        customdata (Union[Unset, UserCustomdata]):
        email (Union[Unset, str]):
        emails (Union[Unset, List['Href']]):
        first_name (Union[Unset, str]):
        fraud_score (Union[Unset, str]):
        full_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_login_at (Union[Unset, datetime.datetime]):
        last_name (Union[Unset, str]):
        max_organizations (Union[Unset, int]):
        max_projects (Union[Unset, int]):
        phone_number (Union[Unset, str]):
        short_id (Union[Unset, str]):
        timezone (Union[Unset, str]):
        two_factor_auth (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    avatar_thumb_url: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    customdata: Union[Unset, 'UserCustomdata'] = UNSET
    email: Union[Unset, str] = UNSET
    emails: Union[Unset, List['Href']] = UNSET
    first_name: Union[Unset, str] = UNSET
    fraud_score: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_login_at: Union[Unset, datetime.datetime] = UNSET
    last_name: Union[Unset, str] = UNSET
    max_organizations: Union[Unset, int] = UNSET
    max_projects: Union[Unset, int] = UNSET
    phone_number: Union[Unset, str] = UNSET
    short_id: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    two_factor_auth: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        avatar_thumb_url = self.avatar_thumb_url
        avatar_url = self.avatar_url
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        email = self.email
        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()

                emails.append(emails_item)




        first_name = self.first_name
        fraud_score = self.fraud_score
        full_name = self.full_name
        href = self.href
        id = self.id
        last_login_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_login_at, Unset):
            last_login_at = self.last_login_at.isoformat()

        last_name = self.last_name
        max_organizations = self.max_organizations
        max_projects = self.max_projects
        phone_number = self.phone_number
        short_id = self.short_id
        timezone = self.timezone
        two_factor_auth = self.two_factor_auth
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if email is not UNSET:
            field_dict["email"] = email
        if emails is not UNSET:
            field_dict["emails"] = emails
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if fraud_score is not UNSET:
            field_dict["fraud_score"] = fraud_score
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_login_at is not UNSET:
            field_dict["last_login_at"] = last_login_at
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if max_organizations is not UNSET:
            field_dict["max_organizations"] = max_organizations
        if max_projects is not UNSET:
            field_dict["max_projects"] = max_projects
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if short_id is not UNSET:
            field_dict["short_id"] = short_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if two_factor_auth is not UNSET:
            field_dict["two_factor_auth"] = two_factor_auth
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.user_customdata import UserCustomdata
        d = src_dict.copy()
        avatar_thumb_url = d.pop("avatar_thumb_url", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, UserCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = UserCustomdata.from_dict(_customdata)




        email = d.pop("email", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in (_emails or []):
            emails_item = Href.from_dict(emails_item_data)



            emails.append(emails_item)


        first_name = d.pop("first_name", UNSET)

        fraud_score = d.pop("fraud_score", UNSET)

        full_name = d.pop("full_name", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_login_at = d.pop("last_login_at", UNSET)
        last_login_at: Union[Unset, datetime.datetime]
        if isinstance(_last_login_at,  Unset):
            last_login_at = UNSET
        else:
            last_login_at = isoparse(_last_login_at)




        last_name = d.pop("last_name", UNSET)

        max_organizations = d.pop("max_organizations", UNSET)

        max_projects = d.pop("max_projects", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        short_id = d.pop("short_id", UNSET)

        timezone = d.pop("timezone", UNSET)

        two_factor_auth = d.pop("two_factor_auth", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        user = cls(
            avatar_thumb_url=avatar_thumb_url,
            avatar_url=avatar_url,
            created_at=created_at,
            customdata=customdata,
            email=email,
            emails=emails,
            first_name=first_name,
            fraud_score=fraud_score,
            full_name=full_name,
            href=href,
            id=id,
            last_login_at=last_login_at,
            last_name=last_name,
            max_organizations=max_organizations,
            max_projects=max_projects,
            phone_number=phone_number,
            short_id=short_id,
            timezone=timezone,
            two_factor_auth=two_factor_auth,
            updated_at=updated_at,
        )

        user.additional_properties = d
        return user

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
