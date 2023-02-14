from typing import List, Dict
from aiohttp import web

from metal.types.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from metal.types.capacity_check_per_metro_list import CapacityCheckPerMetroList
from metal.types.capacity_input import CapacityInput
from metal.types.capacity_list import CapacityList
from metal.types.capacity_per_metro_input import CapacityPerMetroInput
from metal.types.error import Error
from metal.types.metro_capacity_list import MetroCapacityList
from metal import util


async def check_capacity_for_facility(request: web.Request, body) -> web.Response:
    """Check capacity

    Validates if a deploy can be fulfilled.

    :param body: Facility to check capacity in
    :type body: dict | bytes

    """
    body = CapacityInput.from_dict(body)
    return web.Response(status=200)


async def check_capacity_for_metro(request: web.Request, body) -> web.Response:
    """Check capacity for a metro

    Validates if a deploy can be fulfilled in a metro.

    :param body: Metro to check capacity in
    :type body: dict | bytes

    """
    body = CapacityPerMetroInput.from_dict(body)
    return web.Response(status=200)


async def find_capacity_for_facility(request: web.Request, ) -> web.Response:
    """View capacity

    Returns a list of facilities and plans with their current capacity.


    """
    return web.Response(status=200)


async def find_capacity_for_metro(request: web.Request, ) -> web.Response:
    """View capacity for metros

    Returns a list of metros and plans with their current capacity.


    """
    return web.Response(status=200)


async def find_organization_capacity_per_facility(request: web.Request, id) -> web.Response:
    """View available hardware plans per Facility for given organization

    Returns a list of facilities and plans with their current capacity.

    :param id: Organization UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_organization_capacity_per_metro(request: web.Request, id) -> web.Response:
    """View available hardware plans per Metro for given organization

    Returns a list of metros and plans with their current capacity.

    :param id: Organization UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
