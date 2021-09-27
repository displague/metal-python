from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_market_request import SpotMarketRequest




T = TypeVar("T", bound="SpotMarketRequestList")

@attr.s(auto_attribs=True)
class SpotMarketRequestList:
    """
    Attributes:
        spot_market_requests (Union[Unset, List['SpotMarketRequest']]):
    """

    spot_market_requests: Union[Unset, List['SpotMarketRequest']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        spot_market_requests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spot_market_requests, Unset):
            spot_market_requests = []
            for spot_market_requests_item_data in self.spot_market_requests:
                spot_market_requests_item = spot_market_requests_item_data.to_dict()

                spot_market_requests.append(spot_market_requests_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spot_market_requests is not UNSET:
            field_dict["spot_market_requests"] = spot_market_requests

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_market_request import SpotMarketRequest
        d = src_dict.copy()
        spot_market_requests = []
        _spot_market_requests = d.pop("spot_market_requests", UNSET)
        for spot_market_requests_item_data in (_spot_market_requests or []):
            spot_market_requests_item = SpotMarketRequest.from_dict(spot_market_requests_item_data)



            spot_market_requests.append(spot_market_requests_item)


        spot_market_request_list = cls(
            spot_market_requests=spot_market_requests,
        )

        spot_market_request_list.additional_properties = d
        return spot_market_request_list

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
