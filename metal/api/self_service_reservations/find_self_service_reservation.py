from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.self_service_reservation_response import SelfServiceReservationResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/projects/{project_id}/self-service/reservations/{id}".format(
        client.base_url,project_id=project_id,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, SelfServiceReservationResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SelfServiceReservationResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())



        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, SelfServiceReservationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Union[Error, SelfServiceReservationResponse]]:
    """Retrieve a reservation

     Returns a reservation

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SelfServiceReservationResponse]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
id=id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Union[Error, SelfServiceReservationResponse]]:
    """Retrieve a reservation

     Returns a reservation

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SelfServiceReservationResponse]]
    """


    return sync_detailed(
        project_id=project_id,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    id: str,
    *,
    client: Client,

) -> Response[Union[Error, SelfServiceReservationResponse]]:
    """Retrieve a reservation

     Returns a reservation

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SelfServiceReservationResponse]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
id=id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    id: str,
    *,
    client: Client,

) -> Optional[Union[Error, SelfServiceReservationResponse]]:
    """Retrieve a reservation

     Returns a reservation

    Args:
        project_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SelfServiceReservationResponse]]
    """


    return (await asyncio_detailed(
        project_id=project_id,
id=id,
client=client,

    )).parsed

