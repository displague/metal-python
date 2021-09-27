import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.bgp_config_deployment_type import BgpConfigDeploymentType
from ..models.bgp_config_status import BgpConfigStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.bgp_session import BgpSession
  from ..models.global_bgp_range import GlobalBgpRange
  from ..models.href import Href




T = TypeVar("T", bound="BgpConfig")

@attr.s(auto_attribs=True)
class BgpConfig:
    """
    Attributes:
        asn (Union[Unset, int]): Autonomous System Number. ASN is required with Global BGP. With Local BGP the private
            ASN, 65000, is assigned. Example: 65000.
        created_at (Union[Unset, datetime.datetime]):
        deployment_type (Union[Unset, BgpConfigDeploymentType]): In a Local BGP deployment, a customer uses an internal
            ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised
            to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP
            space.
             Example: local.
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        max_prefix (Union[Unset, int]): The maximum number of route filters allowed per server Default: 10.
        md5 (Union[Unset, None, str]): (Optional) Password for BGP session in plaintext (not a checksum)
        project (Union[Unset, Href]):
        ranges (Union[Unset, List['GlobalBgpRange']]): The IP block ranges associated to the ASN (Populated in Global
            BGP only)
        requested_at (Union[Unset, datetime.datetime]):
        route_object (Union[Unset, str]): Specifies AS-MACRO (aka AS-SET) to use when building client route filters
        sessions (Union[Unset, List['BgpSession']]): The direct connections between neighboring routers that want to
            exchange routing information.
        status (Union[Unset, BgpConfigStatus]): Status of the BGP Config. Status "requested" is valid only with the
            "global" deployment_type.
    """

    asn: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deployment_type: Union[Unset, BgpConfigDeploymentType] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    max_prefix: Union[Unset, int] = 10
    md5: Union[Unset, None, str] = UNSET
    project: Union[Unset, 'Href'] = UNSET
    ranges: Union[Unset, List['GlobalBgpRange']] = UNSET
    requested_at: Union[Unset, datetime.datetime] = UNSET
    route_object: Union[Unset, str] = UNSET
    sessions: Union[Unset, List['BgpSession']] = UNSET
    status: Union[Unset, BgpConfigStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        asn = self.asn
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deployment_type: Union[Unset, str] = UNSET
        if not isinstance(self.deployment_type, Unset):
            deployment_type = self.deployment_type.value

        href = self.href
        id = self.id
        max_prefix = self.max_prefix
        md5 = self.md5
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        ranges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()

                ranges.append(ranges_item)




        requested_at: Union[Unset, str] = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        route_object = self.route_object
        sessions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()

                sessions.append(sessions_item)




        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if asn is not UNSET:
            field_dict["asn"] = asn
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deployment_type is not UNSET:
            field_dict["deployment_type"] = deployment_type
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if max_prefix is not UNSET:
            field_dict["max_prefix"] = max_prefix
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if project is not UNSET:
            field_dict["project"] = project
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at
        if route_object is not UNSET:
            field_dict["route_object"] = route_object
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bgp_session import BgpSession
        from ..models.global_bgp_range import GlobalBgpRange
        from ..models.href import Href
        d = src_dict.copy()
        asn = d.pop("asn", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _deployment_type = d.pop("deployment_type", UNSET)
        deployment_type: Union[Unset, BgpConfigDeploymentType]
        if isinstance(_deployment_type,  Unset):
            deployment_type = UNSET
        else:
            deployment_type = BgpConfigDeploymentType(_deployment_type)




        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        max_prefix = d.pop("max_prefix", UNSET)

        md5 = d.pop("md5", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, Href]
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Href.from_dict(_project)




        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in (_ranges or []):
            ranges_item = GlobalBgpRange.from_dict(ranges_item_data)



            ranges.append(ranges_item)


        _requested_at = d.pop("requested_at", UNSET)
        requested_at: Union[Unset, datetime.datetime]
        if isinstance(_requested_at,  Unset):
            requested_at = UNSET
        else:
            requested_at = isoparse(_requested_at)




        route_object = d.pop("route_object", UNSET)

        sessions = []
        _sessions = d.pop("sessions", UNSET)
        for sessions_item_data in (_sessions or []):
            sessions_item = BgpSession.from_dict(sessions_item_data)



            sessions.append(sessions_item)


        _status = d.pop("status", UNSET)
        status: Union[Unset, BgpConfigStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BgpConfigStatus(_status)




        bgp_config = cls(
            asn=asn,
            created_at=created_at,
            deployment_type=deployment_type,
            href=href,
            id=id,
            max_prefix=max_prefix,
            md5=md5,
            project=project,
            ranges=ranges,
            requested_at=requested_at,
            route_object=route_object,
            sessions=sessions,
            status=status,
        )

        bgp_config.additional_properties = d
        return bgp_config

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
