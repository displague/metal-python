from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.verify_email import VerifyEmail
from metal import util


async def consume_verification_request(request: web.Request, body) -> web.Response:
    """Verify a user using an email verification token

    Consumes an email verification token and verifies the user associated with it.

    :param body: Email to create
    :type body: dict | bytes

    """
    body = VerifyEmail.from_dict(body)
    return web.Response(status=200)


async def create_validation_request(request: web.Request, login) -> web.Response:
    """Create an email verification request

    Creates an email verification request

    :param login: Email for verification request
    :type login: str

    """
    return web.Response(status=200)
