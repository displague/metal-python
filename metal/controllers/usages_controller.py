from typing import List, Dict
from aiohttp import web

from metal.types.device_usage_list import DeviceUsageList
from metal.types.error import Error
from metal.types.project_usage_list import ProjectUsageList
from metal import util


async def find_device_usages(request: web.Request, id, created_after=None, created_before=None) -> web.Response:
    """Retrieve all usages for device

    Returns all usages for a device.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param created_after: Filter usages created after this date
    :type created_after: str
    :param created_before: Filter usages created before this date
    :type created_before: str

    """
    return web.Response(status=200)


async def find_project_usage(request: web.Request, id, created_after=None, created_before=None) -> web.Response:
    """Retrieve all usages for project

    Returns all usages for a project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param created_after: Filter usages created after this date
    :type created_after: str
    :param created_before: Filter usages created before this date
    :type created_before: str

    """
    return web.Response(status=200)
