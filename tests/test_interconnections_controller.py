# coding: utf-8

import pytest
import json
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


async def test_create_interconnection_port_virtual_circuit(client):
    """Test case for create_interconnection_port_virtual_circuit

    Create a new Virtual Circuit
    """
    body = metal.CreateInterconnectionPortVirtualCircuitRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/connections/{connection_id}/ports/{port_id}/virtual-circuits'.format(connection_id='connection_id_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_organization_interconnection(client):
    """Test case for create_organization_interconnection

    Request a new interconnection for the organization
    """
    body = {"vlans":[1000,1001],"service_token_type":"a_side","description":"description","project":"project","type":"type","speed":10000000000,"contact_email":"contact_email","tags":["tags","tags"],"mode":"standard","metro":"metro","name":"name","redundancy":"redundancy","vrfs":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/organizations/{organization_id}/connections'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_project_interconnection(client):
    """Test case for create_project_interconnection

    Request a new interconnection for the project's organization
    """
    body = {"vlans":[1000,1001],"service_token_type":"a_side","description":"description","project":"project","type":"type","speed":10000000000,"contact_email":"contact_email","tags":["tags","tags"],"mode":"standard","metro":"metro","name":"name","redundancy":"redundancy","vrfs":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{project_id}/connections'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_interconnection(client):
    """Test case for delete_interconnection

    Delete interconnection
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_virtual_circuit(client):
    """Test case for delete_virtual_circuit

    Delete a virtual circuit
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_interconnection(client):
    """Test case for get_interconnection

    Get interconnection
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_interconnection_port(client):
    """Test case for get_interconnection_port

    Get a interconnection port
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/connections/{connection_id}/ports/{id}'.format(connection_id='connection_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_virtual_circuit(client):
    """Test case for get_virtual_circuit

    Get a virtual circuit
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_interconnection_port_virtual_circuits(client):
    """Test case for list_interconnection_port_virtual_circuits

    List a interconnection port's virtual circuits
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/connections/{connection_id}/ports/{port_id}/virtual-circuits'.format(connection_id='connection_id_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_interconnection_ports(client):
    """Test case for list_interconnection_ports

    List a interconnection's ports
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/connections/{connection_id}/ports'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_interconnection_virtual_circuits(client):
    """Test case for list_interconnection_virtual_circuits

    List a interconnection's virtual circuits
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/connections/{connection_id}/virtual-circuits'.format(connection_id='connection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_organization_list_interconnections(client):
    """Test case for organization_list_interconnections

    List organization connections
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{organization_id}/connections'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_project_list_interconnections(client):
    """Test case for project_list_interconnections

    List project connections
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{project_id}/connections'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_interconnection(client):
    """Test case for update_interconnection

    Update interconnection
    """
    body = {"mode":"standard","name":"name","description":"description","redundancy":"redundancy","contact_email":"contact_email","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_virtual_circuit(client):
    """Test case for update_virtual_circuit

    Update a virtual circuit
    """
    body = metal.UpdateVirtualCircuitRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

