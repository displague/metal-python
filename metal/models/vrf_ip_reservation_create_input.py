from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.vrf_ip_reservation_create_input_customdata import VrfIpReservationCreateInputCustomdata




T = TypeVar("T", bound="VrfIpReservationCreateInput")

@attr.s(auto_attribs=True)
class VrfIpReservationCreateInput:
    """
    Attributes:
        cidr (int): The size of the VRF IP Reservation's subnet Example: 16.
        network (str): The starting address for this VRF IP Reservation's subnet Example: 10.1.2.0.
        type (str): Must be set to 'vrf' Example: vrf.
        vrf_id (str): The ID of the VRF in which this VRF IP Reservation is created. The VRF must have an existing IP
            Range that contains the requested subnet. This field may be aliased as just 'vrf'.
        customdata (Union[Unset, VrfIpReservationCreateInputCustomdata]):
        details (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
    """

    cidr: int
    network: str
    type: str
    vrf_id: str
    customdata: Union[Unset, 'VrfIpReservationCreateInputCustomdata'] = UNSET
    details: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        cidr = self.cidr
        network = self.network
        type = self.type
        vrf_id = self.vrf_id
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        details = self.details
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cidr": cidr,
            "network": network,
            "type": type,
            "vrf_id": vrf_id,
        })
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if details is not UNSET:
            field_dict["details"] = details
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vrf_ip_reservation_create_input_customdata import VrfIpReservationCreateInputCustomdata
        d = src_dict.copy()
        cidr = d.pop("cidr")

        network = d.pop("network")

        type = d.pop("type")

        vrf_id = d.pop("vrf_id")

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, VrfIpReservationCreateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = VrfIpReservationCreateInputCustomdata.from_dict(_customdata)




        details = d.pop("details", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        vrf_ip_reservation_create_input = cls(
            cidr=cidr,
            network=network,
            type=type,
            vrf_id=vrf_id,
            customdata=customdata,
            details=details,
            tags=tags,
        )

        vrf_ip_reservation_create_input.additional_properties = d
        return vrf_ip_reservation_create_input

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
