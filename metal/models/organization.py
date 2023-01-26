import datetime
from io import BytesIO
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
  from ..models.address import Address
  from ..models.href import Href
  from ..models.organization_customdata import OrganizationCustomdata




T = TypeVar("T", bound="Organization")

@attr.s(auto_attribs=True)
class Organization:
    """
    Attributes:
        address (Union[Unset, Address]):
        billing_address (Union[Unset, Address]):
        created_at (Union[Unset, datetime.datetime]):
        credit_amount (Union[Unset, float]):
        customdata (Union[Unset, OrganizationCustomdata]):
        description (Union[Unset, str]):
        enforce_2fa_at (Union[Unset, datetime.datetime]): Force to all members to have enabled the two factor
            authentication after that date, unless the value is null
        id (Union[Unset, str]):
        logo (Union[Unset, File]):
        members (Union[Unset, List['Href']]):
        memberships (Union[Unset, List['Href']]):
        name (Union[Unset, str]):
        projects (Union[Unset, List['Href']]):
        terms (Union[Unset, int]):
        twitter (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        website (Union[Unset, str]):
    """

    address: Union[Unset, 'Address'] = UNSET
    billing_address: Union[Unset, 'Address'] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    credit_amount: Union[Unset, float] = UNSET
    customdata: Union[Unset, 'OrganizationCustomdata'] = UNSET
    description: Union[Unset, str] = UNSET
    enforce_2fa_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    logo: Union[Unset, File] = UNSET
    members: Union[Unset, List['Href']] = UNSET
    memberships: Union[Unset, List['Href']] = UNSET
    name: Union[Unset, str] = UNSET
    projects: Union[Unset, List['Href']] = UNSET
    terms: Union[Unset, int] = UNSET
    twitter: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        credit_amount = self.credit_amount
        customdata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customdata, Unset):
            customdata = self.customdata.to_dict()

        description = self.description
        enforce_2fa_at: Union[Unset, str] = UNSET
        if not isinstance(self.enforce_2fa_at, Unset):
            enforce_2fa_at = self.enforce_2fa_at.isoformat()

        id = self.id
        logo: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_tuple()

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)




        memberships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()

                memberships.append(memberships_item)




        name = self.name
        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)




        terms = self.terms
        twitter = self.twitter
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if credit_amount is not UNSET:
            field_dict["credit_amount"] = credit_amount
        if customdata is not UNSET:
            field_dict["customdata"] = customdata
        if description is not UNSET:
            field_dict["description"] = description
        if enforce_2fa_at is not UNSET:
            field_dict["enforce_2fa_at"] = enforce_2fa_at
        if id is not UNSET:
            field_dict["id"] = id
        if logo is not UNSET:
            field_dict["logo"] = logo
        if members is not UNSET:
            field_dict["members"] = members
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if name is not UNSET:
            field_dict["name"] = name
        if projects is not UNSET:
            field_dict["projects"] = projects
        if terms is not UNSET:
            field_dict["terms"] = terms
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.href import Href
        from ..models.organization_customdata import OrganizationCustomdata
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




        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        credit_amount = d.pop("credit_amount", UNSET)

        _customdata = d.pop("customdata", UNSET)
        customdata: Union[Unset, OrganizationCustomdata]
        if isinstance(_customdata,  Unset):
            customdata = UNSET
        else:
            customdata = OrganizationCustomdata.from_dict(_customdata)




        description = d.pop("description", UNSET)

        _enforce_2fa_at = d.pop("enforce_2fa_at", UNSET)
        enforce_2fa_at: Union[Unset, datetime.datetime]
        if isinstance(_enforce_2fa_at,  Unset):
            enforce_2fa_at = UNSET
        else:
            enforce_2fa_at = isoparse(_enforce_2fa_at)




        id = d.pop("id", UNSET)

        _logo = d.pop("logo", UNSET)
        logo: Union[Unset, File]
        if isinstance(_logo,  Unset):
            logo = UNSET
        else:
            logo = File(
             payload = BytesIO(_logo)
        )




        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in (_members or []):
            members_item = Href.from_dict(members_item_data)



            members.append(members_item)


        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in (_memberships or []):
            memberships_item = Href.from_dict(memberships_item_data)



            memberships.append(memberships_item)


        name = d.pop("name", UNSET)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in (_projects or []):
            projects_item = Href.from_dict(projects_item_data)



            projects.append(projects_item)


        terms = d.pop("terms", UNSET)

        twitter = d.pop("twitter", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        website = d.pop("website", UNSET)

        organization = cls(
            address=address,
            billing_address=billing_address,
            created_at=created_at,
            credit_amount=credit_amount,
            customdata=customdata,
            description=description,
            enforce_2fa_at=enforce_2fa_at,
            id=id,
            logo=logo,
            members=members,
            memberships=memberships,
            name=name,
            projects=projects,
            terms=terms,
            twitter=twitter,
            updated_at=updated_at,
            website=website,
        )

        organization.additional_properties = d
        return organization

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
