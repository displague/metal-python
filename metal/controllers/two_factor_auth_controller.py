from typing import List, Dict
from aiohttp import web

from metal.types.error import Error
from metal import util


async def disable_tfa_app(request: web.Request, ) -> web.Response:
    """Disable two factor authentication

    Disables two factor authentication.


    """
    return web.Response(status=200)


async def disable_tfa_sms(request: web.Request, ) -> web.Response:
    """Disable two factor authentication

    Disables two factor authentication.


    """
    return web.Response(status=200)


async def enable_tfa_app(request: web.Request, ) -> web.Response:
    """Enable two factor auth using app

    Enables two factor authentication using authenticator app.


    """
    return web.Response(status=200)


async def enable_tfa_sms(request: web.Request, ) -> web.Response:
    """Enable two factor auth using sms

    Enables two factor authentication with sms.


    """
    return web.Response(status=200)
