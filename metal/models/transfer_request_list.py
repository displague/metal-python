from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.transfer_request import TransferRequest




T = TypeVar("T", bound="TransferRequestList")

@attr.s(auto_attribs=True)
class TransferRequestList:
    """
    Attributes:
        transfers (Union[Unset, List['TransferRequest']]):
    """

    transfers: Union[Unset, List['TransferRequest']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        transfers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transfers, Unset):
            transfers = []
            for transfers_item_data in self.transfers:
                transfers_item = transfers_item_data.to_dict()

                transfers.append(transfers_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if transfers is not UNSET:
            field_dict["transfers"] = transfers

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transfer_request import TransferRequest
        d = src_dict.copy()
        transfers = []
        _transfers = d.pop("transfers", UNSET)
        for transfers_item_data in (_transfers or []):
            transfers_item = TransferRequest.from_dict(transfers_item_data)



            transfers.append(transfers_item)


        transfer_request_list = cls(
            transfers=transfers,
        )

        transfer_request_list.additional_properties = d
        return transfer_request_list

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
