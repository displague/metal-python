# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.operating_system_list import OperatingSystemList


async def test_find_operating_system_version(client):
    """Test case for find_operating_system_version

    Retrieve all operating system versions
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/operating-system-versions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_operating_systems(client):
    """Test case for find_operating_systems

    Retrieve all operating systems
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/operating-systems',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

