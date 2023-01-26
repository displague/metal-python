from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_prices_per_facility import SpotPricesPerFacility
  from ..models.spot_prices_per_new_facility import SpotPricesPerNewFacility




T = TypeVar("T", bound="SpotPricesReport")

@attr.s(auto_attribs=True)
class SpotPricesReport:
    """
    Attributes:
        ams1 (Union[Unset, SpotPricesPerFacility]):
        atl1 (Union[Unset, SpotPricesPerNewFacility]):
        dfw1 (Union[Unset, SpotPricesPerNewFacility]):
        ewr1 (Union[Unset, SpotPricesPerFacility]):
        fra1 (Union[Unset, SpotPricesPerNewFacility]):
        iad1 (Union[Unset, SpotPricesPerNewFacility]):
        lax1 (Union[Unset, SpotPricesPerNewFacility]):
        nrt1 (Union[Unset, SpotPricesPerFacility]):
        ord1 (Union[Unset, SpotPricesPerNewFacility]):
        sea1 (Union[Unset, SpotPricesPerNewFacility]):
        sin1 (Union[Unset, SpotPricesPerNewFacility]):
        sjc1 (Union[Unset, SpotPricesPerFacility]):
        syd1 (Union[Unset, SpotPricesPerNewFacility]):
        yyz1 (Union[Unset, SpotPricesPerNewFacility]):
    """

    ams1: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    atl1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    dfw1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    ewr1: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    fra1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    iad1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    lax1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    nrt1: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    ord1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    sea1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    sin1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    sjc1: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    syd1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    yyz1: Union[Unset, 'SpotPricesPerNewFacility'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ams1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ams1, Unset):
            ams1 = self.ams1.to_dict()

        atl1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.atl1, Unset):
            atl1 = self.atl1.to_dict()

        dfw1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dfw1, Unset):
            dfw1 = self.dfw1.to_dict()

        ewr1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ewr1, Unset):
            ewr1 = self.ewr1.to_dict()

        fra1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fra1, Unset):
            fra1 = self.fra1.to_dict()

        iad1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iad1, Unset):
            iad1 = self.iad1.to_dict()

        lax1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lax1, Unset):
            lax1 = self.lax1.to_dict()

        nrt1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nrt1, Unset):
            nrt1 = self.nrt1.to_dict()

        ord1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ord1, Unset):
            ord1 = self.ord1.to_dict()

        sea1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sea1, Unset):
            sea1 = self.sea1.to_dict()

        sin1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sin1, Unset):
            sin1 = self.sin1.to_dict()

        sjc1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sjc1, Unset):
            sjc1 = self.sjc1.to_dict()

        syd1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.syd1, Unset):
            syd1 = self.syd1.to_dict()

        yyz1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.yyz1, Unset):
            yyz1 = self.yyz1.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ams1 is not UNSET:
            field_dict["ams1"] = ams1
        if atl1 is not UNSET:
            field_dict["atl1"] = atl1
        if dfw1 is not UNSET:
            field_dict["dfw1"] = dfw1
        if ewr1 is not UNSET:
            field_dict["ewr1"] = ewr1
        if fra1 is not UNSET:
            field_dict["fra1"] = fra1
        if iad1 is not UNSET:
            field_dict["iad1"] = iad1
        if lax1 is not UNSET:
            field_dict["lax1"] = lax1
        if nrt1 is not UNSET:
            field_dict["nrt1"] = nrt1
        if ord1 is not UNSET:
            field_dict["ord1"] = ord1
        if sea1 is not UNSET:
            field_dict["sea1"] = sea1
        if sin1 is not UNSET:
            field_dict["sin1"] = sin1
        if sjc1 is not UNSET:
            field_dict["sjc1"] = sjc1
        if syd1 is not UNSET:
            field_dict["syd1"] = syd1
        if yyz1 is not UNSET:
            field_dict["yyz1"] = yyz1

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_prices_per_facility import SpotPricesPerFacility
        from ..models.spot_prices_per_new_facility import SpotPricesPerNewFacility
        d = src_dict.copy()
        _ams1 = d.pop("ams1", UNSET)
        ams1: Union[Unset, SpotPricesPerFacility]
        if isinstance(_ams1,  Unset):
            ams1 = UNSET
        else:
            ams1 = SpotPricesPerFacility.from_dict(_ams1)




        _atl1 = d.pop("atl1", UNSET)
        atl1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_atl1,  Unset):
            atl1 = UNSET
        else:
            atl1 = SpotPricesPerNewFacility.from_dict(_atl1)




        _dfw1 = d.pop("dfw1", UNSET)
        dfw1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_dfw1,  Unset):
            dfw1 = UNSET
        else:
            dfw1 = SpotPricesPerNewFacility.from_dict(_dfw1)




        _ewr1 = d.pop("ewr1", UNSET)
        ewr1: Union[Unset, SpotPricesPerFacility]
        if isinstance(_ewr1,  Unset):
            ewr1 = UNSET
        else:
            ewr1 = SpotPricesPerFacility.from_dict(_ewr1)




        _fra1 = d.pop("fra1", UNSET)
        fra1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_fra1,  Unset):
            fra1 = UNSET
        else:
            fra1 = SpotPricesPerNewFacility.from_dict(_fra1)




        _iad1 = d.pop("iad1", UNSET)
        iad1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_iad1,  Unset):
            iad1 = UNSET
        else:
            iad1 = SpotPricesPerNewFacility.from_dict(_iad1)




        _lax1 = d.pop("lax1", UNSET)
        lax1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_lax1,  Unset):
            lax1 = UNSET
        else:
            lax1 = SpotPricesPerNewFacility.from_dict(_lax1)




        _nrt1 = d.pop("nrt1", UNSET)
        nrt1: Union[Unset, SpotPricesPerFacility]
        if isinstance(_nrt1,  Unset):
            nrt1 = UNSET
        else:
            nrt1 = SpotPricesPerFacility.from_dict(_nrt1)




        _ord1 = d.pop("ord1", UNSET)
        ord1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_ord1,  Unset):
            ord1 = UNSET
        else:
            ord1 = SpotPricesPerNewFacility.from_dict(_ord1)




        _sea1 = d.pop("sea1", UNSET)
        sea1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_sea1,  Unset):
            sea1 = UNSET
        else:
            sea1 = SpotPricesPerNewFacility.from_dict(_sea1)




        _sin1 = d.pop("sin1", UNSET)
        sin1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_sin1,  Unset):
            sin1 = UNSET
        else:
            sin1 = SpotPricesPerNewFacility.from_dict(_sin1)




        _sjc1 = d.pop("sjc1", UNSET)
        sjc1: Union[Unset, SpotPricesPerFacility]
        if isinstance(_sjc1,  Unset):
            sjc1 = UNSET
        else:
            sjc1 = SpotPricesPerFacility.from_dict(_sjc1)




        _syd1 = d.pop("syd1", UNSET)
        syd1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_syd1,  Unset):
            syd1 = UNSET
        else:
            syd1 = SpotPricesPerNewFacility.from_dict(_syd1)




        _yyz1 = d.pop("yyz1", UNSET)
        yyz1: Union[Unset, SpotPricesPerNewFacility]
        if isinstance(_yyz1,  Unset):
            yyz1 = UNSET
        else:
            yyz1 = SpotPricesPerNewFacility.from_dict(_yyz1)




        spot_prices_report = cls(
            ams1=ams1,
            atl1=atl1,
            dfw1=dfw1,
            ewr1=ewr1,
            fra1=fra1,
            iad1=iad1,
            lax1=lax1,
            nrt1=nrt1,
            ord1=ord1,
            sea1=sea1,
            sin1=sin1,
            sjc1=sjc1,
            syd1=syd1,
            yyz1=yyz1,
        )

        spot_prices_report.additional_properties = d
        return spot_prices_report

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
