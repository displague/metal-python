from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.ssh_key_list import SSHKeyList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    search_string: Union[Unset, None, str] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,

) -> Dict[str, Any]:
    url = "{}/ssh-keys".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["Search string"] = search_string


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



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, SSHKeyList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SSHKeyList.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, SSHKeyList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    search_string: Union[Unset, None, str] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,

) -> Response[Union[Error, SSHKeyList]]:
    """Retrieve all ssh keys

     Returns a collection of the user’s ssh keys.

    Args:
        search_string (Union[Unset, None, str]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SSHKeyList]]
    """


    kwargs = _get_kwargs(
        client=client,
search_string=search_string,
include=include,
exclude=exclude,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    search_string: Union[Unset, None, str] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,

) -> Optional[Union[Error, SSHKeyList]]:
    """Retrieve all ssh keys

     Returns a collection of the user’s ssh keys.

    Args:
        search_string (Union[Unset, None, str]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SSHKeyList]]
    """


    return sync_detailed(
        client=client,
search_string=search_string,
include=include,
exclude=exclude,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    search_string: Union[Unset, None, str] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,

) -> Response[Union[Error, SSHKeyList]]:
    """Retrieve all ssh keys

     Returns a collection of the user’s ssh keys.

    Args:
        search_string (Union[Unset, None, str]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SSHKeyList]]
    """


    kwargs = _get_kwargs(
        client=client,
search_string=search_string,
include=include,
exclude=exclude,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    search_string: Union[Unset, None, str] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,

) -> Optional[Union[Error, SSHKeyList]]:
    """Retrieve all ssh keys

     Returns a collection of the user’s ssh keys.

    Args:
        search_string (Union[Unset, None, str]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SSHKeyList]]
    """


    return (await asyncio_detailed(
        client=client,
search_string=search_string,
include=include,
exclude=exclude,

    )).parsed

