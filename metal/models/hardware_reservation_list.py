from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.hardware_reservation import HardwareReservation
  from ..models.meta import Meta




T = TypeVar("T", bound="HardwareReservationList")

@attr.s(auto_attribs=True)
class HardwareReservationList:
    """
    Attributes:
        hardware_reservations (Union[Unset, List['HardwareReservation']]):
        meta (Union[Unset, Meta]):
    """

    hardware_reservations: Union[Unset, List['HardwareReservation']] = UNSET
    meta: Union[Unset, 'Meta'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        hardware_reservations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hardware_reservations, Unset):
            hardware_reservations = []
            for hardware_reservations_item_data in self.hardware_reservations:
                hardware_reservations_item = hardware_reservations_item_data.to_dict()

                hardware_reservations.append(hardware_reservations_item)




        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hardware_reservations is not UNSET:
            field_dict["hardware_reservations"] = hardware_reservations
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hardware_reservation import HardwareReservation
        from ..models.meta import Meta
        d = src_dict.copy()
        hardware_reservations = []
        _hardware_reservations = d.pop("hardware_reservations", UNSET)
        for hardware_reservations_item_data in (_hardware_reservations or []):
            hardware_reservations_item = HardwareReservation.from_dict(hardware_reservations_item_data)



            hardware_reservations.append(hardware_reservations_item)


        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)




        hardware_reservation_list = cls(
            hardware_reservations=hardware_reservations,
            meta=meta,
        )

        hardware_reservation_list.additional_properties = d
        return hardware_reservation_list

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
