# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation_list import InvitationList
from metal.types.user import User
from metal.types.user_create_input import UserCreateInput
from metal.types.user_list import UserList
from metal.types.user_update_input import UserUpdateInput


async def test_create_user(client):
    """Test case for create_user

    Create a user
    """
    body = {"invitation_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","level":"level","timezone":"timezone","last_name":"last_name","avatar":"","title":"title","nonce":"nonce","emails":[{"default":True,"address":"address"},{"default":True,"address":"address"}],"social_accounts":"{}","password":"password","verified_at":"2000-01-23T04:56:07.000+00:00","company_name":"company_name","company_url":"company_url","phone_number":"phone_number","customdata":"{}","locked":True,"first_name":"first_name","two_factor_auth":"two_factor_auth"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_current_user(client):
    """Test case for find_current_user

    Retrieve the current user
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_invitations(client):
    """Test case for find_invitations

    Retrieve current user invitations
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/invitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_user_by_id(client):
    """Test case for find_user_by_id

    Retrieve a user
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/users/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_user_customdata(client):
    """Test case for find_user_customdata

    Retrieve the custom metadata of a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/users/{id}/customdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_users(client):
    """Test case for find_users

    Retrieve all users
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_current_user(client):
    """Test case for update_current_user

    Update the current user
    """
    body = {"password":"password","timezone":"timezone","last_name":"last_name","phone_number":"phone_number","customdata":"{}","first_name":"first_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

