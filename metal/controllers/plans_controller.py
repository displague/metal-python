from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.plan_list import PlanList
from metal import util


async def find_plans(request: web.Request, type=None, include=None, exclude=None) -> web.Response:
    """Retrieve all plans

    Provides a listing of available plans to provision your device on.

    :param type: Filter plans by its plan type
    :type type: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_plans_by_project(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all plans visible by the project

    Returns a listing of available plans for the given project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
