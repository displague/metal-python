from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.port import Port
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    bulk_enable: Union[Unset, None, bool] = UNSET,

) -> Dict[str, Any]:
    url = "{}/ports/{id}/bond".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["bulk_enable"] = bulk_enable



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Port]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Port.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())



        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())



        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Port]]:
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
    bulk_enable: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Error, Port]]:
    """Enabling bonding

     Enabling bonding for one or all ports

    Args:
        id (str):
        bulk_enable (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Port]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
bulk_enable=bulk_enable,

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
    bulk_enable: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Error, Port]]:
    """Enabling bonding

     Enabling bonding for one or all ports

    Args:
        id (str):
        bulk_enable (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Port]]
    """


    return sync_detailed(
        id=id,
client=client,
bulk_enable=bulk_enable,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    bulk_enable: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Error, Port]]:
    """Enabling bonding

     Enabling bonding for one or all ports

    Args:
        id (str):
        bulk_enable (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Port]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
bulk_enable=bulk_enable,

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
    bulk_enable: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Error, Port]]:
    """Enabling bonding

     Enabling bonding for one or all ports

    Args:
        id (str):
        bulk_enable (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Port]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
bulk_enable=bulk_enable,

    )).parsed
