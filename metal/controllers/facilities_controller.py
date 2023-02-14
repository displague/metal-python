from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.facility_list import FacilityList
from metal import util


async def find_facilities(request: web.Request, include=None, exclude=None) -> web.Response:
    """Retrieve all facilities

    Provides a listing of available datacenters where you can provision Packet devices.

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_facilities_by_organization(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all facilities visible by the organization

    Returns a listing of available datacenters for the given organization

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_facilities_by_project(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all facilities visible by the project

    Returns a listing of available datacenters for the given project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
