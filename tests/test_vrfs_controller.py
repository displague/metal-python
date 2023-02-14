# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.vrf import Vrf
from metal.types.vrf_create_input import VrfCreateInput
from metal.types.vrf_ip_reservation import VrfIpReservation
from metal.types.vrf_ip_reservation_list import VrfIpReservationList
from metal.types.vrf_list import VrfList
from metal.types.vrf_route import VrfRoute
from metal.types.vrf_route_create_input import VrfRouteCreateInput
from metal.types.vrf_route_list import VrfRouteList
from metal.types.vrf_update_input import VrfUpdateInput


async def test_create_vrf(client):
    """Test case for create_vrf

    Create a new VRF in the specified project
    """
    body = {"ip_ranges":["ip_ranges","ip_ranges"],"local_asn":0,"metro":"metro","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/vrfs'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_vrf_route(client):
    """Test case for create_vrf_route

    Create a VRF route
    """
    body = {"prefix":"0.0.0.0/0","next_hop":"192.168.1.254"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/vrfs/{id}/routes'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_vrf(client):
    """Test case for delete_vrf

    Delete the VRF
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/vrfs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_vrf_route_by_id(client):
    """Test case for delete_vrf_route_by_id

    Delete a VRF Route
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/routes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_vrf_by_id(client):
    """Test case for find_vrf_by_id

    Retrieve a VRF
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/vrfs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_vrf_ip_reservation(client):
    """Test case for find_vrf_ip_reservation

    Retrieve all VRF IP Reservations in the VRF
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/vrfs/{vrf_id}/ips/{id}'.format(vrf_id='vrf_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_vrf_ip_reservations(client):
    """Test case for find_vrf_ip_reservations

    Retrieve all VRF IP Reservations in the VRF
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/vrfs/{id}/ips'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_vrf_route_by_id(client):
    """Test case for find_vrf_route_by_id

    Retrieve a VRF Route
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/routes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_vrfs(client):
    """Test case for find_vrfs

    Retrieve all VRFs in the project
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('metro', 'metro_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/vrfs'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_vrf_routes(client):
    """Test case for get_vrf_routes

    Retrieve all routes in the VRF
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/vrfs/{id}/routes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_vrf(client):
    """Test case for update_vrf

    Update the VRF
    """
    body = {"ip_ranges":["ip_ranges","ip_ranges"],"local_asn":0,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/vrfs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_vrf_route_by_id(client):
    """Test case for update_vrf_route_by_id

    Update a VRF Route
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/routes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

