from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.license import License
from metal.types.license_create_input import LicenseCreateInput
from metal.types.license_list import LicenseList
from metal.types.license_update_input import LicenseUpdateInput
from metal import util


async def create_license(request: web.Request, id, body) -> web.Response:
    """Create a License

    Creates a new license for the given project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: License to create
    :type body: dict | bytes

    """
    body = LicenseCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_license(request: web.Request, id) -> web.Response:
    """Delete the license

    Deletes a license.

    :param id: License UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_license_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a license

    Returns a license

    :param id: License UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_project_licenses(request: web.Request, id, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all licenses

    Provides a collection of licenses for a given project.

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


async def update_license(request: web.Request, id, body) -> web.Response:
    """Update the license

    Updates the license.

    :param id: License UUID
    :type id: str
    :type id: str
    :param body: License to update
    :type body: dict | bytes

    """
    body = LicenseUpdateInput.from_dict(body)
    return web.Response(status=200)
