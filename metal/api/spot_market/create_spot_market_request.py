from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.spot_market_request import SpotMarketRequest
from ...models.spot_market_request_create_input import SpotMarketRequestCreateInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: SpotMarketRequestCreateInput,

) -> Dict[str, Any]:
    url = "{}/projects/{id}/spot-market-requests".format(
        client.base_url,id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, SpotMarketRequest]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SpotMarketRequest.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, SpotMarketRequest]]:
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
    json_body: SpotMarketRequestCreateInput,

) -> Response[Union[Error, SpotMarketRequest]]:
    """Create a spot market request

     Creates a new spot market request.

    Type-specific options (such as operating_system for baremetal devices) should be included in the
    main data structure alongside hostname and plan.

    The features attribute allows you to optionally specify what features your server should have. For
    example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\":
    \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).

    The request will fail if there are no available servers matching your criteria. Alternatively, if
    you do not require a certain feature, but would prefer to be assigned a server with that feature if
    there are any available, you may specify that feature with a preferred value (see the example
    request below).

    The request will not fail if we have no servers with that feature in our inventory.

    Args:
        id (str):
        json_body (SpotMarketRequestCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketRequest]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
json_body=json_body,

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
    json_body: SpotMarketRequestCreateInput,

) -> Optional[Union[Error, SpotMarketRequest]]:
    """Create a spot market request

     Creates a new spot market request.

    Type-specific options (such as operating_system for baremetal devices) should be included in the
    main data structure alongside hostname and plan.

    The features attribute allows you to optionally specify what features your server should have. For
    example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\":
    \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).

    The request will fail if there are no available servers matching your criteria. Alternatively, if
    you do not require a certain feature, but would prefer to be assigned a server with that feature if
    there are any available, you may specify that feature with a preferred value (see the example
    request below).

    The request will not fail if we have no servers with that feature in our inventory.

    Args:
        id (str):
        json_body (SpotMarketRequestCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketRequest]]
    """


    return sync_detailed(
        id=id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: SpotMarketRequestCreateInput,

) -> Response[Union[Error, SpotMarketRequest]]:
    """Create a spot market request

     Creates a new spot market request.

    Type-specific options (such as operating_system for baremetal devices) should be included in the
    main data structure alongside hostname and plan.

    The features attribute allows you to optionally specify what features your server should have. For
    example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\":
    \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).

    The request will fail if there are no available servers matching your criteria. Alternatively, if
    you do not require a certain feature, but would prefer to be assigned a server with that feature if
    there are any available, you may specify that feature with a preferred value (see the example
    request below).

    The request will not fail if we have no servers with that feature in our inventory.

    Args:
        id (str):
        json_body (SpotMarketRequestCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketRequest]]
    """


    kwargs = _get_kwargs(
        id=id,
client=client,
json_body=json_body,

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
    json_body: SpotMarketRequestCreateInput,

) -> Optional[Union[Error, SpotMarketRequest]]:
    """Create a spot market request

     Creates a new spot market request.

    Type-specific options (such as operating_system for baremetal devices) should be included in the
    main data structure alongside hostname and plan.

    The features attribute allows you to optionally specify what features your server should have. For
    example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\":
    \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).

    The request will fail if there are no available servers matching your criteria. Alternatively, if
    you do not require a certain feature, but would prefer to be assigned a server with that feature if
    there are any available, you may specify that feature with a preferred value (see the example
    request below).

    The request will not fail if we have no servers with that feature in our inventory.

    Args:
        id (str):
        json_body (SpotMarketRequestCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SpotMarketRequest]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

