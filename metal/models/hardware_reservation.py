import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.device import Device
  from ..models.facility import Facility
  from ..models.plan import Plan
  from ..models.project import Project




T = TypeVar("T", bound="HardwareReservation")

@attr.s(auto_attribs=True)
class HardwareReservation:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        custom_rate (Union[Unset, float]): Amount that will be charged for every billing_cycle. Example: 1050.5.
        device (Union[Unset, Device]):
        facility (Union[Unset, Facility]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        need_of_service (Union[Unset, bool]): Whether this Device requires assistance from Equinix Metal.
        plan (Union[Unset, Plan]):
        project (Union[Unset, Project]):
        provisionable (Union[Unset, bool]): Whether the reserved server is provisionable or not. Spare devices can't be
            provisioned unless they are activated first.
        short_id (Union[Unset, str]): Short version of the ID.
        spare (Union[Unset, bool]): Whether the Hardware Reservation is a spare. Spare Hardware Reservations are used
            when a Hardware Reservations requires service from Equinix Metal
        switch_uuid (Union[Unset, str]): Switch short id. This can be used to determine if two devices are connected to
            the same switch, for example.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    custom_rate: Union[Unset, float] = UNSET
    device: Union[Unset, 'Device'] = UNSET
    facility: Union[Unset, 'Facility'] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    need_of_service: Union[Unset, bool] = UNSET
    plan: Union[Unset, 'Plan'] = UNSET
    project: Union[Unset, 'Project'] = UNSET
    provisionable: Union[Unset, bool] = UNSET
    short_id: Union[Unset, str] = UNSET
    spare: Union[Unset, bool] = UNSET
    switch_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        custom_rate = self.custom_rate
        device: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        facility: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.facility, Unset):
            facility = self.facility.to_dict()

        href = self.href
        id = self.id
        need_of_service = self.need_of_service
        plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        provisionable = self.provisionable
        short_id = self.short_id
        spare = self.spare
        switch_uuid = self.switch_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if custom_rate is not UNSET:
            field_dict["custom_rate"] = custom_rate
        if device is not UNSET:
            field_dict["device"] = device
        if facility is not UNSET:
            field_dict["facility"] = facility
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if need_of_service is not UNSET:
            field_dict["need_of_service"] = need_of_service
        if plan is not UNSET:
            field_dict["plan"] = plan
        if project is not UNSET:
            field_dict["project"] = project
        if provisionable is not UNSET:
            field_dict["provisionable"] = provisionable
        if short_id is not UNSET:
            field_dict["short_id"] = short_id
        if spare is not UNSET:
            field_dict["spare"] = spare
        if switch_uuid is not UNSET:
            field_dict["switch_uuid"] = switch_uuid

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device import Device
        from ..models.facility import Facility
        from ..models.plan import Plan
        from ..models.project import Project
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        custom_rate = d.pop("custom_rate", UNSET)

        _device = d.pop("device", UNSET)
        device: Union[Unset, Device]
        if isinstance(_device,  Unset):
            device = UNSET
        else:
            device = Device.from_dict(_device)




        _facility = d.pop("facility", UNSET)
        facility: Union[Unset, Facility]
        if isinstance(_facility,  Unset):
            facility = UNSET
        else:
            facility = Facility.from_dict(_facility)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        need_of_service = d.pop("need_of_service", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, Plan]
        if isinstance(_plan,  Unset):
            plan = UNSET
        else:
            plan = Plan.from_dict(_plan)




        _project = d.pop("project", UNSET)
        project: Union[Unset, Project]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        provisionable = d.pop("provisionable", UNSET)

        short_id = d.pop("short_id", UNSET)

        spare = d.pop("spare", UNSET)

        switch_uuid = d.pop("switch_uuid", UNSET)

        hardware_reservation = cls(
            created_at=created_at,
            custom_rate=custom_rate,
            device=device,
            facility=facility,
            href=href,
            id=id,
            need_of_service=need_of_service,
            plan=plan,
            project=project,
            provisionable=provisionable,
            short_id=short_id,
            spare=spare,
            switch_uuid=switch_uuid,
        )

        hardware_reservation.additional_properties = d
        return hardware_reservation

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
