from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.metal_gateway import MetalGateway
from ...models.metal_gateway_create_input import MetalGatewayCreateInput
from ...models.vrf_metal_gateway import VrfMetalGateway
from ...models.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    json_body: Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput'],
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Dict[str, Any]:
    url = "{}/projects/{project_id}/metal-gateways".format(
        client.base_url,project_id=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["page"] = page


    params["per_page"] = per_page



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body: Dict[str, Any]

    if isinstance(json_body, MetalGatewayCreateInput):
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
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    if response.status_code == HTTPStatus.CREATED:
        def _parse_response_201(data: object) -> Union['MetalGateway', 'VrfMetalGateway']:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasfind_metal_gateway_by_id_200_response_type_0 = MetalGateway.from_dict(data)



                return componentsschemasfind_metal_gateway_by_id_200_response_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasfind_metal_gateway_by_id_200_response_type_1 = VrfMetalGateway.from_dict(data)



            return componentsschemasfind_metal_gateway_by_id_200_response_type_1

        response_201 = _parse_response_201(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Client,
    json_body: Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput'],
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Create a metal gateway

     Create a metal gateway in a project

    Args:
        project_id (str):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.
        json_body (Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
client=client,
json_body=json_body,
page=page,
per_page=per_page,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    *,
    client: Client,
    json_body: Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput'],
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Create a metal gateway

     Create a metal gateway in a project

    Args:
        project_id (str):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.
        json_body (Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    return sync_detailed(
        project_id=project_id,
client=client,
json_body=json_body,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    json_body: Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput'],
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Create a metal gateway

     Create a metal gateway in a project

    Args:
        project_id (str):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.
        json_body (Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
client=client,
json_body=json_body,
page=page,
per_page=per_page,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    *,
    client: Client,
    json_body: Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput'],
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Optional[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]:
    """Create a metal gateway

     Create a metal gateway in a project

    Args:
        project_id (str):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.
        json_body (Union['MetalGatewayCreateInput', 'VrfMetalGatewayCreateInput']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['MetalGateway', 'VrfMetalGateway']]]
    """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
json_body=json_body,
page=page,
per_page=per_page,

    )).parsed

