from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="Meta")

@attr.s(auto_attribs=True)
class Meta:
    """
    Attributes:
        first (Union[Unset, Href]):
        last (Union[Unset, Href]):
        next_ (Union[Unset, Href]):
        previous (Union[Unset, Href]):
        self_ (Union[Unset, Href]):
        total (Union[Unset, int]):
        current_page (Union[Unset, int]):
        last_page (Union[Unset, int]):
    """

    first: Union[Unset, 'Href'] = UNSET
    last: Union[Unset, 'Href'] = UNSET
    next_: Union[Unset, 'Href'] = UNSET
    previous: Union[Unset, 'Href'] = UNSET
    self_: Union[Unset, 'Href'] = UNSET
    total: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    last_page: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        first: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        last: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        next_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        previous: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        total = self.total
        current_page = self.current_page
        last_page = self.last_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if self_ is not UNSET:
            field_dict["self"] = self_
        if total is not UNSET:
            field_dict["total"] = total
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        _first = d.pop("first", UNSET)
        first: Union[Unset, Href]
        if isinstance(_first,  Unset):
            first = UNSET
        else:
            first = Href.from_dict(_first)




        _last = d.pop("last", UNSET)
        last: Union[Unset, Href]
        if isinstance(_last,  Unset):
            last = UNSET
        else:
            last = Href.from_dict(_last)




        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, Href]
        if isinstance(_next_,  Unset):
            next_ = UNSET
        else:
            next_ = Href.from_dict(_next_)




        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, Href]
        if isinstance(_previous,  Unset):
            previous = UNSET
        else:
            previous = Href.from_dict(_previous)




        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, Href]
        if isinstance(_self_,  Unset):
            self_ = UNSET
        else:
            self_ = Href.from_dict(_self_)




        total = d.pop("total", UNSET)

        current_page = d.pop("current_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        meta = cls(
            first=first,
            last=last,
            next_=next_,
            previous=previous,
            self_=self_,
            total=total,
            current_page=current_page,
            last_page=last_page,
        )

        meta.additional_properties = d
        return meta

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
