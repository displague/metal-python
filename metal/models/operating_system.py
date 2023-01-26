from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operating_system_pricing import OperatingSystemPricing




T = TypeVar("T", bound="OperatingSystem")

@attr.s(auto_attribs=True)
class OperatingSystem:
    """
    Attributes:
        distro (Union[Unset, str]):
        distro_label (Union[Unset, str]):
        id (Union[Unset, str]):
        licensed (Union[Unset, bool]): Licenced OS is priced according to pricing property
        name (Union[Unset, str]):
        preinstallable (Union[Unset, bool]): Servers can be already preinstalled with OS in order to shorten provision
            time.
        pricing (Union[Unset, OperatingSystemPricing]): This object contains price per time unit and optional multiplier
            value if licence price depends on hardware plan or components (e.g. number of cores)
        provisionable_on (Union[Unset, List[str]]):
        slug (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    distro: Union[Unset, str] = UNSET
    distro_label: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    licensed: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    preinstallable: Union[Unset, bool] = UNSET
    pricing: Union[Unset, 'OperatingSystemPricing'] = UNSET
    provisionable_on: Union[Unset, List[str]] = UNSET
    slug: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        distro = self.distro
        distro_label = self.distro_label
        id = self.id
        licensed = self.licensed
        name = self.name
        preinstallable = self.preinstallable
        pricing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        provisionable_on: Union[Unset, List[str]] = UNSET
        if not isinstance(self.provisionable_on, Unset):
            provisionable_on = self.provisionable_on




        slug = self.slug
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if distro is not UNSET:
            field_dict["distro"] = distro
        if distro_label is not UNSET:
            field_dict["distro_label"] = distro_label
        if id is not UNSET:
            field_dict["id"] = id
        if licensed is not UNSET:
            field_dict["licensed"] = licensed
        if name is not UNSET:
            field_dict["name"] = name
        if preinstallable is not UNSET:
            field_dict["preinstallable"] = preinstallable
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if provisionable_on is not UNSET:
            field_dict["provisionable_on"] = provisionable_on
        if slug is not UNSET:
            field_dict["slug"] = slug
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operating_system_pricing import OperatingSystemPricing
        d = src_dict.copy()
        distro = d.pop("distro", UNSET)

        distro_label = d.pop("distro_label", UNSET)

        id = d.pop("id", UNSET)

        licensed = d.pop("licensed", UNSET)

        name = d.pop("name", UNSET)

        preinstallable = d.pop("preinstallable", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, OperatingSystemPricing]
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = OperatingSystemPricing.from_dict(_pricing)




        provisionable_on = cast(List[str], d.pop("provisionable_on", UNSET))


        slug = d.pop("slug", UNSET)

        version = d.pop("version", UNSET)

        operating_system = cls(
            distro=distro,
            distro_label=distro_label,
            id=id,
            licensed=licensed,
            name=name,
            preinstallable=preinstallable,
            pricing=pricing,
            provisionable_on=provisionable_on,
            slug=slug,
            version=version,
        )

        operating_system.additional_properties = d
        return operating_system

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
