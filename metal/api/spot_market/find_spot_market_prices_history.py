from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.spot_prices_history_report import SpotPricesHistoryReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    facility: str,
    plan: str,
    metro: Union[Unset, None, str] = UNSET,
    from_: str,
    until: str,

) -> Dict[str, Any]:
    url = "{}/market/spot/prices/history".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["facility"] = facility


    params["plan"] = plan


    params["metro"] = metro


    params["from"] = from_


    params["until"] = until



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, SpotPricesHistoryReport]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SpotPricesHistoryReport.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, SpotPricesHistoryReport]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    facility: str,
    plan: str,
    metro: Union[Unset, None, str] = UNSET,
    from_: str,
    until: str,

) -> Response[Union[Error, SpotPricesHistoryReport]]:
    """Get spot market prices for a given period of time

     Get spot market prices for a given plan and facility in a fixed period of time

    *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

    Args:
        facility (str):
        plan (str):
        metro (Union[Unset, None, str]):
        from_ (str):
        until (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotPricesHistoryReport]]
    """


    kwargs = _get_kwargs(
        client=client,
facility=facility,
plan=plan,
metro=metro,
from_=from_,
until=until,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Client,
    facility: str,
    plan: str,
    metro: Union[Unset, None, str] = UNSET,
    from_: str,
    until: str,

) -> Optional[Union[Error, SpotPricesHistoryReport]]:
    """Get spot market prices for a given period of time

     Get spot market prices for a given plan and facility in a fixed period of time

    *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

    Args:
        facility (str):
        plan (str):
        metro (Union[Unset, None, str]):
        from_ (str):
        until (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotPricesHistoryReport]]
    """


    return sync_detailed(
        client=client,
facility=facility,
plan=plan,
metro=metro,
from_=from_,
until=until,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    facility: str,
    plan: str,
    metro: Union[Unset, None, str] = UNSET,
    from_: str,
    until: str,

) -> Response[Union[Error, SpotPricesHistoryReport]]:
    """Get spot market prices for a given period of time

     Get spot market prices for a given plan and facility in a fixed period of time

    *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

    Args:
        facility (str):
        plan (str):
        metro (Union[Unset, None, str]):
        from_ (str):
        until (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotPricesHistoryReport]]
    """


    kwargs = _get_kwargs(
        client=client,
facility=facility,
plan=plan,
metro=metro,
from_=from_,
until=until,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Client,
    facility: str,
    plan: str,
    metro: Union[Unset, None, str] = UNSET,
    from_: str,
    until: str,

) -> Optional[Union[Error, SpotPricesHistoryReport]]:
    """Get spot market prices for a given period of time

     Get spot market prices for a given plan and facility in a fixed period of time

    *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

    Args:
        facility (str):
        plan (str):
        metro (Union[Unset, None, str]):
        from_ (str):
        until (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotPricesHistoryReport]]
    """


    return (await asyncio_detailed(
        client=client,
facility=facility,
plan=plan,
metro=metro,
from_=from_,
until=until,

    )).parsed

