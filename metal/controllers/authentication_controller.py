from typing import List, Dict
from aiohttp import web

from metal.types.auth_token import AuthToken
from metal.types.auth_token_input import AuthTokenInput
from metal.types.auth_token_list import AuthTokenList
from metal.types.error import Error
from metal import util


async def create_api_key(request: web.Request, body) -> web.Response:
    """Create an API key

    Creates a API key for the current user.

    :param body: API key to create
    :type body: dict | bytes

    """
    body = AuthTokenInput.from_dict(body)
    return web.Response(status=200)


async def create_project_api_key(request: web.Request, id, body) -> web.Response:
    """Create an API key for a project.

    Creates an API key for a project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: API Key to create
    :type body: dict | bytes

    """
    body = AuthTokenInput.from_dict(body)
    return web.Response(status=200)


async def delete_api_key(request: web.Request, id) -> web.Response:
    """Delete the API key

    Deletes the API key.

    :param id: API Key UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def delete_user_api_key(request: web.Request, id) -> web.Response:
    """Delete the API key

    Deletes the current user API key.

    :param id: API Key UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_api_keys(request: web.Request, include=None, exclude=None) -> web.Response:
    """Retrieve all user API keys

    Returns all API keys for the current user.

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_project_api_keys(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all API keys for the project.

    Returns all API keys for a specific project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
