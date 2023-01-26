import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.vrf_metal_gateway_state import VrfMetalGatewayState
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.project import Project
  from ..models.virtual_network import VirtualNetwork
  from ..models.vrf import Vrf
  from ..models.vrf_ip_reservation import VrfIpReservation




T = TypeVar("T", bound="VrfMetalGateway")

@attr.s(auto_attribs=True)
class VrfMetalGateway:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, Href]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        ip_reservation (Union[Unset, VrfIpReservation]):
        project (Union[Unset, Project]):
        state (Union[Unset, VrfMetalGatewayState]): The current state of the Metal Gateway. 'Ready' indicates the
            gateway record has been configured, but is currently not active on the network. 'Active' indicates the gateway
            has been configured on the network. 'Deleting' is a temporary state used to indicate that the gateway is in the
            process of being un-configured from the network, after which the gateway record will be deleted.
        updated_at (Union[Unset, datetime.datetime]):
        virtual_network (Union[Unset, VirtualNetwork]):
        vrf (Union[Unset, Vrf]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, 'Href'] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_reservation: Union[Unset, 'VrfIpReservation'] = UNSET
    project: Union[Unset, 'Project'] = UNSET
    state: Union[Unset, VrfMetalGatewayState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    virtual_network: Union[Unset, 'VirtualNetwork'] = UNSET
    vrf: Union[Unset, 'Vrf'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        href = self.href
        id = self.id
        ip_reservation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_reservation, Unset):
            ip_reservation = self.ip_reservation.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        virtual_network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.virtual_network, Unset):
            virtual_network = self.virtual_network.to_dict()

        vrf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vrf, Unset):
            vrf = self.vrf.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if ip_reservation is not UNSET:
            field_dict["ip_reservation"] = ip_reservation
        if project is not UNSET:
            field_dict["project"] = project
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if virtual_network is not UNSET:
            field_dict["virtual_network"] = virtual_network
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.project import Project
        from ..models.virtual_network import VirtualNetwork
        from ..models.vrf import Vrf
        from ..models.vrf_ip_reservation import VrfIpReservation
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, Href]
        if isinstance(_created_by,  Unset):
            created_by = UNSET
        else:
            created_by = Href.from_dict(_created_by)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _ip_reservation = d.pop("ip_reservation", UNSET)
        ip_reservation: Union[Unset, VrfIpReservation]
        if isinstance(_ip_reservation,  Unset):
            ip_reservation = UNSET
        else:
            ip_reservation = VrfIpReservation.from_dict(_ip_reservation)




        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        _state = d.pop("state", UNSET)
        state: Union[Unset, VrfMetalGatewayState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = VrfMetalGatewayState(_state)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        _virtual_network = d.pop("virtual_network", UNSET)
        virtual_network: Union[Unset, VirtualNetwork]
        if isinstance(_virtual_network,  Unset):
            virtual_network = UNSET
        else:
            virtual_network = VirtualNetwork.from_dict(_virtual_network)




        _vrf = d.pop("vrf", UNSET)
        vrf: Union[Unset, Vrf]
        if isinstance(_vrf,  Unset):
            vrf = UNSET
        else:
            vrf = Vrf.from_dict(_vrf)




        vrf_metal_gateway = cls(
            created_at=created_at,
            created_by=created_by,
            href=href,
            id=id,
            ip_reservation=ip_reservation,
            project=project,
            state=state,
            updated_at=updated_at,
            virtual_network=virtual_network,
            vrf=vrf,
        )

        vrf_metal_gateway.additional_properties = d
        return vrf_metal_gateway

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
