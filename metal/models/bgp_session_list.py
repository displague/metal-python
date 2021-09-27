from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bgp_session import BgpSession




T = TypeVar("T", bound="BgpSessionList")

@attr.s(auto_attribs=True)
class BgpSessionList:
    """
    Attributes:
        bgp_sessions (Union[Unset, List['BgpSession']]):
    """

    bgp_sessions: Union[Unset, List['BgpSession']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bgp_sessions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_sessions, Unset):
            bgp_sessions = []
            for bgp_sessions_item_data in self.bgp_sessions:
                bgp_sessions_item = bgp_sessions_item_data.to_dict()

                bgp_sessions.append(bgp_sessions_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bgp_sessions is not UNSET:
            field_dict["bgp_sessions"] = bgp_sessions

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bgp_session import BgpSession
        d = src_dict.copy()
        bgp_sessions = []
        _bgp_sessions = d.pop("bgp_sessions", UNSET)
        for bgp_sessions_item_data in (_bgp_sessions or []):
            bgp_sessions_item = BgpSession.from_dict(bgp_sessions_item_data)



            bgp_sessions.append(bgp_sessions_item)


        bgp_session_list = cls(
            bgp_sessions=bgp_sessions,
        )

        bgp_session_list.additional_properties = d
        return bgp_session_list

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
