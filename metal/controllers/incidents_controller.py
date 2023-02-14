from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal import util


async def find_incidents(request: web.Request, include=None, exclude=None) -> web.Response:
    """Retrieve the number of incidents

    Retrieve the number of incidents.

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
