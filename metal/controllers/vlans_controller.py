from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.virtual_network import VirtualNetwork
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput
from metal.types.virtual_network_list import VirtualNetworkList
from metal import util


async def create_virtual_network(request: web.Request, id, body) -> web.Response:
    """Create a virtual network

    Creates an virtual network.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: Virtual Network to create
    :type body: dict | bytes

    """
    body = VirtualNetworkCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_virtual_network(request: web.Request, id) -> web.Response:
    """Delete a virtual network

    Deletes a virtual network.

    :param id: Virtual Network UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_virtual_networks(request: web.Request, id, include=None, exclude=None, facility=None, metro=None) -> web.Response:
    """Retrieve all virtual networks

    Provides a list of virtual networks for a single project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param facility: Filter by Facility ID (uuid) or Facility Code
    :type facility: str
    :param metro: Filter by Metro ID (uuid) or Metro Code
    :type metro: str

    """
    return web.Response(status=200)


async def get_virtual_network(request: web.Request, id) -> web.Response:
    """Get a virtual network

    Get a virtual network.

    :param id: Virtual Network UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
