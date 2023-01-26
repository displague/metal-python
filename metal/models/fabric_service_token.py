import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.fabric_service_token_role import FabricServiceTokenRole
from ..models.fabric_service_token_service_token_type import FabricServiceTokenServiceTokenType
from ..models.fabric_service_token_state import FabricServiceTokenState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FabricServiceToken")

@attr.s(auto_attribs=True)
class FabricServiceToken:
    """
    Attributes:
        expires_at (Union[Unset, datetime.datetime]): The expiration date and time of the Fabric service token. Once a
            service token is expired, it is no longer redeemable.
        id (Union[Unset, str]): The UUID that can be used on the Fabric Portal to redeem either an A-Side or Z-Side
            Service Token.
            For Fabric VCs (Metal Billed), this UUID will represent an A-Side Service Token, which will allow
            interconnections
            to be made from Equinix Metal to other Service Providers on Fabric. For Fabric VCs (Fabric Billed), this UUID
            will
            represent a Z-Side Service Token, which will allow interconnections to be made to connect an owned Fabric Port
            or
            Virtual Device to Equinix Metal.
        max_allowed_speed (Union[Unset, int]): The maximum speed that can be selected on the Fabric Portal when
            configuring a interconnection with either
            an A-Side or Z-Side Service Token. For Fabric VCs (Metal Billed), this is what the billing is based off of, and
            can be one
            of the following options, '50mbps', '200mbps', '500mbps', '1gbps', '2gbps', '5gbps' or '10gbps'. For Fabric VCs
            (Fabric Billed), this will default to 10Gbps. Example: 10000000000.
        role (Union[Unset, FabricServiceTokenRole]): Either primary or secondary, depending on which interconnection the
            service token is associated to.
        service_token_type (Union[Unset, FabricServiceTokenServiceTokenType]): Either 'a_side' or 'z_side', depending on
            which type of Fabric VC was requested.
        state (Union[Unset, FabricServiceTokenState]): The state of the service token that corresponds with the service
            token state on Fabric. An 'inactive' state refers to a token that has not been
            redeemed yet on the Fabric side, an 'active' state refers to a token that has
            already been redeemed, and an 'expired' state refers to a token that has reached
            its expiry time.
    """

    expires_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    max_allowed_speed: Union[Unset, int] = UNSET
    role: Union[Unset, FabricServiceTokenRole] = UNSET
    service_token_type: Union[Unset, FabricServiceTokenServiceTokenType] = UNSET
    state: Union[Unset, FabricServiceTokenState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id = self.id
        max_allowed_speed = self.max_allowed_speed
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        service_token_type: Union[Unset, str] = UNSET
        if not isinstance(self.service_token_type, Unset):
            service_token_type = self.service_token_type.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if max_allowed_speed is not UNSET:
            field_dict["max_allowed_speed"] = max_allowed_speed
        if role is not UNSET:
            field_dict["role"] = role
        if service_token_type is not UNSET:
            field_dict["service_token_type"] = service_token_type
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)




        id = d.pop("id", UNSET)

        max_allowed_speed = d.pop("max_allowed_speed", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, FabricServiceTokenRole]
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = FabricServiceTokenRole(_role)




        _service_token_type = d.pop("service_token_type", UNSET)
        service_token_type: Union[Unset, FabricServiceTokenServiceTokenType]
        if isinstance(_service_token_type,  Unset):
            service_token_type = UNSET
        else:
            service_token_type = FabricServiceTokenServiceTokenType(_service_token_type)




        _state = d.pop("state", UNSET)
        state: Union[Unset, FabricServiceTokenState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = FabricServiceTokenState(_state)




        fabric_service_token = cls(
            expires_at=expires_at,
            id=id,
            max_allowed_speed=max_allowed_speed,
            role=role,
            service_token_type=service_token_type,
            state=state,
        )

        fabric_service_token.additional_properties = d
        return fabric_service_token

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
