from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.facility_features_item import FacilityFeaturesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.address import Address
  from ..models.device_metro import DeviceMetro




T = TypeVar("T", bound="Facility")

@attr.s(auto_attribs=True)
class Facility:
    """
    Attributes:
        address (Union[Unset, Address]):
        code (Union[Unset, str]):
        features (Union[Unset, List[FacilityFeaturesItem]]):  Example: ['baremetal', 'backend_transfer', 'global_ipv4'].
        id (Union[Unset, str]):
        ip_ranges (Union[Unset, List[str]]): IP ranges registered in facility. Can be used for GeoIP location Example:
            ['2604:1380::/36', '147.75.192.0/21'].
        metro (Union[Unset, DeviceMetro]):
        name (Union[Unset, str]):
    """

    address: Union[Unset, 'Address'] = UNSET
    code: Union[Unset, str] = UNSET
    features: Union[Unset, List[FacilityFeaturesItem]] = UNSET
    id: Union[Unset, str] = UNSET
    ip_ranges: Union[Unset, List[str]] = UNSET
    metro: Union[Unset, 'DeviceMetro'] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        code = self.code
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value

                features.append(features_item)




        id = self.id
        ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_ranges, Unset):
            ip_ranges = self.ip_ranges




        metro: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metro, Unset):
            metro = self.metro.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if code is not UNSET:
            field_dict["code"] = code
        if features is not UNSET:
            field_dict["features"] = features
        if id is not UNSET:
            field_dict["id"] = id
        if ip_ranges is not UNSET:
            field_dict["ip_ranges"] = ip_ranges
        if metro is not UNSET:
            field_dict["metro"] = metro
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.device_metro import DeviceMetro
        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)




        code = d.pop("code", UNSET)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in (_features or []):
            features_item = FacilityFeaturesItem(features_item_data)



            features.append(features_item)


        id = d.pop("id", UNSET)

        ip_ranges = cast(List[str], d.pop("ip_ranges", UNSET))


        _metro = d.pop("metro", UNSET)
        metro: Union[Unset, DeviceMetro]
        if isinstance(_metro,  Unset):
            metro = UNSET
        else:
            metro = DeviceMetro.from_dict(_metro)




        name = d.pop("name", UNSET)

        facility = cls(
            address=address,
            code=code,
            features=features,
            id=id,
            ip_ranges=ip_ranges,
            metro=metro,
            name=name,
        )

        facility.additional_properties = d
        return facility

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
