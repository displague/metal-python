from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plan import Plan




T = TypeVar("T", bound="PlanList")

@attr.s(auto_attribs=True)
class PlanList:
    """
    Attributes:
        plans (Union[Unset, List['Plan']]):
    """

    plans: Union[Unset, List['Plan']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        plans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.plans, Unset):
            plans = []
            for plans_item_data in self.plans:
                plans_item = plans_item_data.to_dict()

                plans.append(plans_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if plans is not UNSET:
            field_dict["plans"] = plans

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan import Plan
        d = src_dict.copy()
        plans = []
        _plans = d.pop("plans", UNSET)
        for plans_item_data in (_plans or []):
            plans_item = Plan.from_dict(plans_item_data)



            plans.append(plans_item)


        plan_list = cls(
            plans=plans,
        )

        plan_list.additional_properties = d
        return plan_list

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
