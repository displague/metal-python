from typing import List, Dict
from aiohttp import web

from metal.types.create_interconnection_port_virtual_circuit201_response import CreateInterconnectionPortVirtualCircuit201Response
from metal.types.create_interconnection_port_virtual_circuit_request import CreateInterconnectionPortVirtualCircuitRequest
from metal.types.error import Error
from metal.types.interconnection import Interconnection
from metal.types.interconnection_create_input import InterconnectionCreateInput
from metal.types.interconnection_list import InterconnectionList
from metal.types.interconnection_port import InterconnectionPort
from metal.types.interconnection_port_list import InterconnectionPortList
from metal.types.interconnection_update_input import InterconnectionUpdateInput
from metal.types.update_virtual_circuit_request import UpdateVirtualCircuitRequest
from metal.types.virtual_circuit_list import VirtualCircuitList
from metal import util


async def create_interconnection_port_virtual_circuit(request: web.Request, connection_id, port_id, body) -> web.Response:
    """Create a new Virtual Circuit

    Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF ID and subnet, along with the NNI VLAN value.

    :param connection_id: UUID of the interconnection
    :type connection_id: str
    :type connection_id: str
    :param port_id: UUID of the interconnection port
    :type port_id: str
    :type port_id: str
    :param body: Virtual Circuit details
    :type body: dict | bytes

    """
    body = CreateInterconnectionPortVirtualCircuitRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_interconnection(request: web.Request, organization_id, body) -> web.Response:
    """Request a new interconnection for the organization

    Creates a new interconnection request. A Project ID must be specified in the request body for connections on shared ports.

    :param organization_id: UUID of the organization
    :type organization_id: str
    :type organization_id: str
    :param body: Interconnection details
    :type body: dict | bytes

    """
    body = InterconnectionCreateInput.from_dict(body)
    return web.Response(status=200)


async def create_project_interconnection(request: web.Request, project_id, body) -> web.Response:
    """Request a new interconnection for the project&#39;s organization

    Creates a new interconnection request

    :param project_id: UUID of the project
    :type project_id: str
    :type project_id: str
    :param body: Interconnection details
    :type body: dict | bytes

    """
    body = InterconnectionCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_interconnection(request: web.Request, connection_id) -> web.Response:
    """Delete interconnection

    Delete a interconnection, its associated ports and virtual circuits.

    :param connection_id: Interconnection UUID
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)


async def delete_virtual_circuit(request: web.Request, id) -> web.Response:
    """Delete a virtual circuit

    Delete a virtual circuit from a Dedicated Port.

    :param id: Virtual Circuit UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_interconnection(request: web.Request, connection_id) -> web.Response:
    """Get interconnection

    Get the details of a interconnection

    :param connection_id: Interconnection UUID
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)


async def get_interconnection_port(request: web.Request, connection_id, id) -> web.Response:
    """Get a interconnection port

    Get the details of an interconnection port.

    :param connection_id: UUID of the interconnection
    :type connection_id: str
    :type connection_id: str
    :param id: Port UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_virtual_circuit(request: web.Request, id) -> web.Response:
    """Get a virtual circuit

    Get the details of a virtual circuit

    :param id: Virtual Circuit UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def list_interconnection_port_virtual_circuits(request: web.Request, connection_id, port_id) -> web.Response:
    """List a interconnection port&#39;s virtual circuits

    List the virtual circuit record(s) associatiated with a particular interconnection port.

    :param connection_id: UUID of the interconnection
    :type connection_id: str
    :type connection_id: str
    :param port_id: UUID of the interconnection port
    :type port_id: str
    :type port_id: str

    """
    return web.Response(status=200)


async def list_interconnection_ports(request: web.Request, connection_id) -> web.Response:
    """List a interconnection&#39;s ports

    List the ports associated to an interconnection.

    :param connection_id: UUID of the interconnection
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)


async def list_interconnection_virtual_circuits(request: web.Request, connection_id) -> web.Response:
    """List a interconnection&#39;s virtual circuits

    List the virtual circuit record(s) associated with a particular interconnection id.

    :param connection_id: UUID of the interconnection
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)


async def organization_list_interconnections(request: web.Request, organization_id) -> web.Response:
    """List organization connections

    List the connections belonging to the organization

    :param organization_id: UUID of the organization
    :type organization_id: str
    :type organization_id: str

    """
    return web.Response(status=200)


async def project_list_interconnections(request: web.Request, project_id) -> web.Response:
    """List project connections

    List the connections belonging to the project

    :param project_id: UUID of the project
    :type project_id: str
    :type project_id: str

    """
    return web.Response(status=200)


async def update_interconnection(request: web.Request, connection_id, body) -> web.Response:
    """Update interconnection

    Update the details of a interconnection

    :param connection_id: Interconnection UUID
    :type connection_id: str
    :type connection_id: str
    :param body: Updated interconnection details
    :type body: dict | bytes

    """
    body = InterconnectionUpdateInput.from_dict(body)
    return web.Response(status=200)


async def update_virtual_circuit(request: web.Request, id, body) -> web.Response:
    """Update a virtual circuit

    Update the details of a virtual circuit.

    :param id: Virtual Circuit UUID
    :type id: str
    :type id: str
    :param body: Updated Virtual Circuit details
    :type body: dict | bytes

    """
    body = UpdateVirtualCircuitRequest.from_dict(body)
    return web.Response(status=200)
