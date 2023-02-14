from typing import List, Dict
from aiohttp import web

from metal.types.batch import Batch
from metal.types.batches_list import BatchesList
from metal.types.error import Error
from metal.types.instances_batch_create_input import InstancesBatchCreateInput
from metal import util


async def create_device_batch(request: web.Request, id, body) -> web.Response:
    """Create a devices batch

    Creates new devices in batch and provisions them in our datacenter.

    :param id: Project UUID
    :type id: str
    :type id: str
    :param body: Batches to create
    :type body: dict | bytes

    """
    body = InstancesBatchCreateInput.from_dict(body)
    return web.Response(status=200)


async def delete_batch(request: web.Request, id, remove_associated_instances=None) -> web.Response:
    """Delete the Batch

    Deletes the Batch.

    :param id: Batch UUID
    :type id: str
    :type id: str
    :param remove_associated_instances: Delete all instances created from this batch
    :type remove_associated_instances: bool

    """
    return web.Response(status=200)


async def find_batch_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a Batch

    Returns a Batch

    :param id: Batch UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def find_batches_by_project(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve all batches by project

    Returns all batches for the given project

    :param id: Project UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)
