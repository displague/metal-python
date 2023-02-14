# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.find_ip_address_by_id200_response import FindIPAddressById200Response
from metal.types.ip_assignment_update_input import IPAssignmentUpdateInput
from metal.types.ip_availabilities_list import IPAvailabilitiesList
from metal.types.ip_reservation_list import IPReservationList
from metal.types.request_ip_reservation201_response import RequestIPReservation201Response
from metal.types.request_ip_reservation_request import RequestIPReservationRequest


async def test_delete_ip_address(client):
    """Test case for delete_ip_address

    Unassign an ip address
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/ips/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_address_by_id(client):
    """Test case for find_ip_address_by_id

    Retrieve an ip address
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ips/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_address_customdata(client):
    """Test case for find_ip_address_customdata

    Retrieve the custom metadata of an IP Reservation or IP Assignment
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ips/{id}/customdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_availabilities(client):
    """Test case for find_ip_availabilities

    Retrieve all available subnets of a particular reservation
    """
    params = [('cidr', 'cidr_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ips/{id}/available'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_reservations(client):
    """Test case for find_ip_reservations

    Retrieve all ip reservations
    """
    params = [('types', ['types_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('per_page', 250)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/ips'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_request_ip_reservation(client):
    """Test case for request_ip_reservation

    Requesting IP reservations
    """
    body = metal.RequestIPReservationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/ips'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_ip_address(client):
    """Test case for update_ip_address

    Update an ip address
    """
    body = {"details":"details","customdata":"{}","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/metal/v1/ips/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

