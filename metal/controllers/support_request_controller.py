from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.support_request_input import SupportRequestInput
from metal import util


async def request_suppert(request: web.Request, body) -> web.Response:
    """Create a support ticket

    Support Ticket.

    :param body: Support Request to create
    :type body: dict | bytes

    """
    body = SupportRequestInput.from_dict(body)
    return web.Response(status=200)
