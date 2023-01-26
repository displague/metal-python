from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_prices_per_baremetal import SpotPricesPerBaremetal




T = TypeVar("T", bound="SpotPricesPerNewFacility")

@attr.s(auto_attribs=True)
class SpotPricesPerNewFacility:
    """
    Attributes:
        baremetal_1e (Union[Unset, SpotPricesPerBaremetal]):
    """

    baremetal_1e: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        baremetal_1e: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_1e, Unset):
            baremetal_1e = self.baremetal_1e.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if baremetal_1e is not UNSET:
            field_dict["baremetal_1e"] = baremetal_1e

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_prices_per_baremetal import SpotPricesPerBaremetal
        d = src_dict.copy()
        _baremetal_1e = d.pop("baremetal_1e", UNSET)
        baremetal_1e: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_1e,  Unset):
            baremetal_1e = UNSET
        else:
            baremetal_1e = SpotPricesPerBaremetal.from_dict(_baremetal_1e)




        spot_prices_per_new_facility = cls(
            baremetal_1e=baremetal_1e,
        )

        spot_prices_per_new_facility.additional_properties = d
        return spot_prices_per_new_facility

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
