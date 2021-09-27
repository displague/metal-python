from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.virtual_network_list import VirtualNetworkList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    facility: Union[Unset, None, str] = UNSET,
    metro: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/projects/{id}/virtual-networks".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    json_include: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include, Unset):
        if include is None:
            json_include = None
        else:
            json_include = include




    params["include"] = json_include


    json_exclude: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude, Unset):
        if exclude is None:
            json_exclude = None
        else:
            json_exclude = exclude




    params["exclude"] = json_exclude


    params["facility"] = facility


    params["metro"] = metro



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, VirtualNetworkList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VirtualNetworkList.from_dict(response.json())



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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, VirtualNetworkList]]:
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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    facility: Union[Unset, None, str] = UNSET,
    metro: Union[Unset, None, str] = UNSET,

) -> Response[Union[Error, VirtualNetworkList]]:
    """Retrieve all virtual networks

     Provides a list of virtual networks for a single project.

    Args:
        id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        facility (Union[Unset, None, str]):
        metro (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, VirtualNetworkList]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
include=include,
exclude=exclude,
facility=facility,
metro=metro,

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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    facility: Union[Unset, None, str] = UNSET,
    metro: Union[Unset, None, str] = UNSET,

) -> Optional[Union[Error, VirtualNetworkList]]:
    """Retrieve all virtual networks

     Provides a list of virtual networks for a single project.

    Args:
        id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        facility (Union[Unset, None, str]):
        metro (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, VirtualNetworkList]]
    """


    return sync_detailed(
        id=id,
client=client,
include=include,
exclude=exclude,
facility=facility,
metro=metro,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    facility: Union[Unset, None, str] = UNSET,
    metro: Union[Unset, None, str] = UNSET,

) -> Response[Union[Error, VirtualNetworkList]]:
    """Retrieve all virtual networks

     Provides a list of virtual networks for a single project.

    Args:
        id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        facility (Union[Unset, None, str]):
        metro (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, VirtualNetworkList]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
include=include,
exclude=exclude,
facility=facility,
metro=metro,

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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    facility: Union[Unset, None, str] = UNSET,
    metro: Union[Unset, None, str] = UNSET,

) -> Optional[Union[Error, VirtualNetworkList]]:
    """Retrieve all virtual networks

     Provides a list of virtual networks for a single project.

    Args:
        id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        facility (Union[Unset, None, str]):
        metro (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, VirtualNetworkList]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
include=include,
exclude=exclude,
facility=facility,
metro=metro,

    )).parsed

