# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.recovery_code_list import RecoveryCodeList


async def test_find_ensure_otp(client):
    """Test case for find_ensure_otp

    Verify user by providing an OTP
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/user/otp/verify/{otp}'.format(otp='otp_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_recovery_codes(client):
    """Test case for find_recovery_codes

    Retrieve my recovery codes
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/user/otp/recovery-codes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_receive_codes(client):
    """Test case for receive_codes

    Receive an OTP per sms
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/user/otp/sms/receive',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_regenerate_codes(client):
    """Test case for regenerate_codes

    Generate new recovery codes
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/user/otp/recovery-codes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

