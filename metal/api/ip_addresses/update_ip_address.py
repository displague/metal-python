from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.ip_assignment import IPAssignment
from ...models.ip_assignment_update_input import IPAssignmentUpdateInput
from ...models.ip_reservation import IPReservation
from ...models.vrf_ip_reservation import VrfIpReservation
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: IPAssignmentUpdateInput,

) -> Dict[str, Any]:
    url = "{}/ips/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
    if response.status_code == HTTPStatus.OK:
        def _parse_response_200(data: object) -> Union['IPAssignment', 'IPReservation', 'VrfIpReservation']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasupdate_ip_address_200_response_type_0 = IPAssignment.from_dict(data)



                return componentsschemasupdate_ip_address_200_response_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasupdate_ip_address_200_response_type_1 = IPReservation.from_dict(data)



                return componentsschemasupdate_ip_address_200_response_type_1
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasupdate_ip_address_200_response_type_2 = VrfIpReservation.from_dict(data)



            return componentsschemasupdate_ip_address_200_response_type_2

        response_200 = _parse_response_200(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
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
    json_body: IPAssignmentUpdateInput,

) -> Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
    """Update an ip address

     Update details about an ip address

    Args:
        id (str):
        json_body (IPAssignmentUpdateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]
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
    json_body: IPAssignmentUpdateInput,

) -> Optional[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
    """Update an ip address

     Update details about an ip address

    Args:
        id (str):
        json_body (IPAssignmentUpdateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]
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
    json_body: IPAssignmentUpdateInput,

) -> Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
    """Update an ip address

     Update details about an ip address

    Args:
        id (str):
        json_body (IPAssignmentUpdateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]
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
    json_body: IPAssignmentUpdateInput,

) -> Optional[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]:
    """Update an ip address

     Update details about an ip address

    Args:
        id (str):
        json_body (IPAssignmentUpdateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPAssignment', 'IPReservation', 'VrfIpReservation']]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

