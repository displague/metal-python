# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.ssh_key import SSHKey
from metal.types.ssh_key_create_input import SSHKeyCreateInput
from metal.types.ssh_key_input import SSHKeyInput
from metal.types.ssh_key_list import SSHKeyList


async def test_create_project_ssh_key(client):
    """Test case for create_project_ssh_key

    Create a ssh key for the given project
    """
    body = {"label":"label","instances_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/ssh-keys'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_ssh_key(client):
    """Test case for create_ssh_key

    Create a ssh key for the current user
    """
    body = {"label":"label","instances_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/ssh-keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_ssh_key(client):
    """Test case for delete_ssh_key

    Delete the ssh key
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/ssh-keys/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_device_ssh_keys(client):
    """Test case for find_device_ssh_keys

    Retrieve a device's ssh keys
    """
    params = [('Search string', 'search_string_example'),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/ssh-keys'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_ssh_keys(client):
    """Test case for find_project_ssh_keys

    Retrieve a project's ssh keys
    """
    params = [('query', 'query_example'),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/ssh-keys'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ssh_key_by_id(client):
    """Test case for find_ssh_key_by_id

    Retrieve a ssh key
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ssh-keys/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ssh_keys(client):
    """Test case for find_ssh_keys

    Retrieve all ssh keys
    """
    params = [('Search string', 'search_string_example'),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/ssh-keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_ssh_key(client):
    """Test case for update_ssh_key

    Update the ssh key
    """
    body = {"label":"label","key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/ssh-keys/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

