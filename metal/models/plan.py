from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.plan_deployment_types_item import PlanDeploymentTypesItem
from ..models.plan_line import PlanLine
from ..models.plan_type import PlanType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plan_available_in_inner import PlanAvailableInInner
  from ..models.plan_available_in_metros_inner import PlanAvailableInMetrosInner
  from ..models.plan_pricing import PlanPricing
  from ..models.plan_specs import PlanSpecs




T = TypeVar("T", bound="Plan")

@attr.s(auto_attribs=True)
class Plan:
    """
    Attributes:
        available_in (Union[Unset, List['PlanAvailableInInner']]): Shows which facilities the plan is available in, and
            the facility-based price if it is different from the default price.
        available_in_metros (Union[Unset, List['PlanAvailableInMetrosInner']]): Shows which metros the plan is available
            in, and the metro-based price if it is different from the default price.
        class_ (Union[Unset, str]):  Example: m3.large.x86.
        description (Union[Unset, str]):
        deployment_types (Union[Unset, List[PlanDeploymentTypesItem]]):
        id (Union[Unset, str]):
        legacy (Union[Unset, bool]):
        line (Union[Unset, PlanLine]):
        name (Union[Unset, str]):
        pricing (Union[Unset, PlanPricing]):
        slug (Union[Unset, str]):  Example: m3.large.x86.
        specs (Union[Unset, PlanSpecs]):
        type (Union[Unset, PlanType]): The plan type
    """

    available_in: Union[Unset, List['PlanAvailableInInner']] = UNSET
    available_in_metros: Union[Unset, List['PlanAvailableInMetrosInner']] = UNSET
    class_: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    deployment_types: Union[Unset, List[PlanDeploymentTypesItem]] = UNSET
    id: Union[Unset, str] = UNSET
    legacy: Union[Unset, bool] = UNSET
    line: Union[Unset, PlanLine] = UNSET
    name: Union[Unset, str] = UNSET
    pricing: Union[Unset, 'PlanPricing'] = UNSET
    slug: Union[Unset, str] = UNSET
    specs: Union[Unset, 'PlanSpecs'] = UNSET
    type: Union[Unset, PlanType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        available_in: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_in, Unset):
            available_in = []
            for available_in_item_data in self.available_in:
                available_in_item = available_in_item_data.to_dict()

                available_in.append(available_in_item)




        available_in_metros: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_in_metros, Unset):
            available_in_metros = []
            for available_in_metros_item_data in self.available_in_metros:
                available_in_metros_item = available_in_metros_item_data.to_dict()

                available_in_metros.append(available_in_metros_item)




        class_ = self.class_
        description = self.description
        deployment_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.deployment_types, Unset):
            deployment_types = []
            for deployment_types_item_data in self.deployment_types:
                deployment_types_item = deployment_types_item_data.value

                deployment_types.append(deployment_types_item)




        id = self.id
        legacy = self.legacy
        line: Union[Unset, str] = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.value

        name = self.name
        pricing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        slug = self.slug
        specs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.specs, Unset):
            specs = self.specs.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available_in is not UNSET:
            field_dict["available_in"] = available_in
        if available_in_metros is not UNSET:
            field_dict["available_in_metros"] = available_in_metros
        if class_ is not UNSET:
            field_dict["class"] = class_
        if description is not UNSET:
            field_dict["description"] = description
        if deployment_types is not UNSET:
            field_dict["deployment_types"] = deployment_types
        if id is not UNSET:
            field_dict["id"] = id
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if line is not UNSET:
            field_dict["line"] = line
        if name is not UNSET:
            field_dict["name"] = name
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if slug is not UNSET:
            field_dict["slug"] = slug
        if specs is not UNSET:
            field_dict["specs"] = specs
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_available_in_inner import PlanAvailableInInner
        from ..models.plan_available_in_metros_inner import PlanAvailableInMetrosInner
        from ..models.plan_pricing import PlanPricing
        from ..models.plan_specs import PlanSpecs
        d = src_dict.copy()
        available_in = []
        _available_in = d.pop("available_in", UNSET)
        for available_in_item_data in (_available_in or []):
            available_in_item = PlanAvailableInInner.from_dict(available_in_item_data)



            available_in.append(available_in_item)


        available_in_metros = []
        _available_in_metros = d.pop("available_in_metros", UNSET)
        for available_in_metros_item_data in (_available_in_metros or []):
            available_in_metros_item = PlanAvailableInMetrosInner.from_dict(available_in_metros_item_data)



            available_in_metros.append(available_in_metros_item)


        class_ = d.pop("class", UNSET)

        description = d.pop("description", UNSET)

        deployment_types = []
        _deployment_types = d.pop("deployment_types", UNSET)
        for deployment_types_item_data in (_deployment_types or []):
            deployment_types_item = PlanDeploymentTypesItem(deployment_types_item_data)



            deployment_types.append(deployment_types_item)


        id = d.pop("id", UNSET)

        legacy = d.pop("legacy", UNSET)

        _line = d.pop("line", UNSET)
        line: Union[Unset, PlanLine]
        if isinstance(_line,  Unset):
            line = UNSET
        else:
            line = PlanLine(_line)




        name = d.pop("name", UNSET)

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, PlanPricing]
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = PlanPricing.from_dict(_pricing)




        slug = d.pop("slug", UNSET)

        _specs = d.pop("specs", UNSET)
        specs: Union[Unset, PlanSpecs]
        if isinstance(_specs,  Unset):
            specs = UNSET
        else:
            specs = PlanSpecs.from_dict(_specs)




        _type = d.pop("type", UNSET)
        type: Union[Unset, PlanType]
        if isinstance(_type,  Unset):
            type = UNSET
        else:
            type = PlanType(_type)




        plan = cls(
            available_in=available_in,
            available_in_metros=available_in_metros,
            class_=class_,
            description=description,
            deployment_types=deployment_types,
            id=id,
            legacy=legacy,
            line=line,
            name=name,
            pricing=pricing,
            slug=slug,
            specs=specs,
            type=type,
        )

        plan.additional_properties = d
        return plan

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
