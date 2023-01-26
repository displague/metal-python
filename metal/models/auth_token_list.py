from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.auth_token import AuthToken




T = TypeVar("T", bound="AuthTokenList")

@attr.s(auto_attribs=True)
class AuthTokenList:
    """
    Attributes:
        api_keys (Union[Unset, List['AuthToken']]):
    """

    api_keys: Union[Unset, List['AuthToken']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        api_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()

                api_keys.append(api_keys_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auth_token import AuthToken
        d = src_dict.copy()
        api_keys = []
        _api_keys = d.pop("api_keys", UNSET)
        for api_keys_item_data in (_api_keys or []):
            api_keys_item = AuthToken.from_dict(api_keys_item_data)



            api_keys.append(api_keys_item)


        auth_token_list = cls(
            api_keys=api_keys,
        )

        auth_token_list.additional_properties = d
        return auth_token_list

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
