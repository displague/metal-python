from typing import List, Dict
from aiohttp import web

from metal.types.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from metal.types.error import Error
from metal.types.self_service_reservation_list import SelfServiceReservationList
from metal.types.self_service_reservation_response import SelfServiceReservationResponse
from metal import util


async def create_self_service_reservation(request: web.Request, project_id, body) -> web.Response:
    """Create a reservation

    Creates a reservation.

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param body: reservation to create
    :type body: dict | bytes

    """
    body = CreateSelfServiceReservationRequest.from_dict(body)
    return web.Response(status=200)


async def find_self_service_reservation(request: web.Request, id, project_id) -> web.Response:
    """Retrieve a reservation

    Returns a reservation

    :param id: Reservation short_id
    :type id: str
    :type id: str
    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str

    """
    return web.Response(status=200)


async def find_self_service_reservations(request: web.Request, project_id, page=None, per_page=None) -> web.Response:
    """Retrieve all reservations

    Returns all reservations.

    :param project_id: Project UUID
    :type project_id: str
    :type project_id: str
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)
