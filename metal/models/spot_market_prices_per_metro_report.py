from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_prices_per_facility import SpotPricesPerFacility




T = TypeVar("T", bound="SpotMarketPricesPerMetroReport")

@attr.s(auto_attribs=True)
class SpotMarketPricesPerMetroReport:
    """
    Attributes:
        am (Union[Unset, SpotPricesPerFacility]):
        ch (Union[Unset, SpotPricesPerFacility]):
        da (Union[Unset, SpotPricesPerFacility]):
        la (Union[Unset, SpotPricesPerFacility]):
        ny (Union[Unset, SpotPricesPerFacility]):
        sg (Union[Unset, SpotPricesPerFacility]):
        sv (Union[Unset, SpotPricesPerFacility]):
    """

    am: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    ch: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    da: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    la: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    ny: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    sg: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    sv: Union[Unset, 'SpotPricesPerFacility'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        am: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.am, Unset):
            am = self.am.to_dict()

        ch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ch, Unset):
            ch = self.ch.to_dict()

        da: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.da, Unset):
            da = self.da.to_dict()

        la: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.la, Unset):
            la = self.la.to_dict()

        ny: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ny, Unset):
            ny = self.ny.to_dict()

        sg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sg, Unset):
            sg = self.sg.to_dict()

        sv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sv, Unset):
            sv = self.sv.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if am is not UNSET:
            field_dict["am"] = am
        if ch is not UNSET:
            field_dict["ch"] = ch
        if da is not UNSET:
            field_dict["da"] = da
        if la is not UNSET:
            field_dict["la"] = la
        if ny is not UNSET:
            field_dict["ny"] = ny
        if sg is not UNSET:
            field_dict["sg"] = sg
        if sv is not UNSET:
            field_dict["sv"] = sv

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_prices_per_facility import SpotPricesPerFacility
        d = src_dict.copy()
        _am = d.pop("am", UNSET)
        am: Union[Unset, SpotPricesPerFacility]
        if isinstance(_am,  Unset):
            am = UNSET
        else:
            am = SpotPricesPerFacility.from_dict(_am)




        _ch = d.pop("ch", UNSET)
        ch: Union[Unset, SpotPricesPerFacility]
        if isinstance(_ch,  Unset):
            ch = UNSET
        else:
            ch = SpotPricesPerFacility.from_dict(_ch)




        _da = d.pop("da", UNSET)
        da: Union[Unset, SpotPricesPerFacility]
        if isinstance(_da,  Unset):
            da = UNSET
        else:
            da = SpotPricesPerFacility.from_dict(_da)




        _la = d.pop("la", UNSET)
        la: Union[Unset, SpotPricesPerFacility]
        if isinstance(_la,  Unset):
            la = UNSET
        else:
            la = SpotPricesPerFacility.from_dict(_la)




        _ny = d.pop("ny", UNSET)
        ny: Union[Unset, SpotPricesPerFacility]
        if isinstance(_ny,  Unset):
            ny = UNSET
        else:
            ny = SpotPricesPerFacility.from_dict(_ny)




        _sg = d.pop("sg", UNSET)
        sg: Union[Unset, SpotPricesPerFacility]
        if isinstance(_sg,  Unset):
            sg = UNSET
        else:
            sg = SpotPricesPerFacility.from_dict(_sg)




        _sv = d.pop("sv", UNSET)
        sv: Union[Unset, SpotPricesPerFacility]
        if isinstance(_sv,  Unset):
            sv = UNSET
        else:
            sv = SpotPricesPerFacility.from_dict(_sv)




        spot_market_prices_per_metro_report = cls(
            am=am,
            ch=ch,
            da=da,
            la=la,
            ny=ny,
            sg=sg,
            sv=sv,
        )

        spot_market_prices_per_metro_report.additional_properties = d
        return spot_market_prices_per_metro_report

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
