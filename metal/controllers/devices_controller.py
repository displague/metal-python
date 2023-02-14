from typing import List, Dict
from aiohttp import web

from metal.types.bgp_session_input import BGPSessionInput
from metal.types.bgp_session import BgpSession
from metal.types.bgp_session_list import BgpSessionList
from metal.types.bgp_session_neighbors import BgpSessionNeighbors
from metal.types.create_device_request import CreateDeviceRequest
from metal.types.device import Device
from metal.types.device_action_input import DeviceActionInput
from metal.types.device_list import DeviceList
from metal.types.device_update_input import DeviceUpdateInput
from metal.types.error import Error
from metal.types.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from metal.types.ip_assignment import IPAssignment
from metal.types.ip_assignment_input import IPAssignmentInput
from metal.types.ip_assignment_list import IPAssignmentList
from metal.types.metadata import Metadata
from metal.types.userdata import Userdata
from metal import util


async def create_bgp_session(request: web.Request, id, body) -> web.Response:
    """Create a BGP session

    Creates a BGP session.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param body: BGP session to create
    :type body: dict | bytes

    """
    body = BGPSessionInput.from_dict(body)
    return web.Response(status=200)


async def create_device(request: web.Request, id, body) -> web.Response:
    """Create a device

    Creates a new device and provisions it in the specified location.  Device type-specific options are accepted.  For example, &#x60;baremetal&#x60; devices accept &#x60;operating_system&#x60;, &#x60;hostname&#x60;, and &#x60;plan&#x60;. These parameters may not be accepted for other device types. The default device type is &#x60;baremetal&#x60;.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: Device to create
    :type body: dict | bytes

    """
    body = CreateDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def create_ip_assignment(request: web.Request, id, body) -> web.Response:
    """Create an ip assignment

    Creates an ip assignment for a device.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param body: IPAssignment to create
    :type body: dict | bytes

    """
    body = IPAssignmentInput.from_dict(body)
    return web.Response(status=200)


async def delete_device(request: web.Request, id, force_delete=None) -> web.Response:
    """Delete the device

    Deletes a device and deprovisions it in our datacenter.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param force_delete: Force the deletion of the device, by detaching any storage volume still active.
    :type force_delete: bool

    """
    return web.Response(status=200)


async def find_bgp_sessions(request: web.Request, id) -> web.Response:
    """Retrieve all BGP sessions

    Provides a listing of available BGP sessions for the device.

    :param id: Device UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_device_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a device

    Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning

    :param id: Device UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_device_customdata(request: web.Request, id) -> web.Response:
    """Retrieve the custom metadata of an instance

    Provides the custom metadata stored for this instance in json format

    :param id: Instance UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_device_metadata_by_id(request: web.Request, id) -> web.Response:
    """Retrieve metadata

    Retrieve device metadata

    :param id: Device UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_device_userdata_by_id(request: web.Request, id) -> web.Response:
    """Retrieve userdata

    Retrieve device userdata

    :param id: Device UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_instance_bandwidth(request: web.Request, id, _from, until) -> web.Response:
    """Retrieve an instance bandwidth

    Retrieve an instance bandwidth for a given period of time.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param _from: Timestamp from range
    :type _from: str
    :param until: Timestamp to range
    :type until: str

    """
    return web.Response(status=200)


async def find_ip_assignment_customdata(request: web.Request, instance_id, id) -> web.Response:
    """Retrieve the custom metadata of an IP Assignment

    Provides the custom metadata stored for this IP Assignment in json format

    :param instance_id: Instance UUID
    :type instance_id: str
    :type instance_id: str
    :param id: Ip Assignment UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_ip_assignments(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all ip assignments

    Returns all ip assignments for a device.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_organization_devices(request: web.Request, id, facility=None, hostname=None, reserved=None, tag=None, type=None, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all devices of an organization

    Provides a collection of devices for a given organization.

    :param id: Organization UUID
    :type id: str
    :type id: str
    :param facility: Filter by device facility
    :type facility: str
    :param hostname: Filter by partial hostname
    :type hostname: str
    :param reserved: Filter only reserved instances
    :type reserved: bool
    :param tag: Filter by device tag
    :type tag: str
    :param type: Filter by instance type (ondemand,spot,reserved)
    :type type: str
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


async def find_project_devices(request: web.Request, id, facility=None, hostname=None, reserved=None, tag=None, type=None, include=None, exclude=None, page=None, per_page=None) -> web.Response:
    """Retrieve all devices of a project

    Provides a collection of devices for a given project.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param facility: Filter by device facility
    :type facility: str
    :param hostname: Filter by partial hostname
    :type hostname: str
    :param reserved: Filter only reserved instances
    :type reserved: bool
    :param tag: Filter by device tag
    :type tag: str
    :param type: Filter by instance type (ondemand,spot,reserved)
    :type type: str
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


async def find_traffic(request: web.Request, id, direction, interval=None, bucket=None, timeframe=None) -> web.Response:
    """Retrieve device traffic

    Returns traffic for a specific device.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param direction: Traffic direction
    :type direction: str
    :param interval: Traffic interval
    :type interval: str
    :param bucket: Traffic bucket
    :type bucket: str
    :param timeframe: 
    :type timeframe: dict | bytes
    :type timeframe: Dict[str, ]

    """
    timeframe = .from_dict(timeframe)
    timeframe = {k: object.from_dict(v) for k, v in timeframe}
    return web.Response(status=200)


async def get_bgp_neighbor_data(request: web.Request, id) -> web.Response:
    """Retrieve BGP neighbor data for this device

    Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.

    :param id: Device UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def perform_action(request: web.Request, id, body) -> web.Response:
    """Perform an action

    Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)

    :param id: Device UUID
    :type id: str
    :type id: str
    :param body: Action to perform
    :type body: dict | bytes

    """
    body = DeviceActionInput.from_dict(body)
    return web.Response(status=200)


async def update_device(request: web.Request, id, body) -> web.Response:
    """Update the device

    Updates the device.

    :param id: Device UUID
    :type id: str
    :type id: str
    :param body: Facility to update
    :type body: dict | bytes

    """
    body = DeviceUpdateInput.from_dict(body)
    return web.Response(status=200)
