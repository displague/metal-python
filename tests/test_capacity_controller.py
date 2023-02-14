# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from metal.types.capacity_check_per_metro_list import CapacityCheckPerMetroList
from metal.types.capacity_input import CapacityInput
from metal.types.capacity_list import CapacityList
from metal.types.capacity_per_metro_input import CapacityPerMetroInput
from metal.types.error import Error
from metal.types.metro_capacity_list import MetroCapacityList


async def test_check_capacity_for_facility(client):
    """Test case for check_capacity_for_facility

    Check capacity
    """
    body = {"servers":[{"quantity":"quantity","facility":"facility","plan":"plan"},{"quantity":"quantity","facility":"facility","plan":"plan"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/capacity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_check_capacity_for_metro(client):
    """Test case for check_capacity_for_metro

    Check capacity for a metro
    """
    body = {"servers":[{"quantity":"quantity","metro":"metro","plan":"plan"},{"quantity":"quantity","metro":"metro","plan":"plan"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/capacity/metros',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_capacity_for_facility(client):
    """Test case for find_capacity_for_facility

    View capacity
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/capacity',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_capacity_for_metro(client):
    """Test case for find_capacity_for_metro

    View capacity for metros
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/capacity/metros',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_capacity_per_facility(client):
    """Test case for find_organization_capacity_per_facility

    View available hardware plans per Facility for given organization
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/capacity'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_capacity_per_metro(client):
    """Test case for find_organization_capacity_per_metro

    View available hardware plans per Metro for given organization
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/capacity/metros'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

