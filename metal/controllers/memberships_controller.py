from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.membership import Membership
from metal.types.membership_input import MembershipInput
from metal import util


async def delete_membership(request: web.Request, id) -> web.Response:
    """Delete the membership

    Deletes the membership.

    :param id: Membership UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_membership_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a membership

    Returns a single membership.

    :param id: Membership UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_membership(request: web.Request, id, body) -> web.Response:
    """Update the membership

    Updates the membership.

    :param id: Membership UUID
    :type id: str
    :type id: str
    :param body: Membership to update
    :type body: dict | bytes

    """
    body = MembershipInput.from_dict(body)
    return web.Response(status=200)
