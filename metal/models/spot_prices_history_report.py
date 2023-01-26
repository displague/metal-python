from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_prices_datapoints import SpotPricesDatapoints




T = TypeVar("T", bound="SpotPricesHistoryReport")

@attr.s(auto_attribs=True)
class SpotPricesHistoryReport:
    """
    Attributes:
        prices_history (Union[Unset, SpotPricesDatapoints]):
    """

    prices_history: Union[Unset, 'SpotPricesDatapoints'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        prices_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prices_history, Unset):
            prices_history = self.prices_history.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if prices_history is not UNSET:
            field_dict["prices_history"] = prices_history

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_prices_datapoints import SpotPricesDatapoints
        d = src_dict.copy()
        _prices_history = d.pop("prices_history", UNSET)
        prices_history: Union[Unset, SpotPricesDatapoints]
        if isinstance(_prices_history,  Unset):
            prices_history = UNSET
        else:
            prices_history = SpotPricesDatapoints.from_dict(_prices_history)




        spot_prices_history_report = cls(
            prices_history=prices_history,
        )

        spot_prices_history_report.additional_properties = d
        return spot_prices_history_report

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
