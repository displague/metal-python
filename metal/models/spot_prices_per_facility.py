from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_prices_per_baremetal import SpotPricesPerBaremetal




T = TypeVar("T", bound="SpotPricesPerFacility")

@attr.s(auto_attribs=True)
class SpotPricesPerFacility:
    """
    Attributes:
        baremetal_0 (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_1 (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_2 (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_2a (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_2a2 (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_3 (Union[Unset, SpotPricesPerBaremetal]):
        baremetal_s (Union[Unset, SpotPricesPerBaremetal]):
        c2_medium_x86 (Union[Unset, SpotPricesPerBaremetal]):
        m2_xlarge_x86 (Union[Unset, SpotPricesPerBaremetal]):
    """

    baremetal_0: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_1: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_2: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_2a: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_2a2: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_3: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    baremetal_s: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    c2_medium_x86: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    m2_xlarge_x86: Union[Unset, 'SpotPricesPerBaremetal'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        baremetal_0: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_0, Unset):
            baremetal_0 = self.baremetal_0.to_dict()

        baremetal_1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_1, Unset):
            baremetal_1 = self.baremetal_1.to_dict()

        baremetal_2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_2, Unset):
            baremetal_2 = self.baremetal_2.to_dict()

        baremetal_2a: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_2a, Unset):
            baremetal_2a = self.baremetal_2a.to_dict()

        baremetal_2a2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_2a2, Unset):
            baremetal_2a2 = self.baremetal_2a2.to_dict()

        baremetal_3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_3, Unset):
            baremetal_3 = self.baremetal_3.to_dict()

        baremetal_s: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baremetal_s, Unset):
            baremetal_s = self.baremetal_s.to_dict()

        c2_medium_x86: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.c2_medium_x86, Unset):
            c2_medium_x86 = self.c2_medium_x86.to_dict()

        m2_xlarge_x86: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.m2_xlarge_x86, Unset):
            m2_xlarge_x86 = self.m2_xlarge_x86.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if baremetal_0 is not UNSET:
            field_dict["baremetal_0"] = baremetal_0
        if baremetal_1 is not UNSET:
            field_dict["baremetal_1"] = baremetal_1
        if baremetal_2 is not UNSET:
            field_dict["baremetal_2"] = baremetal_2
        if baremetal_2a is not UNSET:
            field_dict["baremetal_2a"] = baremetal_2a
        if baremetal_2a2 is not UNSET:
            field_dict["baremetal_2a2"] = baremetal_2a2
        if baremetal_3 is not UNSET:
            field_dict["baremetal_3"] = baremetal_3
        if baremetal_s is not UNSET:
            field_dict["baremetal_s"] = baremetal_s
        if c2_medium_x86 is not UNSET:
            field_dict["c2.medium.x86"] = c2_medium_x86
        if m2_xlarge_x86 is not UNSET:
            field_dict["m2.xlarge.x86"] = m2_xlarge_x86

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_prices_per_baremetal import SpotPricesPerBaremetal
        d = src_dict.copy()
        _baremetal_0 = d.pop("baremetal_0", UNSET)
        baremetal_0: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_0,  Unset):
            baremetal_0 = UNSET
        else:
            baremetal_0 = SpotPricesPerBaremetal.from_dict(_baremetal_0)




        _baremetal_1 = d.pop("baremetal_1", UNSET)
        baremetal_1: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_1,  Unset):
            baremetal_1 = UNSET
        else:
            baremetal_1 = SpotPricesPerBaremetal.from_dict(_baremetal_1)




        _baremetal_2 = d.pop("baremetal_2", UNSET)
        baremetal_2: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_2,  Unset):
            baremetal_2 = UNSET
        else:
            baremetal_2 = SpotPricesPerBaremetal.from_dict(_baremetal_2)




        _baremetal_2a = d.pop("baremetal_2a", UNSET)
        baremetal_2a: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_2a,  Unset):
            baremetal_2a = UNSET
        else:
            baremetal_2a = SpotPricesPerBaremetal.from_dict(_baremetal_2a)




        _baremetal_2a2 = d.pop("baremetal_2a2", UNSET)
        baremetal_2a2: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_2a2,  Unset):
            baremetal_2a2 = UNSET
        else:
            baremetal_2a2 = SpotPricesPerBaremetal.from_dict(_baremetal_2a2)




        _baremetal_3 = d.pop("baremetal_3", UNSET)
        baremetal_3: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_3,  Unset):
            baremetal_3 = UNSET
        else:
            baremetal_3 = SpotPricesPerBaremetal.from_dict(_baremetal_3)




        _baremetal_s = d.pop("baremetal_s", UNSET)
        baremetal_s: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_baremetal_s,  Unset):
            baremetal_s = UNSET
        else:
            baremetal_s = SpotPricesPerBaremetal.from_dict(_baremetal_s)




        _c2_medium_x86 = d.pop("c2.medium.x86", UNSET)
        c2_medium_x86: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_c2_medium_x86,  Unset):
            c2_medium_x86 = UNSET
        else:
            c2_medium_x86 = SpotPricesPerBaremetal.from_dict(_c2_medium_x86)




        _m2_xlarge_x86 = d.pop("m2.xlarge.x86", UNSET)
        m2_xlarge_x86: Union[Unset, SpotPricesPerBaremetal]
        if isinstance(_m2_xlarge_x86,  Unset):
            m2_xlarge_x86 = UNSET
        else:
            m2_xlarge_x86 = SpotPricesPerBaremetal.from_dict(_m2_xlarge_x86)




        spot_prices_per_facility = cls(
            baremetal_0=baremetal_0,
            baremetal_1=baremetal_1,
            baremetal_2=baremetal_2,
            baremetal_2a=baremetal_2a,
            baremetal_2a2=baremetal_2a2,
            baremetal_3=baremetal_3,
            baremetal_s=baremetal_s,
            c2_medium_x86=c2_medium_x86,
            m2_xlarge_x86=m2_xlarge_x86,
        )

        spot_prices_per_facility.additional_properties = d
        return spot_prices_per_facility

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
