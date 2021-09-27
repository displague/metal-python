import datetime
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
  from ..models.address import Address
  from ..models.organization_input_customdata import OrganizationInputCustomdata




T = TypeVar("T", bound="OrganizationInput")

@attr.s(auto_attribs=True)
class OrganizationInput:
    """
    Attributes:
        address (Union[Unset, Address]):
        billing_address (Union[Unset, Address]):
        customdata (Union[Unset, OrganizationInputCustomdata]):
        description (Union[Unset, str]):
        enforce_2fa_at (Union[Unset, datetime.datetime]): Force to all members to have enabled the two factor
            authentication after that date, unless the value is null
        logo (Union[Unset, File]):
        name (Union[Unset, str]):
        twitter (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    address: Union[Unset, 'Address'] = UNSET
    billing_address: Union[Unset, 'Address'] = UNSET
    customdata: Union[Unset, 'OrganizationInputCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    enforce_2fa_at: Union[Unset, datetime.datetime] = UNSET
    logo: Union[Unset, File] = UNSET
    name: Union[Unset, str] = UNSET
    twitter: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        enforce_2fa_at: Union[Unset, str] = UNSET
        if not isinstance(self.enforce_2fa_at, Unset):
            enforce_2fa_at = self.enforce_2fa_at.isoformat()

        logo: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_tuple()

        name = self.name
        twitter = self.twitter
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if enforce_2fa_at is not UNSET:
            field_dict["enforce_2fa_at"] = enforce_2fa_at
        if logo is not UNSET:
            field_dict["logo"] = logo
        if name is not UNSET:
            field_dict["name"] = name
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.organization_input_customdata import OrganizationInputCustomdata
        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)




        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, Address]
        if isinstance(_billing_address,  Unset):
            billing_address = UNSET
        else:
            billing_address = Address.from_dict(_billing_address)




        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, OrganizationInputCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = OrganizationInputCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        _enforce_2fa_at = d.pop("enforce_2fa_at", UNSET)
        enforce_2fa_at: Union[Unset, datetime.datetime]
        if isinstance(_enforce_2fa_at,  Unset):
            enforce_2fa_at = UNSET
        else:
            enforce_2fa_at = isoparse(_enforce_2fa_at)




        _logo = d.pop("logo", UNSET)
        logo: Union[Unset, File]
        if isinstance(_logo,  Unset):
            logo = UNSET
        else:
            logo = File(
             payload = BytesIO(_logo)
        )




        name = d.pop("name", UNSET)

        twitter = d.pop("twitter", UNSET)

        website = d.pop("website", UNSET)

        organization_input = cls(
            address=address,
            billing_address=billing_address,
            customdata=customdata,
            description=description,
            enforce_2fa_at=enforce_2fa_at,
            logo=logo,
            name=name,
            twitter=twitter,
            website=website,
        )

        organization_input.additional_properties = d
        return organization_input

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
