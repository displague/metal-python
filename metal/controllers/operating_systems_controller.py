from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.operating_system_list import OperatingSystemList
from metal import util


async def find_operating_system_version(request: web.Request, ) -> web.Response:
    """Retrieve all operating system versions

    Provides a listing of available operating system versions.


    """
    return web.Response(status=200)


async def find_operating_systems(request: web.Request, ) -> web.Response:
    """Retrieve all operating systems

    Provides a listing of available operating systems to provision your new device with.


    """
    return web.Response(status=200)
