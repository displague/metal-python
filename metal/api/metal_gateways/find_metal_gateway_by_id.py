from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.metal_gateway import MetalGateway
from ...models.vrf_metal_gateway import VrfMetalGateway
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/metal-gateways/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    if response.status_code == HTTPStatus.OK:
        def _parse_response_200(data: object) -> Union['MetalGateway', 'VrfMetalGateway']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasfind_metal_gateway_by_id_200_response_type_0 = MetalGateway.from_dict(data)



                return componentsschemasfind_metal_gateway_by_id_200_response_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasfind_metal_gateway_by_id_200_response_type_1 = VrfMetalGateway.from_dict(data)



            return componentsschemasfind_metal_gateway_by_id_200_response_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())



        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
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

) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Returns the metal gateway

     Returns a specific metal gateway

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,

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

) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Returns the metal gateway

     Returns a specific metal gateway

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,

) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Returns the metal gateway

     Returns a specific metal gateway

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,

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

) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Returns the metal gateway

     Returns a specific metal gateway

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed

