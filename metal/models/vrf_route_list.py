from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.meta import Meta
  from ..models.vrf_route import VrfRoute




T = TypeVar("T", bound="VrfRouteList")

@attr.s(auto_attribs=True)
class VrfRouteList:
    """
    Attributes:
        routes (Union[Unset, List['VrfRoute']]):
        meta (Union[Unset, Meta]):
    """

    routes: Union[Unset, List['VrfRoute']] = UNSET
    meta: Union[Unset, 'Meta'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        routes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()

                routes.append(routes_item)




        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if routes is not UNSET:
            field_dict["routes"] = routes
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.meta import Meta
        from ..models.vrf_route import VrfRoute
        d = src_dict.copy()
        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in (_routes or []):
            routes_item = VrfRoute.from_dict(routes_item_data)



            routes.append(routes_item)


        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)




        vrf_route_list = cls(
            routes=routes,
            meta=meta,
        )

        vrf_route_list.additional_properties = d
        return vrf_route_list

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