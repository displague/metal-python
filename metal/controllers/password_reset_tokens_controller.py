from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.new_password import NewPassword
from metal import util


async def create_password_reset_token(request: web.Request, email) -> web.Response:
    """Create a password reset token

    Creates a password reset token

    :param email: Email of user to create password reset token
    :type email: str

    """
    return web.Response(status=200)


async def reset_password(request: web.Request, ) -> web.Response:
    """Reset current user password

    Resets current user password.


    """
    return web.Response(status=200)
