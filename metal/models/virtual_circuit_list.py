from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.virtual_circuit import VirtualCircuit
  from ..models.vrf_virtual_circuit import VrfVirtualCircuit




T = TypeVar("T", bound="VirtualCircuitList")

@attr.s(auto_attribs=True)
class VirtualCircuitList:
    """
    Attributes:
        virtual_circuits (Union[Unset, List[Union['VirtualCircuit', 'VrfVirtualCircuit']]]):
    """

    virtual_circuits: Union[Unset, List[Union['VirtualCircuit', 'VrfVirtualCircuit']]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.virtual_circuit import VirtualCircuit
        virtual_circuits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.virtual_circuits, Unset):
            virtual_circuits = []
            for virtual_circuits_item_data in self.virtual_circuits:
                virtual_circuits_item: Dict[str, Any]

                if isinstance(virtual_circuits_item_data, VirtualCircuit):
                    virtual_circuits_item = virtual_circuits_item_data.to_dict()

                else:
                    virtual_circuits_item = virtual_circuits_item_data.to_dict()



                virtual_circuits.append(virtual_circuits_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if virtual_circuits is not UNSET:
            field_dict["virtual_circuits"] = virtual_circuits

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.virtual_circuit import VirtualCircuit
        from ..models.vrf_virtual_circuit import VrfVirtualCircuit
        d = src_dict.copy()
        virtual_circuits = []
        _virtual_circuits = d.pop("virtual_circuits", UNSET)
        for virtual_circuits_item_data in (_virtual_circuits or []):
            def _parse_virtual_circuits_item(data: object) -> Union['VirtualCircuit', 'VrfVirtualCircuit']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_virtual_circuit_list_virtual_circuits_inner_type_0 = VirtualCircuit.from_dict(data)



                    return componentsschemas_virtual_circuit_list_virtual_circuits_inner_type_0
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_virtual_circuit_list_virtual_circuits_inner_type_1 = VrfVirtualCircuit.from_dict(data)



                return componentsschemas_virtual_circuit_list_virtual_circuits_inner_type_1

            virtual_circuits_item = _parse_virtual_circuits_item(virtual_circuits_item_data)

            virtual_circuits.append(virtual_circuits_item)


        virtual_circuit_list = cls(
            virtual_circuits=virtual_circuits,
        )

        virtual_circuit_list.additional_properties = d
        return virtual_circuit_list

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
