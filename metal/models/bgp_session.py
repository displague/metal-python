import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.bgp_session_address_family import BgpSessionAddressFamily
from ..models.bgp_session_status import BgpSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="BgpSession")

@attr.s(auto_attribs=True)
class BgpSession:
    """
    Attributes:
        address_family (BgpSessionAddressFamily):
        created_at (Union[Unset, datetime.datetime]):
        default_route (Union[Unset, bool]):
        device (Union[Unset, Href]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        learned_routes (Union[Unset, List[str]]):
        status (Union[Unset, BgpSessionStatus]):  The status of the BGP Session. Multiple status values may be reported
            when the device is connected to multiple switches, one value per switch. Each status will start with "unknown"
            and progress to "up" or "down" depending on the connected device. Subsequent "unknown" values indicate a problem
            acquiring status from the switch.
        updated_at (Union[Unset, datetime.datetime]):
    """

    address_family: BgpSessionAddressFamily
    created_at: Union[Unset, datetime.datetime] = UNSET
    default_route: Union[Unset, bool] = UNSET
    device: Union[Unset, 'Href'] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    learned_routes: Union[Unset, List[str]] = UNSET
    status: Union[Unset, BgpSessionStatus] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address_family = self.address_family.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default_route = self.default_route
        device: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        href = self.href
        id = self.id
        learned_routes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.learned_routes, Unset):
            learned_routes = self.learned_routes




        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "address_family": address_family,
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_route is not UNSET:
            field_dict["default_route"] = default_route
        if device is not UNSET:
            field_dict["device"] = device
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if learned_routes is not UNSET:
            field_dict["learned_routes"] = learned_routes
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        address_family = BgpSessionAddressFamily(d.pop("address_family"))




        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        default_route = d.pop("default_route", UNSET)

        _device = d.pop("device", UNSET)
        device: Union[Unset, Href]
        if isinstance(_device,  Unset):
            device = UNSET
        else:
            device = Href.from_dict(_device)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        learned_routes = cast(List[str], d.pop("learned_routes", UNSET))


        _status = d.pop("status", UNSET)
        status: Union[Unset, BgpSessionStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BgpSessionStatus(_status)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        bgp_session = cls(
            address_family=address_family,
            created_at=created_at,
            default_route=default_route,
            device=device,
            href=href,
            id=id,
            learned_routes=learned_routes,
            status=status,
            updated_at=updated_at,
        )

        bgp_session.additional_properties = d
        return bgp_session

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
