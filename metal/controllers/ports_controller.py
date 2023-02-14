from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.port import Port
from metal.types.port_assign_input import PortAssignInput
from metal.types.port_convert_layer3_input import PortConvertLayer3Input
from metal.types.port_vlan_assignment import PortVlanAssignment
from metal.types.port_vlan_assignment_batch import PortVlanAssignmentBatch
from metal.types.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput
from metal.types.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList
from metal.types.port_vlan_assignment_list import PortVlanAssignmentList
from metal import util


async def assign_native_vlan(request: web.Request, id, vnid) -> web.Response:
    """Assign a native VLAN

    Sets a virtual network on this port as a \&quot;native VLAN\&quot;. The VLAN must have already been assigned using the using the \&quot;Assign a port to a virtual network\&quot; operation.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param vnid: Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;).
    :type vnid: str

    """
    return web.Response(status=200)


async def assign_port(request: web.Request, id, body) -> web.Response:
    """Assign a port to virtual network

    Assign a hardware port to a virtual network.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param body: Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;).
    :type body: dict | bytes

    """
    body = PortAssignInput.from_dict(body)
    return web.Response(status=200)


async def bond_port(request: web.Request, id, bulk_enable=None) -> web.Response:
    """Enabling bonding

    Enabling bonding for one or all ports

    :param id: Port UUID
    :type id: str
    :type id: str
    :param bulk_enable: enable both ports
    :type bulk_enable: bool

    """
    return web.Response(status=200)


async def convert_layer2(request: web.Request, id, body) -> web.Response:
    """Convert to Layer 2

    Converts a bond port to Layer 2. IP assignments of the port will be removed.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param body: Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;).
    :type body: dict | bytes

    """
    body = PortAssignInput.from_dict(body)
    return web.Response(status=200)


async def convert_layer3(request: web.Request, id, body=None) -> web.Response:
    """Convert to Layer 3

    Converts a bond port to Layer 3. VLANs must first be unassigned.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param body: IPs to request
    :type body: dict | bytes

    """
    body = PortConvertLayer3Input.from_dict(body)
    return web.Response(status=200)


async def create_port_vlan_assignment_batch(request: web.Request, id, body) -> web.Response:
    """Create a new Port-VLAN Assignment management batch

    Create a new asynchronous batch request which handles adding and/or removing the VLANs to which the port is assigned.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param body: VLAN Assignment batch details
    :type body: dict | bytes

    """
    body = PortVlanAssignmentBatchCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_native_vlan(request: web.Request, id) -> web.Response:
    """Remove native VLAN

    Removes the native VLAN from this port

    :param id: Port UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def disbond_port(request: web.Request, id, bulk_disable=None) -> web.Response:
    """Disabling bonding

    Disabling bonding for one or all ports

    :param id: Port UUID
    :type id: str
    :type id: str
    :param bulk_disable: disable both ports
    :type bulk_disable: bool

    """
    return web.Response(status=200)


async def find_port_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a port

    Returns a port

    :param id: Port UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_port_vlan_assignment_batch_by_port_id_and_batch_id(request: web.Request, id, batch_id) -> web.Response:
    """Retrieve a VLAN Assignment Batch&#39;s details

    Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign or unassign, and the current state of the batch.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param batch_id: Batch ID
    :type batch_id: str
    :type batch_id: str

    """
    return web.Response(status=200)


async def find_port_vlan_assignment_batches(request: web.Request, id) -> web.Response:
    """List the VLAN Assignment Batches for a port

    Show all the VLAN assignment batches that have been created for managing this port&#39;s VLAN assignments

    :param id: Port UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_port_vlan_assignment_by_port_id_and_assignment_id(request: web.Request, id, assignment_id, include=None, exclude=None) -> web.Response:
    """Show a particular Port VLAN assignment&#39;s details

    Show the details of a specific Port-VLAN assignment, including the current state and if the VLAN is set as native.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param assignment_id: Assignment ID
    :type assignment_id: str
    :type assignment_id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_port_vlan_assignments(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """List Current VLAN assignments for a port

    Show the port&#39;s current VLAN assignments, including if this VLAN is set as native, and the current state of the assignment (ex. &#39;assigned&#39; or &#39;unassigning&#39;)

    :param id: Port UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def unassign_port(request: web.Request, id, body) -> web.Response:
    """Unassign a port

    Unassign a port for a hardware.

    :param id: Port UUID
    :type id: str
    :type id: str
    :param body: Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself (ex: &#39;1001&#39;).
    :type body: dict | bytes

    """
    body = PortAssignInput.from_dict(body)
    return web.Response(status=200)
