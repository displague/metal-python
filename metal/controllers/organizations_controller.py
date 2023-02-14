from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation import Invitation
from metal.types.invitation_input import InvitationInput
from metal.types.invitation_list import InvitationList
from metal.types.operating_system_list import OperatingSystemList
from metal.types.organization import Organization
from metal.types.organization_input import OrganizationInput
from metal.types.organization_list import OrganizationList
from metal.types.payment_method import PaymentMethod
from metal.types.payment_method_create_input import PaymentMethodCreateInput
from metal.types.payment_method_list import PaymentMethodList
from metal.types.plan_list import PlanList
from metal.types.project import Project
from metal.types.project_create_input import ProjectCreateInput
from metal.types.project_list import ProjectList
from metal.types.transfer_request_list import TransferRequestList
from metal import util


async def create_organization(request: web.Request, body) -> web.Response:
    """Create an organization

    Creates an organization.

    :param body: Organization to create
    :type body: dict | bytes

    """
    body = OrganizationInput.from_dict(body)
    return web.Response(status=200)


async def create_organization_invitation(request: web.Request, id, body) -> web.Response:
    """Create an invitation for an organization

    In order to add a user to an organization, they must first be invited. To invite to several projects the parameter &#x60;projects_ids:[a,b,c]&#x60; can be used

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param body: Invitation to create
    :type body: dict | bytes

    """
    body = InvitationInput.from_dict(body)
    return web.Response(status=200)


async def create_organization_project(request: web.Request, id, body) -> web.Response:
    """Create a project for the organization

    Creates a new project for the organization

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param body: Project to create
    :type body: dict | bytes

    """
    body = ProjectCreateInput.from_dict(body)
    return web.Response(status=200)


async def create_payment_method(request: web.Request, id, body) -> web.Response:
    """Create a payment method for the given organization

    Creates a payment method.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param body: Payment Method to create
    :type body: dict | bytes

    """
    body = PaymentMethodCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_organization(request: web.Request, id) -> web.Response:
    """Delete the organization

    Deletes the organization.

    :param id: Organization UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_operating_systems_by_organization(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all operating systems visible by the organization

    Returns a listing of available operating systems for the given organization

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_organization_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve an organization&#39;s details

    Returns a single organization&#39;s details, if the user is authorized to view it.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_organization_customdata(request: web.Request, id) -> web.Response:
    """Retrieve the custom metadata of an organization

    Provides the custom metadata stored for this organization in json format

    :param id: Organization UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_organization_invitations(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve organization invitations

    Returns all invitations in an organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_organization_payment_methods(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all payment methods of an organization

    Returns all payment methods of an organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_organization_projects(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all projects of an organization

    Returns a collection of projects that belong to the organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_organization_transfers(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all project transfer requests from or to an organization

    Provides a collection of project transfer requests from or to the organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_organizations(request: web.Request, personal=None, without_projects=None, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all organizations

    Returns a list of organizations that are accessible to the current user.

    :param personal: Include, exclude or show only personal organizations.
    :type personal: str
    :param without_projects: Include, exclude or show only organizations that have no projects.
    :type without_projects: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_plans_by_organization(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all plans visible by the organization

    Returns a listing of available plans for the given organization

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_organization(request: web.Request, id, body) -> web.Response:
    """Update the organization

    Updates the organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param body: Organization to update
    :type body: dict | bytes

    """
    body = OrganizationInput.from_dict(body)
    return web.Response(status=200)
