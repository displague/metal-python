from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.batch import Batch




T = TypeVar("T", bound="BatchesList")

@attr.s(auto_attribs=True)
class BatchesList:
    """
    Attributes:
        batches (Union[Unset, List['Batch']]):
    """

    batches: Union[Unset, List['Batch']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        batches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.batches, Unset):
            batches = []
            for batches_item_data in self.batches:
                batches_item = batches_item_data.to_dict()

                batches.append(batches_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if batches is not UNSET:
            field_dict["batches"] = batches

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch import Batch
        d = src_dict.copy()
        batches = []
        _batches = d.pop("batches", UNSET)
        for batches_item_data in (_batches or []):
            batches_item = Batch.from_dict(batches_item_data)



            batches.append(batches_item)


        batches_list = cls(
            batches=batches,
        )

        batches_list.additional_properties = d
        return batches_list

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
