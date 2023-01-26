from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.interconnection_port import InterconnectionPort
from ...types import Response


def _get_kwargs(
    connection_id: str,
    id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/connections/{connection_id}/ports/{id}".format(
        client.base_url,connection_id=connection_id,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, InterconnectionPort]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InterconnectionPort.from_dict(response.json())



        return response_200
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, InterconnectionPort]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Union[Error, InterconnectionPort]]:
    """Get a interconnection port

     Get the details of an interconnection port.

    Args:
        connection_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InterconnectionPort]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
id=id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    connection_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Union[Error, InterconnectionPort]]:
    """Get a interconnection port

     Get the details of an interconnection port.

    Args:
        connection_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InterconnectionPort]]
    """


    return sync_detailed(
        connection_id=connection_id,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    connection_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Union[Error, InterconnectionPort]]:
    """Get a interconnection port

     Get the details of an interconnection port.

    Args:
        connection_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InterconnectionPort]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
id=id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    connection_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Union[Error, InterconnectionPort]]:
    """Get a interconnection port

     Get the details of an interconnection port.

    Args:
        connection_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InterconnectionPort]]
    """


    return (await asyncio_detailed(
        connection_id=connection_id,
id=id,
client=client,

    )).parsed

