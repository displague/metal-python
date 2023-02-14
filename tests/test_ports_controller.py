# coding: utf-8

import pytest
import json
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


async def test_assign_native_vlan(client):
    """Test case for assign_native_vlan

    Assign a native VLAN
    """
    params = [('vnid', 'vnid_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/native-vlan'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_assign_port(client):
    """Test case for assign_port

    Assign a port to virtual network
    """
    body = {"vnid":"1001"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/assign'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_bond_port(client):
    """Test case for bond_port

    Enabling bonding
    """
    params = [('bulk_enable', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/bond'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_convert_layer2(client):
    """Test case for convert_layer2

    Convert to Layer 2
    """
    body = {"vnid":"1001"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/convert/layer-2'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_convert_layer3(client):
    """Test case for convert_layer3

    Convert to Layer 3
    """
    body = {"request_ips":[{"address_family":0,"public":True},{"address_family":0,"public":True}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/convert/layer-3'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_port_vlan_assignment_batch(client):
    """Test case for create_port_vlan_assignment_batch

    Create a new Port-VLAN Assignment management batch
    """
    body = {"vlan_assignments":[{"vlan":"vlan","native":True,"state":"assigned"},{"vlan":"vlan","native":True,"state":"assigned"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/vlan-assignments/batches'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_native_vlan(client):
    """Test case for delete_native_vlan

    Remove native VLAN
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/ports/{id}/native-vlan'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_disbond_port(client):
    """Test case for disbond_port

    Disabling bonding
    """
    params = [('bulk_disable', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/disbond'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_port_by_id(client):
    """Test case for find_port_by_id

    Retrieve a port
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ports/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_port_vlan_assignment_batch_by_port_id_and_batch_id(client):
    """Test case for find_port_vlan_assignment_batch_by_port_id_and_batch_id

    Retrieve a VLAN Assignment Batch's details
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ports/{id}/vlan-assignments/batches/{batch_id}'.format(id='id_example', batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_port_vlan_assignment_batches(client):
    """Test case for find_port_vlan_assignment_batches

    List the VLAN Assignment Batches for a port
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ports/{id}/vlan-assignments/batches'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_port_vlan_assignment_by_port_id_and_assignment_id(client):
    """Test case for find_port_vlan_assignment_by_port_id_and_assignment_id

    Show a particular Port VLAN assignment's details
    """
    params = [('include', ["port","virtual_network"]),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ports/{id}/vlan-assignments/{assignment_id}'.format(id='id_example', assignment_id='assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_port_vlan_assignments(client):
    """Test case for find_port_vlan_assignments

    List Current VLAN assignments for a port
    """
    params = [('include', ["port","virtual_network"]),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ports/{id}/vlan-assignments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_unassign_port(client):
    """Test case for unassign_port

    Unassign a port
    """
    body = {"vnid":"1001"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ports/{id}/unassign'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

