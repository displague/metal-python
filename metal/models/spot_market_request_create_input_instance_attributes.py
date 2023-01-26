import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.spot_market_request_create_input_instance_attributes_customdata import (
      SpotMarketRequestCreateInputInstanceAttributesCustomdata,
  )




T = TypeVar("T", bound="SpotMarketRequestCreateInputInstanceAttributes")

@attr.s(auto_attribs=True)
class SpotMarketRequestCreateInputInstanceAttributes:
    """
    Attributes:
        always_pxe (Union[Unset, bool]):
        billing_cycle (Union[Unset, str]):
        customdata (Union[Unset, SpotMarketRequestCreateInputInstanceAttributesCustomdata]):
        description (Union[Unset, str]):
        features (Union[Unset, List[str]]):
        hostname (Union[Unset, str]):
        hostnames (Union[Unset, List[str]]):
        locked (Union[Unset, bool]):
        no_ssh_keys (Union[Unset, bool]):
        operating_system (Union[Unset, str]):
        plan (Union[Unset, str]):
        private_ipv4_subnet_size (Union[Unset, int]):
        project_ssh_keys (Union[Unset, List[str]]):
        public_ipv4_subnet_size (Union[Unset, int]):
        tags (Union[Unset, List[str]]):
        termination_time (Union[Unset, datetime.datetime]):
        user_ssh_keys (Union[Unset, List[str]]): The UUIDs of users whose SSH keys should be included on the provisioned
            device.
        userdata (Union[Unset, str]):
    """

    always_pxe: Union[Unset, bool] = UNSET
    billing_cycle: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'SpotMarketRequestCreateInputInstanceAttributesCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    features: Union[Unset, List[str]] = UNSET
    hostname: Union[Unset, str] = UNSET
    hostnames: Union[Unset, List[str]] = UNSET
    locked: Union[Unset, bool] = UNSET
    no_ssh_keys: Union[Unset, bool] = UNSET
    operating_system: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    private_ipv4_subnet_size: Union[Unset, int] = UNSET
    project_ssh_keys: Union[Unset, List[str]] = UNSET
    public_ipv4_subnet_size: Union[Unset, int] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    termination_time: Union[Unset, datetime.datetime] = UNSET
    user_ssh_keys: Union[Unset, List[str]] = UNSET
    userdata: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        always_pxe = self.always_pxe
        billing_cycle = self.billing_cycle
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features




        hostname = self.hostname
        hostnames: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames




        locked = self.locked
        no_ssh_keys = self.no_ssh_keys
        operating_system = self.operating_system
        plan = self.plan
        private_ipv4_subnet_size = self.private_ipv4_subnet_size
        project_ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ssh_keys, Unset):
            project_ssh_keys = self.project_ssh_keys




        public_ipv4_subnet_size = self.public_ipv4_subnet_size
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        termination_time: Union[Unset, str] = UNSET
        if not isinstance(self.termination_time, Unset):
            termination_time = self.termination_time.isoformat()

        user_ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_ssh_keys, Unset):
            user_ssh_keys = self.user_ssh_keys




        userdata = self.userdata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if always_pxe is not UNSET:
            field_dict["always_pxe"] = always_pxe
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if features is not UNSET:
            field_dict["features"] = features
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if locked is not UNSET:
            field_dict["locked"] = locked
        if no_ssh_keys is not UNSET:
            field_dict["no_ssh_keys"] = no_ssh_keys
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if plan is not UNSET:
            field_dict["plan"] = plan
        if private_ipv4_subnet_size is not UNSET:
            field_dict["private_ipv4_subnet_size"] = private_ipv4_subnet_size
        if project_ssh_keys is not UNSET:
            field_dict["project_ssh_keys"] = project_ssh_keys
        if public_ipv4_subnet_size is not UNSET:
            field_dict["public_ipv4_subnet_size"] = public_ipv4_subnet_size
        if tags is not UNSET:
            field_dict["tags"] = tags
        if termination_time is not UNSET:
            field_dict["termination_time"] = termination_time
        if user_ssh_keys is not UNSET:
            field_dict["user_ssh_keys"] = user_ssh_keys
        if userdata is not UNSET:
            field_dict["userdata"] = userdata

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spot_market_request_create_input_instance_attributes_customdata import (
            SpotMarketRequestCreateInputInstanceAttributesCustomdata,
        )
        d = src_dict.copy()
        always_pxe = d.pop("always_pxe", UNSET)

        billing_cycle = d.pop("billing_cycle", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, SpotMarketRequestCreateInputInstanceAttributesCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = SpotMarketRequestCreateInputInstanceAttributesCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        features = cast(List[str], d.pop("features", UNSET))


        hostname = d.pop("hostname", UNSET)

        hostnames = cast(List[str], d.pop("hostnames", UNSET))


        locked = d.pop("locked", UNSET)

        no_ssh_keys = d.pop("no_ssh_keys", UNSET)

        operating_system = d.pop("operating_system", UNSET)

        plan = d.pop("plan", UNSET)

        private_ipv4_subnet_size = d.pop("private_ipv4_subnet_size", UNSET)

        project_ssh_keys = cast(List[str], d.pop("project_ssh_keys", UNSET))


        public_ipv4_subnet_size = d.pop("public_ipv4_subnet_size", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        _termination_time = d.pop("termination_time", UNSET)
        termination_time: Union[Unset, datetime.datetime]
        if isinstance(_termination_time,  Unset):
            termination_time = UNSET
        else:
            termination_time = isoparse(_termination_time)




        user_ssh_keys = cast(List[str], d.pop("user_ssh_keys", UNSET))


        userdata = d.pop("userdata", UNSET)

        spot_market_request_create_input_instance_attributes = cls(
            always_pxe=always_pxe,
            billing_cycle=billing_cycle,
            customdata=customdata,
            description=description,
            features=features,
            hostname=hostname,
            hostnames=hostnames,
            locked=locked,
            no_ssh_keys=no_ssh_keys,
            operating_system=operating_system,
            plan=plan,
            private_ipv4_subnet_size=private_ipv4_subnet_size,
            project_ssh_keys=project_ssh_keys,
            public_ipv4_subnet_size=public_ipv4_subnet_size,
            tags=tags,
            termination_time=termination_time,
            user_ssh_keys=user_ssh_keys,
            userdata=userdata,
        )

        spot_market_request_create_input_instance_attributes.additional_properties = d
        return spot_market_request_create_input_instance_attributes

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
