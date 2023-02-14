# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation import Invitation
from metal.types.invitation_input import InvitationInput
from metal.types.invitation_list import InvitationList
from metal.types.membership_list import MembershipList
from metal.types.project import Project
from metal.types.project_create_from_root_input import ProjectCreateFromRootInput
from metal.types.project_list import ProjectList
from metal.types.project_update_input import ProjectUpdateInput
from metal.types.transfer_request import TransferRequest
from metal.types.transfer_request_input import TransferRequestInput


async def test_create_project(client):
    """Test case for create_project

    Create a project
    """
    body = {"payment_method_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","organization_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","customdata":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_project_invitation(client):
    """Test case for create_project_invitation

    Create an invitation for a project
    """
    body = {"projects_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"organization_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","roles":["admin","admin"],"message":"message","invitee":"invitee"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{project_id}/invitations'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_transfer_request(client):
    """Test case for create_transfer_request

    Create a transfer request
    """
    body = {"target_organization_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/transfers'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_project(client):
    """Test case for delete_project

    Delete the project
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/projects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_reservation_customdata(client):
    """Test case for find_ip_reservation_customdata

    Retrieve the custom metadata of an IP Reservation
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{project_id}/ips/{id}/customdata'.format(project_id='project_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_by_id(client):
    """Test case for find_project_by_id

    Retrieve a project
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_customdata(client):
    """Test case for find_project_customdata

    Retrieve the custom metadata of a project
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/customdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_invitations(client):
    """Test case for find_project_invitations

    Retrieve project invitations
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
        path='/metal/v1/projects/{project_id}/invitations'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_memberships(client):
    """Test case for find_project_memberships

    Retrieve project memberships
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
        path='/metal/v1/projects/{project_id}/memberships'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_projects(client):
    """Test case for find_projects

    Retrieve all projects
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
        path='/metal/v1/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_project(client):
    """Test case for update_project

    Update the project
    """
    body = {"payment_method_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","backend_transfer_enabled":True,"customdata":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/projects/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

