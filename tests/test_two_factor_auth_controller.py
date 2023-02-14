# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error


async def test_disable_tfa_app(client):
    """Test case for disable_tfa_app

    Disable two factor authentication
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/user/otp/app',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_disable_tfa_sms(client):
    """Test case for disable_tfa_sms

    Disable two factor authentication
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/user/otp/sms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_enable_tfa_app(client):
    """Test case for enable_tfa_app

    Enable two factor auth using app
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/user/otp/app',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_enable_tfa_sms(client):
    """Test case for enable_tfa_sms

    Enable two factor auth using sms
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/user/otp/sms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

