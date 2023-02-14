# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.metro import Metro
from metal.types.metro_list import MetroList


async def test_find_metros(client):
    """Test case for find_metros

    Retrieve all metros
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/locations/metros',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_metro(client):
    """Test case for get_metro

    Retrieve a specific Metro's details
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/locations/metros/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

