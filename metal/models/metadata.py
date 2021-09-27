from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.metadata_customdata import MetadataCustomdata
  from ..models.metadata_network import MetadataNetwork
  from ..models.metadata_operating_system import MetadataOperatingSystem
  from ..models.metadata_specs import MetadataSpecs




T = TypeVar("T", bound="Metadata")

@attr.s(auto_attribs=True)
class Metadata:
    """
    Attributes:
        class_ (Union[Unset, str]):
        customdata (Union[Unset, MetadataCustomdata]):
        facility (Union[Unset, str]): The facility code of the instance
        hostname (Union[Unset, str]):
        id (Union[Unset, str]):
        iqn (Union[Unset, str]):
        metro (Union[Unset, str]): The metro code of the instance
        network (Union[Unset, MetadataNetwork]):
        operating_system (Union[Unset, MetadataOperatingSystem]):
        plan (Union[Unset, str]): The plan slug of the instance
        private_subnets (Union[Unset, List[str]]): An array of the private subnets
        reserved (Union[Unset, bool]):
        specs (Union[Unset, MetadataSpecs]): The specs of the plan version of the instance
        ssh_keys (Union[Unset, List[str]]):
        switch_short_id (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        volumes (Union[Unset, List[str]]):
    """

    class_: Union[Unset, str] = UNSET
    customdata: Union[Unset, 'MetadataCustomdata'] = UNSET
    facility: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    iqn: Union[Unset, str] = UNSET
    metro: Union[Unset, str] = UNSET
    network: Union[Unset, 'MetadataNetwork'] = UNSET
    operating_system: Union[Unset, 'MetadataOperatingSystem'] = UNSET
    plan: Union[Unset, str] = UNSET
    private_subnets: Union[Unset, List[str]] = UNSET
    reserved: Union[Unset, bool] = UNSET
    specs: Union[Unset, 'MetadataSpecs'] = UNSET
    ssh_keys: Union[Unset, List[str]] = UNSET
    switch_short_id: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    volumes: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        class_ = self.class_
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        facility = self.facility
        hostname = self.hostname
        id = self.id
        iqn = self.iqn
        metro = self.metro
        network: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        operating_system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system.to_dict()

        plan = self.plan
        private_subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.private_subnets, Unset):
            private_subnets = self.private_subnets




        reserved = self.reserved
        specs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specs, Unset):
            specs = self.specs.to_dict()

        ssh_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = self.ssh_keys




        switch_short_id = self.switch_short_id
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        volumes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = self.volumes





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if class_ is not UNSET:
            field_dict["class"] = class_
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if facility is not UNSET:
            field_dict["facility"] = facility
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if iqn is not UNSET:
            field_dict["iqn"] = iqn
        if metro is not UNSET:
            field_dict["metro"] = metro
        if network is not UNSET:
            field_dict["network"] = network
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if plan is not UNSET:
            field_dict["plan"] = plan
        if private_subnets is not UNSET:
            field_dict["private_subnets"] = private_subnets
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if specs is not UNSET:
            field_dict["specs"] = specs
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if switch_short_id is not UNSET:
            field_dict["switch_short_id"] = switch_short_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_customdata import MetadataCustomdata
        from ..models.metadata_network import MetadataNetwork
        from ..models.metadata_operating_system import MetadataOperatingSystem
        from ..models.metadata_specs import MetadataSpecs
        d = src_dict.copy()
        class_ = d.pop("class", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, MetadataCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = MetadataCustomdata.from_dict(_customdata)




        facility = d.pop("facility", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        iqn = d.pop("iqn", UNSET)

        metro = d.pop("metro", UNSET)

        _network = d.pop("network", UNSET)
        network: Union[Unset, MetadataNetwork]
        if isinstance(_network,  Unset):
            network = UNSET
        else:
            network = MetadataNetwork.from_dict(_network)




        _operating_system = d.pop("operating_system", UNSET)
        operating_system: Union[Unset, MetadataOperatingSystem]
        if isinstance(_operating_system,  Unset):
            operating_system = UNSET
        else:
            operating_system = MetadataOperatingSystem.from_dict(_operating_system)




        plan = d.pop("plan", UNSET)

        private_subnets = cast(List[str], d.pop("private_subnets", UNSET))


        reserved = d.pop("reserved", UNSET)

        _specs = d.pop("specs", UNSET)
        specs: Union[Unset, MetadataSpecs]
        if isinstance(_specs,  Unset):
            specs = UNSET
        else:
            specs = MetadataSpecs.from_dict(_specs)




        ssh_keys = cast(List[str], d.pop("ssh_keys", UNSET))


        switch_short_id = d.pop("switch_short_id", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))


        volumes = cast(List[str], d.pop("volumes", UNSET))


        metadata = cls(
            class_=class_,
            customdata=customdata,
            facility=facility,
            hostname=hostname,
            id=id,
            iqn=iqn,
            metro=metro,
            network=network,
            operating_system=operating_system,
            plan=plan,
            private_subnets=private_subnets,
            reserved=reserved,
            specs=specs,
            ssh_keys=ssh_keys,
            switch_short_id=switch_short_id,
            tags=tags,
            volumes=volumes,
        )

        metadata.additional_properties = d
        return metadata

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
