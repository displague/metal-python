from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from ...models.capacity_input import CapacityInput
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CapacityInput,

) -> Dict[str, Any]:
    url = "{}/capacity".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[CapacityCheckPerFacilityList, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CapacityCheckPerFacilityList.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = Error.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[CapacityCheckPerFacilityList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CapacityInput,

) -> Response[Union[CapacityCheckPerFacilityList, Error]]:
    """Check capacity

     Validates if a deploy can be fulfilled.

    Args:
        json_body (CapacityInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityCheckPerFacilityList, Error]]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    json_body: CapacityInput,

) -> Optional[Union[CapacityCheckPerFacilityList, Error]]:
    """Check capacity

     Validates if a deploy can be fulfilled.

    Args:
        json_body (CapacityInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityCheckPerFacilityList, Error]]
    """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: CapacityInput,

) -> Response[Union[CapacityCheckPerFacilityList, Error]]:
    """Check capacity

     Validates if a deploy can be fulfilled.

    Args:
        json_body (CapacityInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityCheckPerFacilityList, Error]]
    """


    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    json_body: CapacityInput,

) -> Optional[Union[CapacityCheckPerFacilityList, Error]]:
    """Check capacity

     Validates if a deploy can be fulfilled.

    Args:
        json_body (CapacityInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityCheckPerFacilityList, Error]]
    """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed

