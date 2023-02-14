from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal.types.payment_method import PaymentMethod
from metal.types.payment_method_update_input import PaymentMethodUpdateInput
from metal import util


async def delete_payment_method(request: web.Request, id) -> web.Response:
    """Delete the payment method

    Deletes the payment method.

    :param id: Payment Method UUID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def find_payment_method_by_id(request: web.Request, id, include=None, exclude=None) -> web.Response:
    """Retrieve a payment method

    Returns a payment method

    :param id: Payment Method UUID
    :type id: str
    :type id: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def update_payment_method(request: web.Request, id, body) -> web.Response:
    """Update the payment method

    Updates the payment method.

    :param id: Payment Method UUID
    :type id: str
    :type id: str
    :param body: Payment Method to update
    :type body: dict | bytes

    """
    body = PaymentMethodUpdateInput.from_dict(body)
    return web.Response(status=200)
