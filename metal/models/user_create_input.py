import datetime
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
  from ..models.email_input import EmailInput
  from ..models.user_create_input_customdata import UserCreateInputCustomdata
  from ..models.user_create_input_social_accounts import UserCreateInputSocialAccounts




T = TypeVar("T", bound="UserCreateInput")

@attr.s(auto_attribs=True)
class UserCreateInput:
    """
    Attributes:
        emails (List['EmailInput']):
        first_name (str):
        last_name (str):
        avatar (Union[Unset, File]):
        company_name (Union[Unset, str]):
        company_url (Union[Unset, str]):
        customdata (Union[Unset, UserCreateInputCustomdata]):
        level (Union[Unset, str]):
        locked (Union[Unset, bool]):
        password (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        social_accounts (Union[Unset, UserCreateInputSocialAccounts]):
        timezone (Union[Unset, str]):
        title (Union[Unset, str]):
        two_factor_auth (Union[Unset, str]):
        verified_at (Union[Unset, datetime.datetime]):
        invitation_id (Union[Unset, str]):
        nonce (Union[Unset, str]):
    """

    emails: List['EmailInput']
    first_name: str
    last_name: str
    avatar: Union[Unset, File] = UNSET
    company_name: Union[Unset, str] = UNSET
    company_url: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'UserCreateInputCustomdata'] = UNSET
    level: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    password: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    social_accounts: Union[Unset, 'UserCreateInputSocialAccounts'] = UNSET
    timezone: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    two_factor_auth: Union[Unset, str] = UNSET
    verified_at: Union[Unset, datetime.datetime] = UNSET
    invitation_id: Union[Unset, str] = UNSET
    nonce: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()

            emails.append(emails_item)




        first_name = self.first_name
        last_name = self.last_name
        avatar: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_tuple()

        company_name = self.company_name
        company_url = self.company_url
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        level = self.level
        locked = self.locked
        password = self.password
        phone_number = self.phone_number
        social_accounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.social_accounts, Unset):
            social_accounts = self.social_accounts.to_dict()

        timezone = self.timezone
        title = self.title
        two_factor_auth = self.two_factor_auth
        verified_at: Union[Unset, str] = UNSET
        if not isinstance(self.verified_at, Unset):
            verified_at = self.verified_at.isoformat()

        invitation_id = self.invitation_id
        nonce = self.nonce

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "emails": emails,
            "first_name": first_name,
            "last_name": last_name,
        })
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_url is not UNSET:
            field_dict["company_url"] = company_url
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if level is not UNSET:
            field_dict["level"] = level
        if locked is not UNSET:
            field_dict["locked"] = locked
        if password is not UNSET:
            field_dict["password"] = password
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if social_accounts is not UNSET:
            field_dict["social_accounts"] = social_accounts
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if title is not UNSET:
            field_dict["title"] = title
        if two_factor_auth is not UNSET:
            field_dict["two_factor_auth"] = two_factor_auth
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if invitation_id is not UNSET:
            field_dict["invitation_id"] = invitation_id
        if nonce is not UNSET:
            field_dict["nonce"] = nonce

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_input import EmailInput
        from ..models.user_create_input_customdata import UserCreateInputCustomdata
        from ..models.user_create_input_social_accounts import UserCreateInputSocialAccounts
        d = src_dict.copy()
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in (_emails):
            emails_item = EmailInput.from_dict(emails_item_data)



            emails.append(emails_item)


        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, File]
        if isinstance(_avatar,  Unset):
            avatar = UNSET
        else:
            avatar = File(
             payload = BytesIO(_avatar)
        )




        company_name = d.pop("company_name", UNSET)

        company_url = d.pop("company_url", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, UserCreateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = UserCreateInputCustomdata.from_dict(_customdata)




        level = d.pop("level", UNSET)

        locked = d.pop("locked", UNSET)

        password = d.pop("password", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        _social_accounts = d.pop("social_accounts", UNSET)
        social_accounts: Union[Unset, UserCreateInputSocialAccounts]
        if isinstance(_social_accounts,  Unset):
            social_accounts = UNSET
        else:
            social_accounts = UserCreateInputSocialAccounts.from_dict(_social_accounts)




        timezone = d.pop("timezone", UNSET)

        title = d.pop("title", UNSET)

        two_factor_auth = d.pop("two_factor_auth", UNSET)

        _verified_at = d.pop("verified_at", UNSET)
        verified_at: Union[Unset, datetime.datetime]
        if isinstance(_verified_at,  Unset):
            verified_at = UNSET
        else:
            verified_at = isoparse(_verified_at)




        invitation_id = d.pop("invitation_id", UNSET)

        nonce = d.pop("nonce", UNSET)

        user_create_input = cls(
            emails=emails,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            company_name=company_name,
            company_url=company_url,
            customdata=customdata,
            level=level,
            locked=locked,
            password=password,
            phone_number=phone_number,
            social_accounts=social_accounts,
            timezone=timezone,
            title=title,
            two_factor_auth=two_factor_auth,
            verified_at=verified_at,
            invitation_id=invitation_id,
            nonce=nonce,
        )

        user_create_input.additional_properties = d
        return user_create_input

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
