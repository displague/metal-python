from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.ip_assignment import IPAssignment
from ...models.ip_assignment_input import IPAssignmentInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IPAssignmentInput,

) -> Dict[str, Any]:
    url = "{}/devices/{id}/ips".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, IPAssignment]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IPAssignment.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, IPAssignment]]:
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
    json_body: IPAssignmentInput,

) -> Response[Union[Error, IPAssignment]]:
    """Create an ip assignment

     Creates an ip assignment for a device.

    Args:
        id (str):
        json_body (IPAssignmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPAssignment]]
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
    json_body: IPAssignmentInput,

) -> Optional[Union[Error, IPAssignment]]:
    """Create an ip assignment

     Creates an ip assignment for a device.

    Args:
        id (str):
        json_body (IPAssignmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPAssignment]]
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
    json_body: IPAssignmentInput,

) -> Response[Union[Error, IPAssignment]]:
    """Create an ip assignment

     Creates an ip assignment for a device.

    Args:
        id (str):
        json_body (IPAssignmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPAssignment]]
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
    json_body: IPAssignmentInput,

) -> Optional[Union[Error, IPAssignment]]:
    """Create an ip assignment

     Creates an ip assignment for a device.

    Args:
        id (str):
        json_body (IPAssignmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, IPAssignment]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

