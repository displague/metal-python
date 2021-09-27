from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.interconnection import Interconnection
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/connections/{connection_id}".format(
        client.base_url,connection_id=connection_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Interconnection]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = Interconnection.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Interconnection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Client,

) -> Response[Union[Error, Interconnection]]:
    """Delete interconnection

     Delete a interconnection, its associated ports and virtual circuits.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Interconnection]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    connection_id: str,
    *,
    client: Client,

) -> Optional[Union[Error, Interconnection]]:
    """Delete interconnection

     Delete a interconnection, its associated ports and virtual circuits.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Interconnection]]
    """


    return sync_detailed(
        connection_id=connection_id,
client=client,

    ).parsed

async def asyncio_detailed(
    connection_id: str,
    *,
    client: Client,

) -> Response[Union[Error, Interconnection]]:
    """Delete interconnection

     Delete a interconnection, its associated ports and virtual circuits.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Interconnection]]
    """


    kwargs = _get_kwargs(
        connection_id=connection_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    connection_id: str,
    *,
    client: Client,

) -> Optional[Union[Error, Interconnection]]:
    """Delete interconnection

     Delete a interconnection, its associated ports and virtual circuits.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Interconnection]]
    """


    return (await asyncio_detailed(
        connection_id=connection_id,
client=client,

    )).parsed

