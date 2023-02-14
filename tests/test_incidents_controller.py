# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error


async def test_find_incidents(client):
    """Test case for find_incidents

    Retrieve the number of incidents
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

