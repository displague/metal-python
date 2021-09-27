from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error import Error
from ...models.invitation_list import InvitationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    client: Client,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Dict[str, Any]:
    url = "{}/projects/{project_id}/invitations".format(
        client.base_url,project_id=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    json_include: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include, Unset):
        if include is None:
            json_include = None
        else:
            json_include = include




    params["include"] = json_include


    json_exclude: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude, Unset):
        if exclude is None:
            json_exclude = None
        else:
            json_exclude = exclude




    params["exclude"] = json_exclude


    params["page"] = page


    params["per_page"] = per_page



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Error, InvitationList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InvitationList.from_dict(response.json())



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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Error, InvitationList]]:
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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Response[Union[Error, InvitationList]]:
    """Retrieve project invitations

     Returns all invitations in a project.

    Args:
        project_id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InvitationList]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
client=client,
include=include,
exclude=exclude,
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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Optional[Union[Error, InvitationList]]:
    """Retrieve project invitations

     Returns all invitations in a project.

    Args:
        project_id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InvitationList]]
    """


    return sync_detailed(
        project_id=project_id,
client=client,
include=include,
exclude=exclude,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: Client,
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Response[Union[Error, InvitationList]]:
    """Retrieve project invitations

     Returns all invitations in a project.

    Args:
        project_id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InvitationList]]
    """


    kwargs = _get_kwargs(
        project_id=project_id,
client=client,
include=include,
exclude=exclude,
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
    include: Union[Unset, None, List[str]] = UNSET,
    exclude: Union[Unset, None, List[str]] = UNSET,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 10,

) -> Optional[Union[Error, InvitationList]]:
    """Retrieve project invitations

     Returns all invitations in a project.

    Args:
        project_id (str):
        include (Union[Unset, None, List[str]]):
        exclude (Union[Unset, None, List[str]]):
        page (Union[Unset, None, int]):  Default: 1.
        per_page (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InvitationList]]
    """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
include=include,
exclude=exclude,
page=page,
per_page=per_page,

    )).parsed

