# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.create_metal_gateway_request import CreateMetalGatewayRequest
from metal.types.error import Error
from metal.types.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
from metal.types.metal_gateway_list import MetalGatewayList


async def test_create_metal_gateway(client):
    """Test case for create_metal_gateway

    Create a metal gateway
    """
    body = metal.CreateMetalGatewayRequest()
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{project_id}/metal-gateways'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_metal_gateway(client):
    """Test case for delete_metal_gateway

    Deletes the metal gateway
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/metal-gateways/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_metal_gateway_by_id(client):
    """Test case for find_metal_gateway_by_id

    Returns the metal gateway
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/metal-gateways/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_metal_gateways_by_project(client):
    """Test case for find_metal_gateways_by_project

    Returns all metal gateways for a project
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{project_id}/metal-gateways'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

