from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.find_ip_address_by_id200_response import FindIPAddressById200Response
from metal.types.ip_assignment_update_input import IPAssignmentUpdateInput
from metal.types.ip_availabilities_list import IPAvailabilitiesList
from metal.types.ip_reservation_list import IPReservationList
from metal.types.request_ip_reservation201_response import RequestIPReservation201Response
from metal.types.request_ip_reservation_request import RequestIPReservationRequest
from metal import util


async def delete_ip_address(request: web.Request, id) -> web.Response:
    """Unassign an ip address

    Note! This call can be used to un-assign an IP assignment or delete an IP reservation. Un-assign an IP address record. Use the assignment UUID you get after attaching the IP. This will remove the relationship between an IP and the device and will make the IP address available to be assigned to another device. Delete and IP reservation. Use the reservation UUID you get after adding the IP to the project. This will permanently delete the IP block reservation from the project.

    :param id: IP Address UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_ip_address_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve an ip address

    Returns a single ip address if the user has access.

    :param id: IP Address UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_ip_address_customdata(request: web.Request, id) -> web.Response:
    """Retrieve the custom metadata of an IP Reservation or IP Assignment

    Provides the custom metadata stored for this IP Reservation or IP Assignment in json format

    :param id: Ip Reservation UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_ip_availabilities(request: web.Request, id, cidr) -> web.Response:
    """Retrieve all available subnets of a particular reservation

    Provides a list of IP resevations for a single project.

    :param id: IP Reservation UUID
    :type id: str
    :type id: str
    :param cidr: Size of subnets in bits
    :type cidr: str

    """
    return web.Response(status=200)


async def find_ip_reservations(request: web.Request, id, types=None, include=None, exclude=None, per_page=None) -> web.Response:
    """Retrieve all ip reservations

    Provides a paginated list of IP reservations for a single project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param types: Filter project IP reservations by reservation type
    :type types: List[str]
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param per_page: Items returned per page
    :type per_page: int

    """
    return web.Response(status=200)


async def request_ip_reservation(request: web.Request, id, body) -> web.Response:
    """Requesting IP reservations

    Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a &#x60;state&#x60; of &#x60;pending&#x60;. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the &#x60;fail_on_approval_required&#x60; parameter set to &#x60;true&#x60; in the request.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: IP Reservation Request to create
    :type body: dict | bytes

    """
    body = RequestIPReservationRequest.from_dict(body)
    return web.Response(status=200)


async def update_ip_address(request: web.Request, id, body=None) -> web.Response:
    """Update an ip address

    Update details about an ip address

    :param id: IP Address UUID
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IPAssignmentUpdateInput.from_dict(body)
    return web.Response(status=200)
