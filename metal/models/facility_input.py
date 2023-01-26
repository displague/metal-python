from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

T = TypeVar("T", bound="FacilityInput")

@attr.s(auto_attribs=True)
class FacilityInput:
    """
    Attributes:
        facility (Union[List[str], str]): The datacenter where the device should be created.

            Either metro or facility must be provided.

            The API will accept either a single facility `{ "facility": "f1" }`, or it can be instructed to create the
            device in the best available datacenter `{ "facility": "any" }`.

            Additionally it is possible to set a prioritized location selection. For example `{ "facility": ["f3", "f2",
            "any"] }` can be used to prioritize `f3` and then `f2` before accepting `any` facility. If none of the
            facilities provided have availability for the requested device the request will fail.
    """

    facility: Union[List[str], str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        facility: Union[List[str], str]

        if isinstance(self.facility, list):
            facility = self.facility




        else:
            facility = self.facility



        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "facility": facility,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        def _parse_facility(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_facility_input_facility_type_0 = cast(List[str], data)

                return componentsschemas_facility_input_facility_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        facility = _parse_facility(d.pop("facility"))


        facility_input = cls(
            facility=facility,
        )

        facility_input.additional_properties = d
        return facility_input

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
