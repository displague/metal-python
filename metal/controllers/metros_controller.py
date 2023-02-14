from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.metro import Metro
from metal.types.metro_list import MetroList
from metal import util


async def find_metros(request: web.Request, ) -> web.Response:
    """Retrieve all metros

    Provides a listing of available metros


    """
    return web.Response(status=200)


async def get_metro(request: web.Request, id) -> web.Response:
    """Retrieve a specific Metro&#39;s details

    Show the details for a metro, including name, code, and country.

    :param id: Metro UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
