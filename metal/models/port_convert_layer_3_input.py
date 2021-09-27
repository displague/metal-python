from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.port_convert_layer_3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner




T = TypeVar("T", bound="PortConvertLayer3Input")

@attr.s(auto_attribs=True)
class PortConvertLayer3Input:
    """
    Attributes:
        request_ips (Union[Unset, List['PortConvertLayer3InputRequestIpsInner']]):
    """

    request_ips: Union[Unset, List['PortConvertLayer3InputRequestIpsInner']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        request_ips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.request_ips, Unset):
            request_ips = []
            for request_ips_item_data in self.request_ips:
                request_ips_item = request_ips_item_data.to_dict()

                request_ips.append(request_ips_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if request_ips is not UNSET:
            field_dict["request_ips"] = request_ips

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.port_convert_layer_3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner
        d = src_dict.copy()
        request_ips = []
        _request_ips = d.pop("request_ips", UNSET)
        for request_ips_item_data in (_request_ips or []):
            request_ips_item = PortConvertLayer3InputRequestIpsInner.from_dict(request_ips_item_data)



            request_ips.append(request_ips_item)


        port_convert_layer_3_input = cls(
            request_ips=request_ips,
        )

        port_convert_layer_3_input.additional_properties = d
        return port_convert_layer_3_input

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
