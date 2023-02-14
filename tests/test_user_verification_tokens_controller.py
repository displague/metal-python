# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.verify_email import VerifyEmail


async def test_consume_verification_request(client):
    """Test case for consume_verification_request

    Verify a user using an email verification token
    """
    body = {"user_token":"user_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/verify-email',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_validation_request(client):
    """Test case for create_validation_request

    Create an email verification request
    """
    params = [('login', 'login_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/verify-email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

