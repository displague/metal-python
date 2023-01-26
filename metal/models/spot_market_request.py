import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.spot_market_request_metro import SpotMarketRequestMetro




T = TypeVar("T", bound="SpotMarketRequest")

@attr.s(auto_attribs=True)
class SpotMarketRequest:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        devices_max (Union[Unset, int]):
        devices_min (Union[Unset, int]):
        end_at (Union[Unset, datetime.datetime]):
        facilities (Union[Unset, Href]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        instances (Union[Unset, Href]):
        max_bid_price (Union[Unset, float]):
        metro (Union[Unset, SpotMarketRequestMetro]):
        project (Union[Unset, Href]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    devices_max: Union[Unset, int] = UNSET
    devices_min: Union[Unset, int] = UNSET
    end_at: Union[Unset, datetime.datetime] = UNSET
    facilities: Union[Unset, 'Href'] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    instances: Union[Unset, 'Href'] = UNSET
    max_bid_price: Union[Unset, float] = UNSET
    metro: Union[Unset, 'SpotMarketRequestMetro'] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        devices_max = self.devices_max
        devices_min = self.devices_min
        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        facilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = self.facilities.to_dict()

        href = self.href
        id = self.id
        instances: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = self.instances.to_dict()

        max_bid_price = self.max_bid_price
        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if devices_max is not UNSET:
            field_dict["devices_max"] = devices_max
        if devices_min is not UNSET:
            field_dict["devices_min"] = devices_min
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if instances is not UNSET:
            field_dict["instances"] = instances
        if max_bid_price is not UNSET:
            field_dict["max_bid_price"] = max_bid_price
        if metro is not UNSET:
            field_dict["metro"] = metro
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.spot_market_request_metro import SpotMarketRequestMetro
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        devices_max = d.pop("devices_max", UNSET)

        devices_min = d.pop("devices_min", UNSET)

        _end_at = d.pop("end_at", UNSET)
        end_at: Union[Unset, datetime.datetime]
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at)




        _facilities = d.pop("facilities", UNSET)
        facilities: Union[Unset, Href]
        if isinstance(_facilities,  Unset):
            facilities = UNSET
        else:
            facilities = Href.from_dict(_facilities)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _instances = d.pop("instances", UNSET)
        instances: Union[Unset, Href]
        if isinstance(_instances,  Unset):
            instances = UNSET
        else:
            instances = Href.from_dict(_instances)




        max_bid_price = d.pop("max_bid_price", UNSET)

        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, SpotMarketRequestMetro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = SpotMarketRequestMetro.from_dict(_metro)




        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        spot_market_request = cls(
            created_at=created_at,
            devices_max=devices_max,
            devices_min=devices_min,
            end_at=end_at,
            facilities=facilities,
            href=href,
            id=id,
            instances=instances,
            max_bid_price=max_bid_price,
            metro=metro,
            project=project,
        )

        spot_market_request.additional_properties = d
        return spot_market_request

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
