# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.support_request_input import SupportRequestInput


async def test_request_suppert(client):
    """Test case for request_suppert

    Create a support ticket
    """
    body = {"device_id":"device_id","project_id":"project_id","subject":"subject","message":"message","priority":"urgent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/support-requests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

