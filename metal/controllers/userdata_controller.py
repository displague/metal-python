from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal import util


async def validate_userdata(request: web.Request, userdata=None) -> web.Response:
    """Validate user data

    Validates user data (Userdata)

    :param userdata: Userdata to validate
    :type userdata: str

    """
    return web.Response(status=200)
