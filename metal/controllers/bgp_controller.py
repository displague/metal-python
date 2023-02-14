from typing import List, Dict
from aiohttp import web

from metal.types.bgp_config import BgpConfig
from metal.types.bgp_config_request_input import BgpConfigRequestInput
from metal.types.bgp_session import BgpSession
from metal.types.bgp_session_list import BgpSessionList
from metal.types.error import Error
from metal.types.global_bgp_range_list import GlobalBgpRangeList
from metal import util


async def delete_bgp_session(request: web.Request, id) -> web.Response:
    """Delete the BGP session

    Deletes the BGP session.

    :param id: BGP session UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_bgp_config_by_project(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a bgp config

    Returns a bgp config

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_bgp_session_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a BGP session

    Returns a BGP session

    :param id: BGP session UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_global_bgp_ranges(request: web.Request, id) -> web.Response:
    """Retrieve all global bgp ranges

    Returns all global bgp ranges for a project

    :param id: Project UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_project_bgp_sessions(request: web.Request, id) -> web.Response:
    """Retrieve all BGP sessions for project

    Provides a listing of available BGP sessions for the project.

    :param id: Project UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def request_bgp_config(request: web.Request, id, body) -> web.Response:
    """Requesting bgp config

    Requests to enable bgp configuration for a project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: BGP config Request to create
    :type body: dict | bytes

    """
    body = BgpConfigRequestInput.from_dict(body)
    return web.Response(status=200)


async def update_bgp_session(request: web.Request, id, body) -> web.Response:
    """Update the BGP session

    Updates the BGP session by either enabling or disabling the default route functionality.

    :param id: BGP session UUID
    :type id: str
    :type id: str
    :param body: Default route
    :type body: bool

    """
    return web.Response(status=200)
