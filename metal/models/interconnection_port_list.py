from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.interconnection_port import InterconnectionPort




T = TypeVar("T", bound="InterconnectionPortList")

@attr.s(auto_attribs=True)
class InterconnectionPortList:
    """
    Attributes:
        ports (Union[Unset, List['InterconnectionPort']]):
    """

    ports: Union[Unset, List['InterconnectionPort']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()

                ports.append(ports_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interconnection_port import InterconnectionPort
        d = src_dict.copy()
        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in (_ports or []):
            ports_item = InterconnectionPort.from_dict(ports_item_data)



            ports.append(ports_item)


        interconnection_port_list = cls(
            ports=ports,
        )

        interconnection_port_list.additional_properties = d
        return interconnection_port_list

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
