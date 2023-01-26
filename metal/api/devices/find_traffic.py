from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.find_traffic_bucket import FindTrafficBucket
from ...models.find_traffic_direction import FindTrafficDirection
from ...models.find_traffic_interval import FindTrafficInterval
from ...models.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    direction: FindTrafficDirection,
    interval: Union[Unset, None, FindTrafficInterval] = UNSET,
    bucket: Union[Unset, None, FindTrafficBucket] = UNSET,
    timeframe: Union[Unset, None, 'FindTrafficTimeframeParameter'] = UNSET,

) -> Dict[str, Any]:
    url = "{}/devices/{id}/traffic".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    json_direction = direction.value

    params["direction"] = json_direction


    json_interval: Union[Unset, None, str] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval


    json_bucket: Union[Unset, None, str] = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value if bucket else None

    params["bucket"] = json_bucket


    json_timeframe: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(timeframe, Unset):
        json_timeframe = timeframe.to_dict() if timeframe else None

    if not isinstance(json_timeframe, Unset) and json_timeframe is not None:
        params.update(json_timeframe)




    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
    direction: FindTrafficDirection,
    interval: Union[Unset, None, FindTrafficInterval] = UNSET,
    bucket: Union[Unset, None, FindTrafficBucket] = UNSET,
    timeframe: Union[Unset, None, 'FindTrafficTimeframeParameter'] = UNSET,

) -> Response[Union[Any, Error]]:
    """Retrieve device traffic

     Returns traffic for a specific device.

    Args:
        id (str):
        direction (FindTrafficDirection):
        interval (Union[Unset, None, FindTrafficInterval]):
        bucket (Union[Unset, None, FindTrafficBucket]):
        timeframe (Union[Unset, None, FindTrafficTimeframeParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
direction=direction,
interval=interval,
bucket=bucket,
timeframe=timeframe,

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
    direction: FindTrafficDirection,
    interval: Union[Unset, None, FindTrafficInterval] = UNSET,
    bucket: Union[Unset, None, FindTrafficBucket] = UNSET,
    timeframe: Union[Unset, None, 'FindTrafficTimeframeParameter'] = UNSET,

) -> Optional[Union[Any, Error]]:
    """Retrieve device traffic

     Returns traffic for a specific device.

    Args:
        id (str):
        direction (FindTrafficDirection):
        interval (Union[Unset, None, FindTrafficInterval]):
        bucket (Union[Unset, None, FindTrafficBucket]):
        timeframe (Union[Unset, None, FindTrafficTimeframeParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return sync_detailed(
        id=id,
client=client,
direction=direction,
interval=interval,
bucket=bucket,
timeframe=timeframe,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    direction: FindTrafficDirection,
    interval: Union[Unset, None, FindTrafficInterval] = UNSET,
    bucket: Union[Unset, None, FindTrafficBucket] = UNSET,
    timeframe: Union[Unset, None, 'FindTrafficTimeframeParameter'] = UNSET,

) -> Response[Union[Any, Error]]:
    """Retrieve device traffic

     Returns traffic for a specific device.

    Args:
        id (str):
        direction (FindTrafficDirection):
        interval (Union[Unset, None, FindTrafficInterval]):
        bucket (Union[Unset, None, FindTrafficBucket]):
        timeframe (Union[Unset, None, FindTrafficTimeframeParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
direction=direction,
interval=interval,
bucket=bucket,
timeframe=timeframe,

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
    direction: FindTrafficDirection,
    interval: Union[Unset, None, FindTrafficInterval] = UNSET,
    bucket: Union[Unset, None, FindTrafficBucket] = UNSET,
    timeframe: Union[Unset, None, 'FindTrafficTimeframeParameter'] = UNSET,

) -> Optional[Union[Any, Error]]:
    """Retrieve device traffic

     Returns traffic for a specific device.

    Args:
        id (str):
        direction (FindTrafficDirection):
        interval (Union[Unset, None, FindTrafficInterval]):
        bucket (Union[Unset, None, FindTrafficBucket]):
        timeframe (Union[Unset, None, FindTrafficTimeframeParameter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
direction=direction,
interval=interval,
bucket=bucket,
timeframe=timeframe,

    )).parsed

