from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.port_vlan_assignment_batch import PortVlanAssignmentBatch
from ...types import Response


def _get_kwargs(
    id: str,
    batch_id: str,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/ports/{id}/vlan-assignments/batches/{batch_id}".format(
        client.base_url,id=id,batch_id=batch_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, PortVlanAssignmentBatch]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PortVlanAssignmentBatch.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, PortVlanAssignmentBatch]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    batch_id: str,
    *,
    client: Client,

) -> Response[Union[Error, PortVlanAssignmentBatch]]:
    """Retrieve a VLAN Assignment Batch's details

     Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign
    or unassign, and the current state of the batch.

    Args:
        id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortVlanAssignmentBatch]]
    """


    kwargs = _get_kwargs(
        id=id,
batch_id=batch_id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    batch_id: str,
    *,
    client: Client,

) -> Optional[Union[Error, PortVlanAssignmentBatch]]:
    """Retrieve a VLAN Assignment Batch's details

     Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign
    or unassign, and the current state of the batch.

    Args:
        id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortVlanAssignmentBatch]]
    """


    return sync_detailed(
        id=id,
batch_id=batch_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    batch_id: str,
    *,
    client: Client,

) -> Response[Union[Error, PortVlanAssignmentBatch]]:
    """Retrieve a VLAN Assignment Batch's details

     Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign
    or unassign, and the current state of the batch.

    Args:
        id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortVlanAssignmentBatch]]
    """


    kwargs = _get_kwargs(
        id=id,
batch_id=batch_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    batch_id: str,
    *,
    client: Client,

) -> Optional[Union[Error, PortVlanAssignmentBatch]]:
    """Retrieve a VLAN Assignment Batch's details

     Returns the details of an existing Port-VLAN Assignment batch, including the list of VLANs to assign
    or unassign, and the current state of the batch.

    Args:
        id (str):
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PortVlanAssignmentBatch]]
    """


    return (await asyncio_detailed(
        id=id,
batch_id=batch_id,
client=client,

    )).parsed

