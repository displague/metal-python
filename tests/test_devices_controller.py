# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.bgp_session_input import BGPSessionInput
from metal.types.bgp_session import BgpSession
from metal.types.bgp_session_list import BgpSessionList
from metal.types.bgp_session_neighbors import BgpSessionNeighbors
from metal.types.create_device_request import CreateDeviceRequest
from metal.types.device import Device
from metal.types.device_action_input import DeviceActionInput
from metal.types.device_list import DeviceList
from metal.types.device_update_input import DeviceUpdateInput
from metal.types.error import Error
from metal.types.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from metal.types.ip_assignment import IPAssignment
from metal.types.ip_assignment_input import IPAssignmentInput
from metal.types.ip_assignment_list import IPAssignmentList
from metal.types.metadata import Metadata
from metal.types.userdata import Userdata


async def test_create_bgp_session(client):
    """Test case for create_bgp_session

    Create a BGP session
    """
    body = {"address_family":"ipv4","default_route":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/devices/{id}/bgp/sessions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_device(client):
    """Test case for create_device

    Create a device
    """
    body = metal.CreateDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/devices'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_create_ip_assignment(client):
    """Test case for create_ip_assignment

    Create an ip assignment
    """
    body = {"address":"address","customdata":"{}","manageable":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/devices/{id}/ips'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_device(client):
    """Test case for delete_device

    Delete the device
    """
    params = [('force_delete', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/devices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_bgp_sessions(client):
    """Test case for find_bgp_sessions

    Retrieve all BGP sessions
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/bgp/sessions'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_device_by_id(client):
    """Test case for find_device_by_id

    Retrieve a device
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_device_customdata(client):
    """Test case for find_device_customdata

    Retrieve the custom metadata of an instance
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/customdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_device_metadata_by_id(client):
    """Test case for find_device_metadata_by_id

    Retrieve metadata
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/metadata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_device_userdata_by_id(client):
    """Test case for find_device_userdata_by_id

    Retrieve userdata
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/userdata'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_instance_bandwidth(client):
    """Test case for find_instance_bandwidth

    Retrieve an instance bandwidth
    """
    params = [('from', '_from_example'),
                    ('until', 'until_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/bandwidth'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_assignment_customdata(client):
    """Test case for find_ip_assignment_customdata

    Retrieve the custom metadata of an IP Assignment
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{instance_id}/ips/{id}/customdata'.format(instance_id='instance_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_ip_assignments(client):
    """Test case for find_ip_assignments

    Retrieve all ip assignments
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/ips'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_organization_devices(client):
    """Test case for find_organization_devices

    Retrieve all devices of an organization
    """
    params = [('facility', 'facility_example'),
                    ('hostname', 'hostname_example'),
                    ('reserved', True),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
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
        path='/metal/v1/organizations/{id}/devices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_project_devices(client):
    """Test case for find_project_devices

    Retrieve all devices of a project
    """
    params = [('facility', 'facility_example'),
                    ('hostname', 'hostname_example'),
                    ('reserved', True),
                    ('tag', 'tag_example'),
                    ('type', 'type_example'),
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
        path='/metal/v1/projects/{id}/devices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_traffic(client):
    """Test case for find_traffic

    Retrieve device traffic
    """
    params = [('direction', 'direction_example'),
                    ('interval', 'interval_example'),
                    ('bucket', 'bucket_example'),
                    ('timeframe', {'key': metal.FindTrafficTimeframeParameter()})]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/traffic'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_get_bgp_neighbor_data(client):
    """Test case for get_bgp_neighbor_data

    Retrieve BGP neighbor data for this device
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/devices/{id}/bgp/neighbors'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_perform_action(client):
    """Test case for perform_action

    Perform an action
    """
    body = {"preserve_data":True,"force_delete":True,"operating_system":"ubuntu_22_04","ipxe_script_url":"ipxe_script_url","type":"power_on","deprovision_fast":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/devices/{id}/actions'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_device(client):
    """Test case for update_device

    Update the device
    """
    body = {"userdata":"userdata","hostname":"hostname","spot_instance":True,"network_frozen":True,"description":"description","always_pxe":True,"billing_cycle":"billing_cycle","customdata":{"key":""},"ipxe_script_url":"ipxe_script_url","locked":True,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/devices/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

