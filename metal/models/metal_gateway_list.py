from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metal_gateway import MetalGateway
  from ..models.vrf_metal_gateway import VrfMetalGateway




T = TypeVar("T", bound="MetalGatewayList")

@attr.s(auto_attribs=True)
class MetalGatewayList:
    """
    Attributes:
        metal_gateways (Union[Unset, List[Union['MetalGateway', 'VrfMetalGateway']]]):
    """

    metal_gateways: Union[Unset, List[Union['MetalGateway', 'VrfMetalGateway']]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.metal_gateway import MetalGateway
        metal_gateways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metal_gateways, Unset):
            metal_gateways = []
            for metal_gateways_item_data in self.metal_gateways:
                metal_gateways_item: Dict[str, Any]

                if isinstance(metal_gateways_item_data, MetalGateway):
                    metal_gateways_item = metal_gateways_item_data.to_dict()

                else:
                    metal_gateways_item = metal_gateways_item_data.to_dict()



                metal_gateways.append(metal_gateways_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metal_gateways is not UNSET:
            field_dict["metal_gateways"] = metal_gateways

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metal_gateway import MetalGateway
        from ..models.vrf_metal_gateway import VrfMetalGateway
        d = src_dict.copy()
        metal_gateways = []
        _metal_gateways = d.pop("metal_gateways", UNSET)
        for metal_gateways_item_data in (_metal_gateways or []):
            def _parse_metal_gateways_item(data: object) -> Union['MetalGateway', 'VrfMetalGateway']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_metal_gateway_list_metal_gateways_inner_type_0 = MetalGateway.from_dict(data)



                    return componentsschemas_metal_gateway_list_metal_gateways_inner_type_0
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_metal_gateway_list_metal_gateways_inner_type_1 = VrfMetalGateway.from_dict(data)



                return componentsschemas_metal_gateway_list_metal_gateways_inner_type_1

            metal_gateways_item = _parse_metal_gateways_item(metal_gateways_item_data)

            metal_gateways.append(metal_gateways_item)


        metal_gateway_list = cls(
            metal_gateways=metal_gateways,
        )

        metal_gateway_list.additional_properties = d
        return metal_gateway_list

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
