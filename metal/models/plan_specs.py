from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.plan_specs_cpus_inner import PlanSpecsCpusInner
  from ..models.plan_specs_drives_inner import PlanSpecsDrivesInner
  from ..models.plan_specs_features import PlanSpecsFeatures
  from ..models.plan_specs_nics_inner import PlanSpecsNicsInner




T = TypeVar("T", bound="PlanSpecs")

@attr.s(auto_attribs=True)
class PlanSpecs:
    """
    Attributes:
        cpus (Union[Unset, List['PlanSpecsCpusInner']]):
        drives (Union[Unset, List['PlanSpecsDrivesInner']]):
        nics (Union[Unset, List['PlanSpecsNicsInner']]):
        features (Union[Unset, PlanSpecsFeatures]):
    """

    cpus: Union[Unset, List['PlanSpecsCpusInner']] = UNSET
    drives: Union[Unset, List['PlanSpecsDrivesInner']] = UNSET
    nics: Union[Unset, List['PlanSpecsNicsInner']] = UNSET
    features: Union[Unset, 'PlanSpecsFeatures'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        cpus: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cpus, Unset):
            cpus = []
            for cpus_item_data in self.cpus:
                cpus_item = cpus_item_data.to_dict()

                cpus.append(cpus_item)




        drives: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.drives, Unset):
            drives = []
            for drives_item_data in self.drives:
                drives_item = drives_item_data.to_dict()

                drives.append(drives_item)




        nics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nics, Unset):
            nics = []
            for nics_item_data in self.nics:
                nics_item = nics_item_data.to_dict()

                nics.append(nics_item)




        features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if drives is not UNSET:
            field_dict["drives"] = drives
        if nics is not UNSET:
            field_dict["nics"] = nics
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plan_specs_cpus_inner import PlanSpecsCpusInner
        from ..models.plan_specs_drives_inner import PlanSpecsDrivesInner
        from ..models.plan_specs_features import PlanSpecsFeatures
        from ..models.plan_specs_nics_inner import PlanSpecsNicsInner
        d = src_dict.copy()
        cpus = []
        _cpus = d.pop("cpus", UNSET)
        for cpus_item_data in (_cpus or []):
            cpus_item = PlanSpecsCpusInner.from_dict(cpus_item_data)



            cpus.append(cpus_item)


        drives = []
        _drives = d.pop("drives", UNSET)
        for drives_item_data in (_drives or []):
            drives_item = PlanSpecsDrivesInner.from_dict(drives_item_data)



            drives.append(drives_item)


        nics = []
        _nics = d.pop("nics", UNSET)
        for nics_item_data in (_nics or []):
            nics_item = PlanSpecsNicsInner.from_dict(nics_item_data)



            nics.append(nics_item)


        _features = d.pop("features", UNSET)
        features: Union[Unset, PlanSpecsFeatures]
        if isinstance(_features,  Unset):
            features = UNSET
        else:
            features = PlanSpecsFeatures.from_dict(_features)




        plan_specs = cls(
            cpus=cpus,
            drives=drives,
            nics=nics,
            features=features,
        )

        plan_specs.additional_properties = d
        return plan_specs

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
