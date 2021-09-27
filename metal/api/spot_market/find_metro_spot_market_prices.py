from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    metro: Union[Unset, None, str] = UNSET,
    plan: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/market/spot/prices/metros".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["metro"] = metro


    params["plan"] = plan



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, SpotMarketPricesPerMetroList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SpotMarketPricesPerMetroList.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, SpotMarketPricesPerMetroList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    metro: Union[Unset, None, str] = UNSET,
    plan: Union[Unset, None, str] = UNSET,

) -> Response[Union[Error, SpotMarketPricesPerMetroList]]:
    """Get current spot market prices for metros

     Get Equinix Metal current spot market prices for all metros.

    Args:
        metro (Union[Unset, None, str]):
        plan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketPricesPerMetroList]]
    """


    kwargs = _get_kwargs(
        client=client,
metro=metro,
plan=plan,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    metro: Union[Unset, None, str] = UNSET,
    plan: Union[Unset, None, str] = UNSET,

) -> Optional[Union[Error, SpotMarketPricesPerMetroList]]:
    """Get current spot market prices for metros

     Get Equinix Metal current spot market prices for all metros.

    Args:
        metro (Union[Unset, None, str]):
        plan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketPricesPerMetroList]]
    """


    return sync_detailed(
        client=client,
metro=metro,
plan=plan,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    metro: Union[Unset, None, str] = UNSET,
    plan: Union[Unset, None, str] = UNSET,

) -> Response[Union[Error, SpotMarketPricesPerMetroList]]:
    """Get current spot market prices for metros

     Get Equinix Metal current spot market prices for all metros.

    Args:
        metro (Union[Unset, None, str]):
        plan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketPricesPerMetroList]]
    """


    kwargs = _get_kwargs(
        client=client,
metro=metro,
plan=plan,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    metro: Union[Unset, None, str] = UNSET,
    plan: Union[Unset, None, str] = UNSET,

) -> Optional[Union[Error, SpotMarketPricesPerMetroList]]:
    """Get current spot market prices for metros

     Get Equinix Metal current spot market prices for all metros.

    Args:
        metro (Union[Unset, None, str]):
        plan (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketPricesPerMetroList]]
    """


    return (await asyncio_detailed(
        client=client,
metro=metro,
plan=plan,

    )).parsed

