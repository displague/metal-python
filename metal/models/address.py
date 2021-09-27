from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.coordinates import Coordinates




T = TypeVar("T", bound="Address")

@attr.s(auto_attribs=True)
class Address:
    """
    Attributes:
        address (str):
        country (str):
        zip_code (str):
        address2 (Union[Unset, str]):
        city (Union[Unset, str]):
        coordinates (Union[Unset, Coordinates]):
        state (Union[Unset, str]):
    """

    address: str
    country: str
    zip_code: str
    address2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    coordinates: Union[Unset, 'Coordinates'] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        country = self.country
        zip_code = self.zip_code
        address2 = self.address2
        city = self.city
        coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "address": address,
            "country": country,
            "zip_code": zip_code,
        })
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if city is not UNSET:
            field_dict["city"] = city
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinates import Coordinates
        d = src_dict.copy()
        address = d.pop("address")

        country = d.pop("country")

        zip_code = d.pop("zip_code")

        address2 = d.pop("address2", UNSET)

        city = d.pop("city", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Union[Unset, Coordinates]
        if isinstance(_coordinates,  Unset):
            coordinates = UNSET
        else:
            coordinates = Coordinates.from_dict(_coordinates)




        state = d.pop("state", UNSET)

        address = cls(
            address=address,
            country=country,
            zip_code=zip_code,
            address2=address2,
            city=city,
            coordinates=coordinates,
            state=state,
        )

        address.additional_properties = d
        return address

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
