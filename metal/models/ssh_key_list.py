from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.ssh_key import SSHKey




T = TypeVar("T", bound="SSHKeyList")

@attr.s(auto_attribs=True)
class SSHKeyList:
    """
    Attributes:
        ssh_keys (Union[Unset, List['SSHKey']]):
    """

    ssh_keys: Union[Unset, List['SSHKey']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ssh_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = []
            for ssh_keys_item_data in self.ssh_keys:
                ssh_keys_item = ssh_keys_item_data.to_dict()

                ssh_keys.append(ssh_keys_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ssh_key import SSHKey
        d = src_dict.copy()
        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in (_ssh_keys or []):
            ssh_keys_item = SSHKey.from_dict(ssh_keys_item_data)



            ssh_keys.append(ssh_keys_item)


        ssh_key_list = cls(
            ssh_keys=ssh_keys,
        )

        ssh_key_list.additional_properties = d
        return ssh_key_list

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
