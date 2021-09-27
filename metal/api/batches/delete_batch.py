from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    remove_associated_instances: Union[Unset, None, bool] = False,

) -> Dict[str, Any]:
    url = "{}/batches/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["remove_associated_instances"] = remove_associated_instances



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Error]]:
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
    remove_associated_instances: Union[Unset, None, bool] = False,

) -> Response[Union[Any, Error]]:
    """Delete the Batch

     Deletes the Batch.

    Args:
        id (str):
        remove_associated_instances (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
remove_associated_instances=remove_associated_instances,

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
    remove_associated_instances: Union[Unset, None, bool] = False,

) -> Optional[Union[Any, Error]]:
    """Delete the Batch

     Deletes the Batch.

    Args:
        id (str):
        remove_associated_instances (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return sync_detailed(
        id=id,
client=client,
remove_associated_instances=remove_associated_instances,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    remove_associated_instances: Union[Unset, None, bool] = False,

) -> Response[Union[Any, Error]]:
    """Delete the Batch

     Deletes the Batch.

    Args:
        id (str):
        remove_associated_instances (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
remove_associated_instances=remove_associated_instances,

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
    remove_associated_instances: Union[Unset, None, bool] = False,

) -> Optional[Union[Any, Error]]:
    """Delete the Batch

     Deletes the Batch.

    Args:
        id (str):
        remove_associated_instances (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
remove_associated_instances=remove_associated_instances,

    )).parsed

