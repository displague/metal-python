from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.device import Device
from ...models.device_create_in_facility_input import DeviceCreateInFacilityInput
from ...models.device_create_in_metro_input import DeviceCreateInMetroInput
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput'],

) -> Dict[str, Any]:
    url = "{}/projects/{id}/devices".format(
        client.base_url,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body: Dict[str, Any]

    if isinstance(json_body, DeviceCreateInMetroInput):
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Device, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Device.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Device, Error]]:
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
    json_body: Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput'],

) -> Response[Union[Device, Error]]:
    """Create a device

     Creates a new device and provisions it in the specified location.

    Device type-specific options are accepted.  For example, `baremetal` devices accept
    `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device
    types. The default device type is `baremetal`.

    Args:
        id (str):
        json_body (Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Device, Error]]
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
    json_body: Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput'],

) -> Optional[Union[Device, Error]]:
    """Create a device

     Creates a new device and provisions it in the specified location.

    Device type-specific options are accepted.  For example, `baremetal` devices accept
    `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device
    types. The default device type is `baremetal`.

    Args:
        id (str):
        json_body (Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Device, Error]]
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
    json_body: Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput'],

) -> Response[Union[Device, Error]]:
    """Create a device

     Creates a new device and provisions it in the specified location.

    Device type-specific options are accepted.  For example, `baremetal` devices accept
    `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device
    types. The default device type is `baremetal`.

    Args:
        id (str):
        json_body (Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Device, Error]]
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
    json_body: Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput'],

) -> Optional[Union[Device, Error]]:
    """Create a device

     Creates a new device and provisions it in the specified location.

    Device type-specific options are accepted.  For example, `baremetal` devices accept
    `operating_system`, `hostname`, and `plan`. These parameters may not be accepted for other device
    types. The default device type is `baremetal`.

    Args:
        id (str):
        json_body (Union['DeviceCreateInFacilityInput', 'DeviceCreateInMetroInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Device, Error]]
    """


    return (await asyncio_detailed(
        id=id,
client=client,
json_body=json_body,

    )).parsed

