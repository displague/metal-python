from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.event import Event
from metal.types.event_list import EventList
from metal import util


async def find_device_events(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve device&#39;s events

    Returns a list of events pertaining to a specific device

    :param id: Device UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_event_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve an event

    Returns a single event if the user has access

    :param id: Event UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_events(request: web.Request, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve current user&#39;s events

    Returns a list of the current user’s events

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_interconnection_events(request: web.Request, connection_id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve interconnection events

    Returns a list of the interconnection events

    :param connection_id: Interconnection UUID
    :type connection_id: str
    :type connection_id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_interconnection_port_events(request: web.Request, connection_id, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve interconnection port events

    Returns a list of the interconnection port events

    :param connection_id: Interconnection UUID
    :type connection_id: str
    :type connection_id: str
    :param id: Interconnection Port UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_organization_events(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve organization&#39;s events

    Returns a list of events for a single organization

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_project_events(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve project&#39;s events

    Returns a list of events for a single project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def find_virtual_circuit_events(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve interconnection events

    Returns a list of the virtual circuit events

    :param id: Virtual Circuit UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)
