from typing import List, Dict
from aiohttp import web

from metal.types.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from metal.types.error import Error
from metal.types.hardware_reservation import HardwareReservation
from metal.types.hardware_reservation_list import HardwareReservationList
from metal.types.move_hardware_reservation_request import MoveHardwareReservationRequest
from metal import util


async def activate_hardware_reservation(request: web.Request, id, body=None) -> web.Response:
    """Activate a spare hardware reservation

    Activate a spare hardware reservation

    :param id: Hardware Reservation UUID
    :type id: str
    :type id: str
    :param body: Note to attach to the reservation
    :type body: dict | bytes

    """
    body = ActivateHardwareReservationRequest.from_dict(body)
    return web.Response(status=200)


async def find_hardware_reservation_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a hardware reservation

    Returns a single hardware reservation

    :param id: HardwareReservation UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_project_hardware_reservations(request: web.Request, id, query=None, state=None, provisionable=None, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all hardware reservations for a given project

    Provides a collection of hardware reservations for a given project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param query: Search by facility code, plan name, project name, reservation short ID or device hostname
    :type query: str
    :param state: Filter by hardware reservation state
    :type state: str
    :param provisionable: Filter hardware reservation that is provisionable
    :type provisionable: str
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


async def move_hardware_reservation(request: web.Request, id, body) -> web.Response:
    """Move a hardware reservation

    Move a hardware reservation to another project

    :param id: Hardware Reservation UUID
    :type id: str
    :type id: str
    :param body: Destination Project UUID
    :type body: dict | bytes

    """
    body = MoveHardwareReservationRequest.from_dict(body)
    return web.Response(status=200)
