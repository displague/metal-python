from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.self_service_reservation_response import SelfServiceReservationResponse




T = TypeVar("T", bound="SelfServiceReservationList")

@attr.s(auto_attribs=True)
class SelfServiceReservationList:
    """
    Attributes:
        reservations (Union[Unset, List['SelfServiceReservationResponse']]):
    """

    reservations: Union[Unset, List['SelfServiceReservationResponse']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        reservations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = []
            for reservations_item_data in self.reservations:
                reservations_item = reservations_item_data.to_dict()

                reservations.append(reservations_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservations is not UNSET:
            field_dict["reservations"] = reservations

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.self_service_reservation_response import SelfServiceReservationResponse
        d = src_dict.copy()
        reservations = []
        _reservations = d.pop("reservations", UNSET)
        for reservations_item_data in (_reservations or []):
            reservations_item = SelfServiceReservationResponse.from_dict(reservations_item_data)



            reservations.append(reservations_item)


        self_service_reservation_list = cls(
            reservations=reservations,
        )

        self_service_reservation_list.additional_properties = d
        return self_service_reservation_list

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
