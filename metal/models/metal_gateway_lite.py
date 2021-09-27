import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.metal_gateway_lite_state import MetalGatewayLiteState
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetalGatewayLite")

@attr.s(auto_attribs=True)
class MetalGatewayLite:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        gateway_address (Union[Unset, str]): The gateway address with subnet CIDR value for this Metal Gateway. For
            example, a Metal Gateway using an IP reservation with block 10.1.2.0/27 would have a gateway address of
            10.1.2.1/27. Example: 10.1.2.1/27.
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        state (Union[Unset, MetalGatewayLiteState]): The current state of the Metal Gateway. 'Ready' indicates the
            gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway
            has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the
            process of being un-configured from the network, after which the gateway record will be deleted.
        updated_at (Union[Unset, datetime.datetime]):
        vlan (Union[Unset, int]): The VLAN id of the Virtual Network record associated to this Metal Gateway. Example:
            1001.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    gateway_address: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    state: Union[Unset, MetalGatewayLiteState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    vlan: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        gateway_address = self.gateway_address
        href = self.href
        id = self.id
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        vlan = self.vlan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if gateway_address is not UNSET:
            field_dict["gateway_address"] = gateway_address
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        gateway_address = d.pop("gateway_address", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, MetalGatewayLiteState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = MetalGatewayLiteState(_state)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        vlan = d.pop("vlan", UNSET)

        metal_gateway_lite = cls(
            created_at=created_at,
            gateway_address=gateway_address,
            href=href,
            id=id,
            state=state,
            updated_at=updated_at,
            vlan=vlan,
        )

        metal_gateway_lite.additional_properties = d
        return metal_gateway_lite

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
