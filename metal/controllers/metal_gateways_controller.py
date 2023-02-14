from typing import List, Dict
from aiohttp import web

from metal.types.create_metal_gateway_request import CreateMetalGatewayRequest
from metal.types.error import Error
from metal.types.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
from metal.types.metal_gateway_list import MetalGatewayList
from metal import util


async def create_metal_gateway(request: web.Request, project_id, body, page=None, per_page=None) -> web.Response:
    """Create a metal gateway

    Create a metal gateway in a project

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param body: Metal Gateway to create
    :type body: dict | bytes
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    body = CreateMetalGatewayRequest.from_dict(body)
    return web.Response(status=200)


async def delete_metal_gateway(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Deletes the metal gateway

    Deletes a specific metal gateway

    :param id: Metal Gateway UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_metal_gateway_by_id(request: web.Request, id) -> web.Response:
    """Returns the metal gateway

    Returns a specific metal gateway

    :param id: Metal Gateway UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_metal_gateways_by_project(request: web.Request, project_id, page=None, per_page=None) -> web.Response:
    """Returns all metal gateways for a project

    Return all metal gateways for a project

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)
