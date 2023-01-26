import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.virtual_circuit_status import VirtualCircuitStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href




T = TypeVar("T", bound="VirtualCircuit")

@attr.s(auto_attribs=True)
class VirtualCircuit:
    """
    Attributes:
        bill (bool): True if the Virtual Circuit is being billed. Currently, only Virtual Circuits of Fabric VCs (Metal
            Billed) will be billed. Usage will start the first time the Virtual Circuit becomes active, and will not stop
            until it is deleted from Metal.
        description (str):
        id (str):
        name (str):
        nni_vlan (int):
        port (Href):
        project (Href):
        status (VirtualCircuitStatus): The status of a Virtual Circuit is always 'Pending' on creation. The status can
            turn to 'Waiting on Customer VLAN' if a Metro VLAN was not set yet on the Virtual Circuit and is the last step
            needed for full activation. For Dedicated interconnections, as long as the Dedicated Port has been associated to
            the Virtual Circuit and a NNI VNID has been set, it will turn to 'Waiting on Customer VLAN'. For Fabric VCs, it
            will only change to 'Waiting on Customer VLAN' once the corresponding Fabric connection has been found on the
            Fabric side. Once a Metro VLAN is set on the Virtual Circuit (which for Fabric VCs, can be set on creation) and
            the necessary set up is done, it will turn into 'Activating' status as it tries to activate the Virtual Circuit.
            Once the Virtual Circuit fully activates and is configured on the switch, it will turn to staus 'Active'. For
            Fabric VCs (Metal Billed), we will start billing the moment the status of the Virtual Circuit turns to 'Active'.
            If there are any changes to the VLAN after the Virtual Circuit is in an 'Active' status, the status will show
            'Changing VLAN' if a new VLAN has been provided, or 'Deactivating' if we are removing the VLAN. When a deletion
            request is issued for the Virtual Circuit, it will move to a 'deleting' status until it is fully deleted. If the
            Virtual Circuit is on a Fabric VC, it can also change into an 'Expired' status if the associated service token
            has expired.
        tags (List[str]):
        virtual_network (Href):
        vnid (int):
        speed (Union[Unset, int]): For Virtual Circuits on shared and dedicated connections, this speed should match the
            one set on their Interconnection Ports. For Virtual Circuits on Fabric VCs (both Metal and Fabric Billed) that
            have found their corresponding Fabric connection, this is the actual speed of the interconnection that was
            configured when setting up the interconnection on the Fabric Portal. Details on Fabric VCs are included in the
            specification as a developer preview and is generally unavailable. Please contact our Support team for more
            details.
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    description: str
    id: str
    name: str
    nni_vlan: int
    port: 'Href'
    project: 'Href'
    status: VirtualCircuitStatus
    tags: List[str]
    virtual_network: 'Href'
    vnid: int
    bill: bool = False
    speed: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        bill = self.bill
        description = self.description
        id = self.id
        name = self.name
        nni_vlan = self.nni_vlan
        port = self.port.to_dict()

        project = self.project.to_dict()

        status = self.status.value

        tags = self.tags




        virtual_network = self.virtual_network.to_dict()

        vnid = self.vnid
        speed = self.speed
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bill": bill,
            "description": description,
            "id": id,
            "name": name,
            "nni_vlan": nni_vlan,
            "port": port,
            "project": project,
            "status": status,
            "tags": tags,
            "virtual_network": virtual_network,
            "vnid": vnid,
        })
        if speed is not UNSET:
            field_dict["speed"] = speed
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        d = src_dict.copy()
        bill = d.pop("bill")

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        nni_vlan = d.pop("nni_vlan")

        port = Href.from_dict(d.pop("port"))




        project = Href.from_dict(d.pop("project"))




        status = VirtualCircuitStatus(d.pop("status"))




        tags = cast(List[str], d.pop("tags"))


        virtual_network = Href.from_dict(d.pop("virtual_network"))




        vnid = d.pop("vnid")

        speed = d.pop("speed", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        virtual_circuit = cls(
            bill=bill,
            description=description,
            id=id,
            name=name,
            nni_vlan=nni_vlan,
            port=port,
            project=project,
            status=status,
            tags=tags,
            virtual_network=virtual_network,
            vnid=vnid,
            speed=speed,
            created_at=created_at,
            updated_at=updated_at,
        )

        virtual_circuit.additional_properties = d
        return virtual_circuit

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
