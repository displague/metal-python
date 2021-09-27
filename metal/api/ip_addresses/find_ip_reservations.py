from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.find_ip_reservations_types_item import FindIPReservationsTypesItem
from ...models.ip_reservation_list import IPReservationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    types: Union[Unset, None, List[FindIPReservationsTypesItem]] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    per_page: Union[Unset, None, int] = 250,

) -> Dict[str, Any]:
    url = "{}/projects/{id}/ips".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    json_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(types, Unset):
        if types is None:
            json_types = None
        else:
            json_types = []
            for types_item_data in types:
                types_item = types_item_data.value

                json_types.append(types_item)




    params["types"] = json_types


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


    params["per_page"] = per_page



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, IPReservationList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IPReservationList.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, IPReservationList]]:
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
    types: Union[Unset, None, List[FindIPReservationsTypesItem]] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    per_page: Union[Unset, None, int] = 250,

) -> Response[Union[Error, IPReservationList]]:
    """Retrieve all ip reservations

     Provides a paginated list of IP reservations for a single project.

    Args:
        id (str):
        types (Union[Unset, None, List[FindIPReservationsTypesItem]]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        per_page (Union[Unset, None, int]):  Default: 250.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPReservationList]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
types=types,
include=include,
exclude=exclude,
per_page=per_page,

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
    types: Union[Unset, None, List[FindIPReservationsTypesItem]] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    per_page: Union[Unset, None, int] = 250,

) -> Optional[Union[Error, IPReservationList]]:
    """Retrieve all ip reservations

     Provides a paginated list of IP reservations for a single project.

    Args:
        id (str):
        types (Union[Unset, None, List[FindIPReservationsTypesItem]]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        per_page (Union[Unset, None, int]):  Default: 250.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPReservationList]]
    """


    return sync_detailed(
        id=id,
client=client,
types=types,
include=include,
exclude=exclude,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    types: Union[Unset, None, List[FindIPReservationsTypesItem]] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    per_page: Union[Unset, None, int] = 250,

) -> Response[Union[Error, IPReservationList]]:
    """Retrieve all ip reservations

     Provides a paginated list of IP reservations for a single project.

    Args:
        id (str):
        types (Union[Unset, None, List[FindIPReservationsTypesItem]]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        per_page (Union[Unset, None, int]):  Default: 250.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPReservationList]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
types=types,
include=include,
exclude=exclude,
per_page=per_page,

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
    types: Union[Unset, None, List[FindIPReservationsTypesItem]] = UNSET,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    per_page: Union[Unset, None, int] = 250,

) -> Optional[Union[Error, IPReservationList]]:
    """Retrieve all ip reservations

     Provides a paginated list of IP reservations for a single project.

    Args:
        id (str):
        types (Union[Unset, None, List[FindIPReservationsTypesItem]]):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        per_page (Union[Unset, None, int]):  Default: 250.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPReservationList]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
types=types,
include=include,
exclude=exclude,
per_page=per_page,

    )).parsed

