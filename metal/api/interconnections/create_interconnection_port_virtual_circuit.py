from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.virtual_circuit import VirtualCircuit
from ...models.virtual_circuit_create_input import VirtualCircuitCreateInput
from ...models.vrf_virtual_circuit import VrfVirtualCircuit
from ...models.vrf_virtual_circuit_create_input import VrfVirtualCircuitCreateInput
from ...types import Response


def _get_kwargs(
    connection_id: str,
    port_id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput'],

) -> Dict[str, Any]:
    url = "{}/connections/{connection_id}/ports/{port_id}/virtual-circuits".format(
        client.base_url,connection_id=connection_id,port_id=port_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body: Dict[str, Any]

    if isinstance(json_body, VirtualCircuitCreateInput):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()





    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    if response.status_code == HTTPStatus.CREATED:
        def _parse_response_201(data: object) -> Union['VirtualCircuit', 'VrfVirtualCircuit']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascreate_interconnection_port_virtual_circuit_201_response_type_0 = VirtualCircuit.from_dict(data)



                return componentsschemascreate_interconnection_port_virtual_circuit_201_response_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemascreate_interconnection_port_virtual_circuit_201_response_type_1 = VrfVirtualCircuit.from_dict(data)



            return componentsschemascreate_interconnection_port_virtual_circuit_201_response_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())



        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())



        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    port_id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput'],

) -> Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Create a new Virtual Circuit

     Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a
    Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF
    ID and subnet, along with the NNI VLAN value.

    Args:
        connection_id (str):
        port_id (str):
        json_body (Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
port_id=port_id,
client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    connection_id: str,
    port_id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput'],

) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Create a new Virtual Circuit

     Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a
    Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF
    ID and subnet, along with the NNI VLAN value.

    Args:
        connection_id (str):
        port_id (str):
        json_body (Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    return sync_detailed(
        connection_id=connection_id,
port_id=port_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    connection_id: str,
    port_id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput'],

) -> Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Create a new Virtual Circuit

     Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a
    Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF
    ID and subnet, along with the NNI VLAN value.

    Args:
        connection_id (str):
        port_id (str):
        json_body (Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
port_id=port_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    connection_id: str,
    port_id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput'],

) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Create a new Virtual Circuit

     Create a new Virtual Circuit on a Dedicated Port. To create a regular Virtual Circuit, specify a
    Virtual Network record and an NNI VLAN value. To create a VRF-based Virtual Circuit, specify the VRF
    ID and subnet, along with the NNI VLAN value.

    Args:
        connection_id (str):
        port_id (str):
        json_body (Union['VirtualCircuitCreateInput', 'VrfVirtualCircuitCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    return (await asyncio_detailed(
        connection_id=connection_id,
port_id=port_id,
client=client,
json_body=json_body,

    )).parsed

