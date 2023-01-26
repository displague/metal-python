from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.device_update_input_customdata import DeviceUpdateInputCustomdata




T = TypeVar("T", bound="DeviceUpdateInput")

@attr.s(auto_attribs=True)
class DeviceUpdateInput:
    """
    Attributes:
        always_pxe (Union[Unset, bool]):
        billing_cycle (Union[Unset, str]):
        customdata (Union[Unset, DeviceUpdateInputCustomdata]):
        description (Union[Unset, str]):
        hostname (Union[Unset, str]):
        ipxe_script_url (Union[Unset, str]):
        locked (Union[Unset, bool]):
        network_frozen (Union[Unset, bool]): If true, this instance can not be converted to a different network type.
        spot_instance (Union[Unset, bool]): Can be set to false to convert a spot-market instance to on-demand.
        tags (Union[Unset, List[str]]):
        userdata (Union[Unset, str]):
    """

    always_pxe: Union[Unset, bool] = UNSET
    billing_cycle: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'DeviceUpdateInputCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    ipxe_script_url: Union[Unset, str] = UNSET
    locked: Union[Unset, bool] = UNSET
    network_frozen: Union[Unset, bool] = UNSET
    spot_instance: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    userdata: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        always_pxe = self.always_pxe
        billing_cycle = self.billing_cycle
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        hostname = self.hostname
        ipxe_script_url = self.ipxe_script_url
        locked = self.locked
        network_frozen = self.network_frozen
        spot_instance = self.spot_instance
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        userdata = self.userdata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if always_pxe is not UNSET:
            field_dict["always_pxe"] = always_pxe
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ipxe_script_url is not UNSET:
            field_dict["ipxe_script_url"] = ipxe_script_url
        if locked is not UNSET:
            field_dict["locked"] = locked
        if network_frozen is not UNSET:
            field_dict["network_frozen"] = network_frozen
        if spot_instance is not UNSET:
            field_dict["spot_instance"] = spot_instance
        if tags is not UNSET:
            field_dict["tags"] = tags
        if userdata is not UNSET:
            field_dict["userdata"] = userdata

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_update_input_customdata import DeviceUpdateInputCustomdata
        d = src_dict.copy()
        always_pxe = d.pop("always_pxe", UNSET)

        billing_cycle = d.pop("billing_cycle", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, DeviceUpdateInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = DeviceUpdateInputCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        hostname = d.pop("hostname", UNSET)

        ipxe_script_url = d.pop("ipxe_script_url", UNSET)

        locked = d.pop("locked", UNSET)

        network_frozen = d.pop("network_frozen", UNSET)

        spot_instance = d.pop("spot_instance", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        userdata = d.pop("userdata", UNSET)

        device_update_input = cls(
            always_pxe=always_pxe,
            billing_cycle=billing_cycle,
            customdata=customdata,
            description=description,
            hostname=hostname,
            ipxe_script_url=ipxe_script_url,
            locked=locked,
            network_frozen=network_frozen,
            spot_instance=spot_instance,
            tags=tags,
            userdata=userdata,
        )

        device_update_input.additional_properties = d
        return device_update_input

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
