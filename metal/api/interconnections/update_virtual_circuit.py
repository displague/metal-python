from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.virtual_circuit import VirtualCircuit
from ...models.virtual_circuit_update_input import VirtualCircuitUpdateInput
from ...models.vrf_virtual_circuit import VrfVirtualCircuit
from ...models.vrf_virtual_circuit_update_input import VrfVirtualCircuitUpdateInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput'],

) -> Dict[str, Any]:
    url = "{}/virtual-circuits/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body: Dict[str, Any]

    if isinstance(json_body, VirtualCircuitUpdateInput):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()





    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    if response.status_code == HTTPStatus.OK:
        def _parse_response_200(data: object) -> Union['VirtualCircuit', 'VrfVirtualCircuit']:
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

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        def _parse_response_202(data: object) -> Union['VirtualCircuit', 'VrfVirtualCircuit']:
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

        response_202 = _parse_response_202(response.json())

        return response_202
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
    id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput'],

) -> Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Update a virtual circuit

     Update the details of a virtual circuit.

    Args:
        id (str):
        json_body (Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput'],

) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Update a virtual circuit

     Update the details of a virtual circuit.

    Args:
        id (str):
        json_body (Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    return sync_detailed(
        id=id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput'],

) -> Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Update a virtual circuit

     Update the details of a virtual circuit.

    Args:
        id (str):
        json_body (Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput'],

) -> Optional[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]:
    """Update a virtual circuit

     Update the details of a virtual circuit.

    Args:
        id (str):
        json_body (Union['VirtualCircuitUpdateInput', 'VrfVirtualCircuitUpdateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['VirtualCircuit', 'VrfVirtualCircuit']]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

