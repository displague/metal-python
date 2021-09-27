from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.capacity_per_facility import CapacityPerFacility




T = TypeVar("T", bound="MetroCapacityReport")

@attr.s(auto_attribs=True)
class MetroCapacityReport:
    """
    Attributes:
        am (Union[Unset, CapacityPerFacility]):
        at (Union[Unset, CapacityPerFacility]):
        ch (Union[Unset, CapacityPerFacility]):
        da (Union[Unset, CapacityPerFacility]):
        dc (Union[Unset, CapacityPerFacility]):
        fr (Union[Unset, CapacityPerFacility]):
        hk (Union[Unset, CapacityPerFacility]):
        la (Union[Unset, CapacityPerFacility]):
        ld (Union[Unset, CapacityPerFacility]):
        md (Union[Unset, CapacityPerFacility]):
        ny (Union[Unset, CapacityPerFacility]):
        pa (Union[Unset, CapacityPerFacility]):
        se (Union[Unset, CapacityPerFacility]):
        sg (Union[Unset, CapacityPerFacility]):
        sl (Union[Unset, CapacityPerFacility]):
        sp (Union[Unset, CapacityPerFacility]):
        sv (Union[Unset, CapacityPerFacility]):
        sy (Union[Unset, CapacityPerFacility]):
        tr (Union[Unset, CapacityPerFacility]):
        ty (Union[Unset, CapacityPerFacility]):
    """

    am: Union[Unset, 'CapacityPerFacility'] = UNSET
    at: Union[Unset, 'CapacityPerFacility'] = UNSET
    ch: Union[Unset, 'CapacityPerFacility'] = UNSET
    da: Union[Unset, 'CapacityPerFacility'] = UNSET
    dc: Union[Unset, 'CapacityPerFacility'] = UNSET
    fr: Union[Unset, 'CapacityPerFacility'] = UNSET
    hk: Union[Unset, 'CapacityPerFacility'] = UNSET
    la: Union[Unset, 'CapacityPerFacility'] = UNSET
    ld: Union[Unset, 'CapacityPerFacility'] = UNSET
    md: Union[Unset, 'CapacityPerFacility'] = UNSET
    ny: Union[Unset, 'CapacityPerFacility'] = UNSET
    pa: Union[Unset, 'CapacityPerFacility'] = UNSET
    se: Union[Unset, 'CapacityPerFacility'] = UNSET
    sg: Union[Unset, 'CapacityPerFacility'] = UNSET
    sl: Union[Unset, 'CapacityPerFacility'] = UNSET
    sp: Union[Unset, 'CapacityPerFacility'] = UNSET
    sv: Union[Unset, 'CapacityPerFacility'] = UNSET
    sy: Union[Unset, 'CapacityPerFacility'] = UNSET
    tr: Union[Unset, 'CapacityPerFacility'] = UNSET
    ty: Union[Unset, 'CapacityPerFacility'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        am: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.am, Unset):
            am = self.am.to_dict()

        at: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.to_dict()

        ch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ch, Unset):
            ch = self.ch.to_dict()

        da: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.da, Unset):
            da = self.da.to_dict()

        dc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dc, Unset):
            dc = self.dc.to_dict()

        fr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fr, Unset):
            fr = self.fr.to_dict()

        hk: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hk, Unset):
            hk = self.hk.to_dict()

        la: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.la, Unset):
            la = self.la.to_dict()

        ld: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ld, Unset):
            ld = self.ld.to_dict()

        md: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.md, Unset):
            md = self.md.to_dict()

        ny: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ny, Unset):
            ny = self.ny.to_dict()

        pa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pa, Unset):
            pa = self.pa.to_dict()

        se: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.se, Unset):
            se = self.se.to_dict()

        sg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sg, Unset):
            sg = self.sg.to_dict()

        sl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sl, Unset):
            sl = self.sl.to_dict()

        sp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sp, Unset):
            sp = self.sp.to_dict()

        sv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sv, Unset):
            sv = self.sv.to_dict()

        sy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sy, Unset):
            sy = self.sy.to_dict()

        tr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tr, Unset):
            tr = self.tr.to_dict()

        ty: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ty, Unset):
            ty = self.ty.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if am is not UNSET:
            field_dict["am"] = am
        if at is not UNSET:
            field_dict["at"] = at
        if ch is not UNSET:
            field_dict["ch"] = ch
        if da is not UNSET:
            field_dict["da"] = da
        if dc is not UNSET:
            field_dict["dc"] = dc
        if fr is not UNSET:
            field_dict["fr"] = fr
        if hk is not UNSET:
            field_dict["hk"] = hk
        if la is not UNSET:
            field_dict["la"] = la
        if ld is not UNSET:
            field_dict["ld"] = ld
        if md is not UNSET:
            field_dict["md"] = md
        if ny is not UNSET:
            field_dict["ny"] = ny
        if pa is not UNSET:
            field_dict["pa"] = pa
        if se is not UNSET:
            field_dict["se"] = se
        if sg is not UNSET:
            field_dict["sg"] = sg
        if sl is not UNSET:
            field_dict["sl"] = sl
        if sp is not UNSET:
            field_dict["sp"] = sp
        if sv is not UNSET:
            field_dict["sv"] = sv
        if sy is not UNSET:
            field_dict["sy"] = sy
        if tr is not UNSET:
            field_dict["tr"] = tr
        if ty is not UNSET:
            field_dict["ty"] = ty

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.capacity_per_facility import CapacityPerFacility
        d = src_dict.copy()
        _am = d.pop("am", UNSET)
        am: Union[Unset, CapacityPerFacility]
        if isinstance(_am,  Unset):
            am = UNSET
        else:
            am = CapacityPerFacility.from_dict(_am)




        _at = d.pop("at", UNSET)
        at: Union[Unset, CapacityPerFacility]
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = CapacityPerFacility.from_dict(_at)




        _ch = d.pop("ch", UNSET)
        ch: Union[Unset, CapacityPerFacility]
        if isinstance(_ch,  Unset):
            ch = UNSET
        else:
            ch = CapacityPerFacility.from_dict(_ch)




        _da = d.pop("da", UNSET)
        da: Union[Unset, CapacityPerFacility]
        if isinstance(_da,  Unset):
            da = UNSET
        else:
            da = CapacityPerFacility.from_dict(_da)




        _dc = d.pop("dc", UNSET)
        dc: Union[Unset, CapacityPerFacility]
        if isinstance(_dc,  Unset):
            dc = UNSET
        else:
            dc = CapacityPerFacility.from_dict(_dc)




        _fr = d.pop("fr", UNSET)
        fr: Union[Unset, CapacityPerFacility]
        if isinstance(_fr,  Unset):
            fr = UNSET
        else:
            fr = CapacityPerFacility.from_dict(_fr)




        _hk = d.pop("hk", UNSET)
        hk: Union[Unset, CapacityPerFacility]
        if isinstance(_hk,  Unset):
            hk = UNSET
        else:
            hk = CapacityPerFacility.from_dict(_hk)




        _la = d.pop("la", UNSET)
        la: Union[Unset, CapacityPerFacility]
        if isinstance(_la,  Unset):
            la = UNSET
        else:
            la = CapacityPerFacility.from_dict(_la)




        _ld = d.pop("ld", UNSET)
        ld: Union[Unset, CapacityPerFacility]
        if isinstance(_ld,  Unset):
            ld = UNSET
        else:
            ld = CapacityPerFacility.from_dict(_ld)




        _md = d.pop("md", UNSET)
        md: Union[Unset, CapacityPerFacility]
        if isinstance(_md,  Unset):
            md = UNSET
        else:
            md = CapacityPerFacility.from_dict(_md)




        _ny = d.pop("ny", UNSET)
        ny: Union[Unset, CapacityPerFacility]
        if isinstance(_ny,  Unset):
            ny = UNSET
        else:
            ny = CapacityPerFacility.from_dict(_ny)




        _pa = d.pop("pa", UNSET)
        pa: Union[Unset, CapacityPerFacility]
        if isinstance(_pa,  Unset):
            pa = UNSET
        else:
            pa = CapacityPerFacility.from_dict(_pa)




        _se = d.pop("se", UNSET)
        se: Union[Unset, CapacityPerFacility]
        if isinstance(_se,  Unset):
            se = UNSET
        else:
            se = CapacityPerFacility.from_dict(_se)




        _sg = d.pop("sg", UNSET)
        sg: Union[Unset, CapacityPerFacility]
        if isinstance(_sg,  Unset):
            sg = UNSET
        else:
            sg = CapacityPerFacility.from_dict(_sg)




        _sl = d.pop("sl", UNSET)
        sl: Union[Unset, CapacityPerFacility]
        if isinstance(_sl,  Unset):
            sl = UNSET
        else:
            sl = CapacityPerFacility.from_dict(_sl)




        _sp = d.pop("sp", UNSET)
        sp: Union[Unset, CapacityPerFacility]
        if isinstance(_sp,  Unset):
            sp = UNSET
        else:
            sp = CapacityPerFacility.from_dict(_sp)




        _sv = d.pop("sv", UNSET)
        sv: Union[Unset, CapacityPerFacility]
        if isinstance(_sv,  Unset):
            sv = UNSET
        else:
            sv = CapacityPerFacility.from_dict(_sv)




        _sy = d.pop("sy", UNSET)
        sy: Union[Unset, CapacityPerFacility]
        if isinstance(_sy,  Unset):
            sy = UNSET
        else:
            sy = CapacityPerFacility.from_dict(_sy)




        _tr = d.pop("tr", UNSET)
        tr: Union[Unset, CapacityPerFacility]
        if isinstance(_tr,  Unset):
            tr = UNSET
        else:
            tr = CapacityPerFacility.from_dict(_tr)




        _ty = d.pop("ty", UNSET)
        ty: Union[Unset, CapacityPerFacility]
        if isinstance(_ty,  Unset):
            ty = UNSET
        else:
            ty = CapacityPerFacility.from_dict(_ty)




        metro_capacity_report = cls(
            am=am,
            at=at,
            ch=ch,
            da=da,
            dc=dc,
            fr=fr,
            hk=hk,
            la=la,
            ld=ld,
            md=md,
            ny=ny,
            pa=pa,
            se=se,
            sg=sg,
            sl=sl,
            sp=sp,
            sv=sv,
            sy=sy,
            tr=tr,
            ty=ty,
        )

        metro_capacity_report.additional_properties = d
        return metro_capacity_report

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
