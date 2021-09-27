from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    otp: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/user/otp/verify/{otp}".format(
        client.base_url,otp=otp)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
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
    otp: str,
    *,
    client: Client,

) -> Response[Union[Any, Error]]:
    """Verify user by providing an OTP

     It verifies the user once a valid OTP is provided. It gives back a session token, essentially
    logging in the user.

    Args:
        otp (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        otp=otp,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    otp: str,
    *,
    client: Client,

) -> Optional[Union[Any, Error]]:
    """Verify user by providing an OTP

     It verifies the user once a valid OTP is provided. It gives back a session token, essentially
    logging in the user.

    Args:
        otp (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return sync_detailed(
        otp=otp,
client=client,

    ).parsed

async def asyncio_detailed(
    otp: str,
    *,
    client: Client,

) -> Response[Union[Any, Error]]:
    """Verify user by providing an OTP

     It verifies the user once a valid OTP is provided. It gives back a session token, essentially
    logging in the user.

    Args:
        otp (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    kwargs = _get_kwargs(
        otp=otp,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    otp: str,
    *,
    client: Client,

) -> Optional[Union[Any, Error]]:
    """Verify user by providing an OTP

     It verifies the user once a valid OTP is provided. It gives back a session token, essentially
    logging in the user.

    Args:
        otp (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """


    return (await asyncio_detailed(
        otp=otp,
client=client,

    )).parsed

