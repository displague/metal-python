from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotPricesDatapoints")

@attr.s(auto_attribs=True)
class SpotPricesDatapoints:
    """
    Attributes:
        datapoints (Union[Unset, List[List[float]]]):
    """

    datapoints: Union[Unset, List[List[float]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        datapoints: Union[Unset, List[List[float]]] = UNSET
        if not isinstance(self.datapoints, Unset):
            datapoints = []
            for datapoints_item_data in self.datapoints:
                datapoints_item = datapoints_item_data




                datapoints.append(datapoints_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if datapoints is not UNSET:
            field_dict["datapoints"] = datapoints

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        datapoints = []
        _datapoints = d.pop("datapoints", UNSET)
        for datapoints_item_data in (_datapoints or []):
            datapoints_item = cast(List[float], datapoints_item_data)

            datapoints.append(datapoints_item)


        spot_prices_datapoints = cls(
            datapoints=datapoints,
        )

        spot_prices_datapoints.additional_properties = d
        return spot_prices_datapoints

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
