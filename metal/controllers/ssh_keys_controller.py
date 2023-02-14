from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.ssh_key import SSHKey
from metal.types.ssh_key_create_input import SSHKeyCreateInput
from metal.types.ssh_key_input import SSHKeyInput
from metal.types.ssh_key_list import SSHKeyList
from metal import util


async def create_project_ssh_key(request: web.Request, id, body) -> web.Response:
    """Create a ssh key for the given project

    Creates a ssh key.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: ssh key to create
    :type body: dict | bytes

    """
    body = SSHKeyCreateInput.from_dict(body)
    return web.Response(status=200)


async def create_ssh_key(request: web.Request, body) -> web.Response:
    """Create a ssh key for the current user

    Creates a ssh key.

    :param body: ssh key to create
    :type body: dict | bytes

    """
    body = SSHKeyCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_ssh_key(request: web.Request, id) -> web.Response:
    """Delete the ssh key

    Deletes the ssh key.

    :param id: ssh key UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_device_ssh_keys(request: web.Request, id, search_string=None, include=None, exclude=None) -> web.Response:
    """Retrieve a device&#39;s ssh keys

    Returns a collection of the device&#39;s ssh keys.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param search_string: Search by key, label, or fingerprint
    :type search_string: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_project_ssh_keys(request: web.Request, id, query=None, include=None, exclude=None) -> web.Response:
    """Retrieve a project&#39;s ssh keys

    Returns a collection of the project&#39;s ssh keys.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param query: Search by key, label, or fingerprint
    :type query: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_ssh_key_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a ssh key

    Returns a single ssh key if the user has access

    :param id: SSH Key UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_ssh_keys(request: web.Request, search_string=None, include=None, exclude=None) -> web.Response:
    """Retrieve all ssh keys

    Returns a collection of the user’s ssh keys.

    :param search_string: Search by key, label, or fingerprint
    :type search_string: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_ssh_key(request: web.Request, id, body) -> web.Response:
    """Update the ssh key

    Updates the ssh key.

    :param id: SSH Key UUID
    :type id: str
    :type id: str
    :param body: ssh key to update
    :type body: dict | bytes

    """
    body = SSHKeyInput.from_dict(body)
    return web.Response(status=200)
