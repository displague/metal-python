# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.virtual_network import VirtualNetwork
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput
from metal.types.virtual_network_list import VirtualNetworkList


async def test_create_virtual_network(client):
    """Test case for create_virtual_network

    Create a virtual network
    """
    body = {"vxlan":1099,"metro":"metro","description":"description","facility":"facility"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/virtual-networks'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_virtual_network(client):
    """Test case for delete_virtual_network

    Delete a virtual network
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/virtual-networks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_virtual_networks(client):
    """Test case for find_virtual_networks

    Retrieve all virtual networks
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('facility', 'facility_example'),
                    ('metro', 'metro_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/virtual-networks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_virtual_network(client):
    """Test case for get_virtual_network

    Get a virtual network
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/virtual-networks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

