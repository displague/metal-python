# coding: utf-8

import pytest
import json
from aiohttp import web

from metal.types.error import Error
from metal.types.payment_method import PaymentMethod
from metal.types.payment_method_update_input import PaymentMethodUpdateInput


async def test_delete_payment_method(client):
    """Test case for delete_payment_method

    Delete the payment method
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/metal/v1/payment-methods/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_find_payment_method_by_id(client):
    """Test case for find_payment_method_by_id

    Retrieve a payment method
    """
    params = [('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metal/v1/payment-methods/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


async def test_update_payment_method(client):
    """Test case for update_payment_method

    Update the payment method
    """
    body = {"expiration_year":0,"default":True,"expiration_month":"expiration_month","name":"name","billing_address":"{}","cardholder_name":"cardholder_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/metal/v1/payment-methods/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

