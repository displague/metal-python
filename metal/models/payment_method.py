import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.href import Href
  from ..models.payment_method_billing_address import PaymentMethodBillingAddress




T = TypeVar("T", bound="PaymentMethod")

@attr.s(auto_attribs=True)
class PaymentMethod:
    """
    Attributes:
        billing_address (Union[Unset, PaymentMethodBillingAddress]):
        card_type (Union[Unset, str]):
        cardholder_name (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        created_by_user (Union[Unset, Href]):
        default (Union[Unset, bool]):
        email (Union[Unset, str]):
        expiration_month (Union[Unset, str]):
        expiration_year (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        organization (Union[Unset, Href]):
        projects (Union[Unset, List['Href']]):
        type (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    billing_address: Union[Unset, 'PaymentMethodBillingAddress'] = UNSET
    card_type: Union[Unset, str] = UNSET
    cardholder_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by_user: Union[Unset, 'Href'] = UNSET
    default: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    expiration_month: Union[Unset, str] = UNSET
    expiration_year: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    organization: Union[Unset, 'Href'] = UNSET
    projects: Union[Unset, List['Href']] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        billing_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        card_type = self.card_type
        cardholder_name = self.cardholder_name
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = self.created_by_user.to_dict()

        default = self.default
        email = self.email
        expiration_month = self.expiration_month
        expiration_year = self.expiration_year
        id = self.id
        name = self.name
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()

                projects.append(projects_item)




        type = self.type
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if card_type is not UNSET:
            field_dict["card_type"] = card_type
        if cardholder_name is not UNSET:
            field_dict["cardholder_name"] = cardholder_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if default is not UNSET:
            field_dict["default"] = default
        if email is not UNSET:
            field_dict["email"] = email
        if expiration_month is not UNSET:
            field_dict["expiration_month"] = expiration_month
        if expiration_year is not UNSET:
            field_dict["expiration_year"] = expiration_year
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if projects is not UNSET:
            field_dict["projects"] = projects
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.href import Href
        from ..models.payment_method_billing_address import PaymentMethodBillingAddress
        d = src_dict.copy()
        _billing_address = d.pop("billing_address", UNSET)
        billing_address: Union[Unset, PaymentMethodBillingAddress]
        if isinstance(_billing_address,  Unset):
            billing_address = UNSET
        else:
            billing_address = PaymentMethodBillingAddress.from_dict(_billing_address)




        card_type = d.pop("card_type", UNSET)

        cardholder_name = d.pop("cardholder_name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: Union[Unset, Href]
        if isinstance(_created_by_user,  Unset):
            created_by_user = UNSET
        else:
            created_by_user = Href.from_dict(_created_by_user)




        default = d.pop("default", UNSET)

        email = d.pop("email", UNSET)

        expiration_month = d.pop("expiration_month", UNSET)

        expiration_year = d.pop("expiration_year", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Href]
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = Href.from_dict(_organization)




        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in (_projects or []):
            projects_item = Href.from_dict(projects_item_data)



            projects.append(projects_item)


        type = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        payment_method = cls(
            billing_address=billing_address,
            card_type=card_type,
            cardholder_name=cardholder_name,
            created_at=created_at,
            created_by_user=created_by_user,
            default=default,
            email=email,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            id=id,
            name=name,
            organization=organization,
            projects=projects,
            type=type,
            updated_at=updated_at,
        )

        payment_method.additional_properties = d
        return payment_method

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
