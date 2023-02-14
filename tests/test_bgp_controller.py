# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.bgp_config import BgpConfig
from metal.types.bgp_config_request_input import BgpConfigRequestInput
from metal.types.bgp_session import BgpSession
from metal.types.bgp_session_list import BgpSessionList
from metal.types.error import Error
from metal.types.global_bgp_range_list import GlobalBgpRangeList


async def test_delete_bgp_session(client):
    """Test case for delete_bgp_session

    Delete the BGP session
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_bgp_config_by_project(client):
    """Test case for find_bgp_config_by_project

    Retrieve a bgp config
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/bgp-config'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_bgp_session_by_id(client):
    """Test case for find_bgp_session_by_id

    Retrieve a BGP session
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_global_bgp_ranges(client):
    """Test case for find_global_bgp_ranges

    Retrieve all global bgp ranges
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/global-bgp-ranges'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_bgp_sessions(client):
    """Test case for find_project_bgp_sessions

    Retrieve all BGP sessions for project
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/bgp/sessions'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_request_bgp_config(client):
    """Test case for request_bgp_config

    Requesting bgp config
    """
    body = {"use_case":"use_case","deployment_type":"deployment_type","asn":0,"md5":"md5"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/bgp-configs'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_bgp_session(client):
    """Test case for update_bgp_session

    Update the BGP session
    """
    body = True
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

