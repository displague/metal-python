# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.device_usage_list import DeviceUsageList
from metal.types.error import Error
from metal.types.project_usage_list import ProjectUsageList


async def test_find_device_usages(client):
    """Test case for find_device_usages

    Retrieve all usages for device
    """
    params = [('created[after]', 'created_after_example'),
                    ('created[before]', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/usages'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_usage(client):
    """Test case for find_project_usage

    Retrieve all usages for project
    """
    params = [('created[after]', 'created_after_example'),
                    ('created[before]', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/usages'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

