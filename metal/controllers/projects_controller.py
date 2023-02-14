from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation import Invitation
from metal.types.invitation_input import InvitationInput
from metal.types.invitation_list import InvitationList
from metal.types.membership_list import MembershipList
from metal.types.project import Project
from metal.types.project_create_from_root_input import ProjectCreateFromRootInput
from metal.types.project_list import ProjectList
from metal.types.project_update_input import ProjectUpdateInput
from metal.types.transfer_request import TransferRequest
from metal.types.transfer_request_input import TransferRequestInput
from metal import util


async def create_project(request: web.Request, body) -> web.Response:
    """Create a project

    Creates a new project for the user default organization. If the user don&#39;t have an organization, a new one will be created.

    :param body: Project to create
    :type body: dict | bytes

    """
    body = ProjectCreateFromRootInput.from_dict(body)
    return web.Response(status=200)


async def create_project_invitation(request: web.Request, project_id, body) -> web.Response:
    """Create an invitation for a project

    In order to add a user to a project, they must first be invited.

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param body: Invitation to create
    :type body: dict | bytes

    """
    body = InvitationInput.from_dict(body)
    return web.Response(status=200)


async def create_transfer_request(request: web.Request, id, body) -> web.Response:
    """Create a transfer request

    Organization owners can transfer their projects to other organizations.

    :param id: UUID of the project to be transferred
    :type id: str
    :type id: str
    :param body: Transfer Request to create
    :type body: dict | bytes

    """
    body = TransferRequestInput.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, id) -> web.Response:
    """Delete the project

    Deletes the project.

    :param id: Project UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_ip_reservation_customdata(request: web.Request, project_id, id) -> web.Response:
    """Retrieve the custom metadata of an IP Reservation

    Provides the custom metadata stored for this IP Reservation in json format

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param id: Ip Reservation UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_project_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a project

    Returns a single project if the user has access

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_project_customdata(request: web.Request, id) -> web.Response:
    """Retrieve the custom metadata of a project

    Provides the custom metadata stored for this project in json format

    :param id: Project UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_project_invitations(request: web.Request, project_id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve project invitations

    Returns all invitations in a project.

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
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


async def find_project_memberships(request: web.Request, project_id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve project memberships

    Returns all memberships in a project.

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
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


async def find_projects(request: web.Request, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all projects

    Returns a collection of projects that the current user is a member of.

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


async def update_project(request: web.Request, id, body) -> web.Response:
    """Update the project

    Updates the project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: Project to update
    :type body: dict | bytes

    """
    body = ProjectUpdateInput.from_dict(body)
    return web.Response(status=200)
