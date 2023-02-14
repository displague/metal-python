# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from metal.types.error import Error
from metal.types.hardware_reservation import HardwareReservation
from metal.types.hardware_reservation_list import HardwareReservationList
from metal.types.move_hardware_reservation_request import MoveHardwareReservationRequest


async def test_activate_hardware_reservation(client):
    """Test case for activate_hardware_reservation

    Activate a spare hardware reservation
    """
    body = metal.ActivateHardwareReservationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/hardware-reservations/{id}/activate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_hardware_reservation_by_id(client):
    """Test case for find_hardware_reservation_by_id

    Retrieve a hardware reservation
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/hardware-reservations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_hardware_reservations(client):
    """Test case for find_project_hardware_reservations

    Retrieve all hardware reservations for a given project
    """
    params = [('query', 'query_example'),
                    ('state', 'state_example'),
                    ('provisionable', 'provisionable_example'),
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
        path='/metal/v1/projects/{id}/hardware-reservations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_move_hardware_reservation(client):
    """Test case for move_hardware_reservation

    Move a hardware reservation
    """
    body = metal.MoveHardwareReservationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/hardware-reservations/{id}/move'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

