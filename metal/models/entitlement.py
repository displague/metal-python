from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entitlement_feature_access import EntitlementFeatureAccess
  from ..models.entitlement_instance_quota import EntitlementInstanceQuota
  from ..models.entitlement_ip_quota import EntitlementIpQuota
  from ..models.entitlement_volume_limits import EntitlementVolumeLimits
  from ..models.entitlement_volume_quota import EntitlementVolumeQuota




T = TypeVar("T", bound="Entitlement")

@attr.s(auto_attribs=True)
class Entitlement:
    """
    Attributes:
        id (str):
        slug (str):
        weight (int):
        description (Union[Unset, str]):
        feature_access (Union[Unset, EntitlementFeatureAccess]):
        href (Union[Unset, str]):
        instance_quota (Union[Unset, EntitlementInstanceQuota]):
        ip_quota (Union[Unset, EntitlementIpQuota]):
        name (Union[Unset, str]):
        project_quota (Union[Unset, int]):
        volume_limits (Union[Unset, EntitlementVolumeLimits]):
        volume_quota (Union[Unset, EntitlementVolumeQuota]):
    """

    id: str
    slug: str
    weight: int
    description: Union[Unset, str] = UNSET
    feature_access: Union[Unset, 'EntitlementFeatureAccess'] = UNSET
    href: Union[Unset, str] = UNSET
    instance_quota: Union[Unset, 'EntitlementInstanceQuota'] = UNSET
    ip_quota: Union[Unset, 'EntitlementIpQuota'] = UNSET
    name: Union[Unset, str] = UNSET
    project_quota: Union[Unset, int] = 0
    volume_limits: Union[Unset, 'EntitlementVolumeLimits'] = UNSET
    volume_quota: Union[Unset, 'EntitlementVolumeQuota'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        slug = self.slug
        weight = self.weight
        description = self.description
        feature_access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feature_access, Unset):
            feature_access = self.feature_access.to_dict()

        href = self.href
        instance_quota: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instance_quota, Unset):
            instance_quota = self.instance_quota.to_dict()

        ip_quota: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ip_quota, Unset):
            ip_quota = self.ip_quota.to_dict()

        name = self.name
        project_quota = self.project_quota
        volume_limits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.volume_limits, Unset):
            volume_limits = self.volume_limits.to_dict()

        volume_quota: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.volume_quota, Unset):
            volume_quota = self.volume_quota.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "slug": slug,
            "weight": weight,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if feature_access is not UNSET:
            field_dict["feature_access"] = feature_access
        if href is not UNSET:
            field_dict["href"] = href
        if instance_quota is not UNSET:
            field_dict["instance_quota"] = instance_quota
        if ip_quota is not UNSET:
            field_dict["ip_quota"] = ip_quota
        if name is not UNSET:
            field_dict["name"] = name
        if project_quota is not UNSET:
            field_dict["project_quota"] = project_quota
        if volume_limits is not UNSET:
            field_dict["volume_limits"] = volume_limits
        if volume_quota is not UNSET:
            field_dict["volume_quota"] = volume_quota

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entitlement_feature_access import EntitlementFeatureAccess
        from ..models.entitlement_instance_quota import EntitlementInstanceQuota
        from ..models.entitlement_ip_quota import EntitlementIpQuota
        from ..models.entitlement_volume_limits import EntitlementVolumeLimits
        from ..models.entitlement_volume_quota import EntitlementVolumeQuota
        d = src_dict.copy()
        id = d.pop("id")

        slug = d.pop("slug")

        weight = d.pop("weight")

        description = d.pop("description", UNSET)

        _feature_access = d.pop("feature_access", UNSET)
        feature_access: Union[Unset, EntitlementFeatureAccess]
        if isinstance(_feature_access,  Unset):
            feature_access = UNSET
        else:
            feature_access = EntitlementFeatureAccess.from_dict(_feature_access)




        href = d.pop("href", UNSET)

        _instance_quota = d.pop("instance_quota", UNSET)
        instance_quota: Union[Unset, EntitlementInstanceQuota]
        if isinstance(_instance_quota,  Unset):
            instance_quota = UNSET
        else:
            instance_quota = EntitlementInstanceQuota.from_dict(_instance_quota)




        _ip_quota = d.pop("ip_quota", UNSET)
        ip_quota: Union[Unset, EntitlementIpQuota]
        if isinstance(_ip_quota,  Unset):
            ip_quota = UNSET
        else:
            ip_quota = EntitlementIpQuota.from_dict(_ip_quota)




        name = d.pop("name", UNSET)

        project_quota = d.pop("project_quota", UNSET)

        _volume_limits = d.pop("volume_limits", UNSET)
        volume_limits: Union[Unset, EntitlementVolumeLimits]
        if isinstance(_volume_limits,  Unset):
            volume_limits = UNSET
        else:
            volume_limits = EntitlementVolumeLimits.from_dict(_volume_limits)




        _volume_quota = d.pop("volume_quota", UNSET)
        volume_quota: Union[Unset, EntitlementVolumeQuota]
        if isinstance(_volume_quota,  Unset):
            volume_quota = UNSET
        else:
            volume_quota = EntitlementVolumeQuota.from_dict(_volume_quota)




        entitlement = cls(
            id=id,
            slug=slug,
            weight=weight,
            description=description,
            feature_access=feature_access,
            href=href,
            instance_quota=instance_quota,
            ip_quota=ip_quota,
            name=name,
            project_quota=project_quota,
            volume_limits=volume_limits,
            volume_quota=volume_quota,
        )

        entitlement.additional_properties = d
        return entitlement

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
