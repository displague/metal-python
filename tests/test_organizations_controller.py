# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.invitation import Invitation
from metal.types.invitation_input import InvitationInput
from metal.types.invitation_list import InvitationList
from metal.types.operating_system_list import OperatingSystemList
from metal.types.organization import Organization
from metal.types.organization_input import OrganizationInput
from metal.types.organization_list import OrganizationList
from metal.types.payment_method import PaymentMethod
from metal.types.payment_method_create_input import PaymentMethodCreateInput
from metal.types.payment_method_list import PaymentMethodList
from metal.types.plan_list import PlanList
from metal.types.project import Project
from metal.types.project_create_input import ProjectCreateInput
from metal.types.project_list import ProjectList
from metal.types.transfer_request_list import TransferRequestList


async def test_create_organization(client):
    """Test case for create_organization

    Create an organization
    """
    body = {"twitter":"twitter","website":"website","address":{"country":"country","address":"address","address2":"address2","city":"city","coordinates":{"latitude":"latitude","longitude":"longitude"},"state":"state","zip_code":"zip_code"},"name":"name","description":"description","logo":"","billing_address":{"country":"country","address":"address","address2":"address2","city":"city","coordinates":{"latitude":"latitude","longitude":"longitude"},"state":"state","zip_code":"zip_code"},"customdata":"{}","enforce_2fa_at":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/organizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_organization_invitation(client):
    """Test case for create_organization_invitation

    Create an invitation for an organization
    """
    body = {"projects_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"organization_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","roles":["admin","admin"],"message":"message","invitee":"invitee"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/organizations/{id}/invitations'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_organization_project(client):
    """Test case for create_organization_project

    Create a project for the organization
    """
    body = {"payment_method_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","customdata":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/organizations/{id}/projects'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_payment_method(client):
    """Test case for create_payment_method

    Create a payment method for the given organization
    """
    body = {"default":True,"name":"name","nonce":"nonce"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_organization(client):
    """Test case for delete_organization

    Delete the organization
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_operating_systems_by_organization(client):
    """Test case for find_operating_systems_by_organization

    Retrieve all operating systems visible by the organization
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/operating-systems'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_by_id(client):
    """Test case for find_organization_by_id

    Retrieve an organization's details
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_customdata(client):
    """Test case for find_organization_customdata

    Retrieve the custom metadata of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/customdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_invitations(client):
    """Test case for find_organization_invitations

    Retrieve organization invitations
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
        path='/metal/v1/organizations/{id}/invitations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_payment_methods(client):
    """Test case for find_organization_payment_methods

    Retrieve all payment methods of an organization
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
        path='/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_projects(client):
    """Test case for find_organization_projects

    Retrieve all projects of an organization
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
        path='/metal/v1/organizations/{id}/projects'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_transfers(client):
    """Test case for find_organization_transfers

    Retrieve all project transfer requests from or to an organization
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/transfers'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organizations(client):
    """Test case for find_organizations

    Retrieve all organizations
    """
    params = [('personal', 'personal_example'),
                    ('without_projects', 'without_projects_example'),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example']),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_plans_by_organization(client):
    """Test case for find_plans_by_organization

    Retrieve all plans visible by the organization
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/organizations/{id}/plans'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_organization(client):
    """Test case for update_organization

    Update the organization
    """
    body = {"twitter":"twitter","website":"website","address":{"country":"country","address":"address","address2":"address2","city":"city","coordinates":{"latitude":"latitude","longitude":"longitude"},"state":"state","zip_code":"zip_code"},"name":"name","description":"description","logo":"","billing_address":{"country":"country","address":"address","address2":"address2","city":"city","coordinates":{"latitude":"latitude","longitude":"longitude"},"state":"state","zip_code":"zip_code"},"customdata":"{}","enforce_2fa_at":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

