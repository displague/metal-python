from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation_list import InvitationList
from metal.types.user import User
from metal.types.user_create_input import UserCreateInput
from metal.types.user_list import UserList
from metal.types.user_update_input import UserUpdateInput
from metal import util


async def create_user(request: web.Request, body) -> web.Response:
    """Create a user

    Creates a user.

    :param body: User to create
    :type body: dict | bytes

    """
    body = UserCreateInput.from_dict(body)
    return web.Response(status=200)


async def find_current_user(request: web.Request, include=None, exclude=None) -> web.Response:
    """Retrieve the current user

    Returns the user object for the currently logged-in user.

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_invitations(request: web.Request, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve current user invitations

    Returns all invitations in current user.

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


async def find_user_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a user

    Returns a single user if the user has access

    :param id: User UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_user_customdata(request: web.Request, id) -> web.Response:
    """Retrieve the custom metadata of a user

    Provides the custom metadata stored for this user in json format

    :param id: User UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_users(request: web.Request, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all users

    Returns a list of users that the are accessible to the current user (all users in the current user’s projects, essentially).

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


async def update_current_user(request: web.Request, body) -> web.Response:
    """Update the current user

    Updates the currently logged-in user.

    :param body: User to update
    :type body: dict | bytes

    """
    body = UserUpdateInput.from_dict(body)
    return web.Response(status=200)
