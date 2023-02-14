# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.spot_market_prices_list import SpotMarketPricesList
from metal.types.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from metal.types.spot_market_request import SpotMarketRequest
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput
from metal.types.spot_market_request_list import SpotMarketRequestList
from metal.types.spot_prices_history_report import SpotPricesHistoryReport


async def test_create_spot_market_request(client):
    """Test case for create_spot_market_request

    Create a spot market request
    """
    body = {"end_at":"2000-01-23T04:56:07.000+00:00","metro":"metro","instance_attributes":{"user_ssh_keys":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"private_ipv4_subnet_size":1,"description":"description","hostnames":["hostnames","hostnames"],"termination_time":"2000-01-23T04:56:07.000+00:00","project_ssh_keys":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"tags":["tags","tags"],"features":["features","features"],"userdata":"userdata","hostname":"hostname","no_ssh_keys":True,"public_ipv4_subnet_size":5,"operating_system":"operating_system","always_pxe":True,"billing_cycle":"billing_cycle","customdata":"{}","locked":True,"plan":"plan"},"devices_min":6,"devices_max":0,"max_bid_price":5.637377,"facilities":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_delete_spot_market_request(client):
    """Test case for delete_spot_market_request

    Delete the spot market request
    """
    params = [('force_termination', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/spot-market-requests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_metro_spot_market_prices(client):
    """Test case for find_metro_spot_market_prices

    Get current spot market prices for metros
    """
    params = [('metro', 'metro_example'),
                    ('plan', 'plan_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/market/spot/prices/metros',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_spot_market_prices(client):
    """Test case for find_spot_market_prices

    Get current spot market prices
    """
    params = [('facility', 'facility_example'),
                    ('plan', 'plan_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/market/spot/prices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_spot_market_prices_history(client):
    """Test case for find_spot_market_prices_history

    Get spot market prices for a given period of time
    """
    params = [('facility', 'facility_example'),
                    ('plan', 'plan_example'),
                    ('metro', 'metro_example'),
                    ('from', '_from_example'),
                    ('until', 'until_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/market/spot/prices/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_spot_market_request_by_id(client):
    """Test case for find_spot_market_request_by_id

    Retrieve a spot market request
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/spot-market-requests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_list_spot_market_requests(client):
    """Test case for list_spot_market_requests

    List spot market requests
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

