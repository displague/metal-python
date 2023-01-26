import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.auth_token_project import AuthTokenProject
  from ..models.auth_token_user import AuthTokenUser




T = TypeVar("T", bound="AuthToken")

@attr.s(auto_attribs=True)
class AuthToken:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]): Available only for API keys
        id (Union[Unset, str]):
        project (Union[Unset, AuthTokenProject]):
        read_only (Union[Unset, bool]):
        token (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, AuthTokenUser]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    project: Union[Unset, 'AuthTokenProject'] = UNSET
    read_only: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, 'AuthTokenUser'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description
        id = self.id
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        read_only = self.read_only
        token = self.token
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if project is not UNSET:
            field_dict["project"] = project
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if token is not UNSET:
            field_dict["token"] = token
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auth_token_project import AuthTokenProject
        from ..models.auth_token_user import AuthTokenUser
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, AuthTokenProject]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = AuthTokenProject.from_dict(_project)




        read_only = d.pop("read_only", UNSET)

        token = d.pop("token", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        _user = d.pop("user", UNSET)
        user: Union[Unset, AuthTokenUser]
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = AuthTokenUser.from_dict(_user)




        auth_token = cls(
            created_at=created_at,
            description=description,
            id=id,
            project=project,
            read_only=read_only,
            token=token,
            updated_at=updated_at,
            user=user,
        )

        auth_token.additional_properties = d
        return auth_token

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
