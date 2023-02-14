from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.transfer_request import TransferRequest
from metal import util


async def accept_transfer_request(request: web.Request, id) -> web.Response:
    """Accept a transfer request

    Accept a transfer request.

    :param id: Transfer request UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def decline_transfer_request(request: web.Request, id) -> web.Response:
    """Decline a transfer request

    Decline a transfer request.

    :param id: Transfer request UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_transfer_request_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """View a transfer request

    Returns a single transfer request.

    :param id: Transfer request UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
