from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.ip_reservation import IPReservation
from ...models.ip_reservation_request_input import IPReservationRequestInput
from ...models.vrf_ip_reservation import VrfIpReservation
from ...models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: Union['IPReservationRequestInput', 'VrfIpReservationCreateInput'],

) -> Dict[str, Any]:
    url = "{}/projects/{id}/ips".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body: Dict[str, Any]

    if isinstance(json_body, IPReservationRequestInput):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()





    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
    if response.status_code == HTTPStatus.CREATED:
        def _parse_response_201(data: object) -> Union['IPReservation', 'VrfIpReservation']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasrequest_ip_reservation_201_response_type_0 = IPReservation.from_dict(data)



                return componentsschemasrequest_ip_reservation_201_response_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasrequest_ip_reservation_201_response_type_1 = VrfIpReservation.from_dict(data)



            return componentsschemasrequest_ip_reservation_201_response_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())



        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
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
    json_body: Union['IPReservationRequestInput', 'VrfIpReservationCreateInput'],

) -> Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
    """Requesting IP reservations

     Request more IP space for a project in order to have additional IP addresses to assign to devices.
    If the request is within the max quota, an IP reservation will be created. If the project will
    exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with
    a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of
    triggering the review process by providing the `fail_on_approval_required` parameter set to `true`
    in the request.

    Args:
        id (str):
        json_body (Union['IPReservationRequestInput', 'VrfIpReservationCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]
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
    json_body: Union['IPReservationRequestInput', 'VrfIpReservationCreateInput'],

) -> Optional[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
    """Requesting IP reservations

     Request more IP space for a project in order to have additional IP addresses to assign to devices.
    If the request is within the max quota, an IP reservation will be created. If the project will
    exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with
    a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of
    triggering the review process by providing the `fail_on_approval_required` parameter set to `true`
    in the request.

    Args:
        id (str):
        json_body (Union['IPReservationRequestInput', 'VrfIpReservationCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]
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
    json_body: Union['IPReservationRequestInput', 'VrfIpReservationCreateInput'],

) -> Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
    """Requesting IP reservations

     Request more IP space for a project in order to have additional IP addresses to assign to devices.
    If the request is within the max quota, an IP reservation will be created. If the project will
    exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with
    a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of
    triggering the review process by providing the `fail_on_approval_required` parameter set to `true`
    in the request.

    Args:
        id (str):
        json_body (Union['IPReservationRequestInput', 'VrfIpReservationCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]
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
    json_body: Union['IPReservationRequestInput', 'VrfIpReservationCreateInput'],

) -> Optional[Union[Error, Union['IPReservation', 'VrfIpReservation']]]:
    """Requesting IP reservations

     Request more IP space for a project in order to have additional IP addresses to assign to devices.
    If the request is within the max quota, an IP reservation will be created. If the project will
    exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with
    a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of
    triggering the review process by providing the `fail_on_approval_required` parameter set to `true`
    in the request.

    Args:
        id (str):
        json_body (Union['IPReservationRequestInput', 'VrfIpReservationCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['IPReservation', 'VrfIpReservation']]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

