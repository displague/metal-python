import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_market_request_create_input_instance_attributes import (
      SpotMarketRequestCreateInputInstanceAttributes,
  )




T = TypeVar("T", bound="SpotMarketRequestCreateInput")

@attr.s(auto_attribs=True)
class SpotMarketRequestCreateInput:
    """
    Attributes:
        devices_max (Union[Unset, int]):
        devices_min (Union[Unset, int]):
        end_at (Union[Unset, datetime.datetime]):
        facilities (Union[Unset, List[str]]):
        instance_attributes (Union[Unset, SpotMarketRequestCreateInputInstanceAttributes]):
        max_bid_price (Union[Unset, float]):
        metro (Union[Unset, str]): The metro ID or code the spot market request will be created in.
    """

    devices_max: Union[Unset, int] = UNSET
    devices_min: Union[Unset, int] = UNSET
    end_at: Union[Unset, datetime.datetime] = UNSET
    facilities: Union[Unset, List[str]] = UNSET
    instance_attributes: Union[Unset, 'SpotMarketRequestCreateInputInstanceAttributes'] = UNSET
    max_bid_price: Union[Unset, float] = UNSET
    metro: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        devices_max = self.devices_max
        devices_min = self.devices_min
        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        facilities: Union[Unset, List[str]] = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = self.facilities




        instance_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instance_attributes, Unset):
            instance_attributes = self.instance_attributes.to_dict()

        max_bid_price = self.max_bid_price
        metro = self.metro

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if devices_max is not UNSET:
            field_dict["devices_max"] = devices_max
        if devices_min is not UNSET:
            field_dict["devices_min"] = devices_min
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if instance_attributes is not UNSET:
            field_dict["instance_attributes"] = instance_attributes
        if max_bid_price is not UNSET:
            field_dict["max_bid_price"] = max_bid_price
        if metro is not UNSET:
            field_dict["metro"] = metro

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_market_request_create_input_instance_attributes import (
            SpotMarketRequestCreateInputInstanceAttributes,
        )
        d = src_dict.copy()
        devices_max = d.pop("devices_max", UNSET)

        devices_min = d.pop("devices_min", UNSET)

        _end_at = d.pop("end_at", UNSET)
        end_at: Union[Unset, datetime.datetime]
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at)




        facilities = cast(List[str], d.pop("facilities", UNSET))


        _instance_attributes = d.pop("instance_attributes", UNSET)
        instance_attributes: Union[Unset, SpotMarketRequestCreateInputInstanceAttributes]
        if isinstance(_instance_attributes,  Unset):
            instance_attributes = UNSET
        else:
            instance_attributes = SpotMarketRequestCreateInputInstanceAttributes.from_dict(_instance_attributes)




        max_bid_price = d.pop("max_bid_price", UNSET)

        metro = d.pop("metro", UNSET)

        spot_market_request_create_input = cls(
            devices_max=devices_max,
            devices_min=devices_min,
            end_at=end_at,
            facilities=facilities,
            instance_attributes=instance_attributes,
            max_bid_price=max_bid_price,
            metro=metro,
        )

        spot_market_request_create_input.additional_properties = d
        return spot_market_request_create_input

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
