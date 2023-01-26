from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.server_info import ServerInfo




T = TypeVar("T", bound="CapacityInput")

@attr.s(auto_attribs=True)
class CapacityInput:
    """
    Attributes:
        servers (Union[Unset, List['ServerInfo']]):
    """

    servers: Union[Unset, List['ServerInfo']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()

                servers.append(servers_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_info import ServerInfo
        d = src_dict.copy()
        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in (_servers or []):
            servers_item = ServerInfo.from_dict(servers_item_data)



            servers.append(servers_item)


        capacity_input = cls(
            servers=servers,
        )

        capacity_input.additional_properties = d
        return capacity_input

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
