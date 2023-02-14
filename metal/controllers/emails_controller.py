from typing import List, Dict
from aiohttp import web

from metal.types.create_email_input import CreateEmailInput
from metal.types.email import Email
from metal.types.error import Error
from metal.types.update_email_input import UpdateEmailInput
from metal import util


async def create_email(request: web.Request, body) -> web.Response:
    """Create an email

    Add a new email address to the current user.

    :param body: Email to create
    :type body: dict | bytes

    """
    body = CreateEmailInput.from_dict(body)
    return web.Response(status=200)


async def delete_email(request: web.Request, id) -> web.Response:
    """Delete the email

    Deletes the email.

    :param id: Email UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_email_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve an email

    Provides one of the user’s emails.

    :param id: Email UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_email(request: web.Request, id, body) -> web.Response:
    """Update the email

    Updates the email.

    :param id: Email UUID
    :type id: str
    :type id: str
    :param body: email to update
    :type body: dict | bytes

    """
    body = UpdateEmailInput.from_dict(body)
    return web.Response(status=200)
