from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport




T = TypeVar("T", bound="SpotMarketPricesPerMetroList")

@attr.s(auto_attribs=True)
class SpotMarketPricesPerMetroList:
    """
    Attributes:
        spot_market_prices (Union[Unset, SpotMarketPricesPerMetroReport]):
    """

    spot_market_prices: Union[Unset, 'SpotMarketPricesPerMetroReport'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        spot_market_prices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spot_market_prices, Unset):
            spot_market_prices = self.spot_market_prices.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spot_market_prices is not UNSET:
            field_dict["spot_market_prices"] = spot_market_prices

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport
        d = src_dict.copy()
        _spot_market_prices = d.pop("spot_market_prices", UNSET)
        spot_market_prices: Union[Unset, SpotMarketPricesPerMetroReport]
        if isinstance(_spot_market_prices,  Unset):
            spot_market_prices = UNSET
        else:
            spot_market_prices = SpotMarketPricesPerMetroReport.from_dict(_spot_market_prices)




        spot_market_prices_per_metro_list = cls(
            spot_market_prices=spot_market_prices,
        )

        spot_market_prices_per_metro_list.additional_properties = d
        return spot_market_prices_per_metro_list

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
