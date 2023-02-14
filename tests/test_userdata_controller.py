# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error


async def test_validate_userdata(client):
    """Test case for validate_userdata

    Validate user data
    """
    params = [('userdata', 'userdata_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/userdata/validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

