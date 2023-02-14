from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation import Invitation
from metal.types.membership import Membership
from metal import util


async def accept_invitation(request: web.Request, id) -> web.Response:
    """Accept an invitation

    Accept an invitation.

    :param id: Invitation UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def decline_invitation(request: web.Request, id) -> web.Response:
    """Decline an invitation

    Decline an invitation.

    :param id: Invitation UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_invitation_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """View an invitation

    Returns a single invitation. (It include the &#x60;invitable&#x60; to maintain backward compatibility but will be removed soon)

    :param id: Invitation UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
