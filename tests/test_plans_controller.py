# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.plan_list import PlanList


async def test_find_plans(client):
    """Test case for find_plans

    Retrieve all plans
    """
    params = [('type', 'standard'),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_plans_by_project(client):
    """Test case for find_plans_by_project

    Retrieve all plans visible by the project
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/plans'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')
