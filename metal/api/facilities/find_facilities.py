from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.facility_list import FacilityList
from ...models.find_facilities_exclude_item import FindFacilitiesExcludeItem
from ...models.find_facilities_include_item import FindFacilitiesIncludeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    include: Union[Unset, None, List[FindFacilitiesIncludeItem]] = UNSET,
    exclude: Union[Unset, None, List[FindFacilitiesExcludeItem]] = UNSET,

) -> Dict[str, Any]:
    url = "{}/facilities".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    json_include: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include, Unset):
        if include is None:
            json_include = None
        else:
            json_include = []
            for include_item_data in include:
                include_item = include_item_data.value

                json_include.append(include_item)




    params["include"] = json_include


    json_exclude: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude, Unset):
        if exclude is None:
            json_exclude = None
        else:
            json_exclude = []
            for exclude_item_data in exclude:
                exclude_item = exclude_item_data.value

                json_exclude.append(exclude_item)




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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, FacilityList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FacilityList.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, FacilityList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    include: Union[Unset, None, List[FindFacilitiesIncludeItem]] = UNSET,
    exclude: Union[Unset, None, List[FindFacilitiesExcludeItem]] = UNSET,

) -> Response[Union[Error, FacilityList]]:
    """Retrieve all facilities

     Provides a listing of available datacenters where you can provision Packet devices.

    Args:
        include (Union[Unset, None, List[FindFacilitiesIncludeItem]]):
        exclude (Union[Unset, None, List[FindFacilitiesExcludeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FacilityList]]
    """


    kwargs = _get_kwargs(
        client=client,
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
    include: Union[Unset, None, List[FindFacilitiesIncludeItem]] = UNSET,
    exclude: Union[Unset, None, List[FindFacilitiesExcludeItem]] = UNSET,

) -> Optional[Union[Error, FacilityList]]:
    """Retrieve all facilities

     Provides a listing of available datacenters where you can provision Packet devices.

    Args:
        include (Union[Unset, None, List[FindFacilitiesIncludeItem]]):
        exclude (Union[Unset, None, List[FindFacilitiesExcludeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FacilityList]]
    """


    return sync_detailed(
        client=client,
include=include,
exclude=exclude,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    include: Union[Unset, None, List[FindFacilitiesIncludeItem]] = UNSET,
    exclude: Union[Unset, None, List[FindFacilitiesExcludeItem]] = UNSET,

) -> Response[Union[Error, FacilityList]]:
    """Retrieve all facilities

     Provides a listing of available datacenters where you can provision Packet devices.

    Args:
        include (Union[Unset, None, List[FindFacilitiesIncludeItem]]):
        exclude (Union[Unset, None, List[FindFacilitiesExcludeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FacilityList]]
    """


    kwargs = _get_kwargs(
        client=client,
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
    include: Union[Unset, None, List[FindFacilitiesIncludeItem]] = UNSET,
    exclude: Union[Unset, None, List[FindFacilitiesExcludeItem]] = UNSET,

) -> Optional[Union[Error, FacilityList]]:
    """Retrieve all facilities

     Provides a listing of available datacenters where you can provision Packet devices.

    Args:
        include (Union[Unset, None, List[FindFacilitiesIncludeItem]]):
        exclude (Union[Unset, None, List[FindFacilitiesExcludeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FacilityList]]
    """


    return (await asyncio_detailed(
        client=client,
include=include,
exclude=exclude,

    )).parsed

