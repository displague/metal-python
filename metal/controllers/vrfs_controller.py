from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.vrf import Vrf
from metal.types.vrf_create_input import VrfCreateInput
from metal.types.vrf_ip_reservation import VrfIpReservation
from metal.types.vrf_ip_reservation_list import VrfIpReservationList
from metal.types.vrf_list import VrfList
from metal.types.vrf_route import VrfRoute
from metal.types.vrf_route_create_input import VrfRouteCreateInput
from metal.types.vrf_route_list import VrfRouteList
from metal.types.vrf_update_input import VrfUpdateInput
from metal import util


async def create_vrf(request: web.Request, id, body) -> web.Response:
    """Create a new VRF in the specified project

    Creates a new VRF in the specified project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: VRF to create
    :type body: dict | bytes

    """
    body = VrfCreateInput.from_dict(body)
    return web.Response(status=200)


async def create_vrf_route(request: web.Request, id, body) -> web.Response:
    """Create a VRF route

    Create a route in a VRF. Currently only static default routes are supported.  Notice: VRFs are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information. 

    :param id: VRF UUID
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VrfRouteCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_vrf(request: web.Request, id) -> web.Response:
    """Delete the VRF

    Deletes the VRF

    :param id: VRF UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def delete_vrf_route_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Delete a VRF Route

    Trigger the deletion of a VRF Route resource. The status of the route will update to &#39;deleting&#39;, and the route resource will remain accessible while background operations remove the route from the network. Once the route has been removed from the network, the resource will be fully deleted.

    :param id: VRF Route UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_vrf_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a VRF

    Returns a single VRF resource

    :param id: VRF UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_vrf_ip_reservation(request: web.Request, vrf_id, id, include=None, exclude=None) -> web.Response:
    """Retrieve all VRF IP Reservations in the VRF

    Returns the IP Reservation for the VRF.

    :param vrf_id: VRF UUID
    :type vrf_id: str
    :type vrf_id: str
    :param id: IP UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_vrf_ip_reservations(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all VRF IP Reservations in the VRF

    Returns the list of VRF IP Reservations for the VRF.

    :param id: VRF UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_vrf_route_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a VRF Route

    Returns a single VRF Route resource

    :param id: VRF Route UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_vrfs(request: web.Request, id, include=None, exclude=None, metro=None) -> web.Response:
    """Retrieve all VRFs in the project

    Returns the list of VRFs for a single project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param metro: Filter by Metro ID (uuid) or Metro Code
    :type metro: str

    """
    return web.Response(status=200)


async def get_vrf_routes(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all routes in the VRF

    Returns the list of routes for the VRF

    :param id: VRF UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_vrf(request: web.Request, id, body) -> web.Response:
    """Update the VRF

    Updates the VRF.

    :param id: VRF UUID
    :type id: str
    :type id: str
    :param body: VRF to update
    :type body: dict | bytes

    """
    body = VrfUpdateInput.from_dict(body)
    return web.Response(status=200)


async def update_vrf_route_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Update a VRF Route

    Requests a VRF Route be redeployed across the network. Updating the prefix or next-hop address on a route is not currently supported.

    :param id: VRF Route UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
