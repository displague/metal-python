# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.new_password import NewPassword


async def test_create_password_reset_token(client):
    """Test case for create_password_reset_token

    Create a password reset token
    """
    params = [('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/reset-password',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_reset_password(client):
    """Test case for reset_password

    Reset current user password
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/reset-password',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

