import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
  from ..models.self_service_reservation_item_response import SelfServiceReservationItemResponse




T = TypeVar("T", bound="SelfServiceReservationResponse")

@attr.s(auto_attribs=True)
class SelfServiceReservationResponse:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        item (Union[Unset, List['SelfServiceReservationItemResponse']]):
        notes (Union[Unset, str]):
        organization (Union[Unset, str]):
        organization_id (Union[Unset, str]):
        period (Union[Unset, CreateSelfServiceReservationRequestPeriod]):
        project (Union[Unset, str]):
        project_id (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        total_cost (Union[Unset, int]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    item: Union[Unset, List['SelfServiceReservationItemResponse']] = UNSET
    notes: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    period: Union[Unset, 'CreateSelfServiceReservationRequestPeriod'] = UNSET
    project: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    total_cost: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        item: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item, Unset):
            item = []
            for item_item_data in self.item:
                item_item = item_item_data.to_dict()

                item.append(item_item)




        notes = self.notes
        organization = self.organization
        organization_id = self.organization_id
        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        project = self.project
        project_id = self.project_id
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status = self.status
        total_cost = self.total_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if item is not UNSET:
            field_dict["item"] = item
        if notes is not UNSET:
            field_dict["notes"] = notes
        if organization is not UNSET:
            field_dict["organization"] = organization
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if period is not UNSET:
            field_dict["period"] = period
        if project is not UNSET:
            field_dict["project"] = project
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if status is not UNSET:
            field_dict["status"] = status
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
        from ..models.self_service_reservation_item_response import SelfServiceReservationItemResponse
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        item = []
        _item = d.pop("item", UNSET)
        for item_item_data in (_item or []):
            item_item = SelfServiceReservationItemResponse.from_dict(item_item_data)



            item.append(item_item)


        notes = d.pop("notes", UNSET)

        organization = d.pop("organization", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, CreateSelfServiceReservationRequestPeriod]
        if isinstance(_period,  Unset):
            period = UNSET
        else:
            period = CreateSelfServiceReservationRequestPeriod.from_dict(_period)




        project = d.pop("project", UNSET)

        project_id = d.pop("project_id", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)




        status = d.pop("status", UNSET)

        total_cost = d.pop("total_cost", UNSET)

        self_service_reservation_response = cls(
            created_at=created_at,
            item=item,
            notes=notes,
            organization=organization,
            organization_id=organization_id,
            period=period,
            project=project,
            project_id=project_id,
            start_date=start_date,
            status=status,
            total_cost=total_cost,
        )

        self_service_reservation_response.additional_properties = d
        return self_service_reservation_response

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
