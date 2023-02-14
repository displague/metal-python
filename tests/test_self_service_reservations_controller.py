# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from metal.types.error import Error
from metal.types.self_service_reservation_list import SelfServiceReservationList
from metal.types.self_service_reservation_response import SelfServiceReservationResponse


async def test_create_self_service_reservation(client):
    """Test case for create_self_service_reservation

    Create a reservation
    """
    body = {"item":[{"amount":0.8008282,"metro_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","quantity":6,"term":"term","plan_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"amount":0.8008282,"metro_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","quantity":6,"term":"term","plan_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"period":{"unit":"monthly","count":1.4658129805029452},"notes":"notes","start_date":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{project_id}/self-service/reservations'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_self_service_reservation(client):
    """Test case for find_self_service_reservation

    Retrieve a reservation
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{project_id}/self-service/reservations/{id}'.format(id='id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_self_service_reservations(client):
    """Test case for find_self_service_reservations

    Retrieve all reservations
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{project_id}/self-service/reservations'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

